"""Live reads: a read's answer now, then again each time it changes.

A live read is a GET the API also answers as an event stream: the same request with ``Accept: text/event-stream``
gets the read's whole answer now and again each time it changes. Its client carries ``watch`` and ``wait_for``
beside the read. They take exactly the read's parameters, then their own options::

    from whop_sdk import Whop

    client = Whop(token="...")

    for series in client.stats.time_series.watch("gmv", from_="2026-11-01", to="2026-11-30"):
        print(series.data.points)

    series = client.stats.time_series.wait_for(
        "gmv",
        from_="2026-11-01",
        to="2026-11-30",
        until=lambda series: len(series.data.points) == 30,
        timeout=120,
    )

``AsyncWhop``'s clients carry the same, as an async iterator and a coroutine. The pipeline writes each one out
with its read's parameters; the functions here are what they call.

``watch`` returns a stream to iterate. ``close()`` stops it at once from any thread, and a ``with`` block closes it
on the way out; on ``AsyncWhop``, ``await aclose()`` from any task or cancelling the task iterating it does the
same::

    with client.stats.time_series.watch("gmv_usd", account_id="biz_...", from_=..., to=...) as stream:
        threading.Timer(300, stream.close).start()
        for series in stream:
            print(series.data.points)

Each connection sends the request the read itself builds: ``watch`` runs the generated read method against a
stand-in for the HTTP client that records the request instead of sending it, then sends that request asking for
the event stream. The read's ``request_options`` therefore apply to every connection: its headers, query
parameters and timeout. Its ``max_retries`` does not, since each connection is sent once and ``watch`` reconnects
itself. A timeout below 15 seconds, the server's keep-alive interval, drops and reconnects an idle stream.

``watch`` yields each answer as the read's own answer type, reconnects after a drop (each connection starts with
a fresh answer, so nothing is replayed), and ends when the stream closes for good:

- ``not_live`` with no status or a 2xx status ends the iteration: the last answer stands and will not change.
- ``not_live`` with any other status, or ``unreadable``, raises ``StreamClosedError``.
- any other close reconnects.
- a stream that ends without a close is a drop: ``on_disconnect`` gets a ``StreamEndedError``, then it reconnects.
- a client error raises the error the read raises for it, as the server ends a read on one; 408, 429, a server
  error, a network error or a timeout is a drop.
- a success that is not an event stream is the read's one answer: it is yielded, then the iteration ends.

Reconnects back off: the first waits a random 0 to 1 second (at most ``max_backoff``), each after it 1 second doubling
up to ``max_backoff``, plus up to 25% jitter. The count starts over only after a connection that stayed open at least
30 seconds, not after an answer, since every connection opens with one.
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import contextlib
import contextvars
import copy
import dataclasses
import functools
import json
import queue
import random
import socket
import ssl
import threading
import time
import typing

import httpx
import pydantic

from ..core.api_error import ApiError
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as

__all__ = [
    "AsyncLiveStream",
    "CLOSED_EVENT",
    "DEFAULT_MAX_BACKOFF",
    "DEFAULT_WAIT_FOR_TIMEOUT",
    "EVENT_STREAM",
    "LiveStream",
    "OnDisconnect",
    "SNAPSHOT_EVENT",
    "StreamClosedError",
    "StreamEndedError",
    "WaitForFailedError",
    "WaitForTimeoutError",
    "async_wait_for",
    "async_watch",
    "backoff_seconds",
    "resource",
    "wait_for",
    "watch",
]

T = typing.TypeVar("T")
C = typing.TypeVar("C")

SNAPSHOT_EVENT = "stream.snapshot"
CLOSED_EVENT = "stream.closed"
EVENT_STREAM = "text/event-stream"
DEFAULT_MAX_BACKOFF = 30.0
DEFAULT_WAIT_FOR_TIMEOUT = 30.0

_FINAL_CLOSE_REASONS = frozenset({"not_live", "unreadable"})
_RETRIED_CLIENT_ERRORS = frozenset({408, 429})
_DROPS = (httpx.TimeoutException, httpx.NetworkError, httpx.RemoteProtocolError)
_SOCKET_PER_RESPONSE = frozenset({"HTTP/1.0", "HTTP/1.1"})
_STEADY_CONNECTION_SECONDS = 30.0
_clock = time.monotonic

OnDisconnect = typing.Callable[[Exception], None]


class StreamClosedError(Exception):
    """The stream closed for good: ``not_live`` with the status the read now answers, or ``unreadable``."""

    def __init__(self, reason: str, status: typing.Optional[int] = None) -> None:
        super().__init__(
            f"The stream closed: {reason}" if status is None else f"The stream closed: {reason} ({status})"
        )
        self.reason = reason
        self.status = status


class StreamEndedError(Exception):
    """The stream ended without a ``stream.closed`` event: ``watch`` passes it to ``on_disconnect`` and reconnects."""

    def __init__(self) -> None:
        super().__init__("The stream ended without a stream.closed event")


class WaitForTimeoutError(TimeoutError):
    def __init__(self, timeout: float) -> None:
        super().__init__(f"No answer matched within {timeout:g} seconds")
        self.timeout = timeout


class WaitForFailedError(Exception):
    def __init__(self, answer: typing.Any) -> None:
        super().__init__("An answer matched fail_when")
        self.answer = answer


def backoff_seconds(
    attempt: int,
    max_backoff: float = DEFAULT_MAX_BACKOFF,
    jitter: typing.Optional[typing.Callable[[], float]] = None,
) -> float:
    """The wait before reconnect ``attempt``: a random 0 to 1 second (at most ``max_backoff``) for attempt 0, then 1
    second doubling up to ``max_backoff``, plus up to 25%. ``watch`` starts the count over after a connection that
    stayed open at least 30 seconds."""
    fraction = (jitter or random.random)()
    if attempt <= 0:
        return min(max_backoff, 1.0) * fraction
    # Past 2**64 seconds every cap is reached, and a much larger power no longer fits in a float.
    base = min(max_backoff, float(2 ** min(attempt - 1, 64)))
    return base + base * 0.25 * fraction


def resource(parent: object, client: typing.Callable[..., C]) -> C:
    """The resource client under ``parent``, built once from the parent's client wrapper."""
    built: typing.Dict[typing.Any, typing.Any] = parent.__dict__.setdefault("_live_resources", {})
    if client not in built:
        built[client] = client(client_wrapper=getattr(parent, "_client_wrapper"))
    return typing.cast(C, built[client])


