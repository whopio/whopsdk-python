import asyncio
import contextlib
import contextvars
import http.server
import inspect
import json
import ssl
import threading
import time
import typing

import httpx
import pytest

from whop_sdk import AsyncWhop, Whop
from whop_sdk.core.api_error import ApiError
from whop_sdk.core.parse_error import ParsingError
from whop_sdk.core.request_options import RequestOptions
from whop_sdk.environment import WhopEnvironment
from whop_sdk.errors.bad_request_error import BadRequestError
from whop_sdk.errors.forbidden_error import ForbiddenError
from whop_sdk.errors.not_found_error import NotFoundError
from whop_sdk.errors.unauthorized_error import UnauthorizedError
from whop_sdk.lib import live
from whop_sdk.lib.live import (
    StreamClosedError,
    StreamEndedError,
    WaitForFailedError,
    WaitForTimeoutError,
    backoff_seconds,
)
from whop_sdk.stats.time_series.types.retrieve_time_series_response import RetrieveTimeSeriesResponse

API_VERSION = "2026-01-01"
FROM = "2026-11-01"
TO = "2026-11-30"


def answer(timestamp: int) -> typing.Dict[str, typing.Any]:
    return {"data": {"points": [{"timestamp": timestamp, "value": 1.5}]}}


def snapshot(timestamp: int) -> bytes:
    return f"id: {timestamp}\nevent: stream.snapshot\ndata: {json.dumps(answer(timestamp))}\n\n".encode()


def closed(reason: str, status: typing.Optional[int] = None) -> bytes:
    return f"event: stream.closed\ndata: {json.dumps({'reason': reason, 'status': status})}\n\n".encode()


KEEP_ALIVE = b": keep-alive\n\n"


class Frames(httpx.SyncByteStream, httpx.AsyncByteStream):
    """An event stream body: its frames, then optionally an error, or a wait until released or closed, as a socket's
    read waits until data arrives or the socket is shut down."""

    def __init__(
        self,
        frames: typing.Sequence[bytes],
        error: typing.Optional[Exception] = None,
        hold: typing.Optional[threading.Event] = None,
    ) -> None:
        self.frames = frames
        self.error = error
        self.hold = hold
        self.closed = False
        self.after_first: typing.Optional[typing.Callable[[], None]] = None

    def __iter__(self) -> typing.Iterator[bytes]:
        for index, frame in enumerate(self.frames):
            yield frame
            if index == 0 and self.after_first is not None:
                self.after_first()
        if self.hold is not None:
            self.hold.wait()
        if self.error is not None:
            raise self.error

    async def __aiter__(self) -> typing.AsyncIterator[bytes]:
        for index, frame in enumerate(self.frames):
            yield frame
            if index == 0 and self.after_first is not None:
                self.after_first()
        while self.hold is not None and not self.hold.is_set():
            await asyncio.sleep(0.01)
        if self.error is not None:
            raise self.error

    def close(self) -> None:
        self.closed = True
        if self.hold is not None:
            self.hold.set()

    async def aclose(self) -> None:
        self.close()


def events(
    *frames: bytes, error: typing.Optional[Exception] = None, hold: typing.Optional[threading.Event] = None
) -> httpx.Response:
    return stream_of(Frames(frames, error, hold))


def stream_of(frames: Frames) -> httpx.Response:
    return httpx.Response(200, headers={"content-type": "text/event-stream"}, stream=frames)


def status(code: int) -> httpx.Response:
    return httpx.Response(code, json={"error": {"message": f"HTTP {code}"}})


class Server:
    """Answers each connection with the next scripted response and records its request."""

    def __init__(self, *responses: httpx.Response) -> None:
        self.responses = list(responses)
        self.requests: typing.List[httpx.Request] = []

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.responses[len(self.requests) - 1]

    async def handle_async(self, request: httpx.Request) -> httpx.Response:
        return self.handle(request)

    def client(self) -> Whop:
        transport = httpx.MockTransport(self.handle)
        return Whop(token="sk_test", api_version_date=API_VERSION, httpx_client=httpx.Client(transport=transport))

    def async_client(self) -> AsyncWhop:
        transport = httpx.MockTransport(self.handle_async)
        return AsyncWhop(
            token="sk_test", api_version_date=API_VERSION, httpx_client=httpx.AsyncClient(transport=transport)
        )


def timestamps(answers: typing.Iterable[RetrieveTimeSeriesResponse]) -> typing.List[int]:
    return [item.data.points[0].timestamp for item in answers]


