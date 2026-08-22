# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from whop_sdk import Whop, AsyncWhop
from tests.utils import assert_matches_type
from whop_sdk.types import (
    BountySubmission,
    BountySubmissionDeleteResponse,
)
from whop_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBountySubmissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
            affiliate_code="tanyacole",
            deliverable={
                "caption": "Ceramic coating reveal, shot at the Burnet Rd bay",
                "file_ids": ["file_xxxxxxxxxxxxxx"],
                "type": "content_url",
                "urls": ["https://youtube.com/shorts/2"],
            },
            metadata={
                "city": "Austin",
                "country": "US",
                "device": "iPhone 15 Pro",
                "fov": 120,
                "operator": "mwebb",
                "site": "BurnetRd",
                "station": "Bay2",
            },
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Whop) -> None:
        response = client.bounty_submissions.with_raw_response.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = response.parse()
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Whop) -> None:
        with client.bounty_submissions.with_streaming_response.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = response.parse()
            assert_matches_type(BountySubmission, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.retrieve(
            id="id",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.retrieve(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Whop) -> None:
        response = client.bounty_submissions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = response.parse()
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Whop) -> None:
        with client.bounty_submissions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = response.parse()
            assert_matches_type(BountySubmission, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bounty_submissions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.list()
        assert_matches_type(SyncCursorPage[BountySubmission], bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.list(
            account_id="account_id",
            after="after",
            before="before",
            bounty_id="bounty_id",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            status="in_progress",
        )
        assert_matches_type(SyncCursorPage[BountySubmission], bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Whop) -> None:
        response = client.bounty_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = response.parse()
        assert_matches_type(SyncCursorPage[BountySubmission], bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Whop) -> None:
        with client.bounty_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = response.parse()
            assert_matches_type(SyncCursorPage[BountySubmission], bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.delete(
            "id",
        )
        assert_matches_type(BountySubmissionDeleteResponse, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Whop) -> None:
        response = client.bounty_submissions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = response.parse()
        assert_matches_type(BountySubmissionDeleteResponse, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Whop) -> None:
        with client.bounty_submissions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = response.parse()
            assert_matches_type(BountySubmissionDeleteResponse, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bounty_submissions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.submit(
            id="id",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Whop) -> None:
        bounty_submission = client.bounty_submissions.submit(
            id="id",
            deliverable={
                "caption": "Full interior detail, start to finish, on a 2019 Tacoma.",
                "file_ids": ["file_xxxxxxxxxxxxxx"],
                "urls": ["https://youtube.com/shorts/4"],
            },
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Whop) -> None:
        response = client.bounty_submissions.with_raw_response.submit(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = response.parse()
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Whop) -> None:
        with client.bounty_submissions.with_streaming_response.submit(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = response.parse()
            assert_matches_type(BountySubmission, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Whop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bounty_submissions.with_raw_response.submit(
                id="",
            )


class TestAsyncBountySubmissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
            affiliate_code="tanyacole",
            deliverable={
                "caption": "Ceramic coating reveal, shot at the Burnet Rd bay",
                "file_ids": ["file_xxxxxxxxxxxxxx"],
                "type": "content_url",
                "urls": ["https://youtube.com/shorts/2"],
            },
            metadata={
                "city": "Austin",
                "country": "US",
                "device": "iPhone 15 Pro",
                "fov": 120,
                "operator": "mwebb",
                "site": "BurnetRd",
                "station": "Bay2",
            },
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounty_submissions.with_raw_response.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = await response.parse()
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWhop) -> None:
        async with async_client.bounty_submissions.with_streaming_response.create(
            bounty_id="bnty_xxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = await response.parse()
            assert_matches_type(BountySubmission, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.retrieve(
            id="id",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.retrieve(
            id="id",
            account_id="account_id",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounty_submissions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = await response.parse()
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWhop) -> None:
        async with async_client.bounty_submissions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = await response.parse()
            assert_matches_type(BountySubmission, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bounty_submissions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.list()
        assert_matches_type(AsyncCursorPage[BountySubmission], bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.list(
            account_id="account_id",
            after="after",
            before="before",
            bounty_id="bounty_id",
            created_after="created_after",
            created_before="created_before",
            direction="asc",
            first=100,
            last=100,
            order="created_at",
            status="in_progress",
        )
        assert_matches_type(AsyncCursorPage[BountySubmission], bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounty_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = await response.parse()
        assert_matches_type(AsyncCursorPage[BountySubmission], bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWhop) -> None:
        async with async_client.bounty_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = await response.parse()
            assert_matches_type(AsyncCursorPage[BountySubmission], bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.delete(
            "id",
        )
        assert_matches_type(BountySubmissionDeleteResponse, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounty_submissions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = await response.parse()
        assert_matches_type(BountySubmissionDeleteResponse, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWhop) -> None:
        async with async_client.bounty_submissions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = await response.parse()
            assert_matches_type(BountySubmissionDeleteResponse, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bounty_submissions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.submit(
            id="id",
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncWhop) -> None:
        bounty_submission = await async_client.bounty_submissions.submit(
            id="id",
            deliverable={
                "caption": "Full interior detail, start to finish, on a 2019 Tacoma.",
                "file_ids": ["file_xxxxxxxxxxxxxx"],
                "urls": ["https://youtube.com/shorts/4"],
            },
        )
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncWhop) -> None:
        response = await async_client.bounty_submissions.with_raw_response.submit(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bounty_submission = await response.parse()
        assert_matches_type(BountySubmission, bounty_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncWhop) -> None:
        async with async_client.bounty_submissions.with_streaming_response.submit(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bounty_submission = await response.parse()
            assert_matches_type(BountySubmission, bounty_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncWhop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bounty_submissions.with_raw_response.submit(
                id="",
            )
