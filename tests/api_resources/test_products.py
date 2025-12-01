# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    ProductDeleteResponse,
)
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage
from whop_sdk.types.shared import Product, ProductListItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        product = client.products.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        product = client.products.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
            business_type="education_program",
            collect_shipping_address=True,
            custom_cta="get_access",
            custom_cta_url="custom_cta_url",
            custom_statement_descriptor="custom_statement_descriptor",
            description="description",
            experience_ids=["string"],
            global_affiliate_percentage=6.9,
            global_affiliate_status="enabled",
            headline="headline",
            industry_type="trading",
            member_affiliate_percentage=6.9,
            member_affiliate_status="enabled",
            plan_options={
                "base_currency": "usd",
                "billing_period": 42,
                "custom_fields": [
                    {
                        "field_type": "text",
                        "name": "name",
                        "id": "id",
                        "order": 42,
                        "placeholder": "placeholder",
                        "required": True,
                    }
                ],
                "initial_price": 6.9,
                "plan_type": "renewal",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "visibility": "visible",
            },
            product_highlights=[
                {
                    "content": "content",
                    "highlight_type": "qualification",
                    "title": "title",
                }
            ],
            product_tax_code_id="ptc_xxxxxxxxxxxxxx",
            redirect_purchase_url="redirect_purchase_url",
            route="route",
            visibility="visible",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.products.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.products.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        product = client.products.retrieve(
            "prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.products.with_raw_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.products.with_streaming_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        product = client.products.update(
            id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        product = client.products.update(
            id="prod_xxxxxxxxxxxxx",
            business_type="education_program",
            collect_shipping_address=True,
            custom_cta="get_access",
            custom_cta_url="custom_cta_url",
            custom_statement_descriptor="custom_statement_descriptor",
            description="description",
            global_affiliate_percentage=6.9,
            global_affiliate_status="enabled",
            headline="headline",
            industry_type="trading",
            member_affiliate_percentage=6.9,
            member_affiliate_status="enabled",
            product_tax_code_id="ptc_xxxxxxxxxxxxxx",
            redirect_purchase_url="redirect_purchase_url",
            route="route",
            store_page_config={
                "custom_cta": "custom_cta",
                "show_price": True,
            },
            title="title",
            visibility="visible",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.products.with_raw_response.update(
            id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.products.with_streaming_response.update(
            id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        product = client.products.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[ProductListItem], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        product = client.products.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            order="active_memberships_count",
            product_types=["regular"],
            visibilities=["visible"],
        )
        assert_matches_type(SyncCursorPage[ProductListItem], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.products.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncCursorPage[ProductListItem], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.products.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncCursorPage[ProductListItem], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        product = client.products.delete(
            "prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.products.with_raw_response.delete(
            "prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.products.with_streaming_response.delete(
            "prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductDeleteResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.delete(
                "",
            )


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
            business_type="education_program",
            collect_shipping_address=True,
            custom_cta="get_access",
            custom_cta_url="custom_cta_url",
            custom_statement_descriptor="custom_statement_descriptor",
            description="description",
            experience_ids=["string"],
            global_affiliate_percentage=6.9,
            global_affiliate_status="enabled",
            headline="headline",
            industry_type="trading",
            member_affiliate_percentage=6.9,
            member_affiliate_status="enabled",
            plan_options={
                "base_currency": "usd",
                "billing_period": 42,
                "custom_fields": [
                    {
                        "field_type": "text",
                        "name": "name",
                        "id": "id",
                        "order": 42,
                        "placeholder": "placeholder",
                        "required": True,
                    }
                ],
                "initial_price": 6.9,
                "plan_type": "renewal",
                "release_method": "buy_now",
                "renewal_price": 6.9,
                "visibility": "visible",
            },
            product_highlights=[
                {
                    "content": "content",
                    "highlight_type": "qualification",
                    "title": "title",
                }
            ],
            product_tax_code_id="ptc_xxxxxxxxxxxxxx",
            redirect_purchase_url="redirect_purchase_url",
            route="route",
            visibility="visible",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.products.with_raw_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.products.with_streaming_response.create(
            company_id="biz_xxxxxxxxxxxxxx",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.retrieve(
            "prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.products.with_raw_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.products.with_streaming_response.retrieve(
            "prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.update(
            id="prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.update(
            id="prod_xxxxxxxxxxxxx",
            business_type="education_program",
            collect_shipping_address=True,
            custom_cta="get_access",
            custom_cta_url="custom_cta_url",
            custom_statement_descriptor="custom_statement_descriptor",
            description="description",
            global_affiliate_percentage=6.9,
            global_affiliate_status="enabled",
            headline="headline",
            industry_type="trading",
            member_affiliate_percentage=6.9,
            member_affiliate_status="enabled",
            product_tax_code_id="ptc_xxxxxxxxxxxxxx",
            redirect_purchase_url="redirect_purchase_url",
            route="route",
            store_page_config={
                "custom_cta": "custom_cta",
                "show_price": True,
            },
            title="title",
            visibility="visible",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.products.with_raw_response.update(
            id="prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.products.with_streaming_response.update(
            id="prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[ProductListItem], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
            order="active_memberships_count",
            product_types=["regular"],
            visibilities=["visible"],
        )
        assert_matches_type(AsyncCursorPage[ProductListItem], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.products.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncCursorPage[ProductListItem], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.products.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncCursorPage[ProductListItem], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        product = await async_client.products.delete(
            "prod_xxxxxxxxxxxxx",
        )
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.products.with_raw_response.delete(
            "prod_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductDeleteResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.products.with_streaming_response.delete(
            "prod_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductDeleteResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.delete(
                "",
            )
