# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Account,
    AccountFormCompanyResponse,
    AccountTransferOwnershipResponse,
)
from whop_sdk._utils import parse_datetime
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
            banner_image={"id": "id"},
            business_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            business_type="education_program",
            collect_vat_id=True,
            country="country",
            description="description",
            featured_affiliate_product_id="featured_affiliate_product_id",
            home_preferences=["hide_member_count"],
            industry_group="academic_and_test_prep",
            industry_type="trading",
            invoice_prefix="invoice_prefix",
            logo={"id": "id"},
            metadata={"foo": "bar"},
            onboarding_type="platform",
            opengraph_image={"id": "id"},
            opengraph_image_variant="white",
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
            store_page_config={
                "accent_color": "ruby",
                "layout": "featured",
                "profile_variant": "personal",
                "whop_affiliate_link": True,
            },
            target_audience="target_audience",
            tax_collection_enabled_states=["AL"],
            tax_identifiers=[
                {
                    "tax_id_type": "ad_nrt",
                    "tax_id_value": "tax_id_value",
                }
            ],
            tax_remitted_by="whop",
            tax_type="inclusive",
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
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            parent_account_id="parent_account_id",
            query="query",
            status="active",
            volume_max=0,
            volume_min=0,
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
    def test_method_form_company(self, client: Whop) -> None:
        account = client.accounts.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
        )
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_form_company_with_all_params(self, client: Whop) -> None:
        account = client.accounts.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                        "line2": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                    "date_of_birth": "<string>",
                    "ownership_percentage": 123,
                    "roles": ["president"],
                    "ssn": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
            business_address={
                "city": "<string>",
                "country": "<string>",
                "line1": "<string>",
                "postal_code": "<string>",
                "state": "<string>",
                "line2": "<string>",
            },
            business_phone="<string>",
            business_website="<string>",
            entity_suffix="LLC",
            entity_type="llc",
            expedite_ein=True,
            share_structure={
                "number_of_shares": 123,
                "value": 123,
            },
            use_registered_agent=True,
        )
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_form_company(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_form_company(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_form_company(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.form_company(
                account_id="",
                business_name="<string>",
                business_type="<string>",
                formation_state="AL",
                founders=[
                    {
                        "address": {
                            "city": "<string>",
                            "country": "<string>",
                            "line1": "<string>",
                            "postal_code": "<string>",
                            "state": "<string>",
                        },
                        "email": "<string>",
                        "first_name": "<string>",
                        "is_primary": True,
                        "last_name": "<string>",
                        "phone": "<string>",
                    }
                ],
                industry_group="<string>",
                industry_type="<string>",
            )

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
    def test_method_transfer_ownership(self, client: Whop) -> None:
        account = client.accounts.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transfer_ownership_with_all_params(self, client: Whop) -> None:
        account = client.accounts.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
            as_partner=True,
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transfer_ownership(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transfer_ownership(self, client: Whop) -> None:
        with client.accounts.with_streaming_response.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_transfer_ownership(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.transfer_ownership(
                account_id="",
                identifier="identifier",
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
            banner_image={"id": "id"},
            business_address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            business_type="education_program",
            collect_vat_id=True,
            country="country",
            description="description",
            featured_affiliate_product_id="featured_affiliate_product_id",
            home_preferences=["hide_member_count"],
            industry_group="academic_and_test_prep",
            industry_type="trading",
            invoice_prefix="invoice_prefix",
            logo={"id": "id"},
            metadata={"foo": "bar"},
            onboarding_type="platform",
            opengraph_image={"id": "id"},
            opengraph_image_variant="white",
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
            store_page_config={
                "accent_color": "ruby",
                "layout": "featured",
                "profile_variant": "personal",
                "whop_affiliate_link": True,
            },
            target_audience="target_audience",
            tax_collection_enabled_states=["AL"],
            tax_identifiers=[
                {
                    "tax_id_type": "ad_nrt",
                    "tax_id_value": "tax_id_value",
                }
            ],
            tax_remitted_by="whop",
            tax_type="inclusive",
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
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            parent_account_id="parent_account_id",
            query="query",
            status="active",
            volume_max=0,
            volume_min=0,
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
    async def test_method_form_company(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
        )
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_form_company_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                        "line2": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                    "date_of_birth": "<string>",
                    "ownership_percentage": 123,
                    "roles": ["president"],
                    "ssn": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
            business_address={
                "city": "<string>",
                "country": "<string>",
                "line1": "<string>",
                "postal_code": "<string>",
                "state": "<string>",
                "line2": "<string>",
            },
            business_phone="<string>",
            business_website="<string>",
            entity_suffix="LLC",
            entity_type="llc",
            expedite_ein=True,
            share_structure={
                "number_of_shares": 123,
                "value": 123,
            },
            use_registered_agent=True,
        )
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_form_company(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_form_company(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.form_company(
            account_id="account_id",
            business_name="<string>",
            business_type="<string>",
            formation_state="AL",
            founders=[
                {
                    "address": {
                        "city": "<string>",
                        "country": "<string>",
                        "line1": "<string>",
                        "postal_code": "<string>",
                        "state": "<string>",
                    },
                    "email": "<string>",
                    "first_name": "<string>",
                    "is_primary": True,
                    "last_name": "<string>",
                    "phone": "<string>",
                }
            ],
            industry_group="<string>",
            industry_type="<string>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_form_company(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.form_company(
                account_id="",
                business_name="<string>",
                business_type="<string>",
                formation_state="AL",
                founders=[
                    {
                        "address": {
                            "city": "<string>",
                            "country": "<string>",
                            "line1": "<string>",
                            "postal_code": "<string>",
                            "state": "<string>",
                        },
                        "email": "<string>",
                        "first_name": "<string>",
                        "is_primary": True,
                        "last_name": "<string>",
                        "phone": "<string>",
                    }
                ],
                industry_group="<string>",
                industry_type="<string>",
            )

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
    async def test_method_transfer_ownership(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transfer_ownership_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
            as_partner=True,
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transfer_ownership(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transfer_ownership(self, async_client: AsyncWhop) -> None:
        async with async_client.accounts.with_streaming_response.transfer_ownership(
            account_id="account_id",
            identifier="identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_transfer_ownership(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.transfer_ownership(
                account_id="",
                identifier="identifier",
            )
