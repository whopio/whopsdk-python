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
    WebhookDeleteResponse,
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
            body_api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=True,
            events=["payment.succeeded"],
            resource_id="biz_xxxxxxxxxxxxxx",
            header_api_version_date="2026-09-04",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
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
            id="id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.retrieve(
            id="id",
            api_version_date="2026-09-04",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            id="id",
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
                id="",
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
            body_api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=False,
            events=["payment.failed"],
            url="https://example.com/shine-time/whop-updated",
            header_api_version_date="2026-09-04",
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
            api_version_date="2026-09-04",
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
            id="id",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Whop) -> None:
        webhook = client.webhooks.delete(
            id="id",
            api_version_date="2026-09-04",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.webhooks.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.webhooks.with_streaming_response.delete(
            id="id",
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
                id="",
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

        data = """{"id":"msg_xxxxxxxxxxxxxxxxxxxxxxxx","api_version":"v1","api_version_date":"2026-07-20","data":{"id":"biz_xxxxxxxxxxxxxx","balances":[{"balance":"50.0","breakdown":{"available":"1500.0","in_transit":"0","pending":"0","pending_settlements":[{"amount":"12.5","date":"2026-01-01"}],"reserve":"0"},"icon_url":"https://assets.whop.com/tokens/usd.png","name":"US Dollar","price_usd":1,"symbol":"USD","value_usd":"50.00"}],"banner_image_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","business_address":{"city":"Austin","country":"US","line1":"4180 Burnet Rd","line2":"Suite 2","postal_code":"78756","state":"TX"},"business_name":"Shine Time Auto Detailing, LLC","business_type":"other","can_transfer_pending_balance_to_children":false,"capabilities":{"accept_bank_payments":"active","accept_bnpl_payments":"inactive","accept_card_payments":"active","bank_deposit":"inactive","card_deposit":"active","card_issuing":"inactive","crypto_deposit":"active","crypto_payout":"inactive","instant_payout":"inactive","run_ads":"active","standard_payout":"inactive","transfer":"inactive"},"cards":{"kind":"individual","status":"approved"},"collect_vat_id":true,"company_formation":{"documents":[{"id":"file_xxxxxxxxxxxxxx","name":"Articles of Organization","type":"articles_of_organization","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}],"ein_registered":false,"legal_name":"Shine Time Auto Detailing, LLC","signatures":{"form8821":{"status":"pending","expires_at":"2026-01-01T12:00:00.000Z","url":"https://sign.doola.com/shine-time-auto-detailing/form8821"},"ss4":{"status":"pending","expires_at":"2026-01-01T12:00:00.000Z","url":"https://sign.doola.com/shine-time-auto-detailing/form8821"}},"state_registered":true,"status":"draft"},"country":"us","created_at":"2026-01-01T12:00:00.000Z","description":"Mobile ceramic coating, paint correction, and interior detailing across the Austin metro.","email":"marcus@shinetime.example","eula":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"home_preferences":["hide_member_count"],"industry_group":"automotive","industry_type":"other","invoice_prefix":"SHINE","logo_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","metadata":{"external_id":"shop_4417","region":"austin"},"onboarding_type":"seller","opengraph_image_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","opengraph_image_variant":"black","other_business_description":"Mobile auto detailing","other_industry_description":"Automotive services","owner":{"id":"user_xxxxxxxxxxxxxx","name":"Dana Whitfield","profile_picture":{"url":"https://ui-avatars.com/api/"},"username":"danawhitfield"},"parent_account":{"id":"biz_xxxxxxxxxxxxxx","logo_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","route":"shine-time-holdings","title":"Shine Time Holdings"},"payment_controls":{"dispute_alert_auto_refund":{"locked":false,"threshold_usd":500},"dispute_alert_fee_usd":29,"enforce_3ds":false,"financing_disabled":false,"high_risk_processing_fee_percentage":0,"pending_auto_topup_fee_percentage":2,"pending_balance_delay_days":0,"reserve":{"hold_period_days":14,"percentage":15},"resolution_center_auto_refund":{"card_threshold_usd":50,"financing_threshold_usd":25,"locked":false,"paypal_threshold_usd":40},"restricted_payment_methods":["card_visa"],"undated_pending_reason":"pending_information_request","withdrawal_schedule":{"day":0,"frequency":"manual","next_payout_date":"next_payout_date"}},"privacy_policy":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"product_tax_code":{"id":"ptc_xxxxxxxxxxxxxx","name":"General - Digital Goods","product_type":"digital"},"recommended_actions":[{"action":"apply_for_financing","blocked_capabilities":["accept_bnpl_payments"],"cta":"https://whop.com/dashboard/biz_xxxxxxxxxxxxxx/settings/payments/","cta_label":"Apply","description":"Let customers pay over time with buy now, pay later.","icon_url":"https://whop.com/illustrations/orange/piggy-bank.svg","impact_score":86,"reasoning":"Financing lifts conversion on the $249 ceramic coating, the priciest job on the menu.","status":"optional","title":"Offer financing at checkout"}],"require_2fa":true,"required_actions":[{"action":"verify_identity","blocked_capabilities":["standard_payout"],"cta":"https://whop.com/dashboard/biz_xxxxxxxxxxxxxx/balance/","cta_label":"Verify now","description":"Complete verification to withdraw your earnings.","icon_url":"https://whop.com/illustrations/orange/shield.svg","status":"required","title":"Complete your identity verification"}],"return_policy":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"route":"biz_xxxxxxxxxxxxxx","send_customer_emails":false,"show_joined_whops":false,"show_reviews_dtc":false,"show_user_directory":false,"social_links":[{"id":"social_1","title":"@shinetimedetail","url":"https://instagram.com/shinetimedetail","website":"instagram"}],"stablecoin_rails":false,"status":"active","status_reason":"Payments are paused while we review recent chargebacks on this account.","store_page_config":{"accent_color":"red","layout":"compact","profile_variant":"business","whop_affiliate_link":true},"target_audience":"Owners of new and enthusiast vehicles in Austin, TX","tax_collection_enabled_states":["TX"],"tax_identifiers":[{"id":"txid_xxxxxxxxxxxxxx","tax_id_type":"eu_vat","tax_id_value":"DE123456789"}],"tax_remitted_by":"self","tax_type":"inclusive","terms_of_service":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"three_ds_level":"mandate_challenge","title":"Shine Time Auto Detailing","total_earned_usd":0,"total_usd":"50.00","use_logo_as_opengraph_image_fallback":true,"verification":{"business":null,"individual":null},"volume_usd":0,"wallet":{"id":"cwal_xxxxxxxxxxxxxx","address":"0xabc123","network":"ethereum"}},"timestamp":"2025-01-01T00:00:00.000Z","type":"account.updated","account_id":"biz_xxxxxxxxxxxxxx","previous_attributes":{"title":"Webb's Mobile Detailing"}}"""
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
            body_api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=True,
            events=["payment.succeeded"],
            resource_id="biz_xxxxxxxxxxxxxx",
            header_api_version_date="2026-09-04",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
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
            id="id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.retrieve(
            id="id",
            api_version_date="2026-09-04",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            id="id",
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
                id="",
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
            body_api_version_date="2026-01-01",
            child_resource_events=True,
            enabled=False,
            events=["payment.failed"],
            url="https://example.com/shine-time/whop-updated",
            header_api_version_date="2026-09-04",
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
            api_version_date="2026-09-04",
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
            id="id",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWhop) -> None:
        webhook = await async_client.webhooks.delete(
            id="id",
            api_version_date="2026-09-04",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            id="id",
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
                id="",
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

        data = """{"id":"msg_xxxxxxxxxxxxxxxxxxxxxxxx","api_version":"v1","api_version_date":"2026-07-20","data":{"id":"biz_xxxxxxxxxxxxxx","balances":[{"balance":"50.0","breakdown":{"available":"1500.0","in_transit":"0","pending":"0","pending_settlements":[{"amount":"12.5","date":"2026-01-01"}],"reserve":"0"},"icon_url":"https://assets.whop.com/tokens/usd.png","name":"US Dollar","price_usd":1,"symbol":"USD","value_usd":"50.00"}],"banner_image_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","business_address":{"city":"Austin","country":"US","line1":"4180 Burnet Rd","line2":"Suite 2","postal_code":"78756","state":"TX"},"business_name":"Shine Time Auto Detailing, LLC","business_type":"other","can_transfer_pending_balance_to_children":false,"capabilities":{"accept_bank_payments":"active","accept_bnpl_payments":"inactive","accept_card_payments":"active","bank_deposit":"inactive","card_deposit":"active","card_issuing":"inactive","crypto_deposit":"active","crypto_payout":"inactive","instant_payout":"inactive","run_ads":"active","standard_payout":"inactive","transfer":"inactive"},"cards":{"kind":"individual","status":"approved"},"collect_vat_id":true,"company_formation":{"documents":[{"id":"file_xxxxxxxxxxxxxx","name":"Articles of Organization","type":"articles_of_organization","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}],"ein_registered":false,"legal_name":"Shine Time Auto Detailing, LLC","signatures":{"form8821":{"status":"pending","expires_at":"2026-01-01T12:00:00.000Z","url":"https://sign.doola.com/shine-time-auto-detailing/form8821"},"ss4":{"status":"pending","expires_at":"2026-01-01T12:00:00.000Z","url":"https://sign.doola.com/shine-time-auto-detailing/form8821"}},"state_registered":true,"status":"draft"},"country":"us","created_at":"2026-01-01T12:00:00.000Z","description":"Mobile ceramic coating, paint correction, and interior detailing across the Austin metro.","email":"marcus@shinetime.example","eula":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"home_preferences":["hide_member_count"],"industry_group":"automotive","industry_type":"other","invoice_prefix":"SHINE","logo_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","metadata":{"external_id":"shop_4417","region":"austin"},"onboarding_type":"seller","opengraph_image_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","opengraph_image_variant":"black","other_business_description":"Mobile auto detailing","other_industry_description":"Automotive services","owner":{"id":"user_xxxxxxxxxxxxxx","name":"Dana Whitfield","profile_picture":{"url":"https://ui-avatars.com/api/"},"username":"danawhitfield"},"parent_account":{"id":"biz_xxxxxxxxxxxxxx","logo_url":"https://whop-assets-example.s3.amazonaws.com/uploads/image/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","route":"shine-time-holdings","title":"Shine Time Holdings"},"payment_controls":{"dispute_alert_auto_refund":{"locked":false,"threshold_usd":500},"dispute_alert_fee_usd":29,"enforce_3ds":false,"financing_disabled":false,"high_risk_processing_fee_percentage":0,"pending_auto_topup_fee_percentage":2,"pending_balance_delay_days":0,"reserve":{"hold_period_days":14,"percentage":15},"resolution_center_auto_refund":{"card_threshold_usd":50,"financing_threshold_usd":25,"locked":false,"paypal_threshold_usd":40},"restricted_payment_methods":["card_visa"],"undated_pending_reason":"pending_information_request","withdrawal_schedule":{"day":0,"frequency":"manual","next_payout_date":"next_payout_date"}},"privacy_policy":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"product_tax_code":{"id":"ptc_xxxxxxxxxxxxxx","name":"General - Digital Goods","product_type":"digital"},"recommended_actions":[{"action":"apply_for_financing","blocked_capabilities":["accept_bnpl_payments"],"cta":"https://whop.com/dashboard/biz_xxxxxxxxxxxxxx/settings/payments/","cta_label":"Apply","description":"Let customers pay over time with buy now, pay later.","icon_url":"https://whop.com/illustrations/orange/piggy-bank.svg","impact_score":86,"reasoning":"Financing lifts conversion on the $249 ceramic coating, the priciest job on the menu.","status":"optional","title":"Offer financing at checkout"}],"require_2fa":true,"required_actions":[{"action":"verify_identity","blocked_capabilities":["standard_payout"],"cta":"https://whop.com/dashboard/biz_xxxxxxxxxxxxxx/balance/","cta_label":"Verify now","description":"Complete verification to withdraw your earnings.","icon_url":"https://whop.com/illustrations/orange/shield.svg","status":"required","title":"Complete your identity verification"}],"return_policy":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"route":"biz_xxxxxxxxxxxxxx","send_customer_emails":false,"show_joined_whops":false,"show_reviews_dtc":false,"show_user_directory":false,"social_links":[{"id":"social_1","title":"@shinetimedetail","url":"https://instagram.com/shinetimedetail","website":"instagram"}],"stablecoin_rails":false,"status":"active","status_reason":"Payments are paused while we review recent chargebacks on this account.","store_page_config":{"accent_color":"red","layout":"compact","profile_variant":"business","whop_affiliate_link":true},"target_audience":"Owners of new and enthusiast vehicles in Austin, TX","tax_collection_enabled_states":["TX"],"tax_identifiers":[{"id":"txid_xxxxxxxxxxxxxx","tax_id_type":"eu_vat","tax_id_value":"DE123456789"}],"tax_remitted_by":"self","tax_type":"inclusive","terms_of_service":{"id":"file_xxxxxxxxxxxxxx","content_type":"application/pdf","created_at":"2026-01-01T12:00:00.000Z","filename":"evidence.pdf","object":"file","size":9670,"upload_status":"pending","url":"https://whop-assets-example.s3.amazonaws.com/uploads/audio/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","visibility":"private","multipart_chunk_size":5242880,"multipart_upload_id":"upload-id","multipart_upload_urls":[{"part_number":1,"url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"}],"upload_headers":{},"upload_url":"https://whop-assets-example.s3.amazonaws.com/uploads/2026-01-01/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/application.pdf"},"three_ds_level":"mandate_challenge","title":"Shine Time Auto Detailing","total_earned_usd":0,"total_usd":"50.00","use_logo_as_opengraph_image_fallback":true,"verification":{"business":null,"individual":null},"volume_usd":0,"wallet":{"id":"cwal_xxxxxxxxxxxxxx","address":"0xabc123","network":"ethereum"}},"timestamp":"2025-01-01T00:00:00.000Z","type":"account.updated","account_id":"biz_xxxxxxxxxxxxxx","previous_attributes":{"title":"Webb's Mobile Detailing"}}"""
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
