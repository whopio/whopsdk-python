# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import MediaAsset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        media = client.media.retrieve(
            "id",
        )
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.media.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.media.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaAsset, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.media.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: Whop) -> None:
        media = client.media.generate(
            prompt="prompt",
            type="video",
        )
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: Whop) -> None:
        media = client.media.generate(
            prompt="prompt",
            type="video",
            account_id="account_id",
            duration_seconds=5,
            reference_media=["string"],
            resolution="480p",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: Whop) -> None:
        response = client.media.with_raw_response.generate(
            prompt="prompt",
            type="video",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: Whop) -> None:
        with client.media.with_streaming_response.generate(
            prompt="prompt",
            type="video",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaAsset, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        media = await async_client.media.retrieve(
            "id",
        )
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.media.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.media.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaAsset, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.media.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncWhop) -> None:
        media = await async_client.media.generate(
            prompt="prompt",
            type="video",
        )
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncWhop) -> None:
        media = await async_client.media.generate(
            prompt="prompt",
            type="video",
            account_id="account_id",
            duration_seconds=5,
            reference_media=["string"],
            resolution="480p",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncWhop) -> None:
        response = await async_client.media.with_raw_response.generate(
            prompt="prompt",
            type="video",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaAsset, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncWhop) -> None:
        async with async_client.media.with_streaming_response.generate(
            prompt="prompt",
            type="video",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaAsset, media, path=["response"])

        assert cast(Any, response.is_closed) is True