@pytest.fixture(autouse=True)
def no_jitter(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(live.random, "random", lambda: 0.0)


def test_yields_each_snapshot_as_the_reads_answer() -> None:
    server = Server(events(snapshot(1), KEEP_ALIVE, snapshot(2), closed("not_live", 200)))

    answers = list(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO))

    assert timestamps(answers) == [1, 2]
    assert all(isinstance(item, RetrieveTimeSeriesResponse) for item in answers)
    assert len(server.requests) == 1


def test_sends_the_reads_request_asking_for_the_event_stream() -> None:
    server = Server(events(snapshot(1), closed("not_live")))

    list(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, account_id="biz_1"))

    request = server.requests[0]
    assert request.method == "GET"
    assert request.url.path == "/api/v1/stats/time_series/gmv"
    assert dict(request.url.params) == {"from": "2026-11-01", "to": "2026-11-30", "account_id": "biz_1"}
    assert request.headers["accept"] == "text/event-stream"
    assert request.headers["authorization"] == "Bearer sk_test"
    assert request.headers["api-version-date"] == API_VERSION


def test_sends_the_reads_request_options_on_every_connection_but_not_its_retries() -> None:
    drops: typing.List[Exception] = []
    server = Server(status(503), events(snapshot(1), closed("not_live")))
    options: RequestOptions = {
        "additional_headers": {"X-Trace": "abc"},
        "additional_query_parameters": {"extra": "1"},
        "max_retries": 5,
    }

    assert timestamps(
        server.client().stats.time_series.watch(
            "gmv", from_=FROM, to=TO, request_options=options, max_backoff=0, on_disconnect=drops.append
        )
    ) == [1]

    assert [request.headers["x-trace"] for request in server.requests] == ["abc", "abc"]
    assert [request.url.params["extra"] for request in server.requests] == ["1", "1"]
    assert [typing.cast(ApiError, drop).status_code for drop in drops] == [503]


def test_reconnects_after_a_reconnect_close_without_reporting_a_drop() -> None:
    drops: typing.List[Exception] = []
    server = Server(events(snapshot(1), closed("reconnect")), events(snapshot(2), closed("not_live", 200)))

    assert timestamps(
        server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0, on_disconnect=drops.append)
    ) == [1, 2]
    assert len(server.requests) == 2
    assert drops == []


def test_counts_a_stream_that_ends_without_a_close_as_a_drop() -> None:
    drops: typing.List[Exception] = []
    server = Server(events(snapshot(1)), events(snapshot(2), closed("not_live")))

    assert timestamps(
        server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0, on_disconnect=drops.append)
    ) == [1, 2]
    assert [type(drop) for drop in drops] == [StreamEndedError]


def test_reconnects_after_a_dropped_connection() -> None:
    drops: typing.List[Exception] = []
    server = Server(events(snapshot(1), error=httpx.ReadError("reset")), events(snapshot(2), closed("not_live")))

    assert timestamps(
        server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0, on_disconnect=drops.append)
    ) == [1, 2]
    assert [type(drop) for drop in drops] == [httpx.ReadError]


class Aging(Server):
    """A server whose connection ``open_for`` moves the clock ``seconds`` on: while its event stream is
    open, after the first frame, or, ``hung``, while the connect waits for the response."""

    def __init__(self, *responses: httpx.Response, open_for: int, seconds: float, hung: bool = False) -> None:
        super().__init__(*responses)
        self.now = 0.0
        self.open_for = open_for
        self.seconds = seconds
        self.hung = hung

    def handle(self, request: httpx.Request) -> httpx.Response:
        response = super().handle(request)
        if len(self.requests) == self.open_for:
            if self.hung or not isinstance(response.stream, Frames):
                self.now += self.seconds
            else:
                response.stream.after_first = self.age
        return response

    def age(self) -> None:
        self.now += self.seconds


def test_backs_off_until_a_connection_stays_open_30_seconds_answers_or_not(monkeypatch: pytest.MonkeyPatch) -> None:
    waits: typing.List[float] = []
    server = Aging(
        status(503),
        status(502),
        status(500),
        events(snapshot(1), closed("reconnect")),
        events(snapshot(2), closed("reconnect")),
        events(snapshot(3), closed("not_live")),
        open_for=4,
        seconds=30,
    )

    def pause(_stopped: threading.Event, seconds: float) -> bool:
        waits.append(seconds)
        return False

    monkeypatch.setattr(live, "_pause", pause)
    monkeypatch.setattr(live, "_clock", lambda: server.now)
    monkeypatch.setattr(live.random, "random", lambda: 0.5)

    assert timestamps(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO)) == [1, 2, 3]
    assert waits == [0.5, 1.125, 2.25, 0.5, 1.125]


