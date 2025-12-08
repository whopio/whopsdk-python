# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import FeeMarkupType, fee_markup_list_params, fee_markup_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.fee_markup_type import FeeMarkupType
from ..types.fee_markup_list_response import FeeMarkupListResponse
from ..types.fee_markup_create_response import FeeMarkupCreateResponse
from ..types.fee_markup_delete_response import FeeMarkupDeleteResponse

__all__ = ["FeeMarkupsResource", "AsyncFeeMarkupsResource"]


class FeeMarkupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeeMarkupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return FeeMarkupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeeMarkupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return FeeMarkupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        fee_type: FeeMarkupType,
        fixed_fee_usd: Optional[float] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        percentage_fee: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeeMarkupCreateResponse:
        """
        Creates or updates a fee markup for a company.

        Required permissions:

        - `company:update_child_fees`

        Args:
          company_id: The ID (tag) of the company you want to update the fee markup for.

          fee_type: The type of fee this markup applies to.

          fixed_fee_usd: The fixed fee in USD to charge (0-50).

          metadata: Custom metadata to attach to this fee markup.

          notes: Internal notes about this fee markup.

          percentage_fee: The percentage fee to charge (0-25).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fee_markups",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "fee_type": fee_type,
                    "fixed_fee_usd": fixed_fee_usd,
                    "metadata": metadata,
                    "notes": notes,
                    "percentage_fee": percentage_fee,
                },
                fee_markup_create_params.FeeMarkupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeeMarkupCreateResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[FeeMarkupListResponse]:
        """
        Lists fee markups for a company.

        Required permissions:

        - `company:update_child_fees`

        Args:
          company_id: The ID (tag) of the company you want to list the fee markups for. If you pass
              your platform account, you will get the platform default markups.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fee_markups",
            page=SyncCursorPage[FeeMarkupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    fee_markup_list_params.FeeMarkupListParams,
                ),
            ),
            model=FeeMarkupListResponse,
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
    ) -> FeeMarkupDeleteResponse:
        """
        Deletes a fee markup for a company.

        Required permissions:

        - `company:update_child_fees`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/fee_markups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeeMarkupDeleteResponse,
        )


class AsyncFeeMarkupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeeMarkupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeeMarkupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeeMarkupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncFeeMarkupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        fee_type: FeeMarkupType,
        fixed_fee_usd: Optional[float] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        percentage_fee: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeeMarkupCreateResponse:
        """
        Creates or updates a fee markup for a company.

        Required permissions:

        - `company:update_child_fees`

        Args:
          company_id: The ID (tag) of the company you want to update the fee markup for.

          fee_type: The type of fee this markup applies to.

          fixed_fee_usd: The fixed fee in USD to charge (0-50).

          metadata: Custom metadata to attach to this fee markup.

          notes: Internal notes about this fee markup.

          percentage_fee: The percentage fee to charge (0-25).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fee_markups",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "fee_type": fee_type,
                    "fixed_fee_usd": fixed_fee_usd,
                    "metadata": metadata,
                    "notes": notes,
                    "percentage_fee": percentage_fee,
                },
                fee_markup_create_params.FeeMarkupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeeMarkupCreateResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FeeMarkupListResponse, AsyncCursorPage[FeeMarkupListResponse]]:
        """
        Lists fee markups for a company.

        Required permissions:

        - `company:update_child_fees`

        Args:
          company_id: The ID (tag) of the company you want to list the fee markups for. If you pass
              your platform account, you will get the platform default markups.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fee_markups",
            page=AsyncCursorPage[FeeMarkupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    fee_markup_list_params.FeeMarkupListParams,
                ),
            ),
            model=FeeMarkupListResponse,
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
    ) -> FeeMarkupDeleteResponse:
        """
        Deletes a fee markup for a company.

        Required permissions:

        - `company:update_child_fees`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/fee_markups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeeMarkupDeleteResponse,
        )


class FeeMarkupsResourceWithRawResponse:
    def __init__(self, fee_markups: FeeMarkupsResource) -> None:
        self._fee_markups = fee_markups

        self.create = to_raw_response_wrapper(
            fee_markups.create,
        )
        self.list = to_raw_response_wrapper(
            fee_markups.list,
        )
        self.delete = to_raw_response_wrapper(
            fee_markups.delete,
        )


class AsyncFeeMarkupsResourceWithRawResponse:
    def __init__(self, fee_markups: AsyncFeeMarkupsResource) -> None:
        self._fee_markups = fee_markups

        self.create = async_to_raw_response_wrapper(
            fee_markups.create,
        )
        self.list = async_to_raw_response_wrapper(
            fee_markups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            fee_markups.delete,
        )


class FeeMarkupsResourceWithStreamingResponse:
    def __init__(self, fee_markups: FeeMarkupsResource) -> None:
        self._fee_markups = fee_markups

        self.create = to_streamed_response_wrapper(
            fee_markups.create,
        )
        self.list = to_streamed_response_wrapper(
            fee_markups.list,
        )
        self.delete = to_streamed_response_wrapper(
            fee_markups.delete,
        )


class AsyncFeeMarkupsResourceWithStreamingResponse:
    def __init__(self, fee_markups: AsyncFeeMarkupsResource) -> None:
        self._fee_markups = fee_markups

        self.create = async_to_streamed_response_wrapper(
            fee_markups.create,
        )
        self.list = async_to_streamed_response_wrapper(
            fee_markups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            fee_markups.delete,
        )