@functools.lru_cache(maxsize=None)
def _answer_of(read: typing.Callable[..., typing.Any]) -> typing.Any:
    return typing.get_type_hints(read)["return"]


@dataclasses.dataclass(frozen=True)
class _WatchOptions:
    max_backoff: float = DEFAULT_MAX_BACKOFF
    on_disconnect: typing.Optional[OnDisconnect] = None


@dataclasses.dataclass(frozen=True)
class _WaitForOptions:
    watch: _WatchOptions = _WatchOptions()
    timeout: typing.Optional[float] = DEFAULT_WAIT_FOR_TIMEOUT
    fail_when: typing.Optional[typing.Callable[[typing.Any], bool]] = None


def watch(
    read: typing.Callable[..., T],
    arguments: typing.Mapping[str, typing.Any],
    *,
    max_backoff: float = DEFAULT_MAX_BACKOFF,
    on_disconnect: typing.Optional[OnDisconnect] = None,
) -> LiveStream[T]:
    """The answer of ``read(**arguments)`` now and each time it changes, until it is closed or closes for good.

    ``read`` is a resource client's bound read method. ``on_disconnect`` observes each drop before the reconnect;
    ``max_backoff`` caps the wait between reconnects.
    """
    live = _LiveRead(*_bound(read))
    options = _WatchOptions(max_backoff=max_backoff, on_disconnect=on_disconnect)
    return LiveStream(live, live.watch(_Call((), dict(arguments)), options))


def wait_for(
    read: typing.Callable[..., T],
    arguments: typing.Mapping[str, typing.Any],
    *,
    until: typing.Callable[[T], bool],
    fail_when: typing.Optional[typing.Callable[[T], bool]] = None,
    timeout: typing.Optional[float] = DEFAULT_WAIT_FOR_TIMEOUT,
    max_backoff: float = DEFAULT_MAX_BACKOFF,
    on_disconnect: typing.Optional[OnDisconnect] = None,
) -> T:
    """The first answer of ``read(**arguments)`` that ``until`` accepts, the current one included.

    Raises ``WaitForFailedError`` on the first answer ``fail_when`` accepts (checked first), ``WaitForTimeoutError``
    once ``timeout`` seconds pass (``None`` waits indefinitely), and ``StreamClosedError`` when the read stops being
    live first. The stream is read on a background thread, so ``on_disconnect`` runs there; its connection closes as
    this returns.
    """
    live = _LiveRead(*_bound(read))
    options = _WaitForOptions(
        watch=_WatchOptions(max_backoff=max_backoff, on_disconnect=on_disconnect),
        timeout=timeout,
        fail_when=fail_when,
    )
    return typing.cast(T, live.wait_for(_Call((), dict(arguments)), until, options))