def test_keeps_backing_off_after_a_connection_that_dropped_within_30_seconds(monkeypatch: pytest.MonkeyPatch) -> None:
    waits: typing.List[float] = []
    server = Aging(
        status(503),
        events(snapshot(1), closed("reconnect")),
        events(snapshot(2), closed("not_live")),
        open_for=2,
        seconds=29.9,
    )

    def pause(_stopped: threading.Event, seconds: float) -> bool:
        waits.append(seconds)
        return False

    monkeypatch.setattr(live, "_pause", pause)
    monkeypatch.setattr(live, "_clock", lambda: server.now)

    assert timestamps(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO)) == [1, 2]
    assert waits == [0.0, 1.0]


def test_keeps_backing_off_after_a_connect_that_hung_past_30_seconds(monkeypatch: pytest.MonkeyPatch) -> None:
    waits: typing.List[float] = []
    server = Aging(
        status(503),
        status(503),
        status(503),
        events(snapshot(1), closed("not_live")),
        open_for=3,
        seconds=45,
        hung=True,
    )

    def pause(_stopped: threading.Event, seconds: float) -> bool:
        waits.append(seconds)
        return False

    monkeypatch.setattr(live, "_pause", pause)
    monkeypatch.setattr(live, "_clock", lambda: server.now)
    monkeypatch.setattr(live.random, "random", lambda: 0.5)

    assert timestamps(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO)) == [1]
    assert waits == [0.5, 1.125, 2.25]


async def test_async_watch_keeps_backing_off_after_a_connect_that_hung_past_30_seconds(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    waits: typing.List[float] = []
    server = Aging(
        status(503),
        status(503),
        status(503),
        events(snapshot(1), closed("not_live")),
        open_for=3,
        seconds=45,
        hung=True,
    )

    async def pause(_stopped: asyncio.Event, seconds: float) -> bool:
        waits.append(seconds)
        return False

    monkeypatch.setattr(live, "_apause", pause)
    monkeypatch.setattr(live, "_clock", lambda: server.now)
    monkeypatch.setattr(live.random, "random", lambda: 0.5)

    answers = [item async for item in server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO)]

    assert timestamps(answers) == [1]
    assert waits == [0.5, 1.125, 2.25]


def test_backs_off_from_up_to_a_second_to_its_cap_with_up_to_a_quarter_of_jitter() -> None:
    assert [backoff_seconds(attempt, 30, lambda: 0.0) for attempt in range(8)] == [0, 1, 2, 4, 8, 16, 30, 30]
    assert [backoff_seconds(0, 30, lambda: fraction) for fraction in (0.25, 1.0)] == [0.25, 1.0]
    assert backoff_seconds(0, 0.5, lambda: 1.0) == 0.5
    assert backoff_seconds(3, 30, lambda: 1.0) == 5.0


def test_backs_off_without_overflowing_however_many_attempts_have_failed() -> None:
    assert backoff_seconds(10_000, 30, lambda: 0.0) == 30
    assert backoff_seconds(10_000, 30, lambda: 1.0) == 37.5
    assert [backoff_seconds(attempt, 0, lambda: 1.0) for attempt in (0, 1, 2_000, 10_000)] == [0, 0, 0, 0]


def test_ends_quietly_when_the_read_stops_being_live() -> None:
    server = Server(events(snapshot(1), closed("not_live")))

    assert timestamps(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO)) == [1]


@pytest.mark.parametrize("data", ["{not json", '{"data": {"points": "not a list"}}'])
def test_raises_a_parsing_error_for_a_snapshot_that_is_not_the_reads_answer(data: str) -> None:
    server = Server(events(snapshot(1), f"event: stream.snapshot\ndata: {data}\n\n".encode()))
    seen: typing.List[RetrieveTimeSeriesResponse] = []

    with pytest.raises(ParsingError):
        for item in server.client().stats.time_series.watch("gmv", from_=FROM, to=TO):
            seen.append(item)

    assert timestamps(seen) == [1]
    assert len(server.requests) == 1


def test_reconnects_after_a_close_whose_payload_is_not_json() -> None:
    server = Server(
        events(snapshot(1), b"event: stream.closed\ndata: {not json\n\n"), events(snapshot(2), closed("not_live"))
    )

    assert timestamps(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0)) == [1, 2]
    assert len(server.requests) == 2


