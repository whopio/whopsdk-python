# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    MembershipInviteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Membership

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        membership = client.memberships.retrieve(
            "id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        membership = client.memberships.update(
            id="id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        membership = client.memberships.update(
            id="id",
            cancel_at_period_end=True,
            metadata={"seat": "42"},
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        membership = client.memberships.list()
        assert_matches_type(SyncCursorPage[Membership], membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        membership = client.memberships.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            plan_id="plan_id",
            product_id="product_id",
            status="active",
            user_id="user_id",
        )
        assert_matches_type(SyncCursorPage[Membership], membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(SyncCursorPage[Membership], membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(SyncCursorPage[Membership], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Whop) -> None:
        membership = client.memberships.cancel(
            id="id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Whop) -> None:
        membership = client.memberships.cancel(
            id="id",
            reason="chargeback risk",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.cancel(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.cancel(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.cancel(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extend(self, client: Whop) -> None:
        membership = client.memberships.extend(
            id="id",
            days=7,
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extend(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.extend(
            id="id",
            days=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extend(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.extend(
            id="id",
            days=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_extend(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.extend(
                id="",
                days=7,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invite_overload_1(self, client: Whop) -> None:
        membership = client.memberships.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invite_with_all_params_overload_1(self, client: Whop) -> None:
        membership = client.memberships.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
            email="  Dana@Shinetime.example ",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_invite_overload_1(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_invite_overload_1(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipInviteResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invite_overload_2(self, client: Whop) -> None:
        membership = client.memberships.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invite_with_all_params_overload_2(self, client: Whop) -> None:
        membership = client.memberships.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_invite_overload_2(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_invite_overload_2(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipInviteResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Whop) -> None:
        membership = client.memberships.pause(
            id="id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause_with_all_params(self, client: Whop) -> None:
        membership = client.memberships.pause(
            id="id",
            until="2026-01-01T12:00:00.000Z",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.pause(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resume(self, client: Whop) -> None:
        membership = client.memberships.resume(
            "id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resume(self, client: Whop) -> None:
        response = client.memberships.with_raw_response.resume(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resume(self, client: Whop) -> None:
        with client.memberships.with_streaming_response.resume(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_resume(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memberships.with_raw_response.resume(
                "",
            )


class TestAsyncMemberships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.retrieve(
            "id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.update(
            id="id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.update(
            id="id",
            cancel_at_period_end=True,
            metadata={"seat": "42"},
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.list()
        assert_matches_type(AsyncCursorPage[Membership], membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            plan_id="plan_id",
            product_id="product_id",
            status="active",
            user_id="user_id",
        )
        assert_matches_type(AsyncCursorPage[Membership], membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(AsyncCursorPage[Membership], membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(AsyncCursorPage[Membership], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.cancel(
            id="id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.cancel(
            id="id",
            reason="chargeback risk",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.cancel(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.cancel(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.cancel(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extend(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.extend(
            id="id",
            days=7,
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extend(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.extend(
            id="id",
            days=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extend(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.extend(
            id="id",
            days=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_extend(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.extend(
                id="",
                days=7,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invite_overload_1(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invite_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
            email="  Dana@Shinetime.example ",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_invite_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_invite_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.invite(
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipInviteResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invite_overload_2(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invite_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
            user_id="user_xxxxxxxxxxxxxx",
        )
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_invite_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipInviteResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_invite_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.invite(
            email="  Dana@Shinetime.example ",
            plan_id="plan_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipInviteResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.pause(
            id="id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause_with_all_params(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.pause(
            id="id",
            until="2026-01-01T12:00:00.000Z",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.pause(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resume(self, async_client: AsyncWhop) -> None:
        membership = await async_client.memberships.resume(
            "id",
        )
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncWhop) -> None:
        response = await async_client.memberships.with_raw_response.resume(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(Membership, membership, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncWhop) -> None:
        async with async_client.memberships.with_streaming_response.resume(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(Membership, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_resume(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memberships.with_raw_response.resume(
                "",
            )
