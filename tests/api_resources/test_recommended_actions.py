# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    RecommendedActionRunResponse,
    RecommendedActionListResponse,
    RecommendedActionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecommendedActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        recommended_action = client.recommended_actions.retrieve(
            chain_id="chain_id",
        )
        assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        recommended_action = client.recommended_actions.retrieve(
            chain_id="chain_id",
            account_id="account_id",
        )
        assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.recommended_actions.with_raw_response.retrieve(
            chain_id="chain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommended_action = response.parse()
        assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.recommended_actions.with_streaming_response.retrieve(
            chain_id="chain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommended_action = response.parse()
            assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chain_id` but received ''"):
            client.recommended_actions.with_raw_response.retrieve(
                chain_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        recommended_action = client.recommended_actions.list()
        assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        recommended_action = client.recommended_actions.list(
            account_id="account_id",
        )
        assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.recommended_actions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommended_action = response.parse()
        assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.recommended_actions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommended_action = response.parse()
            assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Whop) -> None:
        recommended_action = client.recommended_actions.run(
            chain_id="chain_id",
        )
        assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Whop) -> None:
        recommended_action = client.recommended_actions.run(
            chain_id="chain_id",
            account_id="account_id",
        )
        assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Whop) -> None:
        response = client.recommended_actions.with_raw_response.run(
            chain_id="chain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommended_action = response.parse()
        assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Whop) -> None:
        with client.recommended_actions.with_streaming_response.run(
            chain_id="chain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommended_action = response.parse()
            assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chain_id` but received ''"):
            client.recommended_actions.with_raw_response.run(
                chain_id="",
            )


class TestAsyncRecommendedActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        recommended_action = await async_client.recommended_actions.retrieve(
            chain_id="chain_id",
        )
        assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        recommended_action = await async_client.recommended_actions.retrieve(
            chain_id="chain_id",
            account_id="account_id",
        )
        assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.recommended_actions.with_raw_response.retrieve(
            chain_id="chain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommended_action = await response.parse()
        assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.recommended_actions.with_streaming_response.retrieve(
            chain_id="chain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommended_action = await response.parse()
            assert_matches_type(RecommendedActionRetrieveResponse, recommended_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chain_id` but received ''"):
            await async_client.recommended_actions.with_raw_response.retrieve(
                chain_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        recommended_action = await async_client.recommended_actions.list()
        assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        recommended_action = await async_client.recommended_actions.list(
            account_id="account_id",
        )
        assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.recommended_actions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommended_action = await response.parse()
        assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.recommended_actions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommended_action = await response.parse()
            assert_matches_type(RecommendedActionListResponse, recommended_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncWhop) -> None:
        recommended_action = await async_client.recommended_actions.run(
            chain_id="chain_id",
        )
        assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncWhop) -> None:
        recommended_action = await async_client.recommended_actions.run(
            chain_id="chain_id",
            account_id="account_id",
        )
        assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncWhop) -> None:
        response = await async_client.recommended_actions.with_raw_response.run(
            chain_id="chain_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommended_action = await response.parse()
        assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncWhop) -> None:
        async with async_client.recommended_actions.with_streaming_response.run(
            chain_id="chain_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommended_action = await response.parse()
            assert_matches_type(RecommendedActionRunResponse, recommended_action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chain_id` but received ''"):
            await async_client.recommended_actions.with_raw_response.run(
                chain_id="",
            )