@pytest.mark.parametrize(("reason", "code"), [("not_live", 403), ("unreadable", None)])
def test_raises_when_the_stream_closes_for_good(reason: str, code: typing.Optional[int]) -> None:
    server = Server(events(snapshot(1), closed(reason, code)))
    seen: typing.List[RetrieveTimeSeriesResponse] = []

    with pytest.raises(StreamClosedError) as raised:
        for item in server.client().stats.time_series.watch("gmv", from_=FROM, to=TO):
            seen.append(item)

    assert (raised.value.reason, raised.value.status) == (reason, code)
    assert timestamps(seen) == [1]


def test_yields_a_plain_answer_once_then_ends() -> None:
    server = Server(httpx.Response(200, json=answer(7)))

    answers = list(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO))

    assert timestamps(answers) == [7]
    assert isinstance(answers[0], RetrieveTimeSeriesResponse)
    assert len(server.requests) == 1


@pytest.mark.parametrize(
    ("code", "error"),
    [
        (400, BadRequestError),
        (401, UnauthorizedError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (410, ApiError),
        (422, ApiError),
    ],
)
def test_raises_the_reads_own_error_for_a_status_a_reconnect_would_get_again(
    code: int, error: typing.Type[ApiError]
) -> None:
    drops: typing.List[Exception] = []
    server = Server(status(code))

    with pytest.raises(error) as raised:
        next(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, on_disconnect=drops.append))

    assert raised.value.status_code == code
    assert raised.value.body == {"error": {"message": f"HTTP {code}"}}
    assert len(server.requests) == 1
    assert drops == []


@pytest.mark.parametrize("code", [408, 429])
def test_reconnects_after_a_client_error_the_server_retries(code: int) -> None:
    drops: typing.List[Exception] = []
    server = Server(status(code), events(snapshot(1), closed("not_live")))

    answers = server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0, on_disconnect=drops.append)

    assert timestamps(answers) == [1]
    assert [typing.cast(ApiError, drop).status_code for drop in drops] == [code]


def stalled_error(code: int) -> httpx.Response:
    """A client error whose body drops partway, then, for a reconnect, a read that ends quietly."""
    return httpx.Response(
        code, headers={"content-type": "application/json"}, stream=Frames([b'{"error":'], error=httpx.ReadTimeout("stalled"))
    )


@pytest.mark.parametrize(("code", "error"), [(401, UnauthorizedError), (403, ForbiddenError)])
def test_a_client_error_whose_body_drops_partway_raises_it_without_reconnecting(
    code: int, error: typing.Type[ApiError]
) -> None:
    server = Server(stalled_error(code), events(snapshot(1), closed("not_live", 200)))

    with pytest.raises(error) as raised:
        list(server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0))

    assert raised.value.status_code == code
    assert len(server.requests) == 1


@pytest.mark.parametrize(("code", "error"), [(401, UnauthorizedError), (403, ForbiddenError)])
async def test_an_async_client_error_whose_body_drops_partway_raises_it_without_reconnecting(
    code: int, error: typing.Type[ApiError]
) -> None:
    server = Server(stalled_error(code), events(snapshot(1), closed("not_live", 200)))

    with pytest.raises(error) as raised:
        [item async for item in server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0)]

    assert raised.value.status_code == code
    assert len(server.requests) == 1


def test_raises_a_certificate_the_server_fails_instead_of_reconnecting() -> None:
    drops: typing.List[Exception] = []
    requests: typing.List[httpx.Request] = []

    def refuse(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        raise httpx.ConnectError("certificate verify failed", request=request) from ssl.SSLCertVerificationError(
            1, "certificate verify failed"
        )

    whop = Whop(token="sk_test", api_version_date=API_VERSION, httpx_client=httpx.Client(transport=httpx.MockTransport(refuse)))

    with pytest.raises(httpx.ConnectError):
        list(whop.stats.time_series.watch("gmv", from_=FROM, to=TO, max_backoff=0, on_disconnect=drops.append))

    assert len(requests) == 1
    assert drops == []


def test_closes_the_connection_when_iteration_stops() -> None:
    frames = Frames([snapshot(1), snapshot(2), closed("not_live")])
    server = Server(stream_of(frames))

    watch = server.client().stats.time_series.watch("gmv", from_=FROM, to=TO)
    next(watch)
    watch.close()

    assert frames.closed


class RecordingSocket:
    def __init__(self) -> None:
        self.shut_down = False

    def shutdown(self, _how: int) -> None:
        self.shut_down = True


class NetworkStream:
    def __init__(self, sock: RecordingSocket) -> None:
        self.sock = sock

    def get_extra_info(self, name: str) -> typing.Optional[RecordingSocket]:
        return self.sock if name == "socket" else None


@pytest.mark.parametrize(("version", "shut_down"), [(b"HTTP/1.1", True), (b"HTTP/1.0", True), (b"HTTP/2", False)])
def test_close_shuts_down_a_socket_the_response_has_to_itself_and_closes_any_other(
    version: bytes, shut_down: bool
) -> None:
    sock = RecordingSocket()
    frames = held(snapshot(1))
    response = httpx.Response(
        200, stream=frames, extensions={"http_version": version, "network_stream": NetworkStream(sock)}
    )

    live._interrupt(response)

    assert (sock.shut_down, frames.closed) == (shut_down, not shut_down)


def test_wait_for_returns_the_first_answer_until_accepts() -> None:
    server = Server(events(snapshot(1), snapshot(2), snapshot(3), closed("not_live")))

    time_series = server.client().stats.time_series
    found = time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: item.data.points[0].timestamp >= 2)

    assert found.data.points[0].timestamp == 2


