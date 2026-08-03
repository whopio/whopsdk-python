# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types.users.preferences import NotificationSetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: Whop) -> None:
        notification = client.users.preferences.notifications.set(
            preferences=[
                {
                    "level": "all",
                    "scope": {},
                }
            ],
        )
        assert_matches_type(NotificationSetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Whop) -> None:
        response = client.users.preferences.notifications.with_raw_response.set(
            preferences=[
                {
                    "level": "all",
                    "scope": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationSetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Whop) -> None:
        with client.users.preferences.notifications.with_streaming_response.set(
            preferences=[
                {
                    "level": "all",
                    "scope": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationSetResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncWhop) -> None:
        notification = await async_client.users.preferences.notifications.set(
            preferences=[
                {
                    "level": "all",
                    "scope": {},
                }
            ],
        )
        assert_matches_type(NotificationSetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncWhop) -> None:
        response = await async_client.users.preferences.notifications.with_raw_response.set(
            preferences=[
                {
                    "level": "all",
                    "scope": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationSetResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncWhop) -> None:
        async with async_client.users.preferences.notifications.with_streaming_response.set(
            preferences=[
                {
                    "level": "all",
                    "scope": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationSetResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True
