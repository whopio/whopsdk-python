# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    PixelValidation,
    EventListResponse,
    EventPulseResponse,
    EventCreateResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        event = client.events.create(
            account_id="account_id",
            event_name="course_completed",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        event = client.events.create(
            account_id="account_id",
            event_name="course_completed",
            action_source="email",
            context={
                "ad_campaign_id": "ad_campaign_id",
                "ad_id": "ad_id",
                "ad_set_id": "ad_set_id",
                "fbc": "fbc",
                "fbclid": "fbclid",
                "fbp": "fbp",
                "fingerprint": "fingerprint",
                "fingerprint_confidence": 6.9,
                "ga": "ga",
                "gbraid": "gbraid",
                "gclid": "gclid",
                "ig_sid": "ig_sid",
                "ip_address": "ip_address",
                "language": "language",
                "li_fat_id": "li_fat_id",
                "msclkid": "msclkid",
                "rdt_cid": "rdt_cid",
                "sccid": "sccid",
                "screen_resolution": "screen_resolution",
                "timezone": "timezone",
                "ttclid": "ttclid",
                "ttp": "ttp",
                "twclid": "twclid",
                "user_agent": "user_agent",
                "utm_campaign": "utm_campaign",
                "utm_content": "utm_content",
                "utm_id": "utm_id",
                "utm_medium": "utm_medium",
                "utm_source": "utm_source",
                "utm_term": "utm_term",
                "wbraid": "wbraid",
            },
            currency="usd",
            custom_name="custom_name",
            duration=42,
            event_id="evnt_xxxxxxxxxxxxx",
            event_time=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan_id="plan_xxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            referrer_url="referrer_url",
            resumed=True,
            source="source",
            title="title",
            url="url",
            user={
                "anonymous_id": "anonymous_id",
                "birthdate": "1990-01-15",
                "city": "city",
                "country": "country",
                "email": "email",
                "external_id": "external_id",
                "first_name": "first_name",
                "gender": "male",
                "last_name": "last_name",
                "linked_anonymous_id": "linked_anonymous_id",
                "linked_wuid": "linked_wuid",
                "member_id": "mber_xxxxxxxxxxxxx",
                "membership_id": "mem_xxxxxxxxxxxxxx",
                "name": "name",
                "phone": "phone",
                "postal_code": "postal_code",
                "state": "state",
                "user_id": "user_xxxxxxxxxxxxx",
                "username": "username",
            },
            value=6.9,
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.events.with_raw_response.create(
            account_id="account_id",
            event_name="course_completed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.events.with_streaming_response.create(
            account_id="account_id",
            event_name="course_completed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventCreateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        event = client.events.list()
        assert_matches_type(SyncCursorPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        event = client.events.list(
            account_id="account_id",
            after="after",
            attribution_model="last_touch",
            before="before",
            browser="browser",
            city="city",
            country="country",
            device="device",
            direction="asc",
            event="event",
            first=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            hostname="hostname",
            identifier="identifier",
            os="os",
            page="page",
            source="source",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            utm_source="utm_source",
        )
        assert_matches_type(SyncCursorPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncCursorPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncCursorPage[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pulse(self, client: Whop) -> None:
        event = client.events.pulse()
        assert_matches_type(EventPulseResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pulse_with_all_params(self, client: Whop) -> None:
        event = client.events.pulse(
            after="after",
            before="before",
            event="event",
            first=0,
        )
        assert_matches_type(EventPulseResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pulse(self, client: Whop) -> None:
        response = client.events.with_raw_response.pulse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventPulseResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pulse(self, client: Whop) -> None:
        with client.events.with_streaming_response.pulse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventPulseResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_pixel(self, client: Whop) -> None:
        event = client.events.validate_pixel()
        assert_matches_type(PixelValidation, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_pixel_with_all_params(self, client: Whop) -> None:
        event = client.events.validate_pixel(
            account_id="account_id",
            url="url",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(PixelValidation, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_pixel(self, client: Whop) -> None:
        response = client.events.with_raw_response.validate_pixel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(PixelValidation, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_pixel(self, client: Whop) -> None:
        with client.events.with_streaming_response.validate_pixel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(PixelValidation, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.create(
            account_id="account_id",
            event_name="course_completed",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.create(
            account_id="account_id",
            event_name="course_completed",
            action_source="email",
            context={
                "ad_campaign_id": "ad_campaign_id",
                "ad_id": "ad_id",
                "ad_set_id": "ad_set_id",
                "fbc": "fbc",
                "fbclid": "fbclid",
                "fbp": "fbp",
                "fingerprint": "fingerprint",
                "fingerprint_confidence": 6.9,
                "ga": "ga",
                "gbraid": "gbraid",
                "gclid": "gclid",
                "ig_sid": "ig_sid",
                "ip_address": "ip_address",
                "language": "language",
                "li_fat_id": "li_fat_id",
                "msclkid": "msclkid",
                "rdt_cid": "rdt_cid",
                "sccid": "sccid",
                "screen_resolution": "screen_resolution",
                "timezone": "timezone",
                "ttclid": "ttclid",
                "ttp": "ttp",
                "twclid": "twclid",
                "user_agent": "user_agent",
                "utm_campaign": "utm_campaign",
                "utm_content": "utm_content",
                "utm_id": "utm_id",
                "utm_medium": "utm_medium",
                "utm_source": "utm_source",
                "utm_term": "utm_term",
                "wbraid": "wbraid",
            },
            currency="usd",
            custom_name="custom_name",
            duration=42,
            event_id="evnt_xxxxxxxxxxxxx",
            event_time=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan_id="plan_xxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            referrer_url="referrer_url",
            resumed=True,
            source="source",
            title="title",
            url="url",
            user={
                "anonymous_id": "anonymous_id",
                "birthdate": "1990-01-15",
                "city": "city",
                "country": "country",
                "email": "email",
                "external_id": "external_id",
                "first_name": "first_name",
                "gender": "male",
                "last_name": "last_name",
                "linked_anonymous_id": "linked_anonymous_id",
                "linked_wuid": "linked_wuid",
                "member_id": "mber_xxxxxxxxxxxxx",
                "membership_id": "mem_xxxxxxxxxxxxxx",
                "name": "name",
                "phone": "phone",
                "postal_code": "postal_code",
                "state": "state",
                "user_id": "user_xxxxxxxxxxxxx",
                "username": "username",
            },
            value=6.9,
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.events.with_raw_response.create(
            account_id="account_id",
            event_name="course_completed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.events.with_streaming_response.create(
            account_id="account_id",
            event_name="course_completed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventCreateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.list()
        assert_matches_type(AsyncCursorPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.list(
            account_id="account_id",
            after="after",
            attribution_model="last_touch",
            before="before",
            browser="browser",
            city="city",
            country="country",
            device="device",
            direction="asc",
            event="event",
            first=0,
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            hostname="hostname",
            identifier="identifier",
            os="os",
            page="page",
            source="source",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            utm_source="utm_source",
        )
        assert_matches_type(AsyncCursorPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncCursorPage[EventListResponse], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncCursorPage[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pulse(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.pulse()
        assert_matches_type(EventPulseResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pulse_with_all_params(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.pulse(
            after="after",
            before="before",
            event="event",
            first=0,
        )
        assert_matches_type(EventPulseResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pulse(self, async_client: AsyncWhop) -> None:
        response = await async_client.events.with_raw_response.pulse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventPulseResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pulse(self, async_client: AsyncWhop) -> None:
        async with async_client.events.with_streaming_response.pulse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventPulseResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_pixel(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.validate_pixel()
        assert_matches_type(PixelValidation, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_pixel_with_all_params(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.validate_pixel(
            account_id="account_id",
            url="url",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(PixelValidation, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_pixel(self, async_client: AsyncWhop) -> None:
        response = await async_client.events.with_raw_response.validate_pixel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(PixelValidation, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_pixel(self, async_client: AsyncWhop) -> None:
        async with async_client.events.with_streaming_response.validate_pixel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(PixelValidation, event, path=["response"])

        assert cast(Any, response.is_closed) is True
