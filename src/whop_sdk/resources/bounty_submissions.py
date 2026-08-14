# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import bounty_submission_list_params, bounty_submission_create_params, bounty_submission_submit_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.bounty_submission_delete_response import BountySubmissionDeleteResponse

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

    def create(
        self,
        *,
        bounty_id: str,
        affiliate_code: Optional[str] | Omit = omit,
        deliverable: Optional[bounty_submission_create_params.Deliverable] | Omit = omit,
        metadata: Optional[bounty_submission_create_params.Metadata] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BountySubmission:
        """Creates a submission on a workforce bounty.

        Include a `deliverable` payload —
        any combination of links and uploaded files, with at least one of the two — and
        the submission goes straight to review; create is the only step. For
        `data_capture` bounties, omit the deliverable: this starts a claimed attempt
        whose proof accumulates server-side, and the separate submit endpoint sends it
        to review once complete. Requires a user credential — account API keys cannot
        author submissions.

        Args:
          bounty_id: The bounty to submit to (`bnty_` tag).

          affiliate_code: Affiliate code crediting the referrer, when the worker arrived through one.

          deliverable: The submitted work. Combine `urls`, `file_ids`, and `caption` freely; at least
              one link or file is required.

          metadata: Optional capture metadata describing where and how the footage was recorded.
              Persisted on the submission. On a `data_capture` bounty every field except `fov`
              is required whenever metadata is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/bounty_submissions",
            body=maybe_transform(
                {
                    "bounty_id": bounty_id,
                    "affiliate_code": affiliate_code,
                    "deliverable": deliverable,
                    "metadata": metadata,
                },
                bounty_submission_create_params.BountySubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BountySubmission,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BountySubmission:
        """
        Retrieves one bounty submission the credential can see — one the caller
        authored, or one on a bounty they posted or their account owns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/bounty_submissions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BountySubmission,
        )

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
        order: Literal["created_at", "updated_at"] | Omit = omit,
        status: Literal["in_progress", "submitted", "approved", "denied"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BountySubmission]:
        """
        Lists bounty submissions visible to the credential — for a user token, the
        submissions they authored plus those on bounties they posted; for an account API
        key, the submissions on the account's bounties. For the anonymous view of one
        bounty's reviewed work, use the submissions list under the bounty instead.

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

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BountySubmissionDeleteResponse:
        """
        Cancels the caller's own active attempt on a bounty and discards any accumulated
        capture clips. Only the worker who started the attempt can cancel it — account
        API keys cannot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/bounty_submissions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BountySubmissionDeleteResponse,
        )

    def submit(
        self,
        id: str,
        *,
        deliverable: Optional[bounty_submission_submit_params.Deliverable] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BountySubmission:
        """Submits a claimed attempt for review.

        A livestream attempt needs an ended proof
        stream and can attach an optional `deliverable` — links, files, and a caption in
        any combination; if the attempt already went to review when its stream ended,
        the payload attaches to it once, until reviewers start voting. A data capture
        attempt instead needs enough validated clip time and takes no payload. Only the
        worker who started the attempt can submit it — account API keys cannot.

        Args:
          deliverable: Work to attach to the submission. Combine `urls`, `file_ids`, and `caption`
              freely; all are optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/bounty_submissions/{id}/submit", id=id),
            body=maybe_transform(
                {"deliverable": deliverable}, bounty_submission_submit_params.BountySubmissionSubmitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BountySubmission,
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

    async def create(
        self,
        *,
        bounty_id: str,
        affiliate_code: Optional[str] | Omit = omit,
        deliverable: Optional[bounty_submission_create_params.Deliverable] | Omit = omit,
        metadata: Optional[bounty_submission_create_params.Metadata] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BountySubmission:
        """Creates a submission on a workforce bounty.

        Include a `deliverable` payload —
        any combination of links and uploaded files, with at least one of the two — and
        the submission goes straight to review; create is the only step. For
        `data_capture` bounties, omit the deliverable: this starts a claimed attempt
        whose proof accumulates server-side, and the separate submit endpoint sends it
        to review once complete. Requires a user credential — account API keys cannot
        author submissions.

        Args:
          bounty_id: The bounty to submit to (`bnty_` tag).

          affiliate_code: Affiliate code crediting the referrer, when the worker arrived through one.

          deliverable: The submitted work. Combine `urls`, `file_ids`, and `caption` freely; at least
              one link or file is required.

          metadata: Optional capture metadata describing where and how the footage was recorded.
              Persisted on the submission. On a `data_capture` bounty every field except `fov`
              is required whenever metadata is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/bounty_submissions",
            body=await async_maybe_transform(
                {
                    "bounty_id": bounty_id,
                    "affiliate_code": affiliate_code,
                    "deliverable": deliverable,
                    "metadata": metadata,
                },
                bounty_submission_create_params.BountySubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BountySubmission,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BountySubmission:
        """
        Retrieves one bounty submission the credential can see — one the caller
        authored, or one on a bounty they posted or their account owns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/bounty_submissions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BountySubmission,
        )

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
        order: Literal["created_at", "updated_at"] | Omit = omit,
        status: Literal["in_progress", "submitted", "approved", "denied"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BountySubmission, AsyncCursorPage[BountySubmission]]:
        """
        Lists bounty submissions visible to the credential — for a user token, the
        submissions they authored plus those on bounties they posted; for an account API
        key, the submissions on the account's bounties. For the anonymous view of one
        bounty's reviewed work, use the submissions list under the bounty instead.

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

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BountySubmissionDeleteResponse:
        """
        Cancels the caller's own active attempt on a bounty and discards any accumulated
        capture clips. Only the worker who started the attempt can cancel it — account
        API keys cannot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/bounty_submissions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BountySubmissionDeleteResponse,
        )

    async def submit(
        self,
        id: str,
        *,
        deliverable: Optional[bounty_submission_submit_params.Deliverable] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BountySubmission:
        """Submits a claimed attempt for review.

        A livestream attempt needs an ended proof
        stream and can attach an optional `deliverable` — links, files, and a caption in
        any combination; if the attempt already went to review when its stream ended,
        the payload attaches to it once, until reviewers start voting. A data capture
        attempt instead needs enough validated clip time and takes no payload. Only the
        worker who started the attempt can submit it — account API keys cannot.

        Args:
          deliverable: Work to attach to the submission. Combine `urls`, `file_ids`, and `caption`
              freely; all are optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/bounty_submissions/{id}/submit", id=id),
            body=await async_maybe_transform(
                {"deliverable": deliverable}, bounty_submission_submit_params.BountySubmissionSubmitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BountySubmission,
        )


class BountySubmissionsResourceWithRawResponse:
    def __init__(self, bounty_submissions: BountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.create = to_raw_response_wrapper(
            bounty_submissions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bounty_submissions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bounty_submissions.list,
        )
        self.delete = to_raw_response_wrapper(
            bounty_submissions.delete,
        )
        self.submit = to_raw_response_wrapper(
            bounty_submissions.submit,
        )


class AsyncBountySubmissionsResourceWithRawResponse:
    def __init__(self, bounty_submissions: AsyncBountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.create = async_to_raw_response_wrapper(
            bounty_submissions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bounty_submissions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bounty_submissions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bounty_submissions.delete,
        )
        self.submit = async_to_raw_response_wrapper(
            bounty_submissions.submit,
        )


class BountySubmissionsResourceWithStreamingResponse:
    def __init__(self, bounty_submissions: BountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.create = to_streamed_response_wrapper(
            bounty_submissions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bounty_submissions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bounty_submissions.list,
        )
        self.delete = to_streamed_response_wrapper(
            bounty_submissions.delete,
        )
        self.submit = to_streamed_response_wrapper(
            bounty_submissions.submit,
        )


class AsyncBountySubmissionsResourceWithStreamingResponse:
    def __init__(self, bounty_submissions: AsyncBountySubmissionsResource) -> None:
        self._bounty_submissions = bounty_submissions

        self.create = async_to_streamed_response_wrapper(
            bounty_submissions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bounty_submissions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bounty_submissions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bounty_submissions.delete,
        )
        self.submit = async_to_streamed_response_wrapper(
            bounty_submissions.submit,
        )
