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
            country="US",
            email="marcus@shinetime.example",
            metadata={"external_id": "bar"},
            title="Shine Time Auto Detailing",
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
            affiliate_instructions="Send us your detailing content before promoting. No paid search on our brand terms.",
            banner_image={"id": "file_xxxxxxxxxxxxxx"},
            business_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="  Shine Time Auto Detailing, LLC  ",
            business_type="other",
            collect_vat_id=True,
            country="US",
            description="Mobile ceramic coating, paint correction, and interior detailing across the Austin metro.",
            featured_affiliate_product_id="prod_xxxxxxxxxxxxxx",
            home_preferences=["hide_member_count"],
            industry_group="automotive",
            industry_type="other",
            invoice_prefix="SHINE",
            logo={"id": "file_xxxxxxxxxxxxxx"},
            metadata={
                "external_id": "bar",
                "region": "bar",
            },
            onboarding_type="seller",
            opengraph_image={"id": "file_xxxxxxxxxxxxxx"},
            opengraph_image_variant="black",
            other_business_description="Mobile auto detailing",
            other_industry_description="Automotive services",
            product_tax_code_id="ptc_xxxxxxxxxxxxxx",
            require_2fa=True,
            route="shine-time-detailing",
            send_customer_emails=False,
            show_joined_whops=False,
            show_reviews_dtc=False,
            show_user_directory=False,
            social_links=[
                {
                    "url": "bar",
                    "website": "bar",
                }
            ],
            store_page_config={
                "accent_color": "red",
                "layout": "compact",
                "profile_variant": "business",
                "whop_affiliate_link": True,
            },
            target_audience="Owners of new and enthusiast vehicles in Austin, TX",
            tax_collection_enabled_states=["TX"],
            tax_identifiers=[
                {
                    "tax_id_type": "eu_vat",
                    "tax_id_value": "DE123456789",
                }
            ],
            tax_remitted_by="self",
            tax_type="inclusive",
            three_ds_level="mandate_challenge",
            title="Shine Time Auto Detailing",
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
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
        )
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_form_company_with_all_params(self, client: Whop) -> None:
        account = client.accounts.form_company(
            account_id="account_id",
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                        "line2": "Apt 4",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                    "date_of_birth": "1988-03-14",
                    "ownership_percentage": 100,
                    "roles": ["president"],
                    "ssn": "123-45-6789",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
            business_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "postal_code": "78756",
                "state": "TX",
                "line2": "Suite 2",
            },
            business_phone="+15125550142",
            business_website="https://shinetime.example",
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
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
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
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
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
                business_name="Shine Time Auto Detailing",
                business_type="brick_and_mortar",
                formation_state="TX",
                founders=[
                    {
                        "address": {
                            "city": "Austin",
                            "country": "US",
                            "line1": "907 Ridgemont Dr",
                            "postal_code": "78704",
                            "state": "TX",
                        },
                        "email": "marcus@shinetime.example",
                        "first_name": "Marcus",
                        "is_primary": True,
                        "last_name": "Webb",
                        "phone": "+15125550142",
                    }
                ],
                industry_group="automotive",
                industry_type="car_wash",
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
            identifier="marcus@shinetime.example",
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transfer_ownership_with_all_params(self, client: Whop) -> None:
        account = client.accounts.transfer_ownership(
            account_id="account_id",
            identifier="marcus@shinetime.example",
            as_partner=True,
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transfer_ownership(self, client: Whop) -> None:
        response = client.accounts.with_raw_response.transfer_ownership(
            account_id="account_id",
            identifier="marcus@shinetime.example",
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
            identifier="marcus@shinetime.example",
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
                identifier="marcus@shinetime.example",
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
            country="US",
            email="marcus@shinetime.example",
            metadata={"external_id": "bar"},
            title="Shine Time Auto Detailing",
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
            affiliate_instructions="Send us your detailing content before promoting. No paid search on our brand terms.",
            banner_image={"id": "file_xxxxxxxxxxxxxx"},
            business_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="  Shine Time Auto Detailing, LLC  ",
            business_type="other",
            collect_vat_id=True,
            country="US",
            description="Mobile ceramic coating, paint correction, and interior detailing across the Austin metro.",
            featured_affiliate_product_id="prod_xxxxxxxxxxxxxx",
            home_preferences=["hide_member_count"],
            industry_group="automotive",
            industry_type="other",
            invoice_prefix="SHINE",
            logo={"id": "file_xxxxxxxxxxxxxx"},
            metadata={
                "external_id": "bar",
                "region": "bar",
            },
            onboarding_type="seller",
            opengraph_image={"id": "file_xxxxxxxxxxxxxx"},
            opengraph_image_variant="black",
            other_business_description="Mobile auto detailing",
            other_industry_description="Automotive services",
            product_tax_code_id="ptc_xxxxxxxxxxxxxx",
            require_2fa=True,
            route="shine-time-detailing",
            send_customer_emails=False,
            show_joined_whops=False,
            show_reviews_dtc=False,
            show_user_directory=False,
            social_links=[
                {
                    "url": "bar",
                    "website": "bar",
                }
            ],
            store_page_config={
                "accent_color": "red",
                "layout": "compact",
                "profile_variant": "business",
                "whop_affiliate_link": True,
            },
            target_audience="Owners of new and enthusiast vehicles in Austin, TX",
            tax_collection_enabled_states=["TX"],
            tax_identifiers=[
                {
                    "tax_id_type": "eu_vat",
                    "tax_id_value": "DE123456789",
                }
            ],
            tax_remitted_by="self",
            tax_type="inclusive",
            three_ds_level="mandate_challenge",
            title="Shine Time Auto Detailing",
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
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
        )
        assert_matches_type(AccountFormCompanyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_form_company_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.form_company(
            account_id="account_id",
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                        "line2": "Apt 4",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                    "date_of_birth": "1988-03-14",
                    "ownership_percentage": 100,
                    "roles": ["president"],
                    "ssn": "123-45-6789",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
            business_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "postal_code": "78756",
                "state": "TX",
                "line2": "Suite 2",
            },
            business_phone="+15125550142",
            business_website="https://shinetime.example",
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
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
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
            business_name="Shine Time Auto Detailing",
            business_type="brick_and_mortar",
            formation_state="TX",
            founders=[
                {
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "907 Ridgemont Dr",
                        "postal_code": "78704",
                        "state": "TX",
                    },
                    "email": "marcus@shinetime.example",
                    "first_name": "Marcus",
                    "is_primary": True,
                    "last_name": "Webb",
                    "phone": "+15125550142",
                }
            ],
            industry_group="automotive",
            industry_type="car_wash",
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
                business_name="Shine Time Auto Detailing",
                business_type="brick_and_mortar",
                formation_state="TX",
                founders=[
                    {
                        "address": {
                            "city": "Austin",
                            "country": "US",
                            "line1": "907 Ridgemont Dr",
                            "postal_code": "78704",
                            "state": "TX",
                        },
                        "email": "marcus@shinetime.example",
                        "first_name": "Marcus",
                        "is_primary": True,
                        "last_name": "Webb",
                        "phone": "+15125550142",
                    }
                ],
                industry_group="automotive",
                industry_type="car_wash",
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
            identifier="marcus@shinetime.example",
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transfer_ownership_with_all_params(self, async_client: AsyncWhop) -> None:
        account = await async_client.accounts.transfer_ownership(
            account_id="account_id",
            identifier="marcus@shinetime.example",
            as_partner=True,
        )
        assert_matches_type(AccountTransferOwnershipResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transfer_ownership(self, async_client: AsyncWhop) -> None:
        response = await async_client.accounts.with_raw_response.transfer_ownership(
            account_id="account_id",
            identifier="marcus@shinetime.example",
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
            identifier="marcus@shinetime.example",
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
                identifier="marcus@shinetime.example",
            )
