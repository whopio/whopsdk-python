# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from ..types import lead_list_params, lead_create_params, lead_update_params
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
from ..types.lead import Lead
from .._base_client import AsyncPaginator, make_request_options
from ..types.lead_list_response import LeadListResponse

__all__ = ["LeadsResource", "AsyncLeadsResource"]


class LeadsResource(SyncAPIResource):
    """Leads"""

    @cached_property
    def with_raw_response(self) -> LeadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return LeadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return LeadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        referrer: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lead:
        """
        Record a new lead for a company, capturing a potential customer's interest in a
        specific product.

        Required permissions:

        - `lead:manage`
        - `member:email:read`
        - `access_pass:basic:read`
        - `member:basic:read`

        Args:
          company_id: The unique identifier of the company to create the lead for, starting with
              'biz\\__'.

          metadata: A JSON object of custom metadata to attach to the lead for tracking purposes.

          product_id: The unique identifier of the product the lead is interested in, starting with
              'prod\\__'.

          referrer: The referral URL that brought the lead to the company, such as
              'https://example.com/landing'.

          user_id: The unique identifier of the user to record as the lead. If authenticated as a
              user, that user is used automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/leads",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "metadata": metadata,
                    "product_id": product_id,
                    "referrer": referrer,
                    "user_id": user_id,
                },
                lead_create_params.LeadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lead,
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
    ) -> Lead:
        """
        Retrieves the details of an existing lead.

        Required permissions:

        - `lead:basic:read`
        - `member:email:read`
        - `access_pass:basic:read`
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
            f"/leads/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lead,
        )

    def update(
        self,
        id: str,
        *,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        referrer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lead:
        """
        Update the metadata or referrer information on an existing lead record.

        Required permissions:

        - `lead:manage`
        - `member:email:read`
        - `access_pass:basic:read`
        - `member:basic:read`

        Args:
          metadata: A JSON object of custom metadata to set on the lead, replacing any existing
              metadata.

          referrer: The updated referral URL for the lead, such as 'https://example.com/landing'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/leads/{id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "referrer": referrer,
                },
                lead_update_params.LeadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lead,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[LeadListResponse]:
        """
        Returns a paginated list of leads for a company, with optional filtering by
        product and creation date.

        Required permissions:

        - `lead:basic:read`
        - `member:email:read`
        - `access_pass:basic:read`
        - `member:basic:read`

        Args:
          company_id: The unique identifier of the company to list leads for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return leads created after this timestamp.

          created_before: Only return leads created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_ids: Filter leads to only those associated with these specific product identifiers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/leads",
            page=SyncCursorPage[LeadListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "product_ids": product_ids,
                    },
                    lead_list_params.LeadListParams,
                ),
            ),
            model=LeadListResponse,
        )


class AsyncLeadsResource(AsyncAPIResource):
    """Leads"""

    @cached_property
    def with_raw_response(self) -> AsyncLeadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncLeadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        referrer: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lead:
        """
        Record a new lead for a company, capturing a potential customer's interest in a
        specific product.

        Required permissions:

        - `lead:manage`
        - `member:email:read`
        - `access_pass:basic:read`
        - `member:basic:read`

        Args:
          company_id: The unique identifier of the company to create the lead for, starting with
              'biz\\__'.

          metadata: A JSON object of custom metadata to attach to the lead for tracking purposes.

          product_id: The unique identifier of the product the lead is interested in, starting with
              'prod\\__'.

          referrer: The referral URL that brought the lead to the company, such as
              'https://example.com/landing'.

          user_id: The unique identifier of the user to record as the lead. If authenticated as a
              user, that user is used automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/leads",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "metadata": metadata,
                    "product_id": product_id,
                    "referrer": referrer,
                    "user_id": user_id,
                },
                lead_create_params.LeadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lead,
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
    ) -> Lead:
        """
        Retrieves the details of an existing lead.

        Required permissions:

        - `lead:basic:read`
        - `member:email:read`
        - `access_pass:basic:read`
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
            f"/leads/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lead,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        referrer: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Lead:
        """
        Update the metadata or referrer information on an existing lead record.

        Required permissions:

        - `lead:manage`
        - `member:email:read`
        - `access_pass:basic:read`
        - `member:basic:read`

        Args:
          metadata: A JSON object of custom metadata to set on the lead, replacing any existing
              metadata.

          referrer: The updated referral URL for the lead, such as 'https://example.com/landing'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/leads/{id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "referrer": referrer,
                },
                lead_update_params.LeadUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Lead,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LeadListResponse, AsyncCursorPage[LeadListResponse]]:
        """
        Returns a paginated list of leads for a company, with optional filtering by
        product and creation date.

        Required permissions:

        - `lead:basic:read`
        - `member:email:read`
        - `access_pass:basic:read`
        - `member:basic:read`

        Args:
          company_id: The unique identifier of the company to list leads for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return leads created after this timestamp.

          created_before: Only return leads created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_ids: Filter leads to only those associated with these specific product identifiers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/leads",
            page=AsyncCursorPage[LeadListResponse],
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
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "product_ids": product_ids,
                    },
                    lead_list_params.LeadListParams,
                ),
            ),
            model=LeadListResponse,
        )


class LeadsResourceWithRawResponse:
    def __init__(self, leads: LeadsResource) -> None:
        self._leads = leads

        self.create = to_raw_response_wrapper(
            leads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            leads.retrieve,
        )
        self.update = to_raw_response_wrapper(
            leads.update,
        )
        self.list = to_raw_response_wrapper(
            leads.list,
        )


class AsyncLeadsResourceWithRawResponse:
    def __init__(self, leads: AsyncLeadsResource) -> None:
        self._leads = leads

        self.create = async_to_raw_response_wrapper(
            leads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            leads.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            leads.update,
        )
        self.list = async_to_raw_response_wrapper(
            leads.list,
        )


class LeadsResourceWithStreamingResponse:
    def __init__(self, leads: LeadsResource) -> None:
        self._leads = leads

        self.create = to_streamed_response_wrapper(
            leads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            leads.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            leads.update,
        )
        self.list = to_streamed_response_wrapper(
            leads.list,
        )


class AsyncLeadsResourceWithStreamingResponse:
    def __init__(self, leads: AsyncLeadsResource) -> None:
        self._leads = leads

        self.create = async_to_streamed_response_wrapper(
            leads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            leads.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            leads.update,
        )
        self.list = async_to_streamed_response_wrapper(
            leads.list,
        )
