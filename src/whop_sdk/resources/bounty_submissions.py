# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import bounty_submission_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.bounty_submission import BountySubmission

__all__ = ["BountySubmissionsResource", "AsyncBountySubmissionsResource"]


class BountySubmissionsResource(SyncAPIResource):
    """A Bounty Submission is one worker's attempt on a bounty.

    It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

    Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
    """

    @cached_property
    def with_raw_response(self) -> BountySubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return BountySubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BountySubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return BountySubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        bounty_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        status: Literal["in_progress", "submitted", "approved", "denied"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BountySubmission]:
        """Lists bounty submissions visible to the credential.

        User tokens return the
        submissions they authored plus every submission on bounties they posted; account
        API keys return the submissions on the account's bounties. Pass account_id to
        view another account's submissions as a team member, or bounty_id to narrow the
        list to one bounty.

        Args:
          account_id: Scope the list to submissions on this account's bounties (`biz_` tag). Requires
              read access to the account.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          bounty_id: Only submissions on this bounty (`bnty_` tag).

          created_after: Only submissions created after this ISO 8601 timestamp.

          created_before: Only submissions created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of submissions to return from the start of the window.

          last: Number of submissions to return from the end of the window.

          order: Sort field.

          status: Filter by lifecycle state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bounty_submissions",
            page=SyncCursorPage[BountySubmission],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "bounty_id": bounty_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    bounty_submission_list_params.BountySubmissionListParams,
                ),
            ),
            model=BountySubmission,
        )


class AsyncBountySubmissionsResource(AsyncAPIResource):
    """A Bounty Submission is one worker's attempt on a bounty.

    It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

    Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBountySubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBountySubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBountySubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncBountySubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        bounty_id: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        status: Literal["in_progress", "submitted", "approved", "denied"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BountySubmission, AsyncCursorPage[BountySubmission]]:
        """Lists bounty submissions visible to the credential.

        User tokens return the
        submissions they authored plus every submission on bounties they posted; account
        API keys return the submissions on the account's bounties. Pass account_id to
        view another account's submissions as a team member, or bounty_id to narrow the
        list to one bounty.

        Args:
          account_id: Scope the list to submissions on this account's bounties (`biz_` tag). Requires
              read access to the account.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          bounty_id: Only submissions on this bounty (`bnty_` tag).

          created_after: Only submissions created after this ISO 8601 timestamp.

          created_before: Only submissions created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of submissions to return from the start of the window.

          last: Number of submissions to return from the end of the window.

          order: Sort field.

          status: Filter by lifecycle state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bounty_submissions",
            page=AsyncCursorPage[BountySubmission],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "bounty_id": bounty_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    bounty_submission_list_params.BountySubmissionListParams,
                ),
            ),
            model=BountySubmission,
        )


class BountySubmissionsResourceWithRawResponse:
    def __init__(self, bounty_submissions: BountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.list = to_raw_response_wrapper(
            bounty_submissions.list,
        )


class AsyncBountySubmissionsResourceWithRawResponse:
    def __init__(self, bounty_submissions: AsyncBountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.list = async_to_raw_response_wrapper(
            bounty_submissions.list,
        )


class BountySubmissionsResourceWithStreamingResponse:
    def __init__(self, bounty_submissions: BountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.list = to_streamed_response_wrapper(
            bounty_submissions.list,
        )


class AsyncBountySubmissionsResourceWithStreamingResponse:
    def __init__(self, bounty_submissions: AsyncBountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.list = async_to_streamed_response_wrapper(
            bounty_submissions.list,
        )