def test_wait_for_and_watch_connect_with_the_callers_context_variables() -> None:
    caller: contextvars.ContextVar[str] = contextvars.ContextVar("caller", default="none")
    server = Server(events(snapshot(1), closed("not_live")), events(snapshot(1), closed("not_live")))
    seen: typing.List[str] = []
    answer = server.handle

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(caller.get())
        return answer(request)

    server.handle = handle  # type: ignore[method-assign]
    caller.set("acct_1")
    time_series = server.client().stats.time_series

    time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: True)
    list(time_series.watch("gmv", from_=FROM, to=TO))

    assert seen == ["acct_1", "acct_1"]


def test_wait_for_raises_on_the_first_answer_fail_when_accepts() -> None:
    server = Server(events(snapshot(1), snapshot(2), closed("not_live")))

    with pytest.raises(WaitForFailedError) as raised:
        server.client().stats.time_series.wait_for(
            "gmv",
            from_=FROM,
            to=TO,
            until=lambda item: item.data.points[0].timestamp == 2,
            fail_when=lambda item: item.data.points[0].timestamp == 1,
        )

    assert raised.value.answer.data.points[0].timestamp == 1


def test_wait_for_raises_once_its_timeout_passes() -> None:
    hold = threading.Event()
    server = Server(events(snapshot(1), hold=hold))

    try:
        with pytest.raises(WaitForTimeoutError):
            server.client().stats.time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: False, timeout=0.2)
    finally:
        hold.set()


def test_wait_for_raises_when_the_read_stops_being_live_before_a_match() -> None:
    server = Server(events(snapshot(1), closed("not_live")))

    with pytest.raises(StreamClosedError):
        server.client().stats.time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: False)


def test_wait_for_raises_the_reads_own_error() -> None:
    server = Server(status(401))

    with pytest.raises(UnauthorizedError):
        server.client().stats.time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: True)


async def test_async_watch_yields_snapshots_and_reconnects() -> None:
    drops: typing.List[Exception] = []
    server = Server(
        events(snapshot(1), closed("reconnect")),
        events(snapshot(2), error=httpx.ReadError("reset")),
        events(KEEP_ALIVE, snapshot(3), closed("not_live", 204)),
    )

    answers = [
        item
        async for item in server.async_client().stats.time_series.watch(
            "gmv", from_=FROM, to=TO, max_backoff=0, on_disconnect=drops.append
        )
    ]

    assert timestamps(answers) == [1, 2, 3]
    assert [type(drop) for drop in drops] == [httpx.ReadError]
    assert {request.headers["accept"] for request in server.requests} == {"text/event-stream"}
    assert {request.headers["authorization"] for request in server.requests} == {"Bearer sk_test"}
    assert {request.headers["api-version-date"] for request in server.requests} == {API_VERSION}


async def test_async_watch_yields_a_plain_answer_once_then_ends() -> None:
    server = Server(httpx.Response(200, json=answer(7)))

    answers = [item async for item in server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO)]

    assert timestamps(answers) == [7]


async def test_async_watch_raises_the_reads_own_error() -> None:
    server = Server(status(401))

    with pytest.raises(UnauthorizedError):
        await server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO).__anext__()


async def test_async_watch_raises_when_the_stream_closes_for_good() -> None:
    server = Server(events(snapshot(1), closed("not_live", 403)))

    with pytest.raises(StreamClosedError) as raised:
        async for _item in server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO):
            pass

    assert raised.value.status == 403


