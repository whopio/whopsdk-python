# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    SetupIntent,
    SetupIntentListResponse,
    SetupIntentCreateResponse,
    SetupIntentRetrieveStatusResponse,
    SetupIntentUpdateReturnURLResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSetupIntents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Whop) -> None:
        setup_intent = client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Whop) -> None:
        setup_intent = client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
            currency="usd",
            email="buyer@example.com",
            metadata={"foo": "bar"},
            return_url="https://example.com/path",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Whop) -> None:
        setup_intent = client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Whop) -> None:
        setup_intent = client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            currency="usd",
            email="buyer@example.com",
            metadata={"foo": "bar"},
            return_url="https://example.com/path",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        setup_intent = client.setup_intents.retrieve(
            "sint_xxxxxxxxxxxxx",
        )
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.retrieve(
            "sint_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.retrieve(
            "sint_xxxxxxxxxxxxx",
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
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        setup_intent = client.setup_intents.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        setup_intent = client.setup_intents.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Whop) -> None:
        setup_intent = client.setup_intents.retrieve_status(
            "setup_intent_id",
        )
        assert_matches_type(SetupIntentRetrieveStatusResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.retrieve_status(
            "setup_intent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SetupIntentRetrieveStatusResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.retrieve_status(
            "setup_intent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SetupIntentRetrieveStatusResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setup_intent_id` but received ''"):
            client.setup_intents.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_return_url(self, client: Whop) -> None:
        setup_intent = client.setup_intents.update_return_url(
            setup_intent_id="setup_intent_id",
            return_url="https://merchant.example/thanks",
        )
        assert_matches_type(SetupIntentUpdateReturnURLResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_return_url(self, client: Whop) -> None:
        response = client.setup_intents.with_raw_response.update_return_url(
            setup_intent_id="setup_intent_id",
            return_url="https://merchant.example/thanks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = response.parse()
        assert_matches_type(SetupIntentUpdateReturnURLResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_return_url(self, client: Whop) -> None:
        with client.setup_intents.with_streaming_response.update_return_url(
            setup_intent_id="setup_intent_id",
            return_url="https://merchant.example/thanks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = response.parse()
            assert_matches_type(SetupIntentUpdateReturnURLResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_return_url(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setup_intent_id` but received ''"):
            client.setup_intents.with_raw_response.update_return_url(
                setup_intent_id="",
                return_url="https://merchant.example/thanks",
            )


class TestAsyncSetupIntents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
            currency="usd",
            email="buyer@example.com",
            metadata={"foo": "bar"},
            return_url="https://example.com/path",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            confirmation_token="ctok_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
            currency="usd",
            email="buyer@example.com",
            metadata={"foo": "bar"},
            return_url="https://example.com/path",
        )
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            payment_method_id="pmt_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(SetupIntentCreateResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.retrieve(
            "sint_xxxxxxxxxxxxx",
        )
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.retrieve(
            "sint_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(SetupIntent, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.retrieve(
            "sint_xxxxxxxxxxxxx",
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
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(AsyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(AsyncCursorPage[SetupIntentListResponse], setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.retrieve_status(
            "setup_intent_id",
        )
        assert_matches_type(SetupIntentRetrieveStatusResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.retrieve_status(
            "setup_intent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(SetupIntentRetrieveStatusResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.retrieve_status(
            "setup_intent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(SetupIntentRetrieveStatusResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setup_intent_id` but received ''"):
            await async_client.setup_intents.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_return_url(self, async_client: AsyncWhop) -> None:
        setup_intent = await async_client.setup_intents.update_return_url(
            setup_intent_id="setup_intent_id",
            return_url="https://merchant.example/thanks",
        )
        assert_matches_type(SetupIntentUpdateReturnURLResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_return_url(self, async_client: AsyncWhop) -> None:
        response = await async_client.setup_intents.with_raw_response.update_return_url(
            setup_intent_id="setup_intent_id",
            return_url="https://merchant.example/thanks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup_intent = await response.parse()
        assert_matches_type(SetupIntentUpdateReturnURLResponse, setup_intent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_return_url(self, async_client: AsyncWhop) -> None:
        async with async_client.setup_intents.with_streaming_response.update_return_url(
            setup_intent_id="setup_intent_id",
            return_url="https://merchant.example/thanks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup_intent = await response.parse()
            assert_matches_type(SetupIntentUpdateReturnURLResponse, setup_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_return_url(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setup_intent_id` but received ''"):
            await async_client.setup_intents.with_raw_response.update_return_url(
                setup_intent_id="",
                return_url="https://merchant.example/thanks",
            )
