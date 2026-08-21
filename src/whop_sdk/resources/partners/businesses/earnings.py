# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.partners.businesses import earning_list_params
from ....types.partners.businesses.earning_list_response import EarningListResponse

__all__ = ["EarningsResource", "AsyncEarningsResource"]


class EarningsResource(SyncAPIResource):
    """
    The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def with_raw_response(self) -> EarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return EarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return EarningsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        income_source: List[Literal["sales", "ad_spend", "transfer", "card_interchange"]] | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"] | Omit = omit,
        status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[EarningListResponse]:
        """
        Lists the earnings Whop pays out for one referred business's activity, most
        recent first.

        Args:
          created_after: Only return earnings created after this timestamp.

          created_before: Only return earnings created before this timestamp.

          direction: Sort direction.

          income_source: Filter to earnings from these income sources. Repeat the parameter for each one
              (income_source=sales&income_source=ad_spend).

          order: The field to sort earnings by.

          status: Filter by earning status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/partners/businesses/{id}/earnings", id=id),
            page=SyncCursorPage[EarningListResponse],
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
                        "income_source": income_source,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    earning_list_params.EarningListParams,
                ),
            ),
            model=EarningListResponse,
        )


class AsyncEarningsResource(AsyncAPIResource):
    """
    The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

    Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncEarningsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        income_source: List[Literal["sales", "ad_spend", "transfer", "card_interchange"]] | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "commission_amount", "transaction_amount", "payout_at"] | Omit = omit,
        status: Literal["awaiting_settlement", "pending", "completed", "canceled", "reversed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EarningListResponse, AsyncCursorPage[EarningListResponse]]:
        """
        Lists the earnings Whop pays out for one referred business's activity, most
        recent first.

        Args:
          created_after: Only return earnings created after this timestamp.

          created_before: Only return earnings created before this timestamp.

          direction: Sort direction.

          income_source: Filter to earnings from these income sources. Repeat the parameter for each one
              (income_source=sales&income_source=ad_spend).

          order: The field to sort earnings by.

          status: Filter by earning status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/partners/businesses/{id}/earnings", id=id),
            page=AsyncCursorPage[EarningListResponse],
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
                        "income_source": income_source,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    earning_list_params.EarningListParams,
                ),
            ),
            model=EarningListResponse,
        )


class EarningsResourceWithRawResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.list = to_raw_response_wrapper(
            earnings.list,
        )


class AsyncEarningsResourceWithRawResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.list = async_to_raw_response_wrapper(
            earnings.list,
        )


class EarningsResourceWithStreamingResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

        self.list = to_streamed_response_wrapper(
            earnings.list,
        )


class AsyncEarningsResourceWithStreamingResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

        self.list = async_to_streamed_response_wrapper(
            earnings.list,
        )
