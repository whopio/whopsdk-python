# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import PersonListResponse, PersonRetrieveResponse
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeople:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        person = client.people.retrieve(
            id="id",
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        person = client.people.retrieve(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.people.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.people.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonRetrieveResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.people.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        person = client.people.list()
        assert_matches_type(SyncCursorPage[PersonListResponse], person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        person = client.people.list(
            account_id="account_id",
            after="after",
            attribution_model="last_touch",
            audience_id="audience_id",
            before="before",
            contactable=True,
            country="country",
            custom_event="custom_event",
            direction="asc",
            email="email",
            event_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_name=["payment.completed"],
            event_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            first=0,
            first_seen_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_seen_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_seen_within_days=0,
            has_purchased=True,
            last_seen_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_seen_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_seen_within_days=0,
            order="first_seen_at",
            phone="phone",
            query="query",
            source=["direct"],
            user_id="user_id",
        )
        assert_matches_type(SyncCursorPage[PersonListResponse], person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.people.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(SyncCursorPage[PersonListResponse], person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.people.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(SyncCursorPage[PersonListResponse], person, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPeople:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        person = await async_client.people.retrieve(
            id="id",
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        person = await async_client.people.retrieve(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.people.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.people.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonRetrieveResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.people.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        person = await async_client.people.list()
        assert_matches_type(AsyncCursorPage[PersonListResponse], person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        person = await async_client.people.list(
            account_id="account_id",
            after="after",
            attribution_model="last_touch",
            audience_id="audience_id",
            before="before",
            contactable=True,
            country="country",
            custom_event="custom_event",
            direction="asc",
            email="email",
            event_from=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_name=["payment.completed"],
            event_to=parse_datetime("2019-12-27T18:11:19.117Z"),
            first=0,
            first_seen_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_seen_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_seen_within_days=0,
            has_purchased=True,
            last_seen_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_seen_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_seen_within_days=0,
            order="first_seen_at",
            phone="phone",
            query="query",
            source=["direct"],
            user_id="user_id",
        )
        assert_matches_type(AsyncCursorPage[PersonListResponse], person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.people.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(AsyncCursorPage[PersonListResponse], person, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.people.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(AsyncCursorPage[PersonListResponse], person, path=["response"])

        assert cast(Any, response.is_closed) is True
