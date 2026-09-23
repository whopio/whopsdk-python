# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import SetupIntent
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSetupIntents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        setup_intent = client.setup_intents.retrieve(
            id="id",
        )
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        setup_intent = client.setup_intents.retrieve(
            id="id",
            api_version_date="2026-09-22-3",
        )
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SetupIntent, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.setup_intents.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        setup_intent = client.setup_intents.list()
        assert_matches_type(SyncCursorPage[SetupIntent], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        setup_intent = client.setup_intents.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            status="processing",
            api_version_date="2026-09-22-3",
        )
        assert_matches_type(SyncCursorPage[SetupIntent], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SyncCursorPage[SetupIntent], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SyncCursorPage[SetupIntent], setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSetupIntents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.retrieve(
            id="id",
        )
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.retrieve(
            id="id",
            api_version_date="2026-09-22-3",
        )
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(SetupIntent, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.setup_intents.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.list()
        assert_matches_type(AsyncCursorPage[SetupIntent], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            status="processing",
            api_version_date="2026-09-22-3",
        )
        assert_matches_type(AsyncCursorPage[SetupIntent], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(AsyncCursorPage[SetupIntent], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(AsyncCursorPage[SetupIntent], setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True
