# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    AppListResponse,
    AppLogsResponse,
    AppDeleteResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import App

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        app = client.apps.create(
            name="Shine Time Booking",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        app = client.apps.create(
            name="Shine Time Booking",
            account_id="biz_xxxxxxxxxxxxxx",
            app_type="website",
            base_url="https://booking.shinetime.example",
            icon={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            redirect_uris=["https://booking.shinetime.example/oauth/callback"],
            route="shine-time-booking-site",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.apps.with_raw_response.create(
            name="Shine Time Booking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.apps.with_streaming_response.create(
            name="Shine Time Booking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        app = client.apps.retrieve(
            "id",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.apps.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.apps.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        app = client.apps.update(
            id="id",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        app = client.apps.update(
            id="id",
            app_store_description="Shine Time Booking turns a whop into a booking calendar. Members pick a package, choose a slot that fits the day's route, and pay up front.",
            app_type="b2c_app",
            base_url="https://booking.shinetime.example",
            dashboard_path="/dashboard/[companyId]",
            description="Let members book a mobile detailing appointment without leaving your whop.",
            discover_path="/discover",
            experience_path="/experiences/[experienceId]",
            icon={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            name="Shine Time Booking Pro",
            oauth_client_type="confidential",
            openapi_path="/openapi.json",
            production_android_build_id="apbu_xxxxxxxxxxxxxx",
            production_ios_build_id="apbu_xxxxxxxxxxxxxx",
            production_web_build_id="apbu_xxxxxxxxxxxxxx",
            redirect_uris=["https://booking.shinetime.example/oauth/callback"],
            required_scopes=["read_user"],
            route="shine-time-booking-pro",
            secrets={"BOOKING_CALENDAR_ID": "cal_9f21"},
            skills_path="/skills",
            status="unlisted",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.apps.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.apps.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        app = client.apps.list()
        assert_matches_type(SyncCursorPage[AppListResponse], app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        app = client.apps.list(
            account_id="account_id",
            after="after",
            app_type="b2b_app",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            query="query",
            verified_apps_only=True,
            view_type="hub",
        )
        assert_matches_type(SyncCursorPage[AppListResponse], app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.apps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(SyncCursorPage[AppListResponse], app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.apps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(SyncCursorPage[AppListResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        app = client.apps.delete(
            "id",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.apps.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.apps.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_logs(self, client: Whop) -> None:
        app = client.apps.logs(
            id="id",
        )
        assert_matches_type(AppLogsResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_logs_with_all_params(self, client: Whop) -> None:
        app = client.apps.logs(
            id="id",
            after="after",
            app_build_id="app_build_id",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            first=0,
            level="log",
            query="query",
        )
        assert_matches_type(AppLogsResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_logs(self, client: Whop) -> None:
        response = client.apps.with_raw_response.logs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppLogsResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_logs(self, client: Whop) -> None:
        with client.apps.with_streaming_response.logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppLogsResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_logs(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.with_raw_response.logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_permissions(self, client: Whop) -> None:
        app = client.apps.update_permissions(
            id="id",
            requested_permissions=[
                {
                    "action": "company:basic:read",
                    "is_required": True,
                    "justification": "Reads basic account info to render the dashboard home.",
                }
            ],
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_permissions(self, client: Whop) -> None:
        response = client.apps.with_raw_response.update_permissions(
            id="id",
            requested_permissions=[
                {
                    "action": "company:basic:read",
                    "is_required": True,
                    "justification": "Reads basic account info to render the dashboard home.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_permissions(self, client: Whop) -> None:
        with client.apps.with_streaming_response.update_permissions(
            id="id",
            requested_permissions=[
                {
                    "action": "company:basic:read",
                    "is_required": True,
                    "justification": "Reads basic account info to render the dashboard home.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_permissions(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.apps.with_raw_response.update_permissions(
                id="",
                requested_permissions=[
                    {
                        "action": "company:basic:read",
                        "is_required": True,
                        "justification": "Reads basic account info to render the dashboard home.",
                    }
                ],
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.create(
            name="Shine Time Booking",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.create(
            name="Shine Time Booking",
            account_id="biz_xxxxxxxxxxxxxx",
            app_type="website",
            base_url="https://booking.shinetime.example",
            icon={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            redirect_uris=["https://booking.shinetime.example/oauth/callback"],
            route="shine-time-booking-site",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.create(
            name="Shine Time Booking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.create(
            name="Shine Time Booking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.retrieve(
            "id",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.update(
            id="id",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.update(
            id="id",
            app_store_description="Shine Time Booking turns a whop into a booking calendar. Members pick a package, choose a slot that fits the day's route, and pay up front.",
            app_type="b2c_app",
            base_url="https://booking.shinetime.example",
            dashboard_path="/dashboard/[companyId]",
            description="Let members book a mobile detailing appointment without leaving your whop.",
            discover_path="/discover",
            experience_path="/experiences/[experienceId]",
            icon={
                "id": "file_xxxxxxxxxxxxxx",
                "direct_upload_id": "eyJfcmFpbHMiOnsiZGF0YSI6MSwicHVyIjoiYmxvYl9pZCJ9fQ==--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            name="Shine Time Booking Pro",
            oauth_client_type="confidential",
            openapi_path="/openapi.json",
            production_android_build_id="apbu_xxxxxxxxxxxxxx",
            production_ios_build_id="apbu_xxxxxxxxxxxxxx",
            production_web_build_id="apbu_xxxxxxxxxxxxxx",
            redirect_uris=["https://booking.shinetime.example/oauth/callback"],
            required_scopes=["read_user"],
            route="shine-time-booking-pro",
            secrets={"BOOKING_CALENDAR_ID": "cal_9f21"},
            skills_path="/skills",
            status="unlisted",
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.list()
        assert_matches_type(AsyncCursorPage[AppListResponse], app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.list(
            account_id="account_id",
            after="after",
            app_type="b2b_app",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            query="query",
            verified_apps_only=True,
            view_type="hub",
        )
        assert_matches_type(AsyncCursorPage[AppListResponse], app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AsyncCursorPage[AppListResponse], app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AsyncCursorPage[AppListResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.delete(
            "id",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_logs(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.logs(
            id="id",
        )
        assert_matches_type(AppLogsResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_logs_with_all_params(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.logs(
            id="id",
            after="after",
            app_build_id="app_build_id",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            first=0,
            level="log",
            query="query",
        )
        assert_matches_type(AppLogsResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.logs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppLogsResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppLogsResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_logs(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.with_raw_response.logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_permissions(self, async_client: AsyncWhop) -> None:
        app = await async_client.apps.update_permissions(
            id="id",
            requested_permissions=[
                {
                    "action": "company:basic:read",
                    "is_required": True,
                    "justification": "Reads basic account info to render the dashboard home.",
                }
            ],
        )
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_permissions(self, async_client: AsyncWhop) -> None:
        response = await async_client.apps.with_raw_response.update_permissions(
            id="id",
            requested_permissions=[
                {
                    "action": "company:basic:read",
                    "is_required": True,
                    "justification": "Reads basic account info to render the dashboard home.",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(App, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_permissions(self, async_client: AsyncWhop) -> None:
        async with async_client.apps.with_streaming_response.update_permissions(
            id="id",
            requested_permissions=[
                {
                    "action": "company:basic:read",
                    "is_required": True,
                    "justification": "Reads basic account info to render the dashboard home.",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(App, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_permissions(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.apps.with_raw_response.update_permissions(
                id="",
                requested_permissions=[
                    {
                        "action": "company:basic:read",
                        "is_required": True,
                        "justification": "Reads basic account info to render the dashboard home.",
                    }
                ],
            )
