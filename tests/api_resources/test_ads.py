# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import AdListResponse, AdCreateResponse, AdRetrieveResponse
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        ad = client.ads.create(
            ad_group_id="ad_group_id",
        )
        assert_matches_type(AdCreateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        ad = client.ads.create(
            ad_group_id="ad_group_id",
            creative_set_id="creative_set_id",
            existing_instagram_media_id="existing_instagram_media_id",
            existing_post_id="existing_post_id",
            platform_config={
                "meta": {
                    "call_to_action_type": "LEARN_MORE",
                    "carousel_cards": [
                        {
                            "call_to_action_type": "call_to_action_type",
                            "description": "description",
                            "link": "link",
                            "name": "name",
                        }
                    ],
                    "description": "description",
                    "descriptions": ["string"],
                    "existing_instagram_media_id": "existing_instagram_media_id",
                    "existing_post_id": "existing_post_id",
                    "headline": "headline",
                    "headlines": ["string"],
                    "instagram_actor_id": "instagram_actor_id",
                    "lead_form_config": {"foo": "bar"},
                    "link_url": "link_url",
                    "multi_advertiser_enrollment": "OPT_IN",
                    "name": "name",
                    "page_id": "page_id",
                    "page_welcome_message": {"foo": "bar"},
                    "primary_text": "primary_text",
                    "primary_texts": ["string"],
                    "url_tags": "url_tags",
                },
                "tiktok": {
                    "access_pass_tag": "access_pass_tag",
                    "ad_format": "SINGLE_IMAGE",
                    "ad_name": "ad_name",
                    "ad_text": "ad_text",
                    "ad_texts": ["string"],
                    "aigc_disclosure_type": "UNSET",
                    "auto_disclaimer_types": ["string"],
                    "automate_creative_enabled": True,
                    "brand_safety_postbid_partner": "UNSET",
                    "brand_safety_vast_url": "brand_safety_vast_url",
                    "call_to_action": "LEARN_MORE",
                    "call_to_action_enabled": True,
                    "call_to_action_id": "call_to_action_id",
                    "call_to_action_mode": "STANDARD",
                    "card_id": "card_id",
                    "carousel_image_index": 42,
                    "catalog_id": "catalog_id",
                    "click_tracking_url": "click_tracking_url",
                    "cpp_url": "cpp_url",
                    "creative_authorized": True,
                    "creative_auto_enhancement_strategy_list": ["string"],
                    "dark_post_status": "ON",
                    "deeplink": "deeplink",
                    "deeplink_format_type": "UNSET",
                    "deeplink_type": "deeplink_type",
                    "deeplink_utm_params": [{"foo": "bar"}],
                    "disclaimer_clickable_texts": [{"foo": "bar"}],
                    "disclaimer_text": "disclaimer_text",
                    "disclaimer_type": "NONE",
                    "dynamic_destination": "dynamic_destination",
                    "dynamic_format": "dynamic_format",
                    "end_card_cta": "end_card_cta",
                    "fallback_type": "UNSET",
                    "identity_authorized_bc_id": "identity_authorized_bc_id",
                    "identity_id": "identity_id",
                    "identity_type": "CUSTOMIZED_USER",
                    "image_ids": ["string"],
                    "impression_tracking_url": "impression_tracking_url",
                    "item_duet_status": "ENABLE",
                    "item_group_ids": ["string"],
                    "item_stitch_status": "ENABLE",
                    "landing_page_url": "landing_page_url",
                    "link_url": "link_url",
                    "music_id": "music_id",
                    "page_id": "page_id",
                    "product_display_field_list": ["string"],
                    "product_set_id": "product_set_id",
                    "product_specific_type": "product_specific_type",
                    "promotional_music_disabled": True,
                    "shopping_ads_fallback_type": "UNSET",
                    "shopping_ads_video_package_id": "shopping_ads_video_package_id",
                    "showcase_products": [{"foo": "bar"}],
                    "sku_ids": ["string"],
                    "tiktok_item_id": "tiktok_item_id",
                    "tracking_app_id": "tracking_app_id",
                    "tracking_message_event_set_id": "tracking_message_event_set_id",
                    "tracking_offline_event_set_ids": ["string"],
                    "tracking_pixel_id": "trpx_xxxxxxxxxxxxx",
                    "utm_params": [{"foo": "bar"}],
                    "vertical_video_strategy": "vertical_video_strategy",
                    "video_id": "video_id",
                    "video_view_tracking_url": "video_view_tracking_url",
                    "viewability_postbid_partner": "UNSET",
                    "viewability_vast_url": "viewability_vast_url",
                },
            },
            status="active",
        )
        assert_matches_type(AdCreateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.ads.with_raw_response.create(
            ad_group_id="ad_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdCreateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.ads.with_streaming_response.create(
            ad_group_id="ad_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdCreateResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad = client.ads.retrieve(
            "xad_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ads.with_raw_response.retrieve(
            "xad_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ads.with_streaming_response.retrieve(
            "xad_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdRetrieveResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        ad = client.ads.list()
        assert_matches_type(SyncCursorPage[AdListResponse], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ad = client.ads.list(
            ad_group_id="ad_group_id",
            after="after",
            before="before",
            campaign_id="campaign_id",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            status="active",
        )
        assert_matches_type(SyncCursorPage[AdListResponse], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(SyncCursorPage[AdListResponse], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(SyncCursorPage[AdListResponse], ad, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.create(
            ad_group_id="ad_group_id",
        )
        assert_matches_type(AdCreateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.create(
            ad_group_id="ad_group_id",
            creative_set_id="creative_set_id",
            existing_instagram_media_id="existing_instagram_media_id",
            existing_post_id="existing_post_id",
            platform_config={
                "meta": {
                    "call_to_action_type": "LEARN_MORE",
                    "carousel_cards": [
                        {
                            "call_to_action_type": "call_to_action_type",
                            "description": "description",
                            "link": "link",
                            "name": "name",
                        }
                    ],
                    "description": "description",
                    "descriptions": ["string"],
                    "existing_instagram_media_id": "existing_instagram_media_id",
                    "existing_post_id": "existing_post_id",
                    "headline": "headline",
                    "headlines": ["string"],
                    "instagram_actor_id": "instagram_actor_id",
                    "lead_form_config": {"foo": "bar"},
                    "link_url": "link_url",
                    "multi_advertiser_enrollment": "OPT_IN",
                    "name": "name",
                    "page_id": "page_id",
                    "page_welcome_message": {"foo": "bar"},
                    "primary_text": "primary_text",
                    "primary_texts": ["string"],
                    "url_tags": "url_tags",
                },
                "tiktok": {
                    "access_pass_tag": "access_pass_tag",
                    "ad_format": "SINGLE_IMAGE",
                    "ad_name": "ad_name",
                    "ad_text": "ad_text",
                    "ad_texts": ["string"],
                    "aigc_disclosure_type": "UNSET",
                    "auto_disclaimer_types": ["string"],
                    "automate_creative_enabled": True,
                    "brand_safety_postbid_partner": "UNSET",
                    "brand_safety_vast_url": "brand_safety_vast_url",
                    "call_to_action": "LEARN_MORE",
                    "call_to_action_enabled": True,
                    "call_to_action_id": "call_to_action_id",
                    "call_to_action_mode": "STANDARD",
                    "card_id": "card_id",
                    "carousel_image_index": 42,
                    "catalog_id": "catalog_id",
                    "click_tracking_url": "click_tracking_url",
                    "cpp_url": "cpp_url",
                    "creative_authorized": True,
                    "creative_auto_enhancement_strategy_list": ["string"],
                    "dark_post_status": "ON",
                    "deeplink": "deeplink",
                    "deeplink_format_type": "UNSET",
                    "deeplink_type": "deeplink_type",
                    "deeplink_utm_params": [{"foo": "bar"}],
                    "disclaimer_clickable_texts": [{"foo": "bar"}],
                    "disclaimer_text": "disclaimer_text",
                    "disclaimer_type": "NONE",
                    "dynamic_destination": "dynamic_destination",
                    "dynamic_format": "dynamic_format",
                    "end_card_cta": "end_card_cta",
                    "fallback_type": "UNSET",
                    "identity_authorized_bc_id": "identity_authorized_bc_id",
                    "identity_id": "identity_id",
                    "identity_type": "CUSTOMIZED_USER",
                    "image_ids": ["string"],
                    "impression_tracking_url": "impression_tracking_url",
                    "item_duet_status": "ENABLE",
                    "item_group_ids": ["string"],
                    "item_stitch_status": "ENABLE",
                    "landing_page_url": "landing_page_url",
                    "link_url": "link_url",
                    "music_id": "music_id",
                    "page_id": "page_id",
                    "product_display_field_list": ["string"],
                    "product_set_id": "product_set_id",
                    "product_specific_type": "product_specific_type",
                    "promotional_music_disabled": True,
                    "shopping_ads_fallback_type": "UNSET",
                    "shopping_ads_video_package_id": "shopping_ads_video_package_id",
                    "showcase_products": [{"foo": "bar"}],
                    "sku_ids": ["string"],
                    "tiktok_item_id": "tiktok_item_id",
                    "tracking_app_id": "tracking_app_id",
                    "tracking_message_event_set_id": "tracking_message_event_set_id",
                    "tracking_offline_event_set_ids": ["string"],
                    "tracking_pixel_id": "trpx_xxxxxxxxxxxxx",
                    "utm_params": [{"foo": "bar"}],
                    "vertical_video_strategy": "vertical_video_strategy",
                    "video_id": "video_id",
                    "video_view_tracking_url": "video_view_tracking_url",
                    "viewability_postbid_partner": "UNSET",
                    "viewability_vast_url": "viewability_vast_url",
                },
            },
            status="active",
        )
        assert_matches_type(AdCreateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.create(
            ad_group_id="ad_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdCreateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.create(
            ad_group_id="ad_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdCreateResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.retrieve(
            "xad_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.retrieve(
            "xad_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdRetrieveResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.retrieve(
            "xad_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdRetrieveResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.list()
        assert_matches_type(AsyncCursorPage[AdListResponse], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.list(
            ad_group_id="ad_group_id",
            after="after",
            before="before",
            campaign_id="campaign_id",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            status="active",
        )
        assert_matches_type(AsyncCursorPage[AdListResponse], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AsyncCursorPage[AdListResponse], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AsyncCursorPage[AdListResponse], ad, path=["response"])

        assert cast(Any, response.is_closed) is True
