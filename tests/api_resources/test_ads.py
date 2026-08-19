# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Ad,
    AdDeleteResponse,
    AdDuplicateResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        ad = client.ads.create()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        ad = client.ads.create(
            ad_group={
                "ad_campaign_id": "adcamp_xxxxxxxxxxxxxx",
                "budget_amount": 60,
                "optimization_goal": "conversions",
                "title": "Austin — ceramic coating buyers",
            },
            ad_group_id="adgrp_xxxxxxxxxxxxxx",
            call_to_action="message_page",
            creatives=[
                {
                    "id": "file_xxxxxxxxxxxxxx",
                    "crop": {
                        "height": 1000,
                        "width": 1000,
                        "x": 40,
                        "y": 0,
                    },
                    "format": "square",
                }
            ],
            descriptions=["Two-stage paint correction included"],
            headlines=["Showroom shine, guaranteed"],
            lead_form={
                "completion": {
                    "button_text": "See our work",
                    "description": "We book coatings two days out, so pick a slot when we ring.",
                    "headline": "Thanks — we will call you today",
                    "url": "https://shinetime.example/gallery",
                },
                "disclaimer": {
                    "body": "Ceramic coating requires the vehicle for two days.",
                    "checkboxes": [
                        {
                            "checked_by_default": False,
                            "key": "two_days",
                            "required": True,
                            "text": "I can leave my vehicle for two days",
                        }
                    ],
                    "title": "Before you submit",
                },
                "form_type": "higher_intent",
                "intro": {
                    "description": "Tell us about your vehicle and we will send a fixed price.",
                    "headline": "Get a ceramic coating quote",
                },
                "name": "Ceramic coating quote requests",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "Shine Time privacy policy",
                    "url": "https://shinetime.example/privacy",
                },
                "questions": [
                    {
                        "format": "multiple_choice",
                        "label": "What vehicle are we detailing?",
                        "options": [
                            {
                                "key": "sedan",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 3,
                                },
                                "value": "Sedan or coupe",
                            }
                        ],
                        "type": "phone",
                    }
                ],
            },
            lead_form_id="1037724182084885",
            messaging_config={
                "keyword": "Book an interior deep clean",
                "message": "Hi! Tell us your vehicle and ZIP and we will send an interior deep clean quote.",
            },
            multi_advertiser_ads=False,
            post_id="1784512345678901",
            post_source="instagram",
            primary_texts=["Three-year ceramic coating, booked online in under a minute."],
            social_accounts=[{"id": "sacc_xxxxxxxxxxxxxx"}],
            title="Interior deep clean — DM us",
            url="https://shinetime.example/ceramic-coating",
            url_parameters={"ref": "spring"},
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.ads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.ads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        ad = client.ads.retrieve(
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        ad = client.ads.retrieve(
            id="id",
            attribution_model="last_touch",
            stats_from="stats_from",
            stats_to="stats_to",
            time_zone="time_zone",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.ads.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.ads.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        ad = client.ads.update(
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        ad = client.ads.update(
            id="id",
            call_to_action="learn_more",
            creatives=[
                {
                    "id": "file_xxxxxxxxxxxxxx",
                    "crop": {
                        "height": 1920,
                        "width": 1080,
                        "x": 0,
                        "y": 120,
                    },
                    "format": "vertical",
                }
            ],
            descriptions=["Paint correction included"],
            headlines=["Austin's mobile detailers"],
            lead_form={
                "completion": {
                    "button_text": "See our work",
                    "description": "We book coatings two days out, so pick a slot when we ring.",
                    "headline": "Thanks — we will call you today",
                    "url": "https://shinetime.example/gallery",
                },
                "disclaimer": {
                    "body": "Ceramic coating requires the vehicle for two days.",
                    "checkboxes": [
                        {
                            "checked_by_default": False,
                            "key": "two_days",
                            "required": True,
                            "text": "I can leave my vehicle for two days",
                        }
                    ],
                    "title": "Before you submit",
                },
                "form_type": "higher_intent",
                "intro": {
                    "description": "Tell us about your vehicle and we will send a fixed price.",
                    "headline": "Get a ceramic coating quote",
                },
                "name": "Ceramic coating quote requests",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "Shine Time privacy policy",
                    "url": "https://shinetime.example/privacy",
                },
                "questions": [
                    {
                        "format": "multiple_choice",
                        "label": "What vehicle are we detailing?",
                        "options": [
                            {
                                "key": "sedan",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 3,
                                },
                                "value": "Sedan or coupe",
                            }
                        ],
                        "type": "phone",
                    }
                ],
            },
            lead_form_id="1037724182084885",
            messaging_config={
                "keyword": "Get a ceramic coating quote",
                "message": "Hi! Which vehicle are we coating?",
            },
            multi_advertiser_ads=False,
            post_id="xxxxxxxxxxxxxxxx_98765",
            post_source="facebook",
            primary_texts=["Book a two-day ceramic coating and keep the shine for three years."],
            social_accounts=[{"id": "sacc_xxxxxxxxxxxxxx"}],
            title="Ceramic coating — spring hook v2",
            url="https://shinetime.example/ceramic-coating",
            url_parameters={
                "placement": "{{placement}}",
                "ref": "spring",
            },
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.ads.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.ads.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        ad = client.ads.list()
        assert_matches_type(SyncCursorPage[Ad], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        ad = client.ads.list(
            account_id="account_id",
            ad_campaign_id="ad_campaign_id",
            ad_campaign_ids=["adcamp_xxxxxxxxxxxxxx"],
            ad_group_id="ad_group_id",
            ad_group_ids=["adgrp_xxxxxxxxxxxxxx"],
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
            status="active",
            time_zone="time_zone",
        )
        assert_matches_type(SyncCursorPage[Ad], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.ads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(SyncCursorPage[Ad], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.ads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(SyncCursorPage[Ad], ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        ad = client.ads.delete(
            "id",
        )
        assert_matches_type(AdDeleteResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.ads.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdDeleteResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.ads.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdDeleteResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Whop) -> None:
        ad = client.ads.duplicate(
            id="id",
        )
        assert_matches_type(AdDuplicateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate_with_all_params(self, client: Whop) -> None:
        ad = client.ads.duplicate(
            id="id",
            count=2,
            preserve_engagement=True,
            target_ad_group_id="adgrp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AdDuplicateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Whop) -> None:
        response = client.ads.with_raw_response.duplicate(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdDuplicateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Whop) -> None:
        with client.ads.with_streaming_response.duplicate(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdDuplicateResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.duplicate(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Whop) -> None:
        ad = client.ads.pause(
            "id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Whop) -> None:
        response = client.ads.with_raw_response.pause(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Whop) -> None:
        with client.ads.with_streaming_response.pause(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause(self, client: Whop) -> None:
        ad = client.ads.unpause(
            "id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpause(self, client: Whop) -> None:
        response = client.ads.with_raw_response.unpause(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpause(self, client: Whop) -> None:
        with client.ads.with_streaming_response.unpause(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpause(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ads.with_raw_response.unpause(
                "",
            )


class TestAsyncAds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.create()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.create(
            ad_group={
                "ad_campaign_id": "adcamp_xxxxxxxxxxxxxx",
                "budget_amount": 60,
                "optimization_goal": "conversions",
                "title": "Austin — ceramic coating buyers",
            },
            ad_group_id="adgrp_xxxxxxxxxxxxxx",
            call_to_action="message_page",
            creatives=[
                {
                    "id": "file_xxxxxxxxxxxxxx",
                    "crop": {
                        "height": 1000,
                        "width": 1000,
                        "x": 40,
                        "y": 0,
                    },
                    "format": "square",
                }
            ],
            descriptions=["Two-stage paint correction included"],
            headlines=["Showroom shine, guaranteed"],
            lead_form={
                "completion": {
                    "button_text": "See our work",
                    "description": "We book coatings two days out, so pick a slot when we ring.",
                    "headline": "Thanks — we will call you today",
                    "url": "https://shinetime.example/gallery",
                },
                "disclaimer": {
                    "body": "Ceramic coating requires the vehicle for two days.",
                    "checkboxes": [
                        {
                            "checked_by_default": False,
                            "key": "two_days",
                            "required": True,
                            "text": "I can leave my vehicle for two days",
                        }
                    ],
                    "title": "Before you submit",
                },
                "form_type": "higher_intent",
                "intro": {
                    "description": "Tell us about your vehicle and we will send a fixed price.",
                    "headline": "Get a ceramic coating quote",
                },
                "name": "Ceramic coating quote requests",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "Shine Time privacy policy",
                    "url": "https://shinetime.example/privacy",
                },
                "questions": [
                    {
                        "format": "multiple_choice",
                        "label": "What vehicle are we detailing?",
                        "options": [
                            {
                                "key": "sedan",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 3,
                                },
                                "value": "Sedan or coupe",
                            }
                        ],
                        "type": "phone",
                    }
                ],
            },
            lead_form_id="1037724182084885",
            messaging_config={
                "keyword": "Book an interior deep clean",
                "message": "Hi! Tell us your vehicle and ZIP and we will send an interior deep clean quote.",
            },
            multi_advertiser_ads=False,
            post_id="1784512345678901",
            post_source="instagram",
            primary_texts=["Three-year ceramic coating, booked online in under a minute."],
            social_accounts=[{"id": "sacc_xxxxxxxxxxxxxx"}],
            title="Interior deep clean — DM us",
            url="https://shinetime.example/ceramic-coating",
            url_parameters={"ref": "spring"},
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.retrieve(
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.retrieve(
            id="id",
            attribution_model="last_touch",
            stats_from="stats_from",
            stats_to="stats_to",
            time_zone="time_zone",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.update(
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.update(
            id="id",
            call_to_action="learn_more",
            creatives=[
                {
                    "id": "file_xxxxxxxxxxxxxx",
                    "crop": {
                        "height": 1920,
                        "width": 1080,
                        "x": 0,
                        "y": 120,
                    },
                    "format": "vertical",
                }
            ],
            descriptions=["Paint correction included"],
            headlines=["Austin's mobile detailers"],
            lead_form={
                "completion": {
                    "button_text": "See our work",
                    "description": "We book coatings two days out, so pick a slot when we ring.",
                    "headline": "Thanks — we will call you today",
                    "url": "https://shinetime.example/gallery",
                },
                "disclaimer": {
                    "body": "Ceramic coating requires the vehicle for two days.",
                    "checkboxes": [
                        {
                            "checked_by_default": False,
                            "key": "two_days",
                            "required": True,
                            "text": "I can leave my vehicle for two days",
                        }
                    ],
                    "title": "Before you submit",
                },
                "form_type": "higher_intent",
                "intro": {
                    "description": "Tell us about your vehicle and we will send a fixed price.",
                    "headline": "Get a ceramic coating quote",
                },
                "name": "Ceramic coating quote requests",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "Shine Time privacy policy",
                    "url": "https://shinetime.example/privacy",
                },
                "questions": [
                    {
                        "format": "multiple_choice",
                        "label": "What vehicle are we detailing?",
                        "options": [
                            {
                                "key": "sedan",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 3,
                                },
                                "value": "Sedan or coupe",
                            }
                        ],
                        "type": "phone",
                    }
                ],
            },
            lead_form_id="1037724182084885",
            messaging_config={
                "keyword": "Get a ceramic coating quote",
                "message": "Hi! Which vehicle are we coating?",
            },
            multi_advertiser_ads=False,
            post_id="xxxxxxxxxxxxxxxx_98765",
            post_source="facebook",
            primary_texts=["Book a two-day ceramic coating and keep the shine for three years."],
            social_accounts=[{"id": "sacc_xxxxxxxxxxxxxx"}],
            title="Ceramic coating — spring hook v2",
            url="https://shinetime.example/ceramic-coating",
            url_parameters={
                "placement": "{{placement}}",
                "ref": "spring",
            },
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.list()
        assert_matches_type(AsyncCursorPage[Ad], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.list(
            account_id="account_id",
            ad_campaign_id="ad_campaign_id",
            ad_campaign_ids=["adcamp_xxxxxxxxxxxxxx"],
            ad_group_id="ad_group_id",
            ad_group_ids=["adgrp_xxxxxxxxxxxxxx"],
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
            status="active",
            time_zone="time_zone",
        )
        assert_matches_type(AsyncCursorPage[Ad], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AsyncCursorPage[Ad], ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AsyncCursorPage[Ad], ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.delete(
            "id",
        )
        assert_matches_type(AdDeleteResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdDeleteResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdDeleteResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.duplicate(
            id="id",
        )
        assert_matches_type(AdDuplicateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.duplicate(
            id="id",
            count=2,
            preserve_engagement=True,
            target_ad_group_id="adgrp_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AdDuplicateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.duplicate(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdDuplicateResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.duplicate(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdDuplicateResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.duplicate(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.pause(
            "id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.pause(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.pause(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.pause(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.unpause(
            "id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.unpause(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.unpause(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(Ad, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ads.with_raw_response.unpause(
                "",
            )
