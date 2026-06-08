# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    VerificationCreateResponse,
    VerificationDeleteResponse,
    VerificationUpdateResponse,
    VerificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        verification = client.verifications.create(
            account_id="account_id",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        verification = client.verifications.create(
            account_id="account_id",
            address={"foo": "bar"},
            country="country",
            date_of_birth="date_of_birth",
            first_name="first_name",
            kind="individual",
            last_name="last_name",
            phone="phone",
            restart=True,
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
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
            "verification_id",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.retrieve(
            "verification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.retrieve(
            "verification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.verifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        verification = client.verifications.update(
            verification_id="verification_id",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        verification = client.verifications.update(
            verification_id="verification_id",
            business_address={"foo": "bar"},
            business_name="business_name",
            business_structure="business_structure",
            country="country",
            date_of_birth="date_of_birth",
            first_name="first_name",
            last_name="last_name",
            personal_address={"foo": "bar"},
            rfis=[
                {
                    "id": "id",
                    "address": {"foo": "bar"},
                    "files": [{}],
                    "value": "value",
                    "value_type": "raw",
                }
            ],
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.update(
            verification_id="verification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.update(
            verification_id="verification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.verifications.with_raw_response.update(
                verification_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        verification = client.verifications.delete(
            "verification_id",
        )
        assert_matches_type(VerificationDeleteResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.verifications.with_raw_response.delete(
            "verification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationDeleteResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.verifications.with_streaming_response.delete(
            "verification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationDeleteResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.verifications.with_raw_response.delete(
                "",
            )


class TestAsyncVerifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.create(
            account_id="account_id",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.create(
            account_id="account_id",
            address={"foo": "bar"},
            country="country",
            date_of_birth="date_of_birth",
            first_name="first_name",
            kind="individual",
            last_name="last_name",
            phone="phone",
            restart=True,
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
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
            "verification_id",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.retrieve(
            "verification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.retrieve(
            "verification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.verifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.update(
            verification_id="verification_id",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.update(
            verification_id="verification_id",
            business_address={"foo": "bar"},
            business_name="business_name",
            business_structure="business_structure",
            country="country",
            date_of_birth="date_of_birth",
            first_name="first_name",
            last_name="last_name",
            personal_address={"foo": "bar"},
            rfis=[
                {
                    "id": "id",
                    "address": {"foo": "bar"},
                    "files": [{}],
                    "value": "value",
                    "value_type": "raw",
                }
            ],
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.update(
            verification_id="verification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.update(
            verification_id="verification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.verifications.with_raw_response.update(
                verification_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        verification = await async_client.verifications.delete(
            "verification_id",
        )
        assert_matches_type(VerificationDeleteResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.verifications.with_raw_response.delete(
            "verification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationDeleteResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.verifications.with_streaming_response.delete(
            "verification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationDeleteResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.verifications.with_raw_response.delete(
                "",
            )
