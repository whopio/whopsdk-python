# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    membership_list_params,
    membership_pause_params,
    membership_cancel_params,
    membership_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.shared.direction import Direction
from ..types.shared.membership import Membership
from ..types.membership_list_response import MembershipListResponse
from ..types.shared.membership_status import MembershipStatus

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return MembershipsResourceWithStreamingResponse(self)

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
    ) -> Membership:
        """
        Retrieves a membership by ID or license key

        Required permissions:

        - `member:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/memberships/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def update(
        self,
        id: str,
        *,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Update a membership

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          metadata: The metadata to update the membership with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/memberships/{id}",
            body=maybe_transform({"metadata": metadata}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        cancel_options: Optional[
            List[
                Literal[
                    "too_expensive",
                    "switching",
                    "missing_features",
                    "technical_issues",
                    "bad_experience",
                    "other",
                    "testing",
                ]
            ]
        ]
        | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "status", "canceled_at", "date_joined", "total_spend"]]
        | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        promo_code_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[MembershipStatus]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MembershipListResponse]:
        """
        Lists memberships

        Required permissions:

        - `member:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          cancel_options: The cancel options to filter the memberships by

          company_id: The ID of the company to list memberships for

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          plan_ids: The plan IDs to filter the memberships by

          product_ids: The product IDs to filter the memberships by

          promo_code_ids: The promo code IDs to filter the memberships by

          statuses: The membership status to filter the memberships by

          user_ids: Only return memberships from these whop user ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memberships",
            page=SyncCursorPage[MembershipListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cancel_options": cancel_options,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "promo_code_ids": promo_code_ids,
                        "statuses": statuses,
                        "user_ids": user_ids,
                    },
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=MembershipListResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        cancellation_mode: Optional[Literal["at_period_end", "immediate"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Cancels a membership either immediately or at the end of the current billing
        period

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          cancellation_mode: The mode of cancellation for a membership

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/memberships/{id}/cancel",
            body=maybe_transform(
                {"cancellation_mode": cancellation_mode}, membership_cancel_params.MembershipCancelParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def pause(
        self,
        id: str,
        *,
        void_payments: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Pauses a membership's payments

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          void_payments: Whether to void past_due payments associated with the membership to prevent
              future payment attempts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/memberships/{id}/pause",
            body=maybe_transform({"void_payments": void_payments}, membership_pause_params.MembershipPauseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def resume(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Resumes a membership's payments

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/memberships/{id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncMembershipsResourceWithStreamingResponse(self)

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
    ) -> Membership:
        """
        Retrieves a membership by ID or license key

        Required permissions:

        - `member:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/memberships/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Update a membership

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          metadata: The metadata to update the membership with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/memberships/{id}",
            body=await async_maybe_transform({"metadata": metadata}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        cancel_options: Optional[
            List[
                Literal[
                    "too_expensive",
                    "switching",
                    "missing_features",
                    "technical_issues",
                    "bad_experience",
                    "other",
                    "testing",
                ]
            ]
        ]
        | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "status", "canceled_at", "date_joined", "total_spend"]]
        | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        promo_code_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[MembershipStatus]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MembershipListResponse, AsyncCursorPage[MembershipListResponse]]:
        """
        Lists memberships

        Required permissions:

        - `member:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          cancel_options: The cancel options to filter the memberships by

          company_id: The ID of the company to list memberships for

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          plan_ids: The plan IDs to filter the memberships by

          product_ids: The product IDs to filter the memberships by

          promo_code_ids: The promo code IDs to filter the memberships by

          statuses: The membership status to filter the memberships by

          user_ids: Only return memberships from these whop user ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memberships",
            page=AsyncCursorPage[MembershipListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cancel_options": cancel_options,
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "promo_code_ids": promo_code_ids,
                        "statuses": statuses,
                        "user_ids": user_ids,
                    },
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=MembershipListResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        cancellation_mode: Optional[Literal["at_period_end", "immediate"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Cancels a membership either immediately or at the end of the current billing
        period

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          cancellation_mode: The mode of cancellation for a membership

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/memberships/{id}/cancel",
            body=await async_maybe_transform(
                {"cancellation_mode": cancellation_mode}, membership_cancel_params.MembershipCancelParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def pause(
        self,
        id: str,
        *,
        void_payments: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Pauses a membership's payments

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          void_payments: Whether to void past_due payments associated with the membership to prevent
              future payment attempts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/memberships/{id}/pause",
            body=await async_maybe_transform(
                {"void_payments": void_payments}, membership_pause_params.MembershipPauseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def resume(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Resumes a membership's payments

        Required permissions:

        - `member:manage`
        - `member:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/memberships/{id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = to_raw_response_wrapper(
            memberships.retrieve,
        )
        self.update = to_raw_response_wrapper(
            memberships.update,
        )
        self.list = to_raw_response_wrapper(
            memberships.list,
        )
        self.cancel = to_raw_response_wrapper(
            memberships.cancel,
        )
        self.pause = to_raw_response_wrapper(
            memberships.pause,
        )
        self.resume = to_raw_response_wrapper(
            memberships.resume,
        )


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = async_to_raw_response_wrapper(
            memberships.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            memberships.update,
        )
        self.list = async_to_raw_response_wrapper(
            memberships.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            memberships.cancel,
        )
        self.pause = async_to_raw_response_wrapper(
            memberships.pause,
        )
        self.resume = async_to_raw_response_wrapper(
            memberships.resume,
        )


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = to_streamed_response_wrapper(
            memberships.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            memberships.update,
        )
        self.list = to_streamed_response_wrapper(
            memberships.list,
        )
        self.cancel = to_streamed_response_wrapper(
            memberships.cancel,
        )
        self.pause = to_streamed_response_wrapper(
            memberships.pause,
        )
        self.resume = to_streamed_response_wrapper(
            memberships.resume,
        )


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = async_to_streamed_response_wrapper(
            memberships.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            memberships.update,
        )
        self.list = async_to_streamed_response_wrapper(
            memberships.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            memberships.cancel,
        )
        self.pause = async_to_streamed_response_wrapper(
            memberships.pause,
        )
        self.resume = async_to_streamed_response_wrapper(
            memberships.resume,
        )