async def test_async_wait_for_returns_the_first_match_and_times_out() -> None:
    server = Server(events(snapshot(1), snapshot(2), closed("not_live")))

    time_series = server.async_client().stats.time_series
    found = await time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: item.data.points[0].timestamp == 2)
    assert found.data.points[0].timestamp == 2

    hold = threading.Event()
    waiting = Server(events(snapshot(1), hold=hold))
    try:
        with pytest.raises(WaitForTimeoutError):
            await waiting.async_client().stats.time_series.wait_for(
                "gmv", from_=FROM, to=TO, until=lambda item: False, timeout=0.2
            )
    finally:
        hold.set()


def held(*frames: bytes) -> Frames:
    return Frames(frames, hold=threading.Event())


def test_close_from_another_thread_ends_a_loop_waiting_between_events() -> None:
    drops: typing.List[Exception] = []
    frames = held(snapshot(1))
    server = Server(stream_of(frames))
    stream = server.client().stats.time_series.watch("gmv", from_=FROM, to=TO, on_disconnect=drops.append)

    threading.Timer(0.2, stream.close).start()
    started = time.monotonic()
    answers = list(stream)

    assert timestamps(answers) == [1]
    assert time.monotonic() - started < 2
    assert frames.closed
    assert len(server.requests) == 1
    assert drops == []


def test_a_with_block_closes_the_stream_on_the_way_out() -> None:
    frames = held(snapshot(1), snapshot(2))
    server = Server(stream_of(frames))

    with server.client().stats.time_series.watch("gmv", from_=FROM, to=TO) as stream:
        assert timestamps([next(stream)]) == [1]

    assert frames.closed
    assert list(stream) == []


def test_wait_for_closes_its_connection_as_it_returns() -> None:
    frames = held(snapshot(1))
    server = Server(stream_of(frames))

    found = server.client().stats.time_series.wait_for("gmv", from_=FROM, to=TO, until=lambda item: True)

    assert found.data.points[0].timestamp == 1
    deadline = time.monotonic() + 2
    while not frames.closed and time.monotonic() < deadline:
        time.sleep(0.01)
    assert frames.closed
    assert len(server.requests) == 1


async def test_cancelling_the_task_iterating_an_async_watch_closes_it_without_reconnecting() -> None:
    frames = held(snapshot(1))
    server = Server(stream_of(frames))
    first = asyncio.Event()

    async def iterate() -> None:
        async for _item in server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO):
            first.set()

    task = asyncio.ensure_future(iterate())
    await asyncio.wait_for(first.wait(), 2)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task

    assert frames.closed
    assert len(server.requests) == 1


async def test_aclose_from_another_task_ends_an_async_loop_waiting_between_events() -> None:
    drops: typing.List[Exception] = []
    frames = held(snapshot(1))
    server = Server(stream_of(frames))
    stream = server.async_client().stats.time_series.watch("gmv", from_=FROM, to=TO, on_disconnect=drops.append)

    async def close_soon() -> None:
        await asyncio.sleep(0.2)
        await stream.aclose()

    closing = asyncio.ensure_future(close_soon())
    answers = [item async for item in stream]
    await closing

    assert timestamps(answers) == [1]
    assert frames.closed
    assert len(server.requests) == 1
    assert drops == []


def test_close_during_a_connect_that_never_answers_ends_the_loop_and_closes_the_late_response() -> None:
    answer = threading.Event()
    frames = held(snapshot(1))
    connecting = threading.Event()

    def handle(_request: httpx.Request) -> httpx.Response:
        connecting.set()
        answer.wait(5)
        return stream_of(frames)

    client = Whop(
        token="sk_test",
        api_version_date=API_VERSION,
        httpx_client=httpx.Client(transport=httpx.MockTransport(handle)),
    )
    stream = client.stats.time_series.watch("gmv", from_=FROM, to=TO)

    def close_once_connecting() -> None:
        connecting.wait(2)
        stream.close()

    threading.Thread(target=close_once_connecting, daemon=True).start()
    started = time.monotonic()

    assert list(stream) == []
    assert time.monotonic() - started < 2

    answer.set()
    deadline = time.monotonic() + 2
    while not frames.closed and time.monotonic() < deadline:
        time.sleep(0.01)
    assert frames.closed


async def test_aclose_during_a_connect_that_never_answers_ends_the_loop_and_cancels_the_connect() -> None:
    connecting = asyncio.Event()
    cancelled = asyncio.Event()

    async def handle(_request: httpx.Request) -> httpx.Response:
        connecting.set()
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            cancelled.set()
            raise
        raise AssertionError("unreachable")

    client = AsyncWhop(
        token="sk_test",
        api_version_date=API_VERSION,
        httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
    )
    stream = client.stats.time_series.watch("gmv", from_=FROM, to=TO)

    async def close_once_connecting() -> None:
        await connecting.wait()
        await stream.aclose()

    closing = asyncio.ensure_future(close_once_connecting())
    answers = await asyncio.wait_for(collect(stream), 2)
    await closing

    assert answers == []
    assert cancelled.is_set()