def async_watch(
    read: typing.Callable[..., typing.Awaitable[T]],
    arguments: typing.Mapping[str, typing.Any],
    *,
    max_backoff: float = DEFAULT_MAX_BACKOFF,
    on_disconnect: typing.Optional[OnDisconnect] = None,
) -> AsyncLiveStream[T]:
    """``watch`` for ``AsyncWhop``."""
    live = _AsyncLiveRead(*_bound(read))
    options = _WatchOptions(max_backoff=max_backoff, on_disconnect=on_disconnect)
    return AsyncLiveStream(live, live.watch(_Call((), dict(arguments)), options))


async def async_wait_for(
    read: typing.Callable[..., typing.Awaitable[T]],
    arguments: typing.Mapping[str, typing.Any],
    *,
    until: typing.Callable[[T], bool],
    fail_when: typing.Optional[typing.Callable[[T], bool]] = None,
    timeout: typing.Optional[float] = DEFAULT_WAIT_FOR_TIMEOUT,
    max_backoff: float = DEFAULT_MAX_BACKOFF,
    on_disconnect: typing.Optional[OnDisconnect] = None,
) -> T:
    """``wait_for`` for ``AsyncWhop``. Cancelling the task awaiting it raises ``asyncio.CancelledError``."""
    live = _AsyncLiveRead(*_bound(read))
    options = _WaitForOptions(
        watch=_WatchOptions(max_backoff=max_backoff, on_disconnect=on_disconnect),
        timeout=timeout,
        fail_when=fail_when,
    )
    return typing.cast(T, await live.wait_for(_Call((), dict(arguments)), until, options))


class LiveStream(typing.Generic[T]):
    """What ``watch`` returns: iterate it for the read's answer now and each time it changes.

    ``close()`` stops it at once, from any thread: a loop over it ends without an error, and a connection waiting
    between events closes. A ``with`` block closes it on the way out.
    """

    def __init__(self, live: _LiveRead, answers: typing.Generator[typing.Any, None, None]) -> None:
        self._live = live
        self._answers = answers
        self._reading = threading.Lock()

    def __iter__(self) -> LiveStream[T]:
        return self

    def __next__(self) -> T:
        with self._reading:
            return typing.cast(T, next(self._answers))

    def close(self) -> None:
        # A read in progress ends on its own once stopped and closes its response as it does; one between
        # events is closed here, so its response does not wait for the next `next` to go back to the pool.
        self._live.stop()
        if self._reading.acquire(blocking=False):
            try:
                self._answers.close()
            finally:
                self._reading.release()

    def __enter__(self) -> LiveStream[T]:
        return self

    def __exit__(self, *_exception: object) -> None:
        self.close()


class AsyncLiveStream(typing.Generic[T]):
    """What ``watch`` returns on ``AsyncWhop``: ``async for`` it for the read's answer now and each time it changes.

    ``await aclose()`` stops it at once, from any task, as does cancelling the task iterating it: a loop over it ends
    and a connection waiting between events closes. An ``async with`` block closes it on the way out.
    """

    def __init__(self, live: _AsyncLiveRead, answers: typing.AsyncGenerator[typing.Any, None]) -> None:
        self._live = live
        self._answers = answers
        self._reading = asyncio.Lock()

    def __aiter__(self) -> AsyncLiveStream[T]:
        return self

    async def __anext__(self) -> T:
        async with self._reading:
            return typing.cast(T, await self._answers.__anext__())

    async def aclose(self) -> None:
        # As close() does: a read in progress ends on its own once stopped, one between events is closed here.
        await self._live.stop()
        if not self._reading.locked():
            async with self._reading:
                await self._answers.aclose()

    async def __aenter__(self) -> AsyncLiveStream[T]:
        return self

    async def __aexit__(self, *_exception: object) -> None:
        await self.aclose()


