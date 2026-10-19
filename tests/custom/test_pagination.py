import json
from pathlib import Path
from typing import List, Optional

import httpx
import pytest

from whop_sdk.client import AsyncWhop, Whop
from whop_sdk.core.pagination import AsyncPager, SyncPager

PAGE_SEQUENCES = [
    [[], [], ["pay_0"], []],
    [["pay_19"], [], ["pay_0"], []],
    [None, [], ["pay_0"], None],
    [[], [], []],
    [["pay_2", "pay_1"], ["pay_0"]],
]


def sync_pager(pages: List[Optional[List[str]]], index: int = 0) -> SyncPager[str, int]:
    return SyncPager(
        get_next=lambda: sync_pager(pages, index + 1),
        has_next=index + 1 < len(pages),
        items=pages[index],
        response=index,
    )


def async_pager(pages: List[Optional[List[str]]], index: int = 0) -> AsyncPager[str, int]:
    async def get_next() -> AsyncPager[str, int]:
        return async_pager(pages, index + 1)

    return AsyncPager(
        get_next=get_next,
        has_next=index + 1 < len(pages),
        items=pages[index],
        response=index,
    )


@pytest.mark.parametrize("pages", PAGE_SEQUENCES)
def test_sync_iteration_follows_continuation_through_empty_pages(pages: List[Optional[List[str]]]) -> None:
    pager = sync_pager(pages)

    assert list(pager) == [item for page in pages for item in page or []]
    assert [page.items for page in pager.iter_pages()] == pages


@pytest.mark.parametrize("pages", PAGE_SEQUENCES)
async def test_async_iteration_follows_continuation_through_empty_pages(pages: List[Optional[List[str]]]) -> None:
    pager = async_pager(pages)

    assert [item async for item in pager] == [item for page in pages for item in page or []]
    assert [page.items async for page in pager.iter_pages()] == pages


def test_sync_iteration_stops_when_the_next_page_is_absent() -> None:
    pager: SyncPager[str, None] = SyncPager(get_next=lambda: None, has_next=True, items=["pay_0"], response=None)

    assert list(pager) == ["pay_0"]


async def test_async_iteration_stops_when_the_next_page_is_absent() -> None:
    async def get_next() -> None:
        return None

    pager: AsyncPager[str, None] = AsyncPager(get_next=get_next, has_next=True, items=["pay_0"], response=None)

    assert [item async for item in pager] == ["pay_0"]


def test_pagination_fix_and_regressions_survive_regeneration() -> None:
    root = Path(__file__).resolve().parents[2]
    protected = (root / ".fernignore").read_text().splitlines()

    assert "src/whop_sdk/core/pagination.py" in protected
    assert "tests/custom" in protected


def delivery_transport(cursors: List[Optional[str]]) -> httpx.MockTransport:
    pages = json.loads((Path(__file__).parent / "fixtures" / "webhook_delivery_pages.json").read_text())

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/webhooks/hook_test/deliveries")
        assert request.url.params["status"] == "error"
        assert request.url.params["first"] == "1"
        cursor = request.url.params.get("after")
        cursors.append(cursor)
        return httpx.Response(200, json=pages[int(cursor) if cursor is not None else 0])

    return httpx.MockTransport(handle)


def test_webhook_client_preserves_filters_across_empty_pages() -> None:
    cursors: List[Optional[str]] = []
    with httpx.Client(transport=delivery_transport(cursors)) as http_client:
        client = Whop(token="test", httpx_client=http_client)
        deliveries = client.webhooks.list_deliveries(
            "hook_test", first=1, request_options={"additional_query_parameters": {"status": "error"}}
        )
        assert [delivery.resource_id for delivery in deliveries] == ["pay_0"]

    assert cursors == [None, "1", "2", "3"]


async def test_async_webhook_client_preserves_filters_across_empty_pages() -> None:
    cursors: List[Optional[str]] = []
    async with httpx.AsyncClient(transport=delivery_transport(cursors)) as http_client:
        client = AsyncWhop(token="test", httpx_client=http_client)
        deliveries = await client.webhooks.list_deliveries(
            "hook_test", first=1, request_options={"additional_query_parameters": {"status": "error"}}
        )
        assert [delivery.resource_id async for delivery in deliveries] == ["pay_0"]

    assert cursors == [None, "1", "2", "3"]
