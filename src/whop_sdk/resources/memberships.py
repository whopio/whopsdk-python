# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    membership_list_params,
    membership_pause_params,
    membership_cancel_params,
    membership_extend_params,
    membership_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.shared.membership import Membership

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    """
    A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

    Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, and update metadata.
    """

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
        """Retrieves a membership by ID or license key.

        Accessible to the account and to
        the membership's own user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/memberships/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def update(
        self,
        id: str,
        *,
        cancel_at_period_end: bool | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Updates a membership: merge metadata key-value pairs, or toggle
        `cancel_at_period_end` — `true` schedules the cancellation for the end of the
        current billing period, `false` reverses a pending one.

        Args:
          cancel_at_period_end: `true` cancels at the end of the current billing period (the customer keeps
              access until then); `false` reverses a pending cancellation.

          metadata: Key-value pairs to merge into the membership's metadata. Pass an empty object to
              clear it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/memberships/{id}", id=id),
            body=maybe_transform(
                {
                    "cancel_at_period_end": cancel_at_period_end,
                    "metadata": metadata,
                },
                membership_update_params.MembershipUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        plan_id: str | Omit = omit,
        product_id: str | Omit = omit,
        status: Literal["active", "trialing", "past_due", "completed", "canceled", "expired", "canceling", "paused"]
        | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Membership]:
        """
        Lists every membership the caller can read: an account API key its account's; a
        user credential their own plus those of every account they manage. `account_id`
        and `user_id` only narrow that list — values outside the caller's reach return
        fewer results, not an error.

        Args:
          account_id: Narrow to one account (`biz_` tag). With read access to the account this lists
              all of its memberships; without, only the caller's own memberships in it.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only memberships created after this ISO 8601 timestamp.

          created_before: Only memberships created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of memberships to return from the start of the window.

          last: Number of memberships to return from the end of the window.

          order: Sort field.

          plan_id: Filter to memberships of this plan (`plan_` tag). Repeat as plan_ids[] for
              several.

          product_id: Filter to memberships of this product (`prod_` tag). Repeat as product_ids[] for
              several.

          status: Filter by billing state. `canceling` matches active memberships set to cancel at
              period end; `paused` matches memberships with payment collection paused.

          user_id: Narrow to one user's memberships (`user_` tag, or `me` for the caller). A user
              outside the caller's visible set returns an empty list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memberships",
            page=SyncCursorPage[Membership],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "plan_id": plan_id,
                        "product_id": product_id,
                        "status": status,
                        "user_id": user_id,
                    },
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=Membership,
        )

    def cancel(
        self,
        id: str,
        *,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """Cancels a membership immediately, revoking access right away.

        To cancel at the
        end of the billing period instead, update the membership with
        `cancel_at_period_end: true`.

        Args:
          reason: Free-form note recording why the membership was canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/memberships/{id}/cancel", id=id),
            body=maybe_transform({"reason": reason}, membership_cancel_params.MembershipCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def extend(
        self,
        id: str,
        *,
        days: int,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Adds free days to a membership, extending its current billing period, expiration
        date, or trial depending on the plan type.

        Args:
          days: Number of free days to add (1-1095).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/memberships/{id}/extend", id=id),
            body=maybe_transform({"days": days}, membership_extend_params.MembershipExtendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def pause(
        self,
        id: str,
        *,
        until: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """Pauses a membership's recurring payment collection.

        The customer keeps access
        but is not charged until the membership is resumed.

        Args:
          until: ISO 8601 time to automatically resume payment collection. Must be in the future;
              only supported for memberships billed by Whop.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/memberships/{id}/pause", id=id),
            body=maybe_transform({"until": until}, membership_pause_params.MembershipPauseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def resume(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """Resumes a previously paused membership's recurring payment collection.

        Billing
        resumes on the next cycle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/memberships/{id}/resume", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )


class AsyncMembershipsResource(AsyncAPIResource):
    """
    A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

    Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, and update metadata.
    """

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
        """Retrieves a membership by ID or license key.

        Accessible to the account and to
        the membership's own user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/memberships/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def update(
        self,
        id: str,
        *,
        cancel_at_period_end: bool | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Updates a membership: merge metadata key-value pairs, or toggle
        `cancel_at_period_end` — `true` schedules the cancellation for the end of the
        current billing period, `false` reverses a pending one.

        Args:
          cancel_at_period_end: `true` cancels at the end of the current billing period (the customer keeps
              access until then); `false` reverses a pending cancellation.

          metadata: Key-value pairs to merge into the membership's metadata. Pass an empty object to
              clear it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/memberships/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "cancel_at_period_end": cancel_at_period_end,
                    "metadata": metadata,
                },
                membership_update_params.MembershipUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        plan_id: str | Omit = omit,
        product_id: str | Omit = omit,
        status: Literal["active", "trialing", "past_due", "completed", "canceled", "expired", "canceling", "paused"]
        | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Membership, AsyncCursorPage[Membership]]:
        """
        Lists every membership the caller can read: an account API key its account's; a
        user credential their own plus those of every account they manage. `account_id`
        and `user_id` only narrow that list — values outside the caller's reach return
        fewer results, not an error.

        Args:
          account_id: Narrow to one account (`biz_` tag). With read access to the account this lists
              all of its memberships; without, only the caller's own memberships in it.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only memberships created after this ISO 8601 timestamp.

          created_before: Only memberships created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of memberships to return from the start of the window.

          last: Number of memberships to return from the end of the window.

          order: Sort field.

          plan_id: Filter to memberships of this plan (`plan_` tag). Repeat as plan_ids[] for
              several.

          product_id: Filter to memberships of this product (`prod_` tag). Repeat as product_ids[] for
              several.

          status: Filter by billing state. `canceling` matches active memberships set to cancel at
              period end; `paused` matches memberships with payment collection paused.

          user_id: Narrow to one user's memberships (`user_` tag, or `me` for the caller). A user
              outside the caller's visible set returns an empty list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memberships",
            page=AsyncCursorPage[Membership],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "plan_id": plan_id,
                        "product_id": product_id,
                        "status": status,
                        "user_id": user_id,
                    },
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=Membership,
        )

    async def cancel(
        self,
        id: str,
        *,
        reason: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """Cancels a membership immediately, revoking access right away.

        To cancel at the
        end of the billing period instead, update the membership with
        `cancel_at_period_end: true`.

        Args:
          reason: Free-form note recording why the membership was canceled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/memberships/{id}/cancel", id=id),
            body=await async_maybe_transform({"reason": reason}, membership_cancel_params.MembershipCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def extend(
        self,
        id: str,
        *,
        days: int,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """
        Adds free days to a membership, extending its current billing period, expiration
        date, or trial depending on the plan type.

        Args:
          days: Number of free days to add (1-1095).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/memberships/{id}/extend", id=id),
            body=await async_maybe_transform({"days": days}, membership_extend_params.MembershipExtendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def pause(
        self,
        id: str,
        *,
        until: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """Pauses a membership's recurring payment collection.

        The customer keeps access
        but is not charged until the membership is resumed.

        Args:
          until: ISO 8601 time to automatically resume payment collection. Must be in the future;
              only supported for memberships billed by Whop.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/memberships/{id}/pause", id=id),
            body=await async_maybe_transform({"until": until}, membership_pause_params.MembershipPauseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Membership,
        )

    async def resume(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Membership:
        """Resumes a previously paused membership's recurring payment collection.

        Billing
        resumes on the next cycle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/memberships/{id}/resume", id=id),
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
        self.extend = to_raw_response_wrapper(
            memberships.extend,
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
        self.extend = async_to_raw_response_wrapper(
            memberships.extend,
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
        self.extend = to_streamed_response_wrapper(
            memberships.extend,
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
        self.extend = async_to_streamed_response_wrapper(
            memberships.extend,
        )
        self.pause = async_to_streamed_response_wrapper(
            memberships.pause,
        )
        self.resume = async_to_streamed_response_wrapper(
            memberships.resume,
        )
