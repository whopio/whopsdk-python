# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Account,
    AccountRegisterLlcResponse,
    AccountRecommendActionsResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        account = client.accounts.create()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        account = client.accounts.create(
            country="country",
            email="email",
            metadata={"foo": "bar"},
            title="title",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        account = client.accounts.retrieve(
            "account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        account = client.accounts.update(
            account_id="account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        account = client.accounts.update(
            account_id="account_id",
            affiliate_application_required=True,
            affiliate_instructions="affiliate_instructions",
            banner_image={"foo": "bar"},
            business_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            business_type="business_type",
            country="country",
            description="description",
            featured_affiliate_product_id="featured_affiliate_product_id",
            home_preferences=["string"],
            industry_group="industry_group",
            industry_type="industry_type",
            invoice_prefix="invoice_prefix",
            logo={"foo": "bar"},
            metadata={"foo": "bar"},
            onboarding_type="onboarding_type",
            opengraph_image={"foo": "bar"},
            opengraph_image_variant="opengraph_image_variant",
            other_business_description="other_business_description",
            other_industry_description="other_industry_description",
            product_tax_code_id="product_tax_code_id",
            require_2fa=True,
            route="route",
            send_customer_emails=True,
            show_joined_whops=True,
            show_reviews_dtc=True,
            show_user_directory=True,
            social_links=[{"foo": "bar"}],
            store_page_config={"foo": "bar"},
            target_audience="target_audience",
            tax_collection_enabled_states=["AL"],
            tax_identifiers=[
                {
                    "tax_id_type": "ad_nrt",
                    "tax_id_value": "tax_id_value",
                }
            ],
            tax_remitted_by="whop",
            title="title",
            use_logo_as_opengraph_image_fallback=True,
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.update(
                account_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        account = client.accounts.list()
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        account = client.accounts.list(
            after="after",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
        )
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(SyncCursorPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_me(self, client: Whop) -> None:
        account = client.accounts.me()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_me(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_me(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_recommend_actions(self, client: Whop) -> None:
        account = client.accounts.recommend_actions(
            "account_id",
        )
        assert_matches_type(AccountRecommendActionsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_recommend_actions(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.recommend_actions(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRecommendActionsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_recommend_actions(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.recommend_actions(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRecommendActionsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_recommend_actions(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.recommend_actions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register_llc(self, client: Whop) -> None:
        account = client.accounts.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                }
            ],
        )
        assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register_llc_with_all_params(self, client: Whop) -> None:
        account = client.accounts.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "postal_code": "postal_code",
                    "state": "state",
                    "line2": "line2",
                },
                "entity_suffix": "LLC",
                "expedite_ein": True,
                "phone": "phone",
                "use_registered_agent": True,
                "website": "website",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                        "line2": "line2",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                    "date_of_birth": "date_of_birth",
                    "ssn": "ssn",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_register_llc(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_register_llc(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_register_llc(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.register_llc(
                account_id="",
                business_info={
                    "business_type": "business_type",
                    "formation_state": "AL",
                    "industry_group": "industry_group",
                    "industry_type": "industry_type",
                    "legal_name": "legal_name",
                },
                founders=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "line1": "line1",
                            "postal_code": "postal_code",
                            "state": "state",
                        },
                        "email": "email",
                        "first_name": "first_name",
                        "is_primary": True,
                        "last_name": "last_name",
                        "ownership_percentage": 0,
                        "phone": "phone",
                    }
                ],
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.create()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.create(
            country="country",
            email="email",
            metadata={"foo": "bar"},
            title="title",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.retrieve(
            "account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.update(
            account_id="account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.update(
            account_id="account_id",
            affiliate_application_required=True,
            affiliate_instructions="affiliate_instructions",
            banner_image={"foo": "bar"},
            business_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            business_type="business_type",
            country="country",
            description="description",
            featured_affiliate_product_id="featured_affiliate_product_id",
            home_preferences=["string"],
            industry_group="industry_group",
            industry_type="industry_type",
            invoice_prefix="invoice_prefix",
            logo={"foo": "bar"},
            metadata={"foo": "bar"},
            onboarding_type="onboarding_type",
            opengraph_image={"foo": "bar"},
            opengraph_image_variant="opengraph_image_variant",
            other_business_description="other_business_description",
            other_industry_description="other_industry_description",
            product_tax_code_id="product_tax_code_id",
            require_2fa=True,
            route="route",
            send_customer_emails=True,
            show_joined_whops=True,
            show_reviews_dtc=True,
            show_user_directory=True,
            social_links=[{"foo": "bar"}],
            store_page_config={"foo": "bar"},
            target_audience="target_audience",
            tax_collection_enabled_states=["AL"],
            tax_identifiers=[
                {
                    "tax_id_type": "ad_nrt",
                    "tax_id_value": "tax_id_value",
                }
            ],
            tax_remitted_by="whop",
            title="title",
            use_logo_as_opengraph_image_fallback=True,
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.update(
                account_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.list(
            after="after",
            before="before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
        )
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_me(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.me()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_me(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_recommend_actions(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.recommend_actions(
            "account_id",
        )
        assert_matches_type(AccountRecommendActionsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_recommend_actions(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.recommend_actions(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRecommendActionsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_recommend_actions(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.recommend_actions(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRecommendActionsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_recommend_actions(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.recommend_actions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register_llc(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                }
            ],
        )
        assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register_llc_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "postal_code": "postal_code",
                    "state": "state",
                    "line2": "line2",
                },
                "entity_suffix": "LLC",
                "expedite_ein": True,
                "phone": "phone",
                "use_registered_agent": True,
                "website": "website",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                        "line2": "line2",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                    "date_of_birth": "date_of_birth",
                    "ssn": "ssn",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_register_llc(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_register_llc(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.register_llc(
            account_id="account_id",
            business_info={
                "business_type": "business_type",
                "formation_state": "AL",
                "industry_group": "industry_group",
                "industry_type": "industry_type",
                "legal_name": "legal_name",
            },
            founders=[
                {
                    "address": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "postal_code": "postal_code",
                        "state": "state",
                    },
                    "email": "email",
                    "first_name": "first_name",
                    "is_primary": True,
                    "last_name": "last_name",
                    "ownership_percentage": 0,
                    "phone": "phone",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRegisterLlcResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_register_llc(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.register_llc(
                account_id="",
                business_info={
                    "business_type": "business_type",
                    "formation_state": "AL",
                    "industry_group": "industry_group",
                    "industry_type": "industry_type",
                    "legal_name": "legal_name",
                },
                founders=[
                    {
                        "address": {
                            "city": "city",
                            "country": "country",
                            "line1": "line1",
                            "postal_code": "postal_code",
                            "state": "state",
                        },
                        "email": "email",
                        "first_name": "first_name",
                        "is_primary": True,
                        "last_name": "last_name",
                        "ownership_percentage": 0,
                        "phone": "phone",
                    }
                ],
            )
