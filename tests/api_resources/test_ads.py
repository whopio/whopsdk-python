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
            ad_group={},
            ad_group_id="ad_group_id",
            call_to_action="apply_now",
            creatives=[
                {
                    "id": "id",
                    "crop": {
                        "height": 0,
                        "width": 0,
                        "x": 0,
                        "y": 0,
                    },
                    "format": "square",
                }
            ],
            descriptions=["string"],
            headlines=["string"],
            lead_form={
                "completion": {
                    "button_text": "button_text",
                    "description": "description",
                    "headline": "headline",
                    "url": "url",
                },
                "disclaimer": {
                    "body": "body",
                    "checkboxes": [
                        {
                            "checked_by_default": True,
                            "key": "key",
                            "required": True,
                            "text": "text",
                        }
                    ],
                    "title": "title",
                },
                "form_type": "more_volume",
                "intro": {
                    "description": "description",
                    "headline": "headline",
                },
                "name": "name",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "link_text",
                    "url": "url",
                },
                "questions": [
                    {
                        "format": "short_answer",
                        "label": "label",
                        "options": [
                            {
                                "key": "key",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 0,
                                },
                                "value": "value",
                            }
                        ],
                        "type": "email",
                    }
                ],
            },
            lead_form_id="lead_form_id",
            messaging_config={
                "keyword": "keyword",
                "message": "message",
            },
            multi_advertiser_ads=True,
            post_id="post_id",
            post_source="facebook",
            primary_texts=["string"],
            social_accounts=[{"id": "id"}],
            title="title",
            url="url",
            url_parameters={},
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
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
            call_to_action="apply_now",
            creatives=[
                {
                    "id": "id",
                    "crop": {
                        "height": 0,
                        "width": 0,
                        "x": 0,
                        "y": 0,
                    },
                    "format": "square",
                }
            ],
            descriptions=["string"],
            headlines=["string"],
            lead_form={
                "completion": {
                    "button_text": "button_text",
                    "description": "description",
                    "headline": "headline",
                    "url": "url",
                },
                "disclaimer": {
                    "body": "body",
                    "checkboxes": [
                        {
                            "checked_by_default": True,
                            "key": "key",
                            "required": True,
                            "text": "text",
                        }
                    ],
                    "title": "title",
                },
                "form_type": "more_volume",
                "intro": {
                    "description": "description",
                    "headline": "headline",
                },
                "name": "name",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "link_text",
                    "url": "url",
                },
                "questions": [
                    {
                        "format": "short_answer",
                        "label": "label",
                        "options": [
                            {
                                "key": "key",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 0,
                                },
                                "value": "value",
                            }
                        ],
                        "type": "email",
                    }
                ],
            },
            lead_form_id="lead_form_id",
            messaging_config={
                "keyword": "keyword",
                "message": "message",
            },
            multi_advertiser_ads=True,
            post_id="post_id",
            post_source="facebook",
            primary_texts=["string"],
            social_accounts=[{"id": "id"}],
            title="title",
            url="url",
            url_parameters={},
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
            ad_group_id="ad_group_id",
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
            count=0,
            preserve_engagement=True,
            target_ad_group_id="target_ad_group_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
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
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause_with_all_params(self, client: Whop) -> None:
        ad = client.ads.pause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Whop) -> None:
        response = client.ads.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Whop) -> None:
        with client.ads.with_streaming_response.pause(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause(self, client: Whop) -> None:
        ad = client.ads.unpause(
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpause_with_all_params(self, client: Whop) -> None:
        ad = client.ads.unpause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpause(self, client: Whop) -> None:
        response = client.ads.with_raw_response.unpause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpause(self, client: Whop) -> None:
        with client.ads.with_streaming_response.unpause(
            id="id",
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
                id="",
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
            ad_group={},
            ad_group_id="ad_group_id",
            call_to_action="apply_now",
            creatives=[
                {
                    "id": "id",
                    "crop": {
                        "height": 0,
                        "width": 0,
                        "x": 0,
                        "y": 0,
                    },
                    "format": "square",
                }
            ],
            descriptions=["string"],
            headlines=["string"],
            lead_form={
                "completion": {
                    "button_text": "button_text",
                    "description": "description",
                    "headline": "headline",
                    "url": "url",
                },
                "disclaimer": {
                    "body": "body",
                    "checkboxes": [
                        {
                            "checked_by_default": True,
                            "key": "key",
                            "required": True,
                            "text": "text",
                        }
                    ],
                    "title": "title",
                },
                "form_type": "more_volume",
                "intro": {
                    "description": "description",
                    "headline": "headline",
                },
                "name": "name",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "link_text",
                    "url": "url",
                },
                "questions": [
                    {
                        "format": "short_answer",
                        "label": "label",
                        "options": [
                            {
                                "key": "key",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 0,
                                },
                                "value": "value",
                            }
                        ],
                        "type": "email",
                    }
                ],
            },
            lead_form_id="lead_form_id",
            messaging_config={
                "keyword": "keyword",
                "message": "message",
            },
            multi_advertiser_ads=True,
            post_id="post_id",
            post_source="facebook",
            primary_texts=["string"],
            social_accounts=[{"id": "id"}],
            title="title",
            url="url",
            url_parameters={},
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
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
            call_to_action="apply_now",
            creatives=[
                {
                    "id": "id",
                    "crop": {
                        "height": 0,
                        "width": 0,
                        "x": 0,
                        "y": 0,
                    },
                    "format": "square",
                }
            ],
            descriptions=["string"],
            headlines=["string"],
            lead_form={
                "completion": {
                    "button_text": "button_text",
                    "description": "description",
                    "headline": "headline",
                    "url": "url",
                },
                "disclaimer": {
                    "body": "body",
                    "checkboxes": [
                        {
                            "checked_by_default": True,
                            "key": "key",
                            "required": True,
                            "text": "text",
                        }
                    ],
                    "title": "title",
                },
                "form_type": "more_volume",
                "intro": {
                    "description": "description",
                    "headline": "headline",
                },
                "name": "name",
                "phone_verification": True,
                "privacy_policy": {
                    "link_text": "link_text",
                    "url": "url",
                },
                "questions": [
                    {
                        "format": "short_answer",
                        "label": "label",
                        "options": [
                            {
                                "key": "key",
                                "logic": {
                                    "action": "go_to_question",
                                    "target_end_page_index": 0,
                                    "target_question_index": 0,
                                },
                                "value": "value",
                            }
                        ],
                        "type": "email",
                    }
                ],
            },
            lead_form_id="lead_form_id",
            messaging_config={
                "keyword": "keyword",
                "message": "message",
            },
            multi_advertiser_ads=True,
            post_id="post_id",
            post_source="facebook",
            primary_texts=["string"],
            social_accounts=[{"id": "id"}],
            title="title",
            url="url",
            url_parameters={},
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
            ad_group_id="ad_group_id",
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
            count=0,
            preserve_engagement=True,
            target_ad_group_id="target_ad_group_id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
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
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.pause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.pause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.pause(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.unpause(
            id="id",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpause_with_all_params(self, async_client: AsyncWhop) -> None:
        ad = await async_client.ads.unpause(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncWhop) -> None:
        response = await async_client.ads.with_raw_response.unpause(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(Ad, ad, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncWhop) -> None:
        async with async_client.ads.with_streaming_response.unpause(
            id="id",
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
                id="",
            )
