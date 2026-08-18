# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.bounties import submission_list_params
from ...types.bounties.public_bounty_submission import PublicBountySubmission

__all__ = ["SubmissionsResource", "AsyncSubmissionsResource"]


class SubmissionsResource(SyncAPIResource):
    """A Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
    """

    @cached_property
    def with_raw_response(self) -> SubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return SubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return SubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        bounty_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "updated_at"] | Omit = omit,
        status: Literal["submitted", "approved", "denied"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PublicBountySubmission]:
        """
        Lists a bounty's publicly visible work — submitted, approved, and denied
        submissions in the reduced public shape. Authentication is optional; a bounty
        that is not publicly visible returns `404`.

        Args:
          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

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
        if not bounty_id:
            raise ValueError(f"Expected a non-empty value for `bounty_id` but received {bounty_id!r}")
        return self._get_api_list(
            path_template("/bounties/{bounty_id}/submissions", bounty_id=bounty_id),
            page=SyncCursorPage[PublicBountySubmission],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    submission_list_params.SubmissionListParams,
                ),
            ),
            model=PublicBountySubmission,
        )


class AsyncSubmissionsResource(AsyncAPIResource):
    """A Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncSubmissionsResourceWithStreamingResponse(self)

    def list(
        self,
        bounty_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "updated_at"] | Omit = omit,
        status: Literal["submitted", "approved", "denied"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicBountySubmission, AsyncCursorPage[PublicBountySubmission]]:
        """
        Lists a bounty's publicly visible work — submitted, approved, and denied
        submissions in the reduced public shape. Authentication is optional; a bounty
        that is not publicly visible returns `404`.

        Args:
          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

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
        if not bounty_id:
            raise ValueError(f"Expected a non-empty value for `bounty_id` but received {bounty_id!r}")
        return self._get_api_list(
            path_template("/bounties/{bounty_id}/submissions", bounty_id=bounty_id),
            page=AsyncCursorPage[PublicBountySubmission],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    submission_list_params.SubmissionListParams,
                ),
            ),
            model=PublicBountySubmission,
        )


class SubmissionsResourceWithRawResponse:
    def __init__(self, submissions: SubmissionsResource) -> None:
        self._submissions = submissions

        self.list = to_raw_response_wrapper(
            submissions.list,
        )


class AsyncSubmissionsResourceWithRawResponse:
    def __init__(self, submissions: AsyncSubmissionsResource) -> None:
        self._submissions = submissions

        self.list = async_to_raw_response_wrapper(
            submissions.list,
        )


class SubmissionsResourceWithStreamingResponse:
    def __init__(self, submissions: SubmissionsResource) -> None:
        self._submissions = submissions

        self.list = to_streamed_response_wrapper(
            submissions.list,
        )


class AsyncSubmissionsResourceWithStreamingResponse:
    def __init__(self, submissions: AsyncSubmissionsResource) -> None:
        self._submissions = submissions

        self.list = async_to_streamed_response_wrapper(
            submissions.list,
        )
