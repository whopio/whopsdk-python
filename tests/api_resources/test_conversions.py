# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import ConversionCreateResponse
from whop_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        conversion = client.conversions.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
        )
        assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        conversion = client.conversions.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
            action_source="email",
            context={
                "ad_campaign_id": "ad_campaign_id",
                "ad_id": "ad_id",
                "ad_set_id": "ad_set_id",
                "fbclid": "fbclid",
                "fbp": "fbp",
                "ga": "ga",
                "gclid": "gclid",
                "ig_sid": "ig_sid",
                "ip_address": "ip_address",
                "ttclid": "ttclid",
                "ttp": "ttp",
                "user_agent": "user_agent",
                "utm_campaign": "utm_campaign",
                "utm_content": "utm_content",
                "utm_id": "utm_id",
                "utm_medium": "utm_medium",
                "utm_source": "utm_source",
                "utm_term": "utm_term",
            },
            currency="usd",
            custom_name="custom_name",
            event_id="evnt_xxxxxxxxxxxxx",
            event_time=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan_id="plan_xxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            referrer_url="referrer_url",
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
        )
        assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.conversions.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversion = response.parse()
        assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.conversions.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversion = response.parse()
            assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConversions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        conversion = await async_client.conversions.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
        )
        assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        conversion = await async_client.conversions.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
            action_source="email",
            context={
                "ad_campaign_id": "ad_campaign_id",
                "ad_id": "ad_id",
                "ad_set_id": "ad_set_id",
                "fbclid": "fbclid",
                "fbp": "fbp",
                "ga": "ga",
                "gclid": "gclid",
                "ig_sid": "ig_sid",
                "ip_address": "ip_address",
                "ttclid": "ttclid",
                "ttp": "ttp",
                "user_agent": "user_agent",
                "utm_campaign": "utm_campaign",
                "utm_content": "utm_content",
                "utm_id": "utm_id",
                "utm_medium": "utm_medium",
                "utm_source": "utm_source",
                "utm_term": "utm_term",
            },
            currency="usd",
            custom_name="custom_name",
            event_id="evnt_xxxxxxxxxxxxx",
            event_time=parse_datetime("2023-12-01T05:00:00.401Z"),
            plan_id="plan_xxxxxxxxxxxxx",
            product_id="prod_xxxxxxxxxxxxx",
            referrer_url="referrer_url",
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
        )
        assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.conversions.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversion = await response.parse()
        assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.conversions.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            event_name="lead",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversion = await response.parse()
            assert_matches_type(ConversionCreateResponse, conversion, path=["response"])

        assert cast(Any, response.is_closed) is True
