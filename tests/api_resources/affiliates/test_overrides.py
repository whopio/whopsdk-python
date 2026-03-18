# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.affiliates import (
    OverrideListResponse,
    OverrideCreateResponse,
    OverrideDeleteResponse,
    OverrideUpdateResponse,
    OverrideRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverrides:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Whop) -> None:
        override = client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Whop) -> None:
        override = client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
            applies_to_payments="first_payment",
            commission_type="percentage",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Whop) -> None:
        response = client.affiliates.overrides.with_raw_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Whop) -> None:
        with client.affiliates.overrides.with_streaming_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(OverrideCreateResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.affiliates.overrides.with_raw_response.create(
                path_id="",
                body_id="id",
                commission_value=6.9,
                override_type="standard",
                plan_id="plan_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Whop) -> None:
        override = client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Whop) -> None:
        override = client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
            commission_type="percentage",
            product_id="prod_xxxxxxxxxxxxx",
            revenue_basis="pre_fees",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Whop) -> None:
        response = client.affiliates.overrides.with_raw_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Whop) -> None:
        with client.affiliates.overrides.with_streaming_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(OverrideCreateResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.affiliates.overrides.with_raw_response.create(
                path_id="",
                body_id="id",
                commission_value=6.9,
                override_type="rev_share",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        override = client.affiliates.overrides.retrieve(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideRetrieveResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.affiliates.overrides.with_raw_response.retrieve(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(OverrideRetrieveResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.affiliates.overrides.with_streaming_response.retrieve(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(OverrideRetrieveResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.overrides.with_raw_response.retrieve(
                override_id="override_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `override_id` but received ''"):
            client.affiliates.overrides.with_raw_response.retrieve(
                override_id="",
                id="aff_xxxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        override = client.affiliates.overrides.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideUpdateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        override = client.affiliates.overrides.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
            applies_to_payments="first_payment",
            commission_type="percentage",
            commission_value=6.9,
            revenue_basis="pre_fees",
        )
        assert_matches_type(OverrideUpdateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.affiliates.overrides.with_raw_response.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(OverrideUpdateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.affiliates.overrides.with_streaming_response.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(OverrideUpdateResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.overrides.with_raw_response.update(
                override_id="override_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `override_id` but received ''"):
            client.affiliates.overrides.with_raw_response.update(
                override_id="",
                id="aff_xxxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        override = client.affiliates.overrides.list(
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[OverrideListResponse], override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        override = client.affiliates.overrides.list(
            id="aff_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
            override_type="standard",
        )
        assert_matches_type(SyncCursorPage[OverrideListResponse], override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.affiliates.overrides.with_raw_response.list(
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(SyncCursorPage[OverrideListResponse], override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.affiliates.overrides.with_streaming_response.list(
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(SyncCursorPage[OverrideListResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.overrides.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        override = client.affiliates.overrides.delete(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideDeleteResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.affiliates.overrides.with_raw_response.delete(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(OverrideDeleteResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.affiliates.overrides.with_streaming_response.delete(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(OverrideDeleteResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.affiliates.overrides.with_raw_response.delete(
                override_id="override_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `override_id` but received ''"):
            client.affiliates.overrides.with_raw_response.delete(
                override_id="",
                id="aff_xxxxxxxxxxxxxx",
            )


class TestAsyncOverrides:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
            applies_to_payments="first_payment",
            commission_type="percentage",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.overrides.with_raw_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.overrides.with_streaming_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="standard",
            plan_id="plan_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(OverrideCreateResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.create(
                path_id="",
                body_id="id",
                commission_value=6.9,
                override_type="standard",
                plan_id="plan_xxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
            commission_type="percentage",
            product_id="prod_xxxxxxxxxxxxx",
            revenue_basis="pre_fees",
        )
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.overrides.with_raw_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(OverrideCreateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.overrides.with_streaming_response.create(
            path_id="aff_xxxxxxxxxxxxxx",
            body_id="id",
            commission_value=6.9,
            override_type="rev_share",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(OverrideCreateResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.create(
                path_id="",
                body_id="id",
                commission_value=6.9,
                override_type="rev_share",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.retrieve(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideRetrieveResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.overrides.with_raw_response.retrieve(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(OverrideRetrieveResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.overrides.with_streaming_response.retrieve(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(OverrideRetrieveResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.retrieve(
                override_id="override_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `override_id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.retrieve(
                override_id="",
                id="aff_xxxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideUpdateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
            applies_to_payments="first_payment",
            commission_type="percentage",
            commission_value=6.9,
            revenue_basis="pre_fees",
        )
        assert_matches_type(OverrideUpdateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.overrides.with_raw_response.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(OverrideUpdateResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.overrides.with_streaming_response.update(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(OverrideUpdateResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.update(
                override_id="override_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `override_id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.update(
                override_id="",
                id="aff_xxxxxxxxxxxxxx",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.list(
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[OverrideListResponse], override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.list(
            id="aff_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            first=42,
            last=42,
            override_type="standard",
        )
        assert_matches_type(AsyncCursorPage[OverrideListResponse], override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.overrides.with_raw_response.list(
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(AsyncCursorPage[OverrideListResponse], override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.overrides.with_streaming_response.list(
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(AsyncCursorPage[OverrideListResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        override = await async_client.affiliates.overrides.delete(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )
        assert_matches_type(OverrideDeleteResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.affiliates.overrides.with_raw_response.delete(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(OverrideDeleteResponse, override, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.affiliates.overrides.with_streaming_response.delete(
            override_id="override_id",
            id="aff_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(OverrideDeleteResponse, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.delete(
                override_id="override_id",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `override_id` but received ''"):
            await async_client.affiliates.overrides.with_raw_response.delete(
                override_id="",
                id="aff_xxxxxxxxxxxxxx",
            )
