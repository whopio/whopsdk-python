# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import AdCampaign
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.retrieve(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.retrieve(
            id="id",
            attribution_model="last_touch",
            stats_from="stats_from",
            stats_to="stats_to",
            time_zone="time_zone",
            api_version_date="2026-08-31",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ad_campaigns.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ad_campaigns.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_campaigns.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.update(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.update(
            id="id",
            bid_type="average_target",
            budget_amount=40,
            budget_optimization="ad_campaign",
            budget_type="daily",
            ends_at="2026-01-01T12:00:00.000Z",
            special_ad_categories=["employment"],
            starts_at="2026-01-01T12:00:00.000Z",
            status="active",
            title="Now hiring mobile detailers — Austin & Round Rock",
            api_version_date="2026-08-31",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.ad_campaigns.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.ad_campaigns.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_campaigns.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.list()
        assert_matches_type(SyncCursorPage[AdCampaign], ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.list(
            account_id="account_id",
            after="after",
            attribution_model="last_touch",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            query="query",
            stats_from="stats_from",
            stats_to="stats_to",
            status="draft",
            time_zone="time_zone",
            api_version_date="2026-08-31",
        )
        assert_matches_type(SyncCursorPage[AdCampaign], ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ad_campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = response.parse()
        assert_matches_type(SyncCursorPage[AdCampaign], ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ad_campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = response.parse()
            assert_matches_type(SyncCursorPage[AdCampaign], ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.pause(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause_with_all_params(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.pause(
            id="id",
            api_version_date="2026-08-31",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Whop) -> None:
        response = client.ad_campaigns.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Whop) -> None:
        with client.ad_campaigns.with_streaming_response.pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_campaigns.with_raw_response.pause(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.unpause(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause_with_all_params(self, client: Whop) -> None:
        ad_campaign = client.ad_campaigns.unpause(
            id="id",
            api_version_date="2026-08-31",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpause(self, client: Whop) -> None:
        response = client.ad_campaigns.with_raw_response.unpause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpause(self, client: Whop) -> None:
        with client.ad_campaigns.with_streaming_response.unpause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_campaigns.with_raw_response.unpause(
                id="",
            )


class TestAsyncAdCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.retrieve(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.retrieve(
            id="id",
            attribution_model="last_touch",
            stats_from="stats_from",
            stats_to="stats_to",
            time_zone="time_zone",
            api_version_date="2026-08-31",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_campaigns.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = await response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_campaigns.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = await response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_campaigns.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.update(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.update(
            id="id",
            bid_type="average_target",
            budget_amount=40,
            budget_optimization="ad_campaign",
            budget_type="daily",
            ends_at="2026-01-01T12:00:00.000Z",
            special_ad_categories=["employment"],
            starts_at="2026-01-01T12:00:00.000Z",
            status="active",
            title="Now hiring mobile detailers — Austin & Round Rock",
            api_version_date="2026-08-31",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_campaigns.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = await response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_campaigns.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = await response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_campaigns.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.list()
        assert_matches_type(AsyncCursorPage[AdCampaign], ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.list(
            account_id="account_id",
            after="after",
            attribution_model="last_touch",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            query="query",
            stats_from="stats_from",
            stats_to="stats_to",
            status="draft",
            time_zone="time_zone",
            api_version_date="2026-08-31",
        )
        assert_matches_type(AsyncCursorPage[AdCampaign], ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = await response.parse()
        assert_matches_type(AsyncCursorPage[AdCampaign], ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = await response.parse()
            assert_matches_type(AsyncCursorPage[AdCampaign], ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.pause(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.pause(
            id="id",
            api_version_date="2026-08-31",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_campaigns.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = await response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_campaigns.with_streaming_response.pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = await response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_campaigns.with_raw_response.pause(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.unpause(
            id="id",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_campaign = await async_client.ad_campaigns.unpause(
            id="id",
            api_version_date="2026-08-31",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_campaigns.with_raw_response.unpause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_campaign = await response.parse()
        assert_matches_type(AdCampaign, ad_campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_campaigns.with_streaming_response.unpause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_campaign = await response.parse()
            assert_matches_type(AdCampaign, ad_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_campaigns.with_raw_response.unpause(
                id="",
            )
