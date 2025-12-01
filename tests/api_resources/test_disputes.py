# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import Dispute, DisputeListResponse
from whop_sdk._utils import parse_datetime
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        dispute = client.disputes.retrieve(
            "dspt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.retrieve(
            "dspt_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.retrieve(
            "dspt_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.disputes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        dispute = client.disputes.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPage[DisputeListResponse], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        dispute = client.disputes.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(SyncCursorPage[DisputeListResponse], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(SyncCursorPage[DisputeListResponse], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(SyncCursorPage[DisputeListResponse], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_evidence(self, client: Whop) -> None:
        dispute = client.disputes.submit_evidence(
            "dspt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_evidence(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.submit_evidence(
            "dspt_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_evidence(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.submit_evidence(
            "dspt_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_evidence(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.disputes.with_raw_response.submit_evidence(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_evidence(self, client: Whop) -> None:
        dispute = client.disputes.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_evidence_with_all_params(self, client: Whop) -> None:
        dispute = client.disputes.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
            access_activity_log="access_activity_log",
            billing_address="billing_address",
            cancellation_policy_attachment={"direct_upload_id": "direct_upload_id"},
            cancellation_policy_disclosure="cancellation_policy_disclosure",
            customer_communication_attachment={"direct_upload_id": "direct_upload_id"},
            customer_email_address="customer_email_address",
            customer_name="customer_name",
            notes="notes",
            product_description="product_description",
            refund_policy_attachment={"direct_upload_id": "direct_upload_id"},
            refund_policy_disclosure="refund_policy_disclosure",
            refund_refusal_explanation="refund_refusal_explanation",
            service_date="service_date",
            uncategorized_attachment={"direct_upload_id": "direct_upload_id"},
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_evidence(self, client: Whop) -> None:
        response = client.disputes.with_raw_response.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_evidence(self, client: Whop) -> None:
        with client.disputes.with_streaming_response.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_evidence(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.disputes.with_raw_response.update_evidence(
                id="",
            )


class TestAsyncDisputes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.retrieve(
            "dspt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.retrieve(
            "dspt_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.retrieve(
            "dspt_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.disputes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPage[DisputeListResponse], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.list(
            company_id="biz_xxxxxxxxxxxxxx",
            after="after",
            before="before",
            created_after=parse_datetime("2023-12-01T05:00:00.401Z"),
            created_before=parse_datetime("2023-12-01T05:00:00.401Z"),
            direction="asc",
            first=42,
            last=42,
        )
        assert_matches_type(AsyncCursorPage[DisputeListResponse], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(AsyncCursorPage[DisputeListResponse], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.list(
            company_id="biz_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(AsyncCursorPage[DisputeListResponse], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_evidence(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.submit_evidence(
            "dspt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_evidence(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.submit_evidence(
            "dspt_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_evidence(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.submit_evidence(
            "dspt_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_evidence(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.disputes.with_raw_response.submit_evidence(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_evidence(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_evidence_with_all_params(self, async_client: AsyncWhop) -> None:
        dispute = await async_client.disputes.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
            access_activity_log="access_activity_log",
            billing_address="billing_address",
            cancellation_policy_attachment={"direct_upload_id": "direct_upload_id"},
            cancellation_policy_disclosure="cancellation_policy_disclosure",
            customer_communication_attachment={"direct_upload_id": "direct_upload_id"},
            customer_email_address="customer_email_address",
            customer_name="customer_name",
            notes="notes",
            product_description="product_description",
            refund_policy_attachment={"direct_upload_id": "direct_upload_id"},
            refund_policy_disclosure="refund_policy_disclosure",
            refund_refusal_explanation="refund_refusal_explanation",
            service_date="service_date",
            uncategorized_attachment={"direct_upload_id": "direct_upload_id"},
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_evidence(self, async_client: AsyncWhop) -> None:
        response = await async_client.disputes.with_raw_response.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_evidence(self, async_client: AsyncWhop) -> None:
        async with async_client.disputes.with_streaming_response.update_evidence(
            id="dspt_xxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_evidence(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.disputes.with_raw_response.update_evidence(
                id="",
            )
