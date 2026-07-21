# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    AdGroup,
    ReachEstimate,
    AdGroupDeleteResponse,
    AdGroupSearchTargetingOptionsResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        ad_group = client.ad_groups.create(
            ad_campaign_id="ad_campaign_id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.create(
            ad_campaign_id="ad_campaign_id",
            audiences={
                "exclude": ["string"],
                "include": ["string"],
            },
            bid_type="minimum_cost",
            budget_amount=0,
            budget_type="daily",
            conversion_event="purchase",
            conversion_location="website",
            demographics={
                "automatic": True,
                "gender": "all",
                "maximum_age": 0,
                "minimum_age": 0,
            },
            desired_cost_per_result=0,
            detailed_targeting={
                "behaviors": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
                "demographics": [
                    {
                        "id": "id",
                        "type": "life_events",
                        "name": "name",
                    }
                ],
                "interests": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
            },
            devices={
                "operating_systems": [
                    {
                        "os": "ios",
                        "minimum_version": "minimum_version",
                    }
                ],
                "platforms": ["mobile"],
            },
            dynamic_creative=True,
            ends_at="ends_at",
            frequency_cap={
                "maximum_impressions": 0,
                "per_days": 0,
            },
            languages=["string"],
            message_apps=["messenger"],
            minimum_daily_spend=0,
            optimization_goal="conversions",
            placements="automatic",
            regions={
                "exclude": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
                "include": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
            },
            starts_at="starts_at",
            status="active",
            title="title",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.create(
            ad_campaign_id="ad_campaign_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.create(
            ad_campaign_id="ad_campaign_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad_group = client.ad_groups.retrieve(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.retrieve(
            id="id",
            stats_from="stats_from",
            stats_to="stats_to",
            time_zone="time_zone",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        ad_group = client.ad_groups.update(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.update(
            id="id",
            audiences={
                "exclude": ["string"],
                "include": ["string"],
            },
            bid_type="minimum_cost",
            budget_amount=0,
            budget_type="daily",
            conversion_event="purchase",
            conversion_location="website",
            demographics={
                "automatic": True,
                "gender": "all",
                "maximum_age": 0,
                "minimum_age": 0,
            },
            desired_cost_per_result=0,
            detailed_targeting={
                "behaviors": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
                "demographics": [
                    {
                        "id": "id",
                        "type": "life_events",
                        "name": "name",
                    }
                ],
                "interests": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
            },
            devices={
                "operating_systems": [
                    {
                        "os": "ios",
                        "minimum_version": "minimum_version",
                    }
                ],
                "platforms": ["mobile"],
            },
            ends_at="ends_at",
            frequency_cap={
                "maximum_impressions": 0,
                "per_days": 0,
            },
            languages=["string"],
            message_apps=["messenger"],
            minimum_daily_spend=0,
            optimization_goal="conversions",
            placements="automatic",
            regions={
                "exclude": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
                "include": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
            },
            starts_at="starts_at",
            status="active",
            title="title",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        ad_group = client.ad_groups.list()
        assert_matches_type(SyncCursorPage[AdGroup], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.list(
            account_id="account_id",
            ad_campaign_id="ad_campaign_id",
            after="after",
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
            status="active",
            time_zone="time_zone",
        )
        assert_matches_type(SyncCursorPage[AdGroup], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(SyncCursorPage[AdGroup], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(SyncCursorPage[AdGroup], ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        ad_group = client.ad_groups.delete(
            "id",
        )
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_estimate_reach(self, client: Whop) -> None:
        ad_group = client.ad_groups.estimate_reach(
            platform="meta",
        )
        assert_matches_type(ReachEstimate, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_estimate_reach_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.estimate_reach(
            platform="meta",
            account_id="account_id",
            audiences={
                "exclude": ["string"],
                "include": ["string"],
            },
            demographics={
                "automatic": True,
                "gender": "all",
                "maximum_age": 0,
                "minimum_age": 0,
            },
            detailed_targeting={
                "behaviors": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
                "demographics": [
                    {
                        "id": "id",
                        "type": "life_events",
                        "name": "name",
                    }
                ],
                "interests": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
            },
            devices={
                "operating_systems": [
                    {
                        "os": "ios",
                        "minimum_version": "minimum_version",
                    }
                ],
                "platforms": ["mobile"],
            },
            languages=["string"],
            regions={
                "exclude": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
                "include": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
            },
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ReachEstimate, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_estimate_reach(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.estimate_reach(
            platform="meta",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(ReachEstimate, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_estimate_reach(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.estimate_reach(
            platform="meta",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(ReachEstimate, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Whop) -> None:
        ad_group = client.ad_groups.pause(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.pause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.pause(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_targeting_options(self, client: Whop) -> None:
        ad_group = client.ad_groups.search_targeting_options(
            platform="meta",
        )
        assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_targeting_options_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.search_targeting_options(
            platform="meta",
            account_id="account_id",
            country="country",
            limit=500,
            location_types=["country"],
            query="query",
            types=["interests"],
        )
        assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_targeting_options(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.search_targeting_options(
            platform="meta",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_targeting_options(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.search_targeting_options(
            platform="meta",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause(self, client: Whop) -> None:
        ad_group = client.ad_groups.unpause(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.unpause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpause(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.unpause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpause(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.unpause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.unpause(
                id="",
            )


class TestAsyncAdGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.create(
            ad_campaign_id="ad_campaign_id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.create(
            ad_campaign_id="ad_campaign_id",
            audiences={
                "exclude": ["string"],
                "include": ["string"],
            },
            bid_type="minimum_cost",
            budget_amount=0,
            budget_type="daily",
            conversion_event="purchase",
            conversion_location="website",
            demographics={
                "automatic": True,
                "gender": "all",
                "maximum_age": 0,
                "minimum_age": 0,
            },
            desired_cost_per_result=0,
            detailed_targeting={
                "behaviors": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
                "demographics": [
                    {
                        "id": "id",
                        "type": "life_events",
                        "name": "name",
                    }
                ],
                "interests": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
            },
            devices={
                "operating_systems": [
                    {
                        "os": "ios",
                        "minimum_version": "minimum_version",
                    }
                ],
                "platforms": ["mobile"],
            },
            dynamic_creative=True,
            ends_at="ends_at",
            frequency_cap={
                "maximum_impressions": 0,
                "per_days": 0,
            },
            languages=["string"],
            message_apps=["messenger"],
            minimum_daily_spend=0,
            optimization_goal="conversions",
            placements="automatic",
            regions={
                "exclude": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
                "include": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
            },
            starts_at="starts_at",
            status="active",
            title="title",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.create(
            ad_campaign_id="ad_campaign_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.create(
            ad_campaign_id="ad_campaign_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.retrieve(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.retrieve(
            id="id",
            stats_from="stats_from",
            stats_to="stats_to",
            time_zone="time_zone",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.update(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.update(
            id="id",
            audiences={
                "exclude": ["string"],
                "include": ["string"],
            },
            bid_type="minimum_cost",
            budget_amount=0,
            budget_type="daily",
            conversion_event="purchase",
            conversion_location="website",
            demographics={
                "automatic": True,
                "gender": "all",
                "maximum_age": 0,
                "minimum_age": 0,
            },
            desired_cost_per_result=0,
            detailed_targeting={
                "behaviors": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
                "demographics": [
                    {
                        "id": "id",
                        "type": "life_events",
                        "name": "name",
                    }
                ],
                "interests": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
            },
            devices={
                "operating_systems": [
                    {
                        "os": "ios",
                        "minimum_version": "minimum_version",
                    }
                ],
                "platforms": ["mobile"],
            },
            ends_at="ends_at",
            frequency_cap={
                "maximum_impressions": 0,
                "per_days": 0,
            },
            languages=["string"],
            message_apps=["messenger"],
            minimum_daily_spend=0,
            optimization_goal="conversions",
            placements="automatic",
            regions={
                "exclude": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
                "include": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
            },
            starts_at="starts_at",
            status="active",
            title="title",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.list()
        assert_matches_type(AsyncCursorPage[AdGroup], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.list(
            account_id="account_id",
            ad_campaign_id="ad_campaign_id",
            after="after",
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
            status="active",
            time_zone="time_zone",
        )
        assert_matches_type(AsyncCursorPage[AdGroup], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AsyncCursorPage[AdGroup], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AsyncCursorPage[AdGroup], ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.delete(
            "id",
        )
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_estimate_reach(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.estimate_reach(
            platform="meta",
        )
        assert_matches_type(ReachEstimate, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_estimate_reach_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.estimate_reach(
            platform="meta",
            account_id="account_id",
            audiences={
                "exclude": ["string"],
                "include": ["string"],
            },
            demographics={
                "automatic": True,
                "gender": "all",
                "maximum_age": 0,
                "minimum_age": 0,
            },
            detailed_targeting={
                "behaviors": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
                "demographics": [
                    {
                        "id": "id",
                        "type": "life_events",
                        "name": "name",
                    }
                ],
                "interests": [
                    {
                        "id": "id",
                        "name": "name",
                    }
                ],
            },
            devices={
                "operating_systems": [
                    {
                        "os": "ios",
                        "minimum_version": "minimum_version",
                    }
                ],
                "platforms": ["mobile"],
            },
            languages=["string"],
            regions={
                "exclude": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
                "include": {
                    "cities": [
                        {
                            "key": "key",
                            "name": "name",
                        }
                    ],
                    "countries": ["string"],
                    "country_groups": ["string"],
                    "custom_locations": [
                        {
                            "latitude": 0,
                            "longitude": 0,
                            "radius": 0,
                            "distance_unit": "mile",
                            "name": "name",
                        }
                    ],
                    "regions": ["string"],
                    "zips": ["string"],
                },
            },
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ReachEstimate, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_estimate_reach(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.estimate_reach(
            platform="meta",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(ReachEstimate, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_estimate_reach(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.estimate_reach(
            platform="meta",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(ReachEstimate, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.pause(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.pause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.pause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.pause(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_targeting_options(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.search_targeting_options(
            platform="meta",
        )
        assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_targeting_options_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.search_targeting_options(
            platform="meta",
            account_id="account_id",
            country="country",
            limit=500,
            location_types=["country"],
            query="query",
            types=["interests"],
        )
        assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_targeting_options(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.search_targeting_options(
            platform="meta",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_targeting_options(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.search_targeting_options(
            platform="meta",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroupSearchTargetingOptionsResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.unpause(
            id="id",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.unpause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.unpause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroup, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.unpause(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroup, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.unpause(
                id="",
            )