def _bound(
    read: typing.Callable[..., typing.Any],
) -> typing.Tuple[typing.Any, typing.Callable[..., typing.Any], typing.Any]:
    client = getattr(read, "__self__", None)
    function = getattr(read, "__func__", None)
    if client is None or function is None:
        raise TypeError("watch and wait_for read through a resource client's bound read method")
    return client, function, _answer_of(function)


@dataclasses.dataclass(frozen=True)
class _Call:
    args: typing.Tuple[typing.Any, ...]
    kwargs: typing.Dict[str, typing.Any]

    def sent_once(self) -> typing.Dict[str, typing.Any]:
        options = dict(self.kwargs.get("request_options") or {})
        options["max_retries"] = 0
        return {**self.kwargs, "request_options": options}


@dataclasses.dataclass(frozen=True)
class _Answer:
    value: typing.Any


@dataclasses.dataclass(frozen=True)
class _Closed:
    reason: str
    status: typing.Optional[int]


_Event = typing.Union[_Answer, _Closed]


class _Captured(Exception):
    def __init__(self, request: httpx.Request) -> None:
        super().__init__(f"{request.method} {request.url}")
        self.request = request


class _Capture:
    """Stands in for the httpx client under the generated client: builds the request the read sends, then stops."""

    def __init__(self, client: httpx.Client) -> None:
        self._client = client

    def request(self, **arguments: typing.Any) -> typing.NoReturn:
        raise _Captured(self._client.build_request(**arguments))


class _AsyncCapture:
    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def request(self, **arguments: typing.Any) -> typing.NoReturn:
        raise _Captured(self._client.build_request(**arguments))


class _Replay:
    """Stands in for the httpx client to hand the read a response already received, so the read itself parses it."""

    def __init__(self, response: httpx.Response) -> None:
        self._response = response

    def request(self, **_arguments: typing.Any) -> httpx.Response:
        return self._response


class _AsyncReplay:
    def __init__(self, response: httpx.Response) -> None:
        self._response = response

    async def request(self, **_arguments: typing.Any) -> httpx.Response:
        return self._response


def _wrapper(client: typing.Any) -> typing.Any:
    return client._raw_client._client_wrapper


def _through(client: typing.Any, stand_in: object) -> typing.Any:
    wrapper = copy.copy(_wrapper(client))
    http = copy.copy(wrapper.httpx_client)
    http.httpx_client = stand_in
    wrapper.httpx_client = http
    return type(client)(client_wrapper=wrapper)


def _httpx_client(client: typing.Any) -> typing.Any:
    return _wrapper(client).httpx_client.httpx_client


def _captured(request: typing.Optional[httpx.Request]) -> httpx.Request:
    if request is None:
        raise RuntimeError("The read returned without building a request")
    request.headers["Accept"] = EVENT_STREAM
    return request


def _is_event_stream(response: httpx.Response) -> bool:
    return response.is_success and EVENT_STREAM in response.headers.get("content-type", "")


class _EventParser:
    def __init__(self) -> None:
        self._name = ""
        self._data: typing.List[str] = []

    def feed(self, line: str) -> typing.Optional[typing.Tuple[str, str]]:
        if line == "":
            name, data = self._name or "message", self._data
            self._name, self._data = "", []
            return (name, "\n".join(data)) if data else None
        if line.startswith(":"):
            return None
        field, _, value = line.partition(":")
        value = value[1:] if value.startswith(" ") else value
        if field == "event":
            self._name = value
        elif field == "data":
            self._data.append(value)
        return None


def _event(name: str, data: str, answer: typing.Any, response: httpx.Response) -> typing.Optional[_Event]:
    if name == CLOSED_EVENT:
        try:
            closed: object = json.loads(data)
        except ValueError:
            closed = None
        fields = typing.cast(typing.Dict[str, object], closed) if isinstance(closed, dict) else {}
        reason, status = fields.get("reason"), fields.get("status")
        return _Closed(reason if isinstance(reason, str) else "unknown", status if isinstance(status, int) else None)
    if name != SNAPSHOT_EVENT:
        return None
    body: object = data
    try:
        body = json.loads(data)
        return _Answer(parse_obj_as(answer, body))
    except (ValueError, pydantic.ValidationError) as error:
        raise ParsingError(
            status_code=response.status_code, headers=dict(response.headers), body=body, cause=error
        ) from error


