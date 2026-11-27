"""Each live read's ``watch`` and ``wait_for`` take exactly the read's parameters, then their own options, and
``watch`` sends exactly the request the read sends, with ``Accept: text/event-stream``.

``live_reads.json`` lists the live reads; the pipeline writes it from the spec. Each read and its ``watch`` are
called through one recording transport with a sample for every parameter the read takes.
"""

import collections.abc
import datetime as dt
import functools
import inspect
import json
import pathlib
import typing

import httpx
import pytest

from whop_sdk import AsyncWhop, Whop
from whop_sdk.core.api_error import ApiError
from whop_sdk.lib.live import AsyncLiveStream, LiveStream

LIVE_READS: typing.List[typing.Dict[str, typing.Any]] = json.loads(
    (pathlib.Path(__file__).parent / "live_reads.json").read_text()
)


def _sample(annotation: typing.Any, name: str) -> typing.Any:
    """A value of ``annotation``, or ``inspect.Parameter.empty`` for a type with no sample (a model)."""
    options = [option for option in typing.get_args(annotation) if option not in (type(None), typing.Any)]
    if typing.get_origin(annotation) is typing.Union:
        many = [option for option in options if typing.get_origin(option) in (list, collections.abc.Sequence)]
        return _sample((many or options)[0], name)
    if typing.get_origin(annotation) is typing.Literal:
        return options[0]
    if typing.get_origin(annotation) in (list, collections.abc.Sequence):
        return [_sample(options[0], name), _sample(options[0], f"{name} again")]
    samples: typing.Dict[typing.Any, typing.Any] = {
        str: f"{name} 1/2",
        bool: True,
        int: 7,
        float: 1.5,
        dt.datetime: dt.datetime(2026, 11, 21, 12, 30, tzinfo=dt.timezone.utc),
        dt.date: dt.date(2026, 11, 21),
    }
    return samples.get(annotation, inspect.Parameter.empty)


def _arguments(read: typing.Callable[..., typing.Any]) -> typing.Dict[str, typing.Any]:
    hints = typing.get_type_hints(read)
    arguments: typing.Dict[str, typing.Any] = {}
    for name, parameter in inspect.signature(read).parameters.items():
        if name == "request_options":
            continue
        value = _sample(hints[name], name)
        if value is inspect.Parameter.empty:
            if parameter.default is inspect.Parameter.empty:
                raise AssertionError(f"{read.__qualname__} requires {name}, a {hints[name]} with no sample")
            continue
        arguments[name] = value
    return arguments


def _recording() -> typing.Tuple[typing.List[httpx.Request], httpx.MockTransport]:
    requests: typing.List[httpx.Request] = []

    def answer(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(404, json={"error": {"message": "recorded"}})

    return requests, httpx.MockTransport(answer)


def _assert_streams_the_read(requests: typing.List[httpx.Request]) -> None:
    read, watched = requests
    assert (watched.method, str(watched.url), watched.content) == (read.method, str(read.url), read.content)
    assert _without_accept(watched) == _without_accept(read)
    assert watched.headers["accept"] == "text/event-stream"


def _without_accept(request: httpx.Request) -> typing.List[typing.Tuple[str, str]]:
    return [(name, value) for name, value in request.headers.multi_items() if name != "accept"]


WATCH_OPTIONS = ["max_backoff", "on_disconnect"]
WAIT_FOR_OPTIONS = ["until", "fail_when", "timeout", "max_backoff", "on_disconnect"]


def _parameters(
    method: typing.Callable[..., typing.Any],
) -> typing.List[typing.Tuple[str, typing.Any, typing.Any, typing.Any]]:
    hints = typing.get_type_hints(method)
    return [(name, each.kind, each.default, hints[name]) for name, each in inspect.signature(method).parameters.items()]


def _name(live: typing.Dict[str, typing.Any]) -> str:
    return ".".join([*live["resource"], live["watch"]])


@pytest.mark.parametrize("client", [Whop, AsyncWhop], ids=["Whop", "AsyncWhop"])
@pytest.mark.parametrize("live", LIVE_READS, ids=_name)
def test_watch_and_wait_for_take_their_reads_parameters_then_their_options(
    live: typing.Dict[str, typing.Any], client: typing.Callable[..., typing.Any]
) -> None:
    resource = functools.reduce(getattr, live["resource"], client(token="t"))
    read = getattr(resource, live["read"])
    watch = getattr(resource, live["watch"])
    wait_for = getattr(resource, live["wait_for"])
    parameters = _parameters(read)
    answer = typing.get_type_hints(read)["return"]

    assert _parameters(watch)[: len(parameters)] == parameters
    assert [name for name, *_ in _parameters(watch)[len(parameters) :]] == WATCH_OPTIONS
    assert _parameters(wait_for)[: len(parameters)] == parameters
    assert [name for name, *_ in _parameters(wait_for)[len(parameters) :]] == WAIT_FOR_OPTIONS
    stream = AsyncLiveStream if client is AsyncWhop else LiveStream
    assert typing.get_origin(typing.get_type_hints(watch)["return"]) is stream
    assert typing.get_args(typing.get_type_hints(watch)["return"])[0] == answer
    assert typing.get_type_hints(wait_for)["return"] == answer
    assert typing.get_args(typing.get_type_hints(wait_for)["until"]) == ([answer], bool)


@pytest.mark.parametrize("live", LIVE_READS, ids=_name)
def test_watch_sends_the_request_its_read_sends(live: typing.Dict[str, typing.Any]) -> None:
    requests, transport = _recording()
    resource = functools.reduce(
        getattr, live["resource"], Whop(token="t", httpx_client=httpx.Client(transport=transport))
    )
    arguments = _arguments(getattr(resource, live["read"]))

    with pytest.raises(ApiError):
        getattr(resource, live["read"])(**arguments)
    with pytest.raises(ApiError):
        next(getattr(resource, live["watch"])(**arguments))

    _assert_streams_the_read(requests)


@pytest.mark.parametrize("live", LIVE_READS, ids=_name)
async def test_async_watch_sends_the_request_its_read_sends(live: typing.Dict[str, typing.Any]) -> None:
    requests, transport = _recording()
    client = AsyncWhop(token="t", httpx_client=httpx.AsyncClient(transport=transport))
    resource = functools.reduce(getattr, live["resource"], client)
    arguments = _arguments(getattr(resource, live["read"]))

    with pytest.raises(ApiError):
        await getattr(resource, live["read"])(**arguments)
    with pytest.raises(ApiError):
        await getattr(resource, live["watch"])(**arguments).__anext__()

    _assert_streams_the_read(requests)
