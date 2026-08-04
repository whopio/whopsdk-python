# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    ResolutionCenterCaseDenyResponse,
    ResolutionCenterCaseListResponse,
    ResolutionCenterCaseReplyResponse,
    ResolutionCenterCaseAcceptResponse,
    ResolutionCenterCaseAppealResponse,
    ResolutionCenterCaseCreateResponse,
    ResolutionCenterCaseEventsResponse,
    ResolutionCenterCaseSummaryResponse,
    ResolutionCenterCaseRetrieveResponse,
    ResolutionCenterCaseWithdrawResponse,
    ResolutionCenterCaseRequestInfoResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResolutionCenterCases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
        )
        assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.retrieve(
            "id",
        )
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.list()
        assert_matches_type(SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            outcome=["customer_won"],
            reason=["fraudulent"],
            status=["awaiting_merchant"],
            user_id="user_id",
        )
        assert_matches_type(SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(
                SyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accept(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.accept(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accept_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.accept(
            id="id",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            message="message",
            terminate_membership=True,
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_accept(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.accept(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_accept(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.accept(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_accept(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.accept(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_appeal(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.appeal(
            id="id",
            message="message",
        )
        assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_appeal_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.appeal(
            id="id",
            message="message",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_appeal(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.appeal(
            id="id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_appeal(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.appeal(
            id="id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_appeal(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.appeal(
                id="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deny(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.deny(
            id="id",
            message="message",
        )
        assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deny_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.deny(
            id="id",
            message="message",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deny(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.deny(
            id="id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deny(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.deny(
            id="id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deny(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.deny(
                id="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.events(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_events_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.events(
            id="id",
            after="after",
            before="before",
            first=0,
            last=0,
        )
        assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_events(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.events(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_events(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_events(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reply(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.reply(
            id="id",
            message="message",
        )
        assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reply_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.reply(
            id="id",
            message="message",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.reply(
            id="id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.reply(
            id="id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reply(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.reply(
                id="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_info(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.request_info(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_info_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.request_info(
            id="id",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            message="message",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_info(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.request_info(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_info(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.request_info(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_info(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.request_info(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_summary(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.summary()
        assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_summary_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.summary(
            account_id="account_id",
            created_after="created_after",
            created_before="created_before",
            groups=["status"],
            outcome=["customer_won"],
            reason=["fraudulent"],
            status=["awaiting_merchant"],
            user_id="user_id",
        )
        assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_summary(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_summary(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_withdraw(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.withdraw(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_withdraw_with_all_params(self, client: Whop) -> None:
        resolution_center_case = client.resolution_center_cases.withdraw(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_withdraw(self, client: Whop) -> None:
        response = client.resolution_center_cases.with_raw_response.withdraw(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = response.parse()
        assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_withdraw(self, client: Whop) -> None:
        with client.resolution_center_cases.with_streaming_response.withdraw(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = response.parse()
            assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_withdraw(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.resolution_center_cases.with_raw_response.withdraw(
                id="",
            )


class TestAsyncResolutionCenterCases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
        )
        assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.create(
            message="message",
            reason="fraudulent",
            receipt_id="receipt_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseCreateResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.retrieve(
            "id",
        )
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseRetrieveResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.list()
        assert_matches_type(
            AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.list(
            account_id="account_id",
            after="after",
            before="before",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=0,
            last=0,
            order="created_at",
            outcome=["customer_won"],
            reason=["fraudulent"],
            status=["awaiting_merchant"],
            user_id="user_id",
        )
        assert_matches_type(
            AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(
            AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(
                AsyncCursorPage[ResolutionCenterCaseListResponse], resolution_center_case, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accept(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.accept(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accept_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.accept(
            id="id",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            message="message",
            terminate_membership=True,
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_accept(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.accept(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_accept(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.accept(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseAcceptResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_accept(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.accept(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_appeal(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.appeal(
            id="id",
            message="message",
        )
        assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_appeal_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.appeal(
            id="id",
            message="message",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_appeal(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.appeal(
            id="id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_appeal(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.appeal(
            id="id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseAppealResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_appeal(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.appeal(
                id="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deny(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.deny(
            id="id",
            message="message",
        )
        assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deny_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.deny(
            id="id",
            message="message",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deny(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.deny(
            id="id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deny(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.deny(
            id="id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseDenyResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deny(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.deny(
                id="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.events(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.events(
            id="id",
            after="after",
            before="before",
            first=0,
            last=0,
        )
        assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.events(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.events(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseEventsResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_events(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.events(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.reply(
            id="id",
            message="message",
        )
        assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.reply(
            id="id",
            message="message",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.reply(
            id="id",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.reply(
            id="id",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseReplyResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reply(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.reply(
                id="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_info(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.request_info(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_info_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.request_info(
            id="id",
            attachments=[
                {
                    "id": "id",
                    "direct_upload_id": "direct_upload_id",
                }
            ],
            message="message",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_info(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.request_info(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_info(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.request_info(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseRequestInfoResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_info(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.request_info(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_summary(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.summary()
        assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.summary(
            account_id="account_id",
            created_after="created_after",
            created_before="created_before",
            groups=["status"],
            outcome=["customer_won"],
            reason=["fraudulent"],
            status=["awaiting_merchant"],
            user_id="user_id",
        )
        assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseSummaryResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_withdraw(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.withdraw(
            id="id",
        )
        assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_withdraw_with_all_params(self, async_client: AsyncWhop) -> None:
        resolution_center_case = await async_client.resolution_center_cases.withdraw(
            id="id",
            idempotency_key="d9105228-4a08-46b1-8b91-42fed586d383",
        )
        assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_withdraw(self, async_client: AsyncWhop) -> None:
        response = await async_client.resolution_center_cases.with_raw_response.withdraw(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolution_center_case = await response.parse()
        assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_withdraw(self, async_client: AsyncWhop) -> None:
        async with async_client.resolution_center_cases.with_streaming_response.withdraw(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolution_center_case = await response.parse()
            assert_matches_type(ResolutionCenterCaseWithdrawResponse, resolution_center_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_withdraw(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.resolution_center_cases.with_raw_response.withdraw(
                id="",
            )