def _ends(closed: _Closed) -> bool:
    if closed.reason == "not_live" and (closed.status is None or 200 <= closed.status < 300):
        return True
    if closed.reason in _FINAL_CLOSE_REASONS:
        raise StreamClosedError(closed.reason, closed.status)
    return False


def _steady(connected: typing.Optional[float]) -> bool:
    """Whether the dropped connection's event stream was open at least 30 seconds; a connect that failed
    or hung, however long, opened none."""
    return connected is not None and _clock() - connected >= _STEADY_CONNECTION_SECONDS


def _pause(stopped: threading.Event, seconds: float) -> bool:
    """Waits ``seconds`` before a reconnect, or until the stream is stopped; returns whether it was."""
    return stopped.wait(seconds)


async def _apause(stopped: asyncio.Event, seconds: float) -> bool:
    with contextlib.suppress(asyncio.TimeoutError):
        await asyncio.wait_for(stopped.wait(), seconds)
    return stopped.is_set()


def _interrupt(response: httpx.Response) -> None:
    """Ends a read another thread is blocked in on ``response``.

    An HTTP/1 response has its socket to itself: shutting it down wakes a blocked read on every platform, where
    closing it alone does not on Linux, and the reading thread closes the response as it ends. Closing it here as well
    races that thread's next read, which can then block for good. An HTTP/2 connection's socket carries the client's
    other requests, so there, as on a transport that exposes no socket, the response is closed instead.
    """
    own_socket = response.http_version in _SOCKET_PER_RESPONSE
    network_stream = response.extensions.get("network_stream") if own_socket else None
    sock = network_stream.get_extra_info("socket") if network_stream is not None else None
    if sock is not None:
        with contextlib.suppress(OSError):
            sock.shutdown(socket.SHUT_RDWR)
            return
    with contextlib.suppress(Exception):
        response.close()


def _is_drop(error: Exception) -> bool:
    if isinstance(error, StreamEndedError):
        return True
    if isinstance(error, _DROPS):
        return not _fails_verification(error)
    status = error.status_code if isinstance(error, ApiError) else None
    if status is None or 200 <= status < 300:
        return False
    return not _final(status)


def _final(status: int) -> bool:
    """A client error a reconnect would get again, which fails the read."""
    return 400 <= status < 500 and status not in _RETRIED_CLIENT_ERRORS


def _read_answer(response: httpx.Response) -> httpx.Response:
    """``response`` read in full, or, when a final status's body drops partway, that status with an empty JSON body:
    the read raises its own error for the status either way, where a drop would reconnect and get it again."""
    try:
        response.read()
    except _DROPS:
        if not _final(response.status_code):
            raise
        return _empty_error(response)
    return response


async def _aread_answer(response: httpx.Response) -> httpx.Response:
    try:
        await response.aread()
    except _DROPS:
        if not _final(response.status_code):
            raise
        return _empty_error(response)
    return response


def _empty_error(response: httpx.Response) -> httpx.Response:
    """``response``'s status with ``{}`` as its body: the read decodes an error body as JSON before it picks the
    error for the status, and falls back to a generic ApiError when it cannot."""
    dropped = {"content-length", "content-encoding", "transfer-encoding", "content-type"}
    headers = [(name, value) for name, value in response.headers.multi_items() if name.lower() not in dropped]
    headers.append(("content-type", "application/json"))
    return httpx.Response(response.status_code, headers=headers, content=b"{}", request=response.request)


def _fails_verification(error: BaseException) -> bool:
    """A server whose certificate fails verification fails it again on every reconnect."""
    cause: typing.Optional[BaseException] = error
    while cause is not None:
        if isinstance(cause, ssl.SSLCertVerificationError):
            return True
        cause = cause.__cause__ or cause.__context__
    return False


