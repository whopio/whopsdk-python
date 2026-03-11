# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    ResolutionCenterCaseListResponse,
    ResolutionCenterCaseRetrieveResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResolutionCenterCases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.retrieve(
            "reso_xxxxxxxxxxxxx",
        )
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.retrieve(
            "reso_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.retrieve(
            "reso_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.list()
        assert_matches_type(SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            statuses=["merchant_response_needed"],
        )
        assert_matches_type(SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(
                SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncResolutionCenterCases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.retrieve(
            "reso_xxxxxxxxxxxxx",
        )
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.retrieve(
            "reso_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.retrieve(
            "reso_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.list()
        assert_matches_type(
            AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.list(
            after="after",
            before="before",
            company_id="biz_xxxxxxxxxxxxxx",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            statuses=["merchant_response_needed"],
        )
        assert_matches_type(
            AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(
            AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(
                AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
