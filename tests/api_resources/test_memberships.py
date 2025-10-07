# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import (
    MembershipListResponse,
)
from whopsdk.pagination import SyncCursorPage, AsyncCursorPage
from whopsdk.types.shared import Membership

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whopsdk) -> None:
        membership = client.memberships.retrieve(
            "mem_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.memberships.with_raw_response.retrieve(
            "mem_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
        with client.memberships.with_streaming_response.retrieve(
            "mem_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whopsdk) -> None:
        membership = client.memberships.update(
            id="mem_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whopsdk) -> None:
        membership = client.memberships.update(
            id="mem_xxxxxxxxxxxxxx",
            metadata={},
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whopsdk) -> None:
        response = client.memberships.with_raw_response.update(
            id="mem_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whopsdk) -> None:
        with client.memberships.with_streaming_response.update(
            id="mem_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        membership = client.memberships.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
        membership = client.memberships.list(
            company_id="biz_xxxxxxxxxxxxxx",
            access_pass_ids=["string"],
            after="after",
            before="before",
            cancel_options=["too_expensive"],
            created_after=1701406800,
            created_before=1701406800,
            direction="asc",
            first=42,
            last=42,
            order="id",
            plan_ids=["string"],
            promo_code_ids=["string"],
            statuses=["trialing"],
        )
        assert_matches_type(SyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.memberships.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(SyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.memberships.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(SyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Whopsdk) -> None:
        membership = client.memberships.cancel(
            id="mem_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Whopsdk) -> None:
        membership = client.memberships.cancel(
            id="mem_xxxxxxxxxxxxxx",
            cancellation_mode="at_period_end",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Whopsdk) -> None:
        response = client.memberships.with_raw_response.cancel(
            id="mem_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Whopsdk) -> None:
        with client.memberships.with_streaming_response.cancel(
            id="mem_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.cancel(
                id="",
            )


class TestAsyncMemberships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.retrieve(
            "mem_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.memberships.with_raw_response.retrieve(
            "mem_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.memberships.with_streaming_response.retrieve(
            "mem_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.update(
            id="mem_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.update(
            id="mem_xxxxxxxxxxxxxx",
            metadata={},
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.memberships.with_raw_response.update(
            id="mem_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.memberships.with_streaming_response.update(
            id="mem_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.list(
            company_id="biz_xxxxxxxxxxxxxx",
            access_pass_ids=["string"],
            after="after",
            before="before",
            cancel_options=["too_expensive"],
            created_after=1701406800,
            created_before=1701406800,
            direction="asc",
            first=42,
            last=42,
            order="id",
            plan_ids=["string"],
            promo_code_ids=["string"],
            statuses=["trialing"],
        )
        assert_matches_type(AsyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.memberships.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(AsyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.memberships.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(AsyncCursorPage[Optional[MembershipListResponse]], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.cancel(
            id="mem_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        membership = await async_client.memberships.cancel(
            id="mem_xxxxxxxxxxxxxx",
            cancellation_mode="at_period_end",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.memberships.with_raw_response.cancel(
            id="mem_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.memberships.with_streaming_response.cancel(
            id="mem_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.cancel(
                id="",
            )
