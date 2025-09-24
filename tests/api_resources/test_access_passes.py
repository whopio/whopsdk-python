# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whopsdk import Whopsdk, AsyncWhopsdk
from tests.utils import assert_matches_type
from whopsdk.types import AccessPassListResponse, AccessPassRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessPasses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whopsdk) -> None:
        access_pass = client.access_passes.retrieve(
            "prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(AccessPassRetrieveResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whopsdk) -> None:
        response = client.access_passes.with_raw_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_pass = response.parse()
        assert_matches_type(AccessPassRetrieveResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whopsdk) -> None:
        with client.access_passes.with_streaming_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_pass = response.parse()
            assert_matches_type(AccessPassRetrieveResponse, access_pass, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.access_passes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whopsdk) -> None:
        access_pass = client.access_passes.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whopsdk) -> None:
        access_pass = client.access_passes.list(
            company_id="biz_xxxxxxxxxxxxxx",
            access_pass_type="regular",
            after="after",
            before="before",
            first=0,
            last=0,
        )
        assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whopsdk) -> None:
        response = client.access_passes.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_pass = response.parse()
        assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whopsdk) -> None:
        with client.access_passes.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_pass = response.parse()
            assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccessPasses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhopsdk) -> None:
        access_pass = await async_client.access_passes.retrieve(
            "prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(AccessPassRetrieveResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.access_passes.with_raw_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_pass = await response.parse()
        assert_matches_type(AccessPassRetrieveResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.access_passes.with_streaming_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_pass = await response.parse()
            assert_matches_type(AccessPassRetrieveResponse, access_pass, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhopsdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.access_passes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhopsdk) -> None:
        access_pass = await async_client.access_passes.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhopsdk) -> None:
        access_pass = await async_client.access_passes.list(
            company_id="biz_xxxxxxxxxxxxxx",
            access_pass_type="regular",
            after="after",
            before="before",
            first=0,
            last=0,
        )
        assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhopsdk) -> None:
        response = await async_client.access_passes.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_pass = await response.parse()
        assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhopsdk) -> None:
        async with async_client.access_passes.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_pass = await response.parse()
            assert_matches_type(AccessPassListResponse, access_pass, path=["response"])

        assert cast(Any, response.is_closed) is True