class SlowToCloseBody(httpx.AsyncByteStream):
    def __init__(self) -> None:
        self.closing = asyncio.Event()
        self.closed = asyncio.Event()

    async def __aiter__(self) -> typing.AsyncIterator[bytes]:
        await asyncio.Event().wait()
        yield b""

    async def aclose(self) -> None:
        self.closing.set()
        await asyncio.sleep(0.05)
        self.closed.set()


async def test_cancelling_as_the_connect_answers_closes_the_response_even_when_cancelled_again() -> None:
    body = SlowToCloseBody()
    reading: typing.Optional[asyncio.Future[typing.List[RetrieveTimeSeriesResponse]]] = None

    async def handle(_request: httpx.Request) -> httpx.Response:
        assert reading is not None
        reading.cancel()
        return httpx.Response(200, headers={"content-type": "text/event-stream"}, stream=body)

    client = AsyncWhop(
        token="sk_test",
        api_version_date=API_VERSION,
        httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
    )
    reading = asyncio.ensure_future(collect(client.stats.time_series.watch("gmv", from_=FROM, to=TO)))
    await asyncio.wait_for(body.closing.wait(), 2)
    reading.cancel()

    with pytest.raises(asyncio.CancelledError):
        await reading
    await asyncio.wait_for(body.closed.wait(), 2)


class SnapshotThenSlowToClose(httpx.AsyncByteStream):
    def __init__(self) -> None:
        self.closing = asyncio.Event()
        self.closed = asyncio.Event()

    async def __aiter__(self) -> typing.AsyncIterator[bytes]:
        yield snapshot(1)
        await asyncio.Event().wait()
        yield b""

    async def aclose(self) -> None:
        self.closing.set()
        await asyncio.sleep(0.05)
        self.closed.set()


async def test_cancelling_the_iterating_task_again_during_the_close_still_closes_the_response() -> None:
    body = SnapshotThenSlowToClose()
    stream = Server(stream_of_body(body)).async_client().stats.time_series.watch("gmv", from_=FROM, to=TO)
    first = asyncio.Event()

    async def iterate() -> None:
        async for _ in stream:
            first.set()

    reading = asyncio.ensure_future(iterate())
    await asyncio.wait_for(first.wait(), 2)
    reading.cancel()
    await asyncio.wait_for(body.closing.wait(), 2)
    reading.cancel()

    with pytest.raises(asyncio.CancelledError):
        await reading
    await asyncio.wait_for(body.closed.wait(), 2)


async def test_cancelling_an_aclose_partway_still_closes_the_response() -> None:
    body = SnapshotThenSlowToClose()
    stream = Server(stream_of_body(body)).async_client().stats.time_series.watch("gmv", from_=FROM, to=TO)
    await stream.__anext__()

    closing = asyncio.ensure_future(stream.aclose())
    await asyncio.wait_for(body.closing.wait(), 2)
    closing.cancel()

    with pytest.raises(asyncio.CancelledError):
        await closing
    await asyncio.wait_for(body.closed.wait(), 2)


def stream_of_body(body: httpx.AsyncByteStream) -> httpx.Response:
    return httpx.Response(200, headers={"content-type": "text/event-stream"}, stream=body)


async def collect(stream: typing.AsyncIterator[RetrieveTimeSeriesResponse]) -> typing.List[RetrieveTimeSeriesResponse]:
    return [answer async for answer in stream]


class EventStreamServer:
    """A local HTTP/1.1 server answering each request with an event stream: a snapshot, then a keep-alive comment
    every ``keep_alive`` seconds, or nothing more when it is ``None``, until the client goes away or the server stops.
    """

    def __init__(self, keep_alive: typing.Optional[float]) -> None:
        self.requests = 0
        self.stopping = threading.Event()
        server = self

        class Handler(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self) -> None:
                server.requests += 1
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Connection", "close")
                self.end_headers()
                with contextlib.suppress(OSError):
                    self.wfile.write(snapshot(1))
                    while not server.stopping.wait(keep_alive):
                        self.wfile.write(KEEP_ALIVE)

            def log_message(self, *_arguments: typing.Any) -> None:
                pass

        self.http = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.environment = WhopEnvironment(
            api=f"http://127.0.0.1:{self.http.server_address[1]}/api/v1",
            vault=f"http://127.0.0.1:{self.http.server_address[1]}/api/v1",
        )

    def __enter__(self) -> "EventStreamServer":
        threading.Thread(target=self.http.serve_forever, name="event-stream-server", daemon=True).start()
        return self

    def __exit__(self, *_exception: object) -> None:
        self.stopping.set()
        self.http.shutdown()
        self.http.server_close()


