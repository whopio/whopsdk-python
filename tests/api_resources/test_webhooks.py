# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast
from datetime import datetime, timezone

import pytest
import standardwebhooks

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Webhook,
    WebhookListResponse,
    WebhookTestResponse,
    WebhookDeleteResponse,
    WebhookReplayResponse,
    WebhookListDeliveriesResponse,
    WebhookReplayDeliveryResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        webhook = client.webhooks.create(
            url="https://example.com/hooks",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.create(
            url="https://example.com/hooks",
            api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=True,
            events=["payment.succeeded"],
            resource_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.create(
            url="https://example.com/hooks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.create(
            url="https://example.com/hooks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        webhook = client.webhooks.retrieve(
            "id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        webhook = client.webhooks.update(
            id="id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.update(
            id="id",
            api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=False,
            events=["payment.failed"],
            url="https://example.com/shine-time/whop-updated",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        webhook = client.webhooks.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPage[WebhookListResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.list(
            account_id="account_id",
            after="after",
            app_id="app_id",
            before="before",
            first=0,
            has_failures=True,
            include_app_webhooks=True,
            last=0,
        )
        assert_matches_type(SyncCursorPage[WebhookListResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncCursorPage[WebhookListResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncCursorPage[WebhookListResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        webhook = client.webhooks.delete(
            "id",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_deliveries(self, client: Whop) -> None:
        webhook = client.webhooks.list_deliveries(
            id="id",
        )
        assert_matches_type(SyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_deliveries_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.list_deliveries(
            id="id",
            after="after",
            first=0,
        )
        assert_matches_type(SyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_deliveries(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.list_deliveries(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_deliveries(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.list_deliveries(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_deliveries(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.list_deliveries(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay(self, client: Whop) -> None:
        webhook = client.webhooks.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
        )
        assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
            events=["string"],
            failed_only=True,
            sent_before="sent_before",
        )
        assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replay(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replay(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replay(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.replay(
                id="",
                sent_after="2026-01-01T12:00:00.000Z",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay_delivery(self, client: Whop) -> None:
        webhook = client.webhooks.replay_delivery(
            delivery_id="delivery_id",
            id="id",
        )
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replay_delivery(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.replay_delivery(
            delivery_id="delivery_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replay_delivery(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.replay_delivery(
            delivery_id="delivery_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replay_delivery(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.replay_delivery(
                delivery_id="delivery_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.webhooks.with_raw_response.replay_delivery(
                delivery_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Whop) -> None:
        webhook = client.webhooks.test(
            id="id",
            event="payment.succeeded",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.test(
            id="id",
            event="payment.succeeded",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.test(
            id="id",
            event="payment.succeeded",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.test(
                id="",
                event="payment.succeeded",
            )

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_unwrap(self, client: Whop, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        client = client.with_options(webhook_key=client_opt)

        data = """{"id":"msg_xxxxxxxxxxxxxxxxxxxxxxxx","api_version":"v1","api_version_date":"2026-07-20","data":{"id":"adcamp_xxxxxxxxxxxxxx","added_to_cart_value":12650,"added_to_carts":165,"budget_amount":50,"budget_optimization":"ad_group","budget_type":"daily","click_through_rate":0.025,"clicks":5500,"completed_registration_value":1650,"completed_registrations":55,"contact_value":2640,"contacts":88,"cost_per_added_to_cart":8,"cost_per_click":0.24,"cost_per_completed_registration":24,"cost_per_contact":15,"cost_per_lead":10,"cost_per_mille":6,"cost_per_purchase":30,"cost_per_result":40,"cost_per_schedule":22,"cost_per_submitted_application":120,"cost_per_unique_click":0.4,"cost_per_viewed_content":1.1,"created_at":"2026-01-01T12:00:00.000Z","custom_conversions":41,"custom_event_counts":{"gift_card_purchased":5,"quote_requested":33},"custom_event_values":{"gift_card_purchased":750,"quote_requested":0},"delivery_status":"issues","frequency":0,"impressions":220000,"issues":[{"id":"adiss_xxxxxxxxxxxxxx","message":"Your ad was rejected for unacceptable business practices. Edit the ad's content and resubmit.","resource_id":"ad_xxxxxxxxxxxxxx","resource_type":"ad"}],"lead_value":3960,"leads":132,"objective":"leads","optimization_goal":"optimization_goal","platform":"meta","purchase_value":7920,"purchases":44,"reach":0,"result_event":"custom","result_event_name":"quote_requested","results":33,"return_on_ad_spend":6,"schedule_value":5400,"schedules":60,"special_ad_categories":["employment"],"spend":1320,"spend_currency":"usd","status":"active","submitted_application_value":1320,"submitted_applications":11,"title":"Ceramic coating — Austin leads","unique_click_through_rate":0,"unique_clicks":3300,"updated_at":"2026-01-01T12:00:00.000Z","viewed_content_value":8400,"viewed_contents":1200,"bid_type":"average_target"},"timestamp":"2025-01-01T00:00:00.000Z","type":"ad_campaign.payment_failed","company_id":"biz_xxxxxxxxxxxxxx"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=method_opt)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.create(
            url="https://example.com/hooks",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.create(
            url="https://example.com/hooks",
            api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=True,
            events=["payment.succeeded"],
            resource_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            url="https://example.com/hooks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            url="https://example.com/hooks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.retrieve(
            "id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.update(
            id="id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.update(
            id="id",
            api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=False,
            events=["payment.failed"],
            url="https://example.com/shine-time/whop-updated",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPage[WebhookListResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.list(
            account_id="account_id",
            after="after",
            app_id="app_id",
            before="before",
            first=0,
            has_failures=True,
            include_app_webhooks=True,
            last=0,
        )
        assert_matches_type(AsyncCursorPage[WebhookListResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncCursorPage[WebhookListResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncCursorPage[WebhookListResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.delete(
            "id",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_deliveries(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.list_deliveries(
            id="id",
        )
        assert_matches_type(AsyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_deliveries_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.list_deliveries(
            id="id",
            after="after",
            first=0,
        )
        assert_matches_type(AsyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_deliveries(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.list_deliveries(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_deliveries(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.list_deliveries(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncCursorPage[WebhookListDeliveriesResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_deliveries(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.list_deliveries(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
        )
        assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
            events=["string"],
            failed_only=True,
            sent_before="sent_before",
        )
        assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.replay(
            id="id",
            sent_after="2026-01-01T12:00:00.000Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookReplayResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replay(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.replay(
                id="",
                sent_after="2026-01-01T12:00:00.000Z",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay_delivery(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.replay_delivery(
            delivery_id="delivery_id",
            id="id",
        )
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replay_delivery(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.replay_delivery(
            delivery_id="delivery_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replay_delivery(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.replay_delivery(
            delivery_id="delivery_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replay_delivery(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.replay_delivery(
                delivery_id="delivery_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.webhooks.with_raw_response.replay_delivery(
                delivery_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.test(
            id="id",
            event="payment.succeeded",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.test(
            id="id",
            event="payment.succeeded",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.test(
            id="id",
            event="payment.succeeded",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.test(
                id="",
                event="payment.succeeded",
            )

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_unwrap(self, async_client: Whop, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        async_client = async_client.with_options(webhook_key=client_opt)

        data = """{"id":"msg_xxxxxxxxxxxxxxxxxxxxxxxx","api_version":"v1","api_version_date":"2026-07-20","data":{"id":"adcamp_xxxxxxxxxxxxxx","added_to_cart_value":12650,"added_to_carts":165,"budget_amount":50,"budget_optimization":"ad_group","budget_type":"daily","click_through_rate":0.025,"clicks":5500,"completed_registration_value":1650,"completed_registrations":55,"contact_value":2640,"contacts":88,"cost_per_added_to_cart":8,"cost_per_click":0.24,"cost_per_completed_registration":24,"cost_per_contact":15,"cost_per_lead":10,"cost_per_mille":6,"cost_per_purchase":30,"cost_per_result":40,"cost_per_schedule":22,"cost_per_submitted_application":120,"cost_per_unique_click":0.4,"cost_per_viewed_content":1.1,"created_at":"2026-01-01T12:00:00.000Z","custom_conversions":41,"custom_event_counts":{"gift_card_purchased":5,"quote_requested":33},"custom_event_values":{"gift_card_purchased":750,"quote_requested":0},"delivery_status":"issues","frequency":0,"impressions":220000,"issues":[{"id":"adiss_xxxxxxxxxxxxxx","message":"Your ad was rejected for unacceptable business practices. Edit the ad's content and resubmit.","resource_id":"ad_xxxxxxxxxxxxxx","resource_type":"ad"}],"lead_value":3960,"leads":132,"objective":"leads","optimization_goal":"optimization_goal","platform":"meta","purchase_value":7920,"purchases":44,"reach":0,"result_event":"custom","result_event_name":"quote_requested","results":33,"return_on_ad_spend":6,"schedule_value":5400,"schedules":60,"special_ad_categories":["employment"],"spend":1320,"spend_currency":"usd","status":"active","submitted_application_value":1320,"submitted_applications":11,"title":"Ceramic coating — Austin leads","unique_click_through_rate":0,"unique_clicks":3300,"updated_at":"2026-01-01T12:00:00.000Z","viewed_content_value":8400,"viewed_contents":1200,"bid_type":"average_target"},"timestamp":"2025-01-01T00:00:00.000Z","type":"ad_campaign.payment_failed","company_id":"biz_xxxxxxxxxxxxxx"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = async_client.webhooks.unwrap(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = async_client.webhooks.unwrap(data, headers=bad_header, key=method_opt)
