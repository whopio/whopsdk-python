# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest
import standardwebhooks

from whop_sdk import Whop

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_unwrap(self, client: Whop) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"id":"msg_xxxxxxxxxxxxxxxxxxxxxxxx","api_version":"v1","data":{"id":"inv_xxxxxxxxxxxxxx","created_at":"2023-12-01T05:00:00.401Z","current_plan":{"id":"plan_xxxxxxxxxxxxx","currency":"usd","formatted_price":"$10.00"},"due_date":"2023-12-01T05:00:00.401Z","email_address":"customer@example.com","fetch_invoice_token":"fetch_invoice_token","number":"#0001","status":"open","user":{"id":"user_xxxxxxxxxxxxx","name":"John Doe","username":"johndoe42"}},"timestamp":"2025-01-01T00:00:00.000Z","type":"invoice.created"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    def test_method_unwrap(self, client: Whop) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"id":"msg_xxxxxxxxxxxxxxxxxxxxxxxx","api_version":"v1","data":{"id":"inv_xxxxxxxxxxxxxx","created_at":"2023-12-01T05:00:00.401Z","current_plan":{"id":"plan_xxxxxxxxxxxxx","currency":"usd","formatted_price":"$10.00"},"due_date":"2023-12-01T05:00:00.401Z","email_address":"customer@example.com","fetch_invoice_token":"fetch_invoice_token","number":"#0001","status":"open","user":{"id":"user_xxxxxxxxxxxxx","name":"John Doe","username":"johndoe42"}},"timestamp":"2025-01-01T00:00:00.000Z","type":"invoice.created"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)