class _LiveRead:
    def __init__(self, client: typing.Any, read: typing.Callable[..., typing.Any], answer: typing.Any) -> None:
        self._client = client
        self._read = read
        self._answer = answer
        self._stopped = threading.Event()
        self._lock = threading.Lock()
        self._connected: typing.Optional[float] = None
        self._sending: typing.Optional[concurrent.futures.Future[httpx.Response]] = None
        self._response: typing.Optional[httpx.Response] = None

    def stop(self) -> None:
        self._stopped.set()
        with self._lock:
            sending, response = self._sending, self._response
        if sending is not None:
            sending.cancel()
        if response is not None:
            _interrupt(response)

    def watch(self, call: _Call, options: _WatchOptions) -> typing.Generator[typing.Any, None, None]:
        attempt = 0
        while not self._stopped.is_set():
            self._connected = None
            try:
                with contextlib.closing(self._connect(call)) as events:
                    for event in events:
                        if isinstance(event, _Closed):
                            if _ends(event):
                                return
                            break
                        yield event.value
            except Exception as error:
                if self._stopped.is_set():
                    return
                if not _is_drop(error):
                    raise
                if options.on_disconnect is not None:
                    options.on_disconnect(error)
            if _steady(self._connected):
                attempt = 0
            if _pause(self._stopped, backoff_seconds(attempt, options.max_backoff)):
                return
            attempt += 1

    def wait_for(
        self, call: _Call, predicate: typing.Callable[[typing.Any], bool], options: _WaitForOptions
    ) -> typing.Any:
        arrivals: queue.Queue[typing.Union[_Answer, BaseException]] = queue.Queue()

        def pump() -> None:
            try:
                with contextlib.closing(self.watch(call, options.watch)) as answers:
                    for answer in answers:
                        arrivals.put(_Answer(answer))
                arrivals.put(StreamClosedError("not_live"))
            except BaseException as error:
                arrivals.put(error)

        context = contextvars.copy_context()
        threading.Thread(target=context.run, args=(pump,), name="whop-live-wait-for", daemon=True).start()
        deadline = None if options.timeout is None else time.monotonic() + options.timeout
        try:
            while True:
                remaining = None if deadline is None else max(0.0, deadline - time.monotonic())
                try:
                    arrival = arrivals.get(timeout=remaining)
                except queue.Empty:
                    raise WaitForTimeoutError(options.timeout or 0.0) from None
                if isinstance(arrival, BaseException):
                    raise arrival
                if options.fail_when is not None and options.fail_when(arrival.value):
                    raise WaitForFailedError(arrival.value)
                if predicate(arrival.value):
                    return arrival.value
        finally:
            self.stop()

    def _connect(self, call: _Call) -> typing.Generator[_Event, None, None]:
        http = _httpx_client(self._client)
        request: typing.Optional[httpx.Request] = None
        try:
            self._read(_through(self._client, _Capture(http)), *call.args, **call.sent_once())
        except _Captured as captured:
            request = captured.request
        response = self._send(http, _captured(request))
        if response is None:
            return
        with self._lock:
            self._response = response
        try:
            if self._stopped.is_set():
                return
            if not _is_event_stream(response):
                answered = _read_answer(response)
                yield _Answer(self._read(_through(self._client, _Replay(answered)), *call.args, **call.sent_once()))
                yield _Closed("not_live", response.status_code)
                return
            self._connected = _clock()
            parser = _EventParser()
            for line in response.iter_lines():
                if self._stopped.is_set():
                    return
                parsed = parser.feed(line)
                event = None if parsed is None else _event(*parsed, self._answer, response)
                if event is not None:
                    yield event
                    if isinstance(event, _Closed):
                        return
            raise StreamEndedError()
        finally:
            with self._lock:
                self._response = None
            response.close()

    def _send(self, http: typing.Any, request: httpx.Request) -> typing.Optional[httpx.Response]:
        """Sends ``request`` on a helper thread, so that stop() ends the wait for its response: httpx cannot interrupt
        a send from another thread. Answers None once stopped, and closes a response that arrives after that."""
        sending: concurrent.futures.Future[httpx.Response] = concurrent.futures.Future()

        def send() -> None:
            try:
                response = http.send(request, stream=True)
            except BaseException as error:
                with contextlib.suppress(concurrent.futures.InvalidStateError):
                    sending.set_exception(error)
                return
            try:
                sending.set_result(response)
            except concurrent.futures.InvalidStateError:
                response.close()

        with self._lock:
            self._sending = sending
        try:
            if self._stopped.is_set():
                return None
            context = contextvars.copy_context()
            threading.Thread(target=context.run, args=(send,), name="whop-live-connect", daemon=True).start()
            try:
                return sending.result()
            except concurrent.futures.CancelledError:
                return None
        finally:
            with self._lock:
                self._sending = None


async def _close(response: httpx.Response) -> None:
    """Closes ``response`` to the end, shielded: a cancel that arrives again during the close, as anyio's
    level-triggered cancellation does at every await, cannot leave the connection open."""

    async def close() -> None:
        with contextlib.suppress(Exception):
            await response.aclose()

    await asyncio.shield(close())


