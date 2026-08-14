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
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        event = client.events.create(
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
            action_source="website",
            context={
                "ad_campaign_id": "23851234567890123",
                "ad_id": "23851234567890125",
                "ad_set_id": "23851234567890124",
                "fbc": "fb.1.xxxxxxxxxx.IwAR0shine",
                "fbclid": "IwAR0shineTimeAutoDetailing",
                "fbp": "fb.1.xxxxxxxxxx.xxxxxxxxxx",
                "fingerprint": "fp_4d19c7",
                "fingerprint_confidence": 6.9,
                "ga": "GA1.1.xxxxxxxxxx.xxxxxxxxxx",
                "gbraid": "0AAAAA-shinetime",
                "gclid": "Cj0KCQiAshinetime",
                "ig_sid": "ig_shinetime_1",
                "ip_address": "1.2.3.4",
                "language": "en-US",
                "li_fat_id": "lifat-shinetime",
                "msclkid": "a1b2c3d4shine",
                "rdt_cid": "t2_shinetime",
                "sccid": "sccid-shinetime",
                "screen_resolution": "390x844",
                "timezone": "America/Chicago",
                "ttclid": "E.C.P.ttclid.shine",
                "ttp": "2ShineTimeTtp",
                "twclid": "twclid-shinetime",
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15",
                "utm_campaign": "ceramic-coating-spring",
                "utm_content": "carousel-a",
                "utm_id": "utm_88213",
                "utm_medium": "cpc",
                "utm_source": "google",
                "utm_term": "ceramic coating austin",
                "wbraid": "Cj0KCQjw-wbraid-shine",
            },
            currency="usd",
            custom_name="coating_deposit_paid",
            duration=42,
            event_id="evnt_xxxxxxxxxxxxx",
            event_time=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan_id="plan_xxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            referrer_url="https://www.google.com/",
            resumed=False,
            source="website",
            title="Ceramic coating quote request",
            url="https://shinetime.example/quote",
            user={
                "anonymous_id": "anon_8f2c41",
                "birthdate": "1990-01-15",
                "city": "Austin",
                "country": "US",
                "email": "marcus@shinetime.example",
                "external_id": "crm_8842",
                "first_name": "Dana",
                "gender": "female",
                "last_name": "Whitfield",
                "linked_anonymous_id": "anon_1b9de0",
                "linked_wuid": "user_xxxxxxxxxxxxxx",
                "member_id": "mber_xxxxxxxxxxxxx",
                "membership_id": "mem_xxxxxxxxxxxxxx",
                "name": "Dana Whitfield",
                "phone": "+xxxxxxxxxxx",
                "postal_code": "78756",
                "state": "TX",
                "user_id": "user_xxxxxxxxxxxxx",
                "username": "danawhitfield",
            },
            value=6.9,
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.events.with_raw_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.events.with_streaming_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
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
            account_id="biz_xxxxxxxxxxxxxx",
            url="https://shinetime.example/checkout/complete",
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
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        event = await async_client.events.create(
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
            action_source="website",
            context={
                "ad_campaign_id": "23851234567890123",
                "ad_id": "23851234567890125",
                "ad_set_id": "23851234567890124",
                "fbc": "fb.1.xxxxxxxxxx.IwAR0shine",
                "fbclid": "IwAR0shineTimeAutoDetailing",
                "fbp": "fb.1.xxxxxxxxxx.xxxxxxxxxx",
                "fingerprint": "fp_4d19c7",
                "fingerprint_confidence": 6.9,
                "ga": "GA1.1.xxxxxxxxxx.xxxxxxxxxx",
                "gbraid": "0AAAAA-shinetime",
                "gclid": "Cj0KCQiAshinetime",
                "ig_sid": "ig_shinetime_1",
                "ip_address": "1.2.3.4",
                "language": "en-US",
                "li_fat_id": "lifat-shinetime",
                "msclkid": "a1b2c3d4shine",
                "rdt_cid": "t2_shinetime",
                "sccid": "sccid-shinetime",
                "screen_resolution": "390x844",
                "timezone": "America/Chicago",
                "ttclid": "E.C.P.ttclid.shine",
                "ttp": "2ShineTimeTtp",
                "twclid": "twclid-shinetime",
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15",
                "utm_campaign": "ceramic-coating-spring",
                "utm_content": "carousel-a",
                "utm_id": "utm_88213",
                "utm_medium": "cpc",
                "utm_source": "google",
                "utm_term": "ceramic coating austin",
                "wbraid": "Cj0KCQjw-wbraid-shine",
            },
            currency="usd",
            custom_name="coating_deposit_paid",
            duration=42,
            event_id="evnt_xxxxxxxxxxxxx",
            event_time=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan_id="plan_xxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            referrer_url="https://www.google.com/",
            resumed=False,
            source="website",
            title="Ceramic coating quote request",
            url="https://shinetime.example/quote",
            user={
                "anonymous_id": "anon_8f2c41",
                "birthdate": "1990-01-15",
                "city": "Austin",
                "country": "US",
                "email": "marcus@shinetime.example",
                "external_id": "crm_8842",
                "first_name": "Dana",
                "gender": "female",
                "last_name": "Whitfield",
                "linked_anonymous_id": "anon_1b9de0",
                "linked_wuid": "user_xxxxxxxxxxxxxx",
                "member_id": "mber_xxxxxxxxxxxxx",
                "membership_id": "mem_xxxxxxxxxxxxxx",
                "name": "Dana Whitfield",
                "phone": "+xxxxxxxxxxx",
                "postal_code": "78756",
                "state": "TX",
                "user_id": "user_xxxxxxxxxxxxx",
                "username": "danawhitfield",
            },
            value=6.9,
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.events.with_raw_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.events.with_streaming_response.create(
            account_id="biz_xxxxxxxxxxxxxx",
            event_name="coating_deposit_paid",
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
            account_id="biz_xxxxxxxxxxxxxx",
            url="https://shinetime.example/checkout/complete",
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
