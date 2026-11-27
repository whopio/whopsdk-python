"""Type-checked, never run: the functions each live client's ``watch`` and ``wait_for`` call give the read's answer
type and take only their own options.

Every line marked with an ignore must be an error under both mypy (``--warn-unused-ignores``) and pyright
(``reportUnnecessaryTypeIgnoreComment``), and every ``assert_type`` must hold.
"""

from typing_extensions import assert_type

from whop_sdk.lib import live


class Answer:
    total: int


class Reads:
    def retrieve(self, metric: str) -> Answer:
        raise NotImplementedError


class AsyncReads:
    async def retrieve(self, metric: str) -> Answer:
        raise NotImplementedError


def check_watch(reads: Reads) -> None:
    for answer in live.watch(reads.retrieve, {"metric": "gmv"}, max_backoff=5):
        assert_type(answer, Answer)
    with live.watch(reads.retrieve, {"metric": "gmv"}) as stream:
        assert_type(stream, live.LiveStream[Answer])
        stream.close()
    assert_type(live.wait_for(reads.retrieve, {"metric": "gmv"}, until=lambda answer: answer.total > 0), Answer)
    live.watch(reads.retrieve, {"metric": "gmv"}, not_an_option=1)  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
    live.wait_for(reads.retrieve, {"metric": "gmv"})  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
    live.wait_for(reads.retrieve, {"metric": "gmv"}, until=lambda answer: answer.not_a_field)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]


async def check_async_watch(reads: AsyncReads) -> None:
    async for answer in live.async_watch(reads.retrieve, {"metric": "gmv"}):
        assert_type(answer, Answer)
    async with live.async_watch(reads.retrieve, {"metric": "gmv"}) as stream:
        assert_type(stream, live.AsyncLiveStream[Answer])
        await stream.aclose()
    assert_type(await live.async_wait_for(reads.retrieve, {"metric": "gmv"}, until=lambda answer: True), Answer)
    await live.async_wait_for(reads.retrieve, {"metric": "gmv"}, until=lambda answer: answer.not_a_field)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