KEEP_ALIVES = pytest.mark.parametrize("keep_alive", [0.2, None], ids=["keep-alive", "silent"])


@KEEP_ALIVES
def test_close_from_another_thread_ends_a_loop_reading_a_real_socket(keep_alive: typing.Optional[float]) -> None:
    with EventStreamServer(keep_alive) as server, httpx.Client(trust_env=False) as http_client:
        client = Whop(
            token="sk_test", api_version_date=API_VERSION, environment=server.environment, httpx_client=http_client
        )
        stream = client.stats.time_series.watch("gmv", from_=FROM, to=TO)
        answers: typing.List[RetrieveTimeSeriesResponse] = []
        first = threading.Event()

        def iterate() -> None:
            for item in stream:
                answers.append(item)
                first.set()

        reader = threading.Thread(target=iterate, daemon=True)
        reader.start()
        assert first.wait(2)
        time.sleep(0.3)
        stream.close()
        reader.join(2)

        assert not reader.is_alive()
        assert timestamps(answers) == [1]
        assert server.requests == 1


@KEEP_ALIVES
def test_close_between_events_closes_the_response_without_another_next(keep_alive: typing.Optional[float]) -> None:
    with EventStreamServer(keep_alive) as server, httpx.Client(trust_env=False) as http_client:
        client = Whop(
            token="sk_test", api_version_date=API_VERSION, environment=server.environment, httpx_client=http_client
        )
        stream = client.stats.time_series.watch("gmv", from_=FROM, to=TO)
        assert timestamps([next(stream)]) == [1]
        stream.close()

        assert inspect.getgeneratorstate(stream._answers) == inspect.GEN_CLOSED
        assert list(stream) == []
        assert server.requests == 1


@KEEP_ALIVES
async def test_aclose_between_events_closes_the_response(keep_alive: typing.Optional[float]) -> None:
    with EventStreamServer(keep_alive) as server:
        async with httpx.AsyncClient(trust_env=False) as http_client:
            client = AsyncWhop(
                token="sk_test", api_version_date=API_VERSION, environment=server.environment, httpx_client=http_client
            )
            stream = client.stats.time_series.watch("gmv", from_=FROM, to=TO)
            assert timestamps([await stream.__anext__()]) == [1]
            await asyncio.wait_for(stream.aclose(), 2)

            assert stream._answers.ag_frame is None
            assert [answer async for answer in stream] == []
            assert server.requests == 1


async def aclose_from_another_task_ends_the_loop(client: AsyncWhop, server: EventStreamServer) -> None:
    stream = client.stats.time_series.watch("gmv", from_=FROM, to=TO)
    answers: typing.List[RetrieveTimeSeriesResponse] = []
    first = asyncio.Event()

    async def iterate() -> None:
        async for item in stream:
            answers.append(item)
            first.set()

    reading = asyncio.ensure_future(iterate())
    await asyncio.wait_for(first.wait(), 2)
    await asyncio.sleep(0.3)
    await asyncio.wait_for(stream.aclose(), 2)
    await asyncio.wait_for(reading, 2)

    assert timestamps(answers) == [1]
    assert server.requests == 1


@KEEP_ALIVES
async def test_aclose_from_another_task_ends_a_loop_reading_a_real_socket(keep_alive: typing.Optional[float]) -> None:
    with EventStreamServer(keep_alive) as server:
        async with httpx.AsyncClient(trust_env=False) as http_client:
            client = AsyncWhop(
                token="sk_test", api_version_date=API_VERSION, environment=server.environment, httpx_client=http_client
            )
            await aclose_from_another_task_ends_the_loop(client, server)


@pytest.mark.aiohttp
@KEEP_ALIVES
async def test_aclose_from_another_task_ends_a_loop_reading_through_httpx_aiohttp(
    keep_alive: typing.Optional[float],
) -> None:
    httpx_aiohttp = pytest.importorskip("httpx_aiohttp")
    with EventStreamServer(keep_alive) as server:
        async with httpx_aiohttp.HttpxAiohttpClient(trust_env=False) as http_client:
            client = AsyncWhop(
                token="sk_test", api_version_date=API_VERSION, environment=server.environment, httpx_client=http_client
            )
            await aclose_from_another_task_ends_the_loop(client, server)
