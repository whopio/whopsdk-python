# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import NotificationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        notification = client.notifications.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        notification = client.notifications.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
            account_id="biz_xxxxxxxxxxxxxx",
            experience_id="exp_xxxxxxxxxxxxxx",
            icon_user_id="user_xxxxxxxxxxxxxx",
            rest_path="/bookings/upcoming",
            subtitle="Tuesday 9:00 AM, Bay 2",
            user_ids=["user_xxxxxxxxxxxxxx"],
            api_version_date="2026-09-02-2",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.notifications.with_raw_response.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.notifications.with_streaming_response.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationCreateResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        notification = await async_client.notifications.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        notification = await async_client.notifications.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
            account_id="biz_xxxxxxxxxxxxxx",
            experience_id="exp_xxxxxxxxxxxxxx",
            icon_user_id="user_xxxxxxxxxxxxxx",
            rest_path="/bookings/upcoming",
            subtitle="Tuesday 9:00 AM, Bay 2",
            user_ids=["user_xxxxxxxxxxxxxx"],
            api_version_date="2026-09-02-2",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.notifications.with_raw_response.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.notifications.with_streaming_response.create(
            content="Drop off at 4180 Burnet Rd. Plan on two days for the full coating.",
            title="Your ceramic coating is booked",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationCreateResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True
