# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    IdentityProfile,
    IdentityProfileListResponse,
    IdentityProfileListVerificationsResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentityProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        identity_profile = client.identity_profiles.retrieve(
            "idpf_xxxxxxxxxxxxx",
        )
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.identity_profiles.with_raw_response.retrieve(
            "idpf_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = response.parse()
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.identity_profiles.with_streaming_response.retrieve(
            "idpf_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = response.parse()
            assert_matches_type(IdentityProfile, identity_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.identity_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        identity_profile = client.identity_profiles.list()
        assert_matches_type(SyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        identity_profile = client.identity_profiles.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            first=42,
            last=42,
            profile_type="individual",
            status="not_started",
        )
        assert_matches_type(SyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.identity_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = response.parse()
        assert_matches_type(SyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.identity_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = response.parse()
            assert_matches_type(SyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        identity_profile = client.identity_profiles.delete(
            id="idpf_xxxxxxxxxxxxx",
            ledger_account_id="ldgr_xxxxxxxxxxxxx",
        )
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.identity_profiles.with_raw_response.delete(
            id="idpf_xxxxxxxxxxxxx",
            ledger_account_id="ldgr_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = response.parse()
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.identity_profiles.with_streaming_response.delete(
            id="idpf_xxxxxxxxxxxxx",
            ledger_account_id="ldgr_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = response.parse()
            assert_matches_type(IdentityProfile, identity_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.identity_profiles.with_raw_response.delete(
                id="",
                ledger_account_id="ldgr_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_verifications(self, client: Whop) -> None:
        identity_profile = client.identity_profiles.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            SyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_verifications_with_all_params(self, client: Whop) -> None:
        identity_profile = client.identity_profiles.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(
            SyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_verifications(self, client: Whop) -> None:
        response = client.identity_profiles.with_raw_response.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = response.parse()
        assert_matches_type(
            SyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_verifications(self, client: Whop) -> None:
        with client.identity_profiles.with_streaming_response.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = response.parse()
            assert_matches_type(
                SyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_verifications(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.identity_profiles.with_raw_response.list_verifications(
                id="",
            )


class TestAsyncIdentityProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        identity_profile = await async_client.identity_profiles.retrieve(
            "idpf_xxxxxxxxxxxxx",
        )
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.identity_profiles.with_raw_response.retrieve(
            "idpf_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = await response.parse()
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.identity_profiles.with_streaming_response.retrieve(
            "idpf_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = await response.parse()
            assert_matches_type(IdentityProfile, identity_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.identity_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        identity_profile = await async_client.identity_profiles.list()
        assert_matches_type(AsyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        identity_profile = await async_client.identity_profiles.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            first=42,
            last=42,
            profile_type="individual",
            status="not_started",
        )
        assert_matches_type(AsyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.identity_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = await response.parse()
        assert_matches_type(AsyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.identity_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = await response.parse()
            assert_matches_type(AsyncCursorPage[IdentityProfileListResponse], identity_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        identity_profile = await async_client.identity_profiles.delete(
            id="idpf_xxxxxxxxxxxxx",
            ledger_account_id="ldgr_xxxxxxxxxxxxx",
        )
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.identity_profiles.with_raw_response.delete(
            id="idpf_xxxxxxxxxxxxx",
            ledger_account_id="ldgr_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = await response.parse()
        assert_matches_type(IdentityProfile, identity_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.identity_profiles.with_streaming_response.delete(
            id="idpf_xxxxxxxxxxxxx",
            ledger_account_id="ldgr_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = await response.parse()
            assert_matches_type(IdentityProfile, identity_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.identity_profiles.with_raw_response.delete(
                id="",
                ledger_account_id="ldgr_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_verifications(self, async_client: AsyncWhop) -> None:
        identity_profile = await async_client.identity_profiles.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
        )
        assert_matches_type(
            AsyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_verifications_with_all_params(self, async_client: AsyncWhop) -> None:
        identity_profile = await async_client.identity_profiles.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
        )
        assert_matches_type(
            AsyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_verifications(self, async_client: AsyncWhop) -> None:
        response = await async_client.identity_profiles.with_raw_response.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_profile = await response.parse()
        assert_matches_type(
            AsyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_verifications(self, async_client: AsyncWhop) -> None:
        async with async_client.identity_profiles.with_streaming_response.list_verifications(
            id="idpf_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_profile = await response.parse()
            assert_matches_type(
                AsyncCursorPage[IdentityProfileListVerificationsResponse], identity_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_verifications(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.identity_profiles.with_raw_response.list_verifications(
                id="",
            )
