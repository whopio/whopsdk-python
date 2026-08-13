# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    Dispute,
    DisputeSummaryResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        dispute = client.disputes.retrieve(
            "id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.disputes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Whop) -> None:
        dispute = client.disputes.update(
            id="id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Whop) -> None:
        dispute = client.disputes.update(
            id="id",
            evidence={
                "access_activity_log": "access_activity_log",
                "billing_address": "billing_address",
                "cancellation_policy_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "cancellation_policy_disclosure": "cancellation_policy_disclosure",
                "customer_communication_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "customer_email_address": "customer_email_address",
                "customer_name": "customer_name",
                "notes": "notes",
                "product_description": "product_description",
                "refund_policy_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "refund_policy_disclosure": "refund_policy_disclosure",
                "refund_refusal_explanation": "refund_refusal_explanation",
                "service_date": "service_date",
                "uncategorized_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
            },
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.disputes.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        dispute = client.disputes.list()
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        dispute = client.disputes.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            currency="currency",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            status=["needs_response"],
        )
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Whop) -> None:
        dispute = client.disputes.submit(
            "id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.submit(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.submit(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.disputes.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_summary(self, client: Whop) -> None:
        dispute = client.disputes.summary()
        assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_summary_with_all_params(self, client: Whop) -> None:
        dispute = client.disputes.summary(
            account_id="account_id",
            created_after="created_after",
            created_before="created_before",
            currency="currency",
            groups=["status"],
            status=["needs_response"],
        )
        assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_summary(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_summary(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDisputes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.retrieve(
            "id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.disputes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.update(
            id="id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.update(
            id="id",
            evidence={
                "access_activity_log": "access_activity_log",
                "billing_address": "billing_address",
                "cancellation_policy_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "cancellation_policy_disclosure": "cancellation_policy_disclosure",
                "customer_communication_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "customer_email_address": "customer_email_address",
                "customer_name": "customer_name",
                "notes": "notes",
                "product_description": "product_description",
                "refund_policy_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
                "refund_policy_disclosure": "refund_policy_disclosure",
                "refund_refusal_explanation": "refund_refusal_explanation",
                "service_date": "service_date",
                "uncategorized_attachment": {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                },
            },
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.disputes.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.list()
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            currency="currency",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            status=["needs_response"],
        )
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.submit(
            "id",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.submit(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.submit(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.disputes.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_summary(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.summary()
        assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.summary(
            account_id="account_id",
            created_after="created_after",
            created_before="created_before",
            currency="currency",
            groups=["status"],
            status=["needs_response"],
        )
        assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(DisputeSummaryResponse, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True
