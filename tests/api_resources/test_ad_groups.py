# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    AdGroupListResponse,
    AdGroupCreateResponse,
    AdGroupDeleteResponse,
    AdGroupUpdateResponse,
    AdGroupRetrieveResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        ad_group = client.ad_groups.create(
            campaign_id="campaign_id",
        )
        assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.create(
            campaign_id="campaign_id",
            budget=6.9,
            budget_type="daily",
            config={
                "bid_amount": 42,
                "bid_strategy": "lowest_cost",
                "billing_event": "impressions",
                "end_time": "end_time",
                "frequency_cap": 42,
                "frequency_cap_interval_days": 42,
                "optimization_goal": "conversions",
                "pacing": "standard",
                "start_time": "start_time",
                "targeting": {
                    "age_max": 42,
                    "age_min": 42,
                    "countries": ["string"],
                    "device_platforms": ["mobile"],
                    "exclude_audience_ids": ["string"],
                    "genders": ["male"],
                    "include_audience_ids": ["string"],
                    "interest_ids": ["string"],
                    "languages": ["string"],
                    "placement_type": "automatic",
                },
            },
            daily_budget=6.9,
            name="name",
            platform_config={
                "meta": {
                    "android_devices": ["string"],
                    "attribution_setting": "attribution_setting",
                    "attribution_spec": [
                        {
                            "event_type": "event_type",
                            "window_days": 42,
                        }
                    ],
                    "audience_network_positions": ["string"],
                    "audience_type": "audience_type",
                    "bid_amount": 42,
                    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
                    "billing_event": "APP_INSTALLS",
                    "brand_safety_content_filter_levels": ["string"],
                    "budget_remaining": "budget_remaining",
                    "cost_per_result_goal": 6.9,
                    "created_time": "created_time",
                    "daily_budget": 42,
                    "daily_min_spend_target": "daily_min_spend_target",
                    "daily_spend_cap": "daily_spend_cap",
                    "destination_type": "UNDEFINED",
                    "dsa_beneficiary": "dsa_beneficiary",
                    "dsa_payor": "dsa_payor",
                    "end_time": "end_time",
                    "excluded_geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "facebook_positions": ["string"],
                    "frequency_control_count": 42,
                    "frequency_control_days": 42,
                    "frequency_control_type": "frequency_control_type",
                    "geo_cities": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "geo_regions": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_zips": ["string"],
                    "instagram_actor_id": "instagram_actor_id",
                    "instagram_positions": ["string"],
                    "ios_devices": ["string"],
                    "is_dynamic_creative": True,
                    "lead_conversion_location": "website",
                    "lead_form_config": {
                        "name": "name",
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "type": "type",
                                "conditional_questions_group_id": "conditional_questions_group_id",
                                "dependent_conditional_questions": [
                                    {
                                        "type": "type",
                                        "inline_context": "inline_context",
                                        "key": "key",
                                        "label": "label",
                                        "options": [
                                            {
                                                "key": "key",
                                                "value": "value",
                                                "logic": {
                                                    "type": "type",
                                                    "target_end_page_index": 42,
                                                    "target_question_index": 42,
                                                },
                                            }
                                        ],
                                    }
                                ],
                                "inline_context": "inline_context",
                                "key": "key",
                                "label": "label",
                                "options": [
                                    {
                                        "key": "key",
                                        "value": "value",
                                        "logic": {
                                            "type": "type",
                                            "target_end_page_index": 42,
                                            "target_question_index": 42,
                                        },
                                    }
                                ],
                                "question_format": "question_format",
                            }
                        ],
                        "background_image_source": "background_image_source",
                        "background_image_url": "background_image_url",
                        "conditional_logic_enabled": True,
                        "context_card_button_text": "context_card_button_text",
                        "context_card_content": ["string"],
                        "context_card_style": "context_card_style",
                        "context_card_title": "context_card_title",
                        "custom_disclaimer_body": "custom_disclaimer_body",
                        "custom_disclaimer_checkboxes": [
                            {
                                "key": "key",
                                "text": "text",
                                "is_checked_by_default": True,
                                "is_required": True,
                            }
                        ],
                        "custom_disclaimer_title": "custom_disclaimer_title",
                        "form_type": "form_type",
                        "messenger_enabled": True,
                        "phone_verification_enabled": True,
                        "privacy_policy_link_text": "privacy_policy_link_text",
                        "question_page_custom_headline": "question_page_custom_headline",
                        "rich_creative_headline": "rich_creative_headline",
                        "rich_creative_overview": "rich_creative_overview",
                        "rich_creative_url": "rich_creative_url",
                        "thank_you_pages": [
                            {
                                "body": "body",
                                "business_phone": "business_phone",
                                "button_text": "button_text",
                                "button_type": "button_type",
                                "conditional_question_group_id": "conditional_question_group_id",
                                "enable_messenger": True,
                                "gated_file_url": "gated_file_url",
                                "link": "link",
                                "name": "name",
                                "title": "title",
                            }
                        ],
                    },
                    "lead_gen_form_id": "lead_gen_form_id",
                    "lifetime_budget": 42,
                    "lifetime_min_spend_target": "lifetime_min_spend_target",
                    "lifetime_spend_cap": "lifetime_spend_cap",
                    "location_types": ["string"],
                    "messenger_positions": ["string"],
                    "optimization_goal": "NONE",
                    "page_id": "page_id",
                    "pixel_id": "pixel_id",
                    "promoted_object": {
                        "custom_conversion_id": "custom_conversion_id",
                        "custom_event_str": "custom_event_str",
                        "custom_event_type": "custom_event_type",
                        "page_id": "page_id",
                        "pixel_id": "pixel_id",
                        "whatsapp_phone_number": "whatsapp_phone_number",
                    },
                    "publisher_platforms": ["string"],
                    "source_adset_id": "source_adset_id",
                    "start_time": "start_time",
                    "status": "ACTIVE",
                    "targeting_automation": {"advantage_audience": 42},
                    "threads_positions": ["string"],
                    "updated_time": "updated_time",
                    "user_device": ["string"],
                    "user_os": ["string"],
                    "whatsapp_phone_number": "whatsapp_phone_number",
                    "whatsapp_positions": ["string"],
                },
                "tiktok": {
                    "actions": [
                        {
                            "action_category_ids": ["string"],
                            "action_period": 42,
                            "action_scene": "VIDEO_RELATED",
                            "video_user_actions": ["WATCHED_TO_END"],
                        }
                    ],
                    "age_groups": ["AGE_13_17"],
                    "app_id": "app_xxxxxxxxxxxxxx",
                    "attribution_event_count": "UNSET",
                    "audience_ids": ["string"],
                    "audience_rule": {"foo": "bar"},
                    "audience_type": "NORMAL",
                    "bid_price": 6.9,
                    "bid_type": "BID_TYPE_NO_BID",
                    "billing_event": "CPC",
                    "brand_safety_type": "NO_BRAND_SAFETY",
                    "budget_mode": "BUDGET_MODE_DAY",
                    "carrier_ids": ["string"],
                    "category_exclusion_ids": ["string"],
                    "click_attribution_window": "OFF",
                    "comment_disabled": True,
                    "contextual_tag_ids": ["string"],
                    "conversion_bid_price": 6.9,
                    "creative_material_mode": "creative_material_mode",
                    "dayparting": "dayparting",
                    "deep_funnel_event_source": "deep_funnel_event_source",
                    "deep_funnel_event_source_id": "deep_funnel_event_source_id",
                    "deep_funnel_optimization_status": "ON",
                    "device_model_ids": ["string"],
                    "device_price_ranges": ["string"],
                    "engaged_view_attribution_window": "OFF",
                    "excluded_audience_ids": ["string"],
                    "excluded_location_ids": ["string"],
                    "frequency": 42,
                    "frequency_schedule": 42,
                    "gender": "GENDER_UNLIMITED",
                    "identity_authorized_bc_id": "identity_authorized_bc_id",
                    "identity_id": "identity_id",
                    "identity_type": "identity_type",
                    "instant_form_config": {
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "field_type": "field_type",
                                "label": "label",
                            }
                        ],
                        "button_text": "button_text",
                        "greeting": "greeting",
                        "name": "name",
                    },
                    "instant_form_id": "instant_form_id",
                    "interest_category_ids": ["string"],
                    "interest_keyword_ids": ["string"],
                    "inventory_filter_enabled": True,
                    "ios14_targeting": "UNSET",
                    "isp_ids": ["string"],
                    "languages": ["string"],
                    "location_ids": ["string"],
                    "min_android_version": "min_android_version",
                    "min_ios_version": "min_ios_version",
                    "network_types": ["string"],
                    "operating_systems": ["ANDROID"],
                    "operation_status": "ENABLE",
                    "optimization_event": "optimization_event",
                    "optimization_goal": "CLICK",
                    "pacing": "PACING_MODE_SMOOTH",
                    "pangle_audience_package_exclude_ids": ["string"],
                    "pangle_audience_package_include_ids": ["string"],
                    "pangle_block_app_ids": ["string"],
                    "pixel_id": "pixel_id",
                    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                    "placements": ["string"],
                    "product_set_id": "product_set_id",
                    "product_source": "CATALOG",
                    "promotion_type": "promotion_type",
                    "schedule_end_time": "schedule_end_time",
                    "schedule_start_time": "schedule_start_time",
                    "schedule_type": "SCHEDULE_START_END",
                    "secondary_optimization_event": "secondary_optimization_event",
                    "shopping_ads_retargeting_actions_days": 42,
                    "shopping_ads_retargeting_type": "OFF",
                    "spending_power": "ALL",
                    "tiktok_subplacements": ["string"],
                    "vertical_sensitivity_id": "vertical_sensitivity_id",
                    "video_download_disabled": True,
                    "video_user_actions": ["string"],
                    "view_attribution_window": "OFF",
                },
            },
            status="active",
        )
        assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.create(
            campaign_id="campaign_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.create(
            campaign_id="campaign_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad_group = client.ad_groups.retrieve(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupRetrieveResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.retrieve(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupRetrieveResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.retrieve(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroupRetrieveResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ad_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        ad_group = client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
            budget=6.9,
            budget_type="daily",
            config={
                "bid_amount": 42,
                "bid_strategy": "lowest_cost",
                "billing_event": "impressions",
                "end_time": "end_time",
                "frequency_cap": 42,
                "frequency_cap_interval_days": 42,
                "optimization_goal": "conversions",
                "pacing": "standard",
                "start_time": "start_time",
                "targeting": {
                    "age_max": 42,
                    "age_min": 42,
                    "countries": ["string"],
                    "device_platforms": ["mobile"],
                    "exclude_audience_ids": ["string"],
                    "genders": ["male"],
                    "include_audience_ids": ["string"],
                    "interest_ids": ["string"],
                    "languages": ["string"],
                    "placement_type": "automatic",
                },
            },
            daily_budget=6.9,
            name="name",
            platform_config={
                "meta": {
                    "android_devices": ["string"],
                    "attribution_setting": "attribution_setting",
                    "attribution_spec": [
                        {
                            "event_type": "event_type",
                            "window_days": 42,
                        }
                    ],
                    "audience_network_positions": ["string"],
                    "audience_type": "audience_type",
                    "bid_amount": 42,
                    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
                    "billing_event": "APP_INSTALLS",
                    "brand_safety_content_filter_levels": ["string"],
                    "budget_remaining": "budget_remaining",
                    "cost_per_result_goal": 6.9,
                    "created_time": "created_time",
                    "daily_budget": 42,
                    "daily_min_spend_target": "daily_min_spend_target",
                    "daily_spend_cap": "daily_spend_cap",
                    "destination_type": "UNDEFINED",
                    "dsa_beneficiary": "dsa_beneficiary",
                    "dsa_payor": "dsa_payor",
                    "end_time": "end_time",
                    "excluded_geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "facebook_positions": ["string"],
                    "frequency_control_count": 42,
                    "frequency_control_days": 42,
                    "frequency_control_type": "frequency_control_type",
                    "geo_cities": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "geo_regions": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_zips": ["string"],
                    "instagram_actor_id": "instagram_actor_id",
                    "instagram_positions": ["string"],
                    "ios_devices": ["string"],
                    "is_dynamic_creative": True,
                    "lead_conversion_location": "website",
                    "lead_form_config": {
                        "name": "name",
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "type": "type",
                                "conditional_questions_group_id": "conditional_questions_group_id",
                                "dependent_conditional_questions": [
                                    {
                                        "type": "type",
                                        "inline_context": "inline_context",
                                        "key": "key",
                                        "label": "label",
                                        "options": [
                                            {
                                                "key": "key",
                                                "value": "value",
                                                "logic": {
                                                    "type": "type",
                                                    "target_end_page_index": 42,
                                                    "target_question_index": 42,
                                                },
                                            }
                                        ],
                                    }
                                ],
                                "inline_context": "inline_context",
                                "key": "key",
                                "label": "label",
                                "options": [
                                    {
                                        "key": "key",
                                        "value": "value",
                                        "logic": {
                                            "type": "type",
                                            "target_end_page_index": 42,
                                            "target_question_index": 42,
                                        },
                                    }
                                ],
                                "question_format": "question_format",
                            }
                        ],
                        "background_image_source": "background_image_source",
                        "background_image_url": "background_image_url",
                        "conditional_logic_enabled": True,
                        "context_card_button_text": "context_card_button_text",
                        "context_card_content": ["string"],
                        "context_card_style": "context_card_style",
                        "context_card_title": "context_card_title",
                        "custom_disclaimer_body": "custom_disclaimer_body",
                        "custom_disclaimer_checkboxes": [
                            {
                                "key": "key",
                                "text": "text",
                                "is_checked_by_default": True,
                                "is_required": True,
                            }
                        ],
                        "custom_disclaimer_title": "custom_disclaimer_title",
                        "form_type": "form_type",
                        "messenger_enabled": True,
                        "phone_verification_enabled": True,
                        "privacy_policy_link_text": "privacy_policy_link_text",
                        "question_page_custom_headline": "question_page_custom_headline",
                        "rich_creative_headline": "rich_creative_headline",
                        "rich_creative_overview": "rich_creative_overview",
                        "rich_creative_url": "rich_creative_url",
                        "thank_you_pages": [
                            {
                                "body": "body",
                                "business_phone": "business_phone",
                                "button_text": "button_text",
                                "button_type": "button_type",
                                "conditional_question_group_id": "conditional_question_group_id",
                                "enable_messenger": True,
                                "gated_file_url": "gated_file_url",
                                "link": "link",
                                "name": "name",
                                "title": "title",
                            }
                        ],
                    },
                    "lead_gen_form_id": "lead_gen_form_id",
                    "lifetime_budget": 42,
                    "lifetime_min_spend_target": "lifetime_min_spend_target",
                    "lifetime_spend_cap": "lifetime_spend_cap",
                    "location_types": ["string"],
                    "messenger_positions": ["string"],
                    "optimization_goal": "NONE",
                    "page_id": "page_id",
                    "pixel_id": "pixel_id",
                    "promoted_object": {
                        "custom_conversion_id": "custom_conversion_id",
                        "custom_event_str": "custom_event_str",
                        "custom_event_type": "custom_event_type",
                        "page_id": "page_id",
                        "pixel_id": "pixel_id",
                        "whatsapp_phone_number": "whatsapp_phone_number",
                    },
                    "publisher_platforms": ["string"],
                    "source_adset_id": "source_adset_id",
                    "start_time": "start_time",
                    "status": "ACTIVE",
                    "targeting_automation": {"advantage_audience": 42},
                    "threads_positions": ["string"],
                    "updated_time": "updated_time",
                    "user_device": ["string"],
                    "user_os": ["string"],
                    "whatsapp_phone_number": "whatsapp_phone_number",
                    "whatsapp_positions": ["string"],
                },
                "tiktok": {
                    "actions": [
                        {
                            "action_category_ids": ["string"],
                            "action_period": 42,
                            "action_scene": "VIDEO_RELATED",
                            "video_user_actions": ["WATCHED_TO_END"],
                        }
                    ],
                    "age_groups": ["AGE_13_17"],
                    "app_id": "app_xxxxxxxxxxxxxx",
                    "attribution_event_count": "UNSET",
                    "audience_ids": ["string"],
                    "audience_rule": {"foo": "bar"},
                    "audience_type": "NORMAL",
                    "bid_price": 6.9,
                    "bid_type": "BID_TYPE_NO_BID",
                    "billing_event": "CPC",
                    "brand_safety_type": "NO_BRAND_SAFETY",
                    "budget_mode": "BUDGET_MODE_DAY",
                    "carrier_ids": ["string"],
                    "category_exclusion_ids": ["string"],
                    "click_attribution_window": "OFF",
                    "comment_disabled": True,
                    "contextual_tag_ids": ["string"],
                    "conversion_bid_price": 6.9,
                    "creative_material_mode": "creative_material_mode",
                    "dayparting": "dayparting",
                    "deep_funnel_event_source": "deep_funnel_event_source",
                    "deep_funnel_event_source_id": "deep_funnel_event_source_id",
                    "deep_funnel_optimization_status": "ON",
                    "device_model_ids": ["string"],
                    "device_price_ranges": ["string"],
                    "engaged_view_attribution_window": "OFF",
                    "excluded_audience_ids": ["string"],
                    "excluded_location_ids": ["string"],
                    "frequency": 42,
                    "frequency_schedule": 42,
                    "gender": "GENDER_UNLIMITED",
                    "identity_authorized_bc_id": "identity_authorized_bc_id",
                    "identity_id": "identity_id",
                    "identity_type": "identity_type",
                    "instant_form_config": {
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "field_type": "field_type",
                                "label": "label",
                            }
                        ],
                        "button_text": "button_text",
                        "greeting": "greeting",
                        "name": "name",
                    },
                    "instant_form_id": "instant_form_id",
                    "interest_category_ids": ["string"],
                    "interest_keyword_ids": ["string"],
                    "inventory_filter_enabled": True,
                    "ios14_targeting": "UNSET",
                    "isp_ids": ["string"],
                    "languages": ["string"],
                    "location_ids": ["string"],
                    "min_android_version": "min_android_version",
                    "min_ios_version": "min_ios_version",
                    "network_types": ["string"],
                    "operating_systems": ["ANDROID"],
                    "operation_status": "ENABLE",
                    "optimization_event": "optimization_event",
                    "optimization_goal": "CLICK",
                    "pacing": "PACING_MODE_SMOOTH",
                    "pangle_audience_package_exclude_ids": ["string"],
                    "pangle_audience_package_include_ids": ["string"],
                    "pangle_block_app_ids": ["string"],
                    "pixel_id": "pixel_id",
                    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                    "placements": ["string"],
                    "product_set_id": "product_set_id",
                    "product_source": "CATALOG",
                    "promotion_type": "promotion_type",
                    "schedule_end_time": "schedule_end_time",
                    "schedule_start_time": "schedule_start_time",
                    "schedule_type": "SCHEDULE_START_END",
                    "secondary_optimization_event": "secondary_optimization_event",
                    "shopping_ads_retargeting_actions_days": 42,
                    "shopping_ads_retargeting_type": "OFF",
                    "spending_power": "ALL",
                    "tiktok_subplacements": ["string"],
                    "vertical_sensitivity_id": "vertical_sensitivity_id",
                    "video_download_disabled": True,
                    "video_user_actions": ["string"],
                    "view_attribution_window": "OFF",
                },
            },
            status="active",
        )
        assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.update(
            id="adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.update(
            id="adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

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
        assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ad_group = client.ad_groups.list(
            after="after",
            before="before",
            campaign_id="campaign_id",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            query="query",
            status="active",
        )
        assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = response.parse()
            assert_matches_type(SyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        ad_group = client.ad_groups.delete(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.ad_groups.with_raw_response.delete(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = response.parse()
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.ad_groups.with_streaming_response.delete(
            "adgrp_xxxxxxxxxxxx",
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


class TestAsyncAdGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.create(
            campaign_id="campaign_id",
        )
        assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.create(
            campaign_id="campaign_id",
            budget=6.9,
            budget_type="daily",
            config={
                "bid_amount": 42,
                "bid_strategy": "lowest_cost",
                "billing_event": "impressions",
                "end_time": "end_time",
                "frequency_cap": 42,
                "frequency_cap_interval_days": 42,
                "optimization_goal": "conversions",
                "pacing": "standard",
                "start_time": "start_time",
                "targeting": {
                    "age_max": 42,
                    "age_min": 42,
                    "countries": ["string"],
                    "device_platforms": ["mobile"],
                    "exclude_audience_ids": ["string"],
                    "genders": ["male"],
                    "include_audience_ids": ["string"],
                    "interest_ids": ["string"],
                    "languages": ["string"],
                    "placement_type": "automatic",
                },
            },
            daily_budget=6.9,
            name="name",
            platform_config={
                "meta": {
                    "android_devices": ["string"],
                    "attribution_setting": "attribution_setting",
                    "attribution_spec": [
                        {
                            "event_type": "event_type",
                            "window_days": 42,
                        }
                    ],
                    "audience_network_positions": ["string"],
                    "audience_type": "audience_type",
                    "bid_amount": 42,
                    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
                    "billing_event": "APP_INSTALLS",
                    "brand_safety_content_filter_levels": ["string"],
                    "budget_remaining": "budget_remaining",
                    "cost_per_result_goal": 6.9,
                    "created_time": "created_time",
                    "daily_budget": 42,
                    "daily_min_spend_target": "daily_min_spend_target",
                    "daily_spend_cap": "daily_spend_cap",
                    "destination_type": "UNDEFINED",
                    "dsa_beneficiary": "dsa_beneficiary",
                    "dsa_payor": "dsa_payor",
                    "end_time": "end_time",
                    "excluded_geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "facebook_positions": ["string"],
                    "frequency_control_count": 42,
                    "frequency_control_days": 42,
                    "frequency_control_type": "frequency_control_type",
                    "geo_cities": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "geo_regions": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_zips": ["string"],
                    "instagram_actor_id": "instagram_actor_id",
                    "instagram_positions": ["string"],
                    "ios_devices": ["string"],
                    "is_dynamic_creative": True,
                    "lead_conversion_location": "website",
                    "lead_form_config": {
                        "name": "name",
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "type": "type",
                                "conditional_questions_group_id": "conditional_questions_group_id",
                                "dependent_conditional_questions": [
                                    {
                                        "type": "type",
                                        "inline_context": "inline_context",
                                        "key": "key",
                                        "label": "label",
                                        "options": [
                                            {
                                                "key": "key",
                                                "value": "value",
                                                "logic": {
                                                    "type": "type",
                                                    "target_end_page_index": 42,
                                                    "target_question_index": 42,
                                                },
                                            }
                                        ],
                                    }
                                ],
                                "inline_context": "inline_context",
                                "key": "key",
                                "label": "label",
                                "options": [
                                    {
                                        "key": "key",
                                        "value": "value",
                                        "logic": {
                                            "type": "type",
                                            "target_end_page_index": 42,
                                            "target_question_index": 42,
                                        },
                                    }
                                ],
                                "question_format": "question_format",
                            }
                        ],
                        "background_image_source": "background_image_source",
                        "background_image_url": "background_image_url",
                        "conditional_logic_enabled": True,
                        "context_card_button_text": "context_card_button_text",
                        "context_card_content": ["string"],
                        "context_card_style": "context_card_style",
                        "context_card_title": "context_card_title",
                        "custom_disclaimer_body": "custom_disclaimer_body",
                        "custom_disclaimer_checkboxes": [
                            {
                                "key": "key",
                                "text": "text",
                                "is_checked_by_default": True,
                                "is_required": True,
                            }
                        ],
                        "custom_disclaimer_title": "custom_disclaimer_title",
                        "form_type": "form_type",
                        "messenger_enabled": True,
                        "phone_verification_enabled": True,
                        "privacy_policy_link_text": "privacy_policy_link_text",
                        "question_page_custom_headline": "question_page_custom_headline",
                        "rich_creative_headline": "rich_creative_headline",
                        "rich_creative_overview": "rich_creative_overview",
                        "rich_creative_url": "rich_creative_url",
                        "thank_you_pages": [
                            {
                                "body": "body",
                                "business_phone": "business_phone",
                                "button_text": "button_text",
                                "button_type": "button_type",
                                "conditional_question_group_id": "conditional_question_group_id",
                                "enable_messenger": True,
                                "gated_file_url": "gated_file_url",
                                "link": "link",
                                "name": "name",
                                "title": "title",
                            }
                        ],
                    },
                    "lead_gen_form_id": "lead_gen_form_id",
                    "lifetime_budget": 42,
                    "lifetime_min_spend_target": "lifetime_min_spend_target",
                    "lifetime_spend_cap": "lifetime_spend_cap",
                    "location_types": ["string"],
                    "messenger_positions": ["string"],
                    "optimization_goal": "NONE",
                    "page_id": "page_id",
                    "pixel_id": "pixel_id",
                    "promoted_object": {
                        "custom_conversion_id": "custom_conversion_id",
                        "custom_event_str": "custom_event_str",
                        "custom_event_type": "custom_event_type",
                        "page_id": "page_id",
                        "pixel_id": "pixel_id",
                        "whatsapp_phone_number": "whatsapp_phone_number",
                    },
                    "publisher_platforms": ["string"],
                    "source_adset_id": "source_adset_id",
                    "start_time": "start_time",
                    "status": "ACTIVE",
                    "targeting_automation": {"advantage_audience": 42},
                    "threads_positions": ["string"],
                    "updated_time": "updated_time",
                    "user_device": ["string"],
                    "user_os": ["string"],
                    "whatsapp_phone_number": "whatsapp_phone_number",
                    "whatsapp_positions": ["string"],
                },
                "tiktok": {
                    "actions": [
                        {
                            "action_category_ids": ["string"],
                            "action_period": 42,
                            "action_scene": "VIDEO_RELATED",
                            "video_user_actions": ["WATCHED_TO_END"],
                        }
                    ],
                    "age_groups": ["AGE_13_17"],
                    "app_id": "app_xxxxxxxxxxxxxx",
                    "attribution_event_count": "UNSET",
                    "audience_ids": ["string"],
                    "audience_rule": {"foo": "bar"},
                    "audience_type": "NORMAL",
                    "bid_price": 6.9,
                    "bid_type": "BID_TYPE_NO_BID",
                    "billing_event": "CPC",
                    "brand_safety_type": "NO_BRAND_SAFETY",
                    "budget_mode": "BUDGET_MODE_DAY",
                    "carrier_ids": ["string"],
                    "category_exclusion_ids": ["string"],
                    "click_attribution_window": "OFF",
                    "comment_disabled": True,
                    "contextual_tag_ids": ["string"],
                    "conversion_bid_price": 6.9,
                    "creative_material_mode": "creative_material_mode",
                    "dayparting": "dayparting",
                    "deep_funnel_event_source": "deep_funnel_event_source",
                    "deep_funnel_event_source_id": "deep_funnel_event_source_id",
                    "deep_funnel_optimization_status": "ON",
                    "device_model_ids": ["string"],
                    "device_price_ranges": ["string"],
                    "engaged_view_attribution_window": "OFF",
                    "excluded_audience_ids": ["string"],
                    "excluded_location_ids": ["string"],
                    "frequency": 42,
                    "frequency_schedule": 42,
                    "gender": "GENDER_UNLIMITED",
                    "identity_authorized_bc_id": "identity_authorized_bc_id",
                    "identity_id": "identity_id",
                    "identity_type": "identity_type",
                    "instant_form_config": {
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "field_type": "field_type",
                                "label": "label",
                            }
                        ],
                        "button_text": "button_text",
                        "greeting": "greeting",
                        "name": "name",
                    },
                    "instant_form_id": "instant_form_id",
                    "interest_category_ids": ["string"],
                    "interest_keyword_ids": ["string"],
                    "inventory_filter_enabled": True,
                    "ios14_targeting": "UNSET",
                    "isp_ids": ["string"],
                    "languages": ["string"],
                    "location_ids": ["string"],
                    "min_android_version": "min_android_version",
                    "min_ios_version": "min_ios_version",
                    "network_types": ["string"],
                    "operating_systems": ["ANDROID"],
                    "operation_status": "ENABLE",
                    "optimization_event": "optimization_event",
                    "optimization_goal": "CLICK",
                    "pacing": "PACING_MODE_SMOOTH",
                    "pangle_audience_package_exclude_ids": ["string"],
                    "pangle_audience_package_include_ids": ["string"],
                    "pangle_block_app_ids": ["string"],
                    "pixel_id": "pixel_id",
                    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                    "placements": ["string"],
                    "product_set_id": "product_set_id",
                    "product_source": "CATALOG",
                    "promotion_type": "promotion_type",
                    "schedule_end_time": "schedule_end_time",
                    "schedule_start_time": "schedule_start_time",
                    "schedule_type": "SCHEDULE_START_END",
                    "secondary_optimization_event": "secondary_optimization_event",
                    "shopping_ads_retargeting_actions_days": 42,
                    "shopping_ads_retargeting_type": "OFF",
                    "spending_power": "ALL",
                    "tiktok_subplacements": ["string"],
                    "vertical_sensitivity_id": "vertical_sensitivity_id",
                    "video_download_disabled": True,
                    "video_user_actions": ["string"],
                    "view_attribution_window": "OFF",
                },
            },
            status="active",
        )
        assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.create(
            campaign_id="campaign_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.create(
            campaign_id="campaign_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroupCreateResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.retrieve(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupRetrieveResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.retrieve(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupRetrieveResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.retrieve(
            "adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroupRetrieveResponse, ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ad_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.update(
            id="adgrp_xxxxxxxxxxxx",
            budget=6.9,
            budget_type="daily",
            config={
                "bid_amount": 42,
                "bid_strategy": "lowest_cost",
                "billing_event": "impressions",
                "end_time": "end_time",
                "frequency_cap": 42,
                "frequency_cap_interval_days": 42,
                "optimization_goal": "conversions",
                "pacing": "standard",
                "start_time": "start_time",
                "targeting": {
                    "age_max": 42,
                    "age_min": 42,
                    "countries": ["string"],
                    "device_platforms": ["mobile"],
                    "exclude_audience_ids": ["string"],
                    "genders": ["male"],
                    "include_audience_ids": ["string"],
                    "interest_ids": ["string"],
                    "languages": ["string"],
                    "placement_type": "automatic",
                },
            },
            daily_budget=6.9,
            name="name",
            platform_config={
                "meta": {
                    "android_devices": ["string"],
                    "attribution_setting": "attribution_setting",
                    "attribution_spec": [
                        {
                            "event_type": "event_type",
                            "window_days": 42,
                        }
                    ],
                    "audience_network_positions": ["string"],
                    "audience_type": "audience_type",
                    "bid_amount": 42,
                    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
                    "billing_event": "APP_INSTALLS",
                    "brand_safety_content_filter_levels": ["string"],
                    "budget_remaining": "budget_remaining",
                    "cost_per_result_goal": 6.9,
                    "created_time": "created_time",
                    "daily_budget": 42,
                    "daily_min_spend_target": "daily_min_spend_target",
                    "daily_spend_cap": "daily_spend_cap",
                    "destination_type": "UNDEFINED",
                    "dsa_beneficiary": "dsa_beneficiary",
                    "dsa_payor": "dsa_payor",
                    "end_time": "end_time",
                    "excluded_geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "facebook_positions": ["string"],
                    "frequency_control_count": 42,
                    "frequency_control_days": 42,
                    "frequency_control_type": "frequency_control_type",
                    "geo_cities": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_locations": {
                        "cities": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "countries": ["string"],
                        "location_types": ["string"],
                        "regions": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                        "zips": [
                            {
                                "key": "key",
                                "country": "country",
                                "name": "name",
                                "radius": 42,
                            }
                        ],
                    },
                    "geo_regions": [
                        {
                            "key": "key",
                            "country": "country",
                            "name": "name",
                            "radius": 42,
                        }
                    ],
                    "geo_zips": ["string"],
                    "instagram_actor_id": "instagram_actor_id",
                    "instagram_positions": ["string"],
                    "ios_devices": ["string"],
                    "is_dynamic_creative": True,
                    "lead_conversion_location": "website",
                    "lead_form_config": {
                        "name": "name",
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "type": "type",
                                "conditional_questions_group_id": "conditional_questions_group_id",
                                "dependent_conditional_questions": [
                                    {
                                        "type": "type",
                                        "inline_context": "inline_context",
                                        "key": "key",
                                        "label": "label",
                                        "options": [
                                            {
                                                "key": "key",
                                                "value": "value",
                                                "logic": {
                                                    "type": "type",
                                                    "target_end_page_index": 42,
                                                    "target_question_index": 42,
                                                },
                                            }
                                        ],
                                    }
                                ],
                                "inline_context": "inline_context",
                                "key": "key",
                                "label": "label",
                                "options": [
                                    {
                                        "key": "key",
                                        "value": "value",
                                        "logic": {
                                            "type": "type",
                                            "target_end_page_index": 42,
                                            "target_question_index": 42,
                                        },
                                    }
                                ],
                                "question_format": "question_format",
                            }
                        ],
                        "background_image_source": "background_image_source",
                        "background_image_url": "background_image_url",
                        "conditional_logic_enabled": True,
                        "context_card_button_text": "context_card_button_text",
                        "context_card_content": ["string"],
                        "context_card_style": "context_card_style",
                        "context_card_title": "context_card_title",
                        "custom_disclaimer_body": "custom_disclaimer_body",
                        "custom_disclaimer_checkboxes": [
                            {
                                "key": "key",
                                "text": "text",
                                "is_checked_by_default": True,
                                "is_required": True,
                            }
                        ],
                        "custom_disclaimer_title": "custom_disclaimer_title",
                        "form_type": "form_type",
                        "messenger_enabled": True,
                        "phone_verification_enabled": True,
                        "privacy_policy_link_text": "privacy_policy_link_text",
                        "question_page_custom_headline": "question_page_custom_headline",
                        "rich_creative_headline": "rich_creative_headline",
                        "rich_creative_overview": "rich_creative_overview",
                        "rich_creative_url": "rich_creative_url",
                        "thank_you_pages": [
                            {
                                "body": "body",
                                "business_phone": "business_phone",
                                "button_text": "button_text",
                                "button_type": "button_type",
                                "conditional_question_group_id": "conditional_question_group_id",
                                "enable_messenger": True,
                                "gated_file_url": "gated_file_url",
                                "link": "link",
                                "name": "name",
                                "title": "title",
                            }
                        ],
                    },
                    "lead_gen_form_id": "lead_gen_form_id",
                    "lifetime_budget": 42,
                    "lifetime_min_spend_target": "lifetime_min_spend_target",
                    "lifetime_spend_cap": "lifetime_spend_cap",
                    "location_types": ["string"],
                    "messenger_positions": ["string"],
                    "optimization_goal": "NONE",
                    "page_id": "page_id",
                    "pixel_id": "pixel_id",
                    "promoted_object": {
                        "custom_conversion_id": "custom_conversion_id",
                        "custom_event_str": "custom_event_str",
                        "custom_event_type": "custom_event_type",
                        "page_id": "page_id",
                        "pixel_id": "pixel_id",
                        "whatsapp_phone_number": "whatsapp_phone_number",
                    },
                    "publisher_platforms": ["string"],
                    "source_adset_id": "source_adset_id",
                    "start_time": "start_time",
                    "status": "ACTIVE",
                    "targeting_automation": {"advantage_audience": 42},
                    "threads_positions": ["string"],
                    "updated_time": "updated_time",
                    "user_device": ["string"],
                    "user_os": ["string"],
                    "whatsapp_phone_number": "whatsapp_phone_number",
                    "whatsapp_positions": ["string"],
                },
                "tiktok": {
                    "actions": [
                        {
                            "action_category_ids": ["string"],
                            "action_period": 42,
                            "action_scene": "VIDEO_RELATED",
                            "video_user_actions": ["WATCHED_TO_END"],
                        }
                    ],
                    "age_groups": ["AGE_13_17"],
                    "app_id": "app_xxxxxxxxxxxxxx",
                    "attribution_event_count": "UNSET",
                    "audience_ids": ["string"],
                    "audience_rule": {"foo": "bar"},
                    "audience_type": "NORMAL",
                    "bid_price": 6.9,
                    "bid_type": "BID_TYPE_NO_BID",
                    "billing_event": "CPC",
                    "brand_safety_type": "NO_BRAND_SAFETY",
                    "budget_mode": "BUDGET_MODE_DAY",
                    "carrier_ids": ["string"],
                    "category_exclusion_ids": ["string"],
                    "click_attribution_window": "OFF",
                    "comment_disabled": True,
                    "contextual_tag_ids": ["string"],
                    "conversion_bid_price": 6.9,
                    "creative_material_mode": "creative_material_mode",
                    "dayparting": "dayparting",
                    "deep_funnel_event_source": "deep_funnel_event_source",
                    "deep_funnel_event_source_id": "deep_funnel_event_source_id",
                    "deep_funnel_optimization_status": "ON",
                    "device_model_ids": ["string"],
                    "device_price_ranges": ["string"],
                    "engaged_view_attribution_window": "OFF",
                    "excluded_audience_ids": ["string"],
                    "excluded_location_ids": ["string"],
                    "frequency": 42,
                    "frequency_schedule": 42,
                    "gender": "GENDER_UNLIMITED",
                    "identity_authorized_bc_id": "identity_authorized_bc_id",
                    "identity_id": "identity_id",
                    "identity_type": "identity_type",
                    "instant_form_config": {
                        "privacy_policy_url": "privacy_policy_url",
                        "questions": [
                            {
                                "field_type": "field_type",
                                "label": "label",
                            }
                        ],
                        "button_text": "button_text",
                        "greeting": "greeting",
                        "name": "name",
                    },
                    "instant_form_id": "instant_form_id",
                    "interest_category_ids": ["string"],
                    "interest_keyword_ids": ["string"],
                    "inventory_filter_enabled": True,
                    "ios14_targeting": "UNSET",
                    "isp_ids": ["string"],
                    "languages": ["string"],
                    "location_ids": ["string"],
                    "min_android_version": "min_android_version",
                    "min_ios_version": "min_ios_version",
                    "network_types": ["string"],
                    "operating_systems": ["ANDROID"],
                    "operation_status": "ENABLE",
                    "optimization_event": "optimization_event",
                    "optimization_goal": "CLICK",
                    "pacing": "PACING_MODE_SMOOTH",
                    "pangle_audience_package_exclude_ids": ["string"],
                    "pangle_audience_package_include_ids": ["string"],
                    "pangle_block_app_ids": ["string"],
                    "pixel_id": "pixel_id",
                    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                    "placements": ["string"],
                    "product_set_id": "product_set_id",
                    "product_source": "CATALOG",
                    "promotion_type": "promotion_type",
                    "schedule_end_time": "schedule_end_time",
                    "schedule_start_time": "schedule_start_time",
                    "schedule_type": "SCHEDULE_START_END",
                    "secondary_optimization_event": "secondary_optimization_event",
                    "shopping_ads_retargeting_actions_days": 42,
                    "shopping_ads_retargeting_type": "OFF",
                    "spending_power": "ALL",
                    "tiktok_subplacements": ["string"],
                    "vertical_sensitivity_id": "vertical_sensitivity_id",
                    "video_download_disabled": True,
                    "video_user_actions": ["string"],
                    "view_attribution_window": "OFF",
                },
            },
            status="active",
        )
        assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.update(
            id="adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.update(
            id="adgrp_xxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AdGroupUpdateResponse, ad_group, path=["response"])

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
        assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.list(
            after="after",
            before="before",
            campaign_id="campaign_id",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            first=42,
            last=42,
            query="query",
            status="active",
        )
        assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad_group = await response.parse()
            assert_matches_type(AsyncCursorPage[AdGroupListResponse], ad_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        ad_group = await async_client.ad_groups.delete(
            "adgrp_xxxxxxxxxxxx",
        )
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.ad_groups.with_raw_response.delete(
            "adgrp_xxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad_group = await response.parse()
        assert_matches_type(AdGroupDeleteResponse, ad_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.ad_groups.with_streaming_response.delete(
            "adgrp_xxxxxxxxxxxx",
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
