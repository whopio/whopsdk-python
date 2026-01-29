# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    DmMemberListResponse,
    DmMemberCreateResponse,
    DmMemberDeleteResponse,
    DmMemberUpdateResponse,
    DmMemberRetrieveResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDmMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        dm_member = client.dm_members.create(
            channel_id="channel_id",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(DmMemberCreateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.dm_members.with_raw_response.create(
            channel_id="channel_id",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = response.parse()
        assert_matches_type(DmMemberCreateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.dm_members.with_streaming_response.create(
            channel_id="channel_id",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = response.parse()
            assert_matches_type(DmMemberCreateResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        dm_member = client.dm_members.retrieve(
            "id",
        )
        assert_matches_type(DmMemberRetrieveResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.dm_members.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = response.parse()
        assert_matches_type(DmMemberRetrieveResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.dm_members.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = response.parse()
            assert_matches_type(DmMemberRetrieveResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dm_members.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        dm_member = client.dm_members.update(
            id="id",
        )
        assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        dm_member = client.dm_members.update(
            id="id",
            notification_preference="all",
            status="requested",
        )
        assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.dm_members.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = response.parse()
        assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.dm_members.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = response.parse()
            assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dm_members.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        dm_member = client.dm_members.list(
            channel_id="channel_id",
        )
        assert_matches_type(SyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        dm_member = client.dm_members.list(
            channel_id="channel_id",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.dm_members.with_raw_response.list(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = response.parse()
        assert_matches_type(SyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.dm_members.with_streaming_response.list(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = response.parse()
            assert_matches_type(SyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        dm_member = client.dm_members.delete(
            "id",
        )
        assert_matches_type(DmMemberDeleteResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.dm_members.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = response.parse()
        assert_matches_type(DmMemberDeleteResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.dm_members.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = response.parse()
            assert_matches_type(DmMemberDeleteResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dm_members.with_raw_response.delete(
                "",
            )


class TestAsyncDmMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.create(
            channel_id="channel_id",
            user_id="user_xxxxxxxxxxxxx",
        )
        assert_matches_type(DmMemberCreateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.dm_members.with_raw_response.create(
            channel_id="channel_id",
            user_id="user_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = await response.parse()
        assert_matches_type(DmMemberCreateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.dm_members.with_streaming_response.create(
            channel_id="channel_id",
            user_id="user_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = await response.parse()
            assert_matches_type(DmMemberCreateResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.retrieve(
            "id",
        )
        assert_matches_type(DmMemberRetrieveResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.dm_members.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = await response.parse()
        assert_matches_type(DmMemberRetrieveResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.dm_members.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = await response.parse()
            assert_matches_type(DmMemberRetrieveResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dm_members.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.update(
            id="id",
        )
        assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.update(
            id="id",
            notification_preference="all",
            status="requested",
        )
        assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.dm_members.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = await response.parse()
        assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.dm_members.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = await response.parse()
            assert_matches_type(DmMemberUpdateResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dm_members.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.list(
            channel_id="channel_id",
        )
        assert_matches_type(AsyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.list(
            channel_id="channel_id",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.dm_members.with_raw_response.list(
            channel_id="channel_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = await response.parse()
        assert_matches_type(AsyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.dm_members.with_streaming_response.list(
            channel_id="channel_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = await response.parse()
            assert_matches_type(AsyncCursorPage[DmMemberListResponse], dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        dm_member = await async_client.dm_members.delete(
            "id",
        )
        assert_matches_type(DmMemberDeleteResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.dm_members.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm_member = await response.parse()
        assert_matches_type(DmMemberDeleteResponse, dm_member, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.dm_members.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm_member = await response.parse()
            assert_matches_type(DmMemberDeleteResponse, dm_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dm_members.with_raw_response.delete(
                "",
            )
