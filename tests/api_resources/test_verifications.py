# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    VerificationListResponse,
    VerificationCreateResponse,
    VerificationUpdateResponse,
    VerificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Whop) -> None:
        verification = client.verifications.create(
            account_id="account_id",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Whop) -> None:
        verification = client.verifications.create(
            account_id="account_id",
            address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="Shine Time Auto Detailing LLC",
            business_structure="private_corporation",
            business_tax_identification_number="12-3456789",
            business_website="https://shinetime.example",
            country="US",
            date_of_birth="2026-01-01",
            document_type="RESIDENCE_PERMIT",
            documents={
                "drivers_back": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "drivers_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "id_card_back": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "id_card_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "passport_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "residence_permit_back": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "residence_permit_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "selfie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
            },
            first_name="Marcus",
            kind="individual",
            last_name="Webb",
            phone="+xxxxxxxxxxx",
            share_token="_act-sbx-jwt-eyJhbGciOiJub25l",
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Whop) -> None:
        verification = client.verifications.create(
            account_id="account_id",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Whop) -> None:
        verification = client.verifications.create(
            account_id="account_id",
            address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="Shine Time Auto Detailing LLC",
            business_structure="private_corporation",
            business_tax_identification_number="12-3456789",
            business_website="https://shinetime.example",
            country="US",
            date_of_birth="2026-01-01",
            first_name="Marcus",
            kind="business",
            last_name="Webb",
            place_of_incorporation="TX",
            share_token="_act-sbx-jwt-eyJhbGciOiJub25l",
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        verification = client.verifications.retrieve(
            "id",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.verifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Whop) -> None:
        verification = client.verifications.update(
            id="id",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Whop) -> None:
        verification = client.verifications.update(
            id="id",
            business_name="Shine Time Auto Detailing",
            business_structure="sole_proprietorship",
            business_tax_identification_number="12-3456789",
            country="US",
            date_of_birth="2026-01-01",
            first_name="Marcus",
            last_name="Webb",
            personal_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            requested_information=[
                {
                    "id": "inrqi_xxxxxxxxxxxxxx",
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "4180 Burnet Rd",
                        "line2": "Suite 2",
                        "postal_code": "78756",
                        "state": "TX",
                    },
                    "documents": {
                        "drivers_back": "file_xxxxxxxxxxxxxx",
                        "drivers_front": "file_xxxxxxxxxxxxxx",
                        "id_card_back": "file_xxxxxxxxxxxxxx",
                        "id_card_front": "file_xxxxxxxxxxxxxx",
                        "passport_front": "file_xxxxxxxxxxxxxx",
                        "residence_permit_back": "file_xxxxxxxxxxxxxx",
                        "residence_permit_front": "file_xxxxxxxxxxxxxx",
                    },
                    "files": ["file_xxxxxxxxxxxxxx"],
                    "value": "Mobile detailing only; no retail storefront.",
                    "value_type": "raw",
                }
            ],
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.verifications.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Whop) -> None:
        verification = client.verifications.update(
            id="id",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Whop) -> None:
        verification = client.verifications.update(
            id="id",
            business_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="Shine Time Auto Detailing",
            business_structure="sole_proprietorship",
            business_tax_identification_number="12-3456789",
            country="US",
            date_of_birth="2026-01-01",
            first_name="Marcus",
            last_name="Webb",
            requested_information=[
                {
                    "id": "inrqi_xxxxxxxxxxxxxx",
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "4180 Burnet Rd",
                        "line2": "Suite 2",
                        "postal_code": "78756",
                        "state": "TX",
                    },
                    "documents": {
                        "drivers_back": "file_xxxxxxxxxxxxxx",
                        "drivers_front": "file_xxxxxxxxxxxxxx",
                        "id_card_back": "file_xxxxxxxxxxxxxx",
                        "id_card_front": "file_xxxxxxxxxxxxxx",
                        "passport_front": "file_xxxxxxxxxxxxxx",
                        "residence_permit_back": "file_xxxxxxxxxxxxxx",
                        "residence_permit_front": "file_xxxxxxxxxxxxxx",
                    },
                    "files": ["file_xxxxxxxxxxxxxx"],
                    "value": "Mobile detailing only; no retail storefront.",
                    "value_type": "raw",
                }
            ],
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.verifications.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        verification = client.verifications.list(
            account_id="account_id",
        )
        assert_matches_type(VerificationListResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        verification = client.verifications.list(
            account_id="account_id",
            direction="asc",
            order="updated_at",
        )
        assert_matches_type(VerificationListResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationListResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationListResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.create(
            account_id="account_id",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.create(
            account_id="account_id",
            address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="Shine Time Auto Detailing LLC",
            business_structure="private_corporation",
            business_tax_identification_number="12-3456789",
            business_website="https://shinetime.example",
            country="US",
            date_of_birth="2026-01-01",
            document_type="RESIDENCE_PERMIT",
            documents={
                "drivers_back": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "drivers_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "id_card_back": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "id_card_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "passport_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "residence_permit_back": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "residence_permit_front": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
                "selfie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
            },
            first_name="Marcus",
            kind="individual",
            last_name="Webb",
            phone="+xxxxxxxxxxx",
            share_token="_act-sbx-jwt-eyJhbGciOiJub25l",
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.create(
            account_id="account_id",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.create(
            account_id="account_id",
            address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="Shine Time Auto Detailing LLC",
            business_structure="private_corporation",
            business_tax_identification_number="12-3456789",
            business_website="https://shinetime.example",
            country="US",
            date_of_birth="2026-01-01",
            first_name="Marcus",
            kind="business",
            last_name="Webb",
            place_of_incorporation="TX",
            share_token="_act-sbx-jwt-eyJhbGciOiJub25l",
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.retrieve(
            "id",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.verifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.update(
            id="id",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.update(
            id="id",
            business_name="Shine Time Auto Detailing",
            business_structure="sole_proprietorship",
            business_tax_identification_number="12-3456789",
            country="US",
            date_of_birth="2026-01-01",
            first_name="Marcus",
            last_name="Webb",
            personal_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            requested_information=[
                {
                    "id": "inrqi_xxxxxxxxxxxxxx",
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "4180 Burnet Rd",
                        "line2": "Suite 2",
                        "postal_code": "78756",
                        "state": "TX",
                    },
                    "documents": {
                        "drivers_back": "file_xxxxxxxxxxxxxx",
                        "drivers_front": "file_xxxxxxxxxxxxxx",
                        "id_card_back": "file_xxxxxxxxxxxxxx",
                        "id_card_front": "file_xxxxxxxxxxxxxx",
                        "passport_front": "file_xxxxxxxxxxxxxx",
                        "residence_permit_back": "file_xxxxxxxxxxxxxx",
                        "residence_permit_front": "file_xxxxxxxxxxxxxx",
                    },
                    "files": ["file_xxxxxxxxxxxxxx"],
                    "value": "Mobile detailing only; no retail storefront.",
                    "value_type": "raw",
                }
            ],
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.verifications.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.update(
            id="id",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.update(
            id="id",
            business_address={
                "city": "Austin",
                "country": "US",
                "line1": "4180 Burnet Rd",
                "line2": "Suite 2",
                "postal_code": "78756",
                "state": "TX",
            },
            business_name="Shine Time Auto Detailing",
            business_structure="sole_proprietorship",
            business_tax_identification_number="12-3456789",
            country="US",
            date_of_birth="2026-01-01",
            first_name="Marcus",
            last_name="Webb",
            requested_information=[
                {
                    "id": "inrqi_xxxxxxxxxxxxxx",
                    "address": {
                        "city": "Austin",
                        "country": "US",
                        "line1": "4180 Burnet Rd",
                        "line2": "Suite 2",
                        "postal_code": "78756",
                        "state": "TX",
                    },
                    "documents": {
                        "drivers_back": "file_xxxxxxxxxxxxxx",
                        "drivers_front": "file_xxxxxxxxxxxxxx",
                        "id_card_back": "file_xxxxxxxxxxxxxx",
                        "id_card_front": "file_xxxxxxxxxxxxxx",
                        "passport_front": "file_xxxxxxxxxxxxxx",
                        "residence_permit_back": "file_xxxxxxxxxxxxxx",
                        "residence_permit_front": "file_xxxxxxxxxxxxxx",
                    },
                    "files": ["file_xxxxxxxxxxxxxx"],
                    "value": "Mobile detailing only; no retail storefront.",
                    "value_type": "raw",
                }
            ],
            tax_identification_number="123456789",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.verifications.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.list(
            account_id="account_id",
        )
        assert_matches_type(VerificationListResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.list(
            account_id="account_id",
            direction="asc",
            order="updated_at",
        )
        assert_matches_type(VerificationListResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationListResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationListResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True
