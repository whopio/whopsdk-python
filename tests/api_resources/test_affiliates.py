# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Affiliate,
    AffiliateListResponse,
    AffiliateArchiveResponse,
    AffiliateUnarchiveResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAffiliates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        affiliate = client.affiliates.create(
            company_id="biz_xxxxxxxxxxxxxx",
            user_identifier="user_identifier",
        )
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.affiliates.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            user_identifier="user_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = response.parse()
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.affiliates.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            user_identifier="user_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = response.parse()
            assert_matches_type(Affiliate, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        affiliate = client.affiliates.retrieve(
            "aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.affiliates.with_raw_response.retrieve(
            "aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = response.parse()
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.affiliates.with_streaming_response.retrieve(
            "aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = response.parse()
            assert_matches_type(Affiliate, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        affiliate = client.affiliates.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        affiliate = client.affiliates.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            direction="asc",
            first=42,
            last=42,
            order="id",
            query="query",
            status="active",
        )
        assert_matches_type(SyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.affiliates.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = response.parse()
        assert_matches_type(SyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.affiliates.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = response.parse()
            assert_matches_type(SyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Whop) -> None:
        affiliate = client.affiliates.archive(
            "aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AffiliateArchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Whop) -> None:
        response = client.affiliates.with_raw_response.archive(
            "aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = response.parse()
        assert_matches_type(AffiliateArchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Whop) -> None:
        with client.affiliates.with_streaming_response.archive(
            "aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = response.parse()
            assert_matches_type(AffiliateArchiveResponse, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Whop) -> None:
        affiliate = client.affiliates.unarchive(
            "aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AffiliateUnarchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Whop) -> None:
        response = client.affiliates.with_raw_response.unarchive(
            "aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = response.parse()
        assert_matches_type(AffiliateUnarchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Whop) -> None:
        with client.affiliates.with_streaming_response.unarchive(
            "aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = response.parse()
            assert_matches_type(AffiliateUnarchiveResponse, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.with_raw_response.unarchive(
                "",
            )


class TestAsyncAffiliates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        affiliate = await async_client.affiliates.create(
            company_id="biz_xxxxxxxxxxxxxx",
            user_identifier="user_identifier",
        )
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            user_identifier="user_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = await response.parse()
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            user_identifier="user_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = await response.parse()
            assert_matches_type(Affiliate, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        affiliate = await async_client.affiliates.retrieve(
            "aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.with_raw_response.retrieve(
            "aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = await response.parse()
        assert_matches_type(Affiliate, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.with_streaming_response.retrieve(
            "aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = await response.parse()
            assert_matches_type(Affiliate, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        affiliate = await async_client.affiliates.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        affiliate = await async_client.affiliates.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            direction="asc",
            first=42,
            last=42,
            order="id",
            query="query",
            status="active",
        )
        assert_matches_type(AsyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = await response.parse()
        assert_matches_type(AsyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = await response.parse()
            assert_matches_type(AsyncCursorPage[AffiliateListResponse], affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncWhop) -> None:
        affiliate = await async_client.affiliates.archive(
            "aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AffiliateArchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.with_raw_response.archive(
            "aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = await response.parse()
        assert_matches_type(AffiliateArchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.with_streaming_response.archive(
            "aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = await response.parse()
            assert_matches_type(AffiliateArchiveResponse, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncWhop) -> None:
        affiliate = await async_client.affiliates.unarchive(
            "aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AffiliateUnarchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.with_raw_response.unarchive(
            "aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        affiliate = await response.parse()
        assert_matches_type(AffiliateUnarchiveResponse, affiliate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.with_streaming_response.unarchive(
            "aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            affiliate = await response.parse()
            assert_matches_type(AffiliateUnarchiveResponse, affiliate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.with_raw_response.unarchive(
                "",
            )