async def _close_when_sent(sending: asyncio.Task[httpx.Response]) -> None:
    """Waits out a send the caller gave up on, and closes the response it got anyway. Shielded by the caller, so a
    second cancel cannot cut the close short."""
    try:
        response = await sending
    except (asyncio.CancelledError, Exception):
        return
    await response.aclose()


class _AsyncLiveRead:
    def __init__(self, client: typing.Any, read: typing.Callable[..., typing.Any], answer: typing.Any) -> None:
        self._client = client
        self._read = read
        self._answer = answer
        self._stopped = asyncio.Event()
        self._connected: typing.Optional[float] = None
        self._sending: typing.Optional[asyncio.Task[httpx.Response]] = None
        self._response: typing.Optional[httpx.Response] = None

    async def stop(self) -> None:
        self._stopped.set()
        if self._sending is not None:
            self._sending.cancel()
        response = self._response
        if response is not None:
            await _close(response)

    async def watch(self, call: _Call, options: _WatchOptions) -> typing.AsyncGenerator[typing.Any, None]:
        attempt = 0
        while not self._stopped.is_set():
            self._connected = None
            try:
                async with contextlib.aclosing(self._connect(call)) as events:
                    async for event in events:
                        if isinstance(event, _Closed):
                            if _ends(event):
                                return
                            break
                        yield event.value
            except Exception as error:
                if self._stopped.is_set():
                    return
                if not _is_drop(error):
                    raise
                if options.on_disconnect is not None:
                    options.on_disconnect(error)
            if _steady(self._connected):
                attempt = 0
            if await _apause(self._stopped, backoff_seconds(attempt, options.max_backoff)):
                return
            attempt += 1

    async def wait_for(
        self, call: _Call, predicate: typing.Callable[[typing.Any], bool], options: _WaitForOptions
    ) -> typing.Any:
        async def first_match() -> typing.Any:
            async with contextlib.aclosing(self.watch(call, options.watch)) as answers:
                async for answer in answers:
                    if options.fail_when is not None and options.fail_when(answer):
                        raise WaitForFailedError(answer)
                    if predicate(answer):
                        return answer
            raise StreamClosedError("not_live")

        matching = asyncio.ensure_future(first_match())
        try:
            done, _pending = await asyncio.wait({matching}, timeout=options.timeout)
            if not done:
                raise WaitForTimeoutError(options.timeout or 0.0)
            return matching.result()
        finally:
            matching.cancel()
            await asyncio.gather(matching, return_exceptions=True)

    async def _connect(self, call: _Call) -> typing.AsyncGenerator[_Event, None]:
        http = _httpx_client(self._client)
        request: typing.Optional[httpx.Request] = None
        try:
            await self._read(_through(self._client, _AsyncCapture(http)), *call.args, **call.sent_once())
        except _Captured as captured:
            request = captured.request
        response = await self._send(http, _captured(request))
        if response is None:
            return
        self._response = response
        try:
            if self._stopped.is_set():
                return
            if not _is_event_stream(response):
                replayed = _through(self._client, _AsyncReplay(await _aread_answer(response)))
                yield _Answer(await self._read(replayed, *call.args, **call.sent_once()))
                yield _Closed("not_live", response.status_code)
                return
            self._connected = _clock()
            parser = _EventParser()
            async for line in response.aiter_lines():
                if self._stopped.is_set():
                    return
                parsed = parser.feed(line)
                event = None if parsed is None else _event(*parsed, self._answer, response)
                if event is not None:
                    yield event
                    if isinstance(event, _Closed):
                        return
            raise StreamEndedError()
        finally:
            self._response = None
            await _close(response)

    async def _send(self, http: typing.Any, request: httpx.Request) -> typing.Optional[httpx.Response]:
        """Sends ``request`` as a task stop() cancels; answers None once stopped."""
        if self._stopped.is_set():
            return None
        sending: asyncio.Task[httpx.Response] = asyncio.ensure_future(http.send(request, stream=True))
        self._sending = sending
        try:
            await asyncio.wait({sending})
        except BaseException:
            sending.cancel()
            await asyncio.shield(_close_when_sent(sending))
            raise
        finally:
            self._sending = None
        if sending.cancelled():
            return None
        return sending.result()
