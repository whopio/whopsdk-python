# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from ..types import company_list_params, company_create_params, company_update_params
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
from ..types.shared.company import Company
from ..types.shared.direction import Direction
from ..types.company_list_response import CompanyListResponse
from ..types.shared.business_types import BusinessTypes
from ..types.shared.industry_types import IndustryTypes

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        parent_company_id: str,
        title: str,
        business_type: Optional[BusinessTypes] | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Create a new connected account for your platform

        Required permissions:

        - `company:create_child`
        - `company:basic:read`

        Args:
          email: The email of the user who the company will belong to.

          parent_company_id: The company ID of the platform creating this company.

          title: The name of the company being created.

          business_type: The different business types a company can be.

          industry_type: The different industry types a company can be in.

          metadata: Additional metadata for the account

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Includes: order confirmations, payment failures, refund notifications, upcoming
              renewals, and membership cancelations/expirations. When disabled, the platform
              is responsible for handling these communications. This is defaulted to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/companies",
            body=maybe_transform(
                {
                    "email": email,
                    "parent_company_id": parent_company_id,
                    "title": title,
                    "business_type": business_type,
                    "industry_type": industry_type,
                    "metadata": metadata,
                    "send_customer_emails": send_customer_emails,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
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
    ) -> Company:
        """
        Retrieves an company by ID or its url route

        Required permissions:

        - `company:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def update(
        self,
        id: str,
        *,
        banner_image: Optional[company_update_params.BannerImage] | Omit = omit,
        business_type: Optional[BusinessTypes] | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        logo: Optional[company_update_params.Logo] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """Update an existing company.

        Either a regular company, platform company, or one
        of a platform's connected accounts

        Required permissions:

        - `company:update`
        - `company:basic:read`

        Args:
          banner_image: The banner image for the company in png or jpeg format

          business_type: The different business types a company can be.

          industry_type: The different industry types a company can be in.

          logo: The logo for the company in png, jpeg, or gif format

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Includes: order confirmations, payment failures, refund notifications, upcoming
              renewals, and membership cancelations/expirations. When disabled, the platform
              is responsible for handling these communications.

          title: The title of the company

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/companies/{id}",
            body=maybe_transform(
                {
                    "banner_image": banner_image,
                    "business_type": business_type,
                    "industry_type": industry_type,
                    "logo": logo,
                    "send_customer_emails": send_customer_emails,
                    "title": title,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def list(
        self,
        *,
        parent_company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CompanyListResponse]:
        """
        Lists companies the current user has access to

        Required permissions:

        - `company:basic:read`

        Args:
          parent_company_id: The ID of the parent company to list connected accounts for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/companies",
            page=SyncCursorPage[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "parent_company_id": parent_company_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        parent_company_id: str,
        title: str,
        business_type: Optional[BusinessTypes] | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Create a new connected account for your platform

        Required permissions:

        - `company:create_child`
        - `company:basic:read`

        Args:
          email: The email of the user who the company will belong to.

          parent_company_id: The company ID of the platform creating this company.

          title: The name of the company being created.

          business_type: The different business types a company can be.

          industry_type: The different industry types a company can be in.

          metadata: Additional metadata for the account

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Includes: order confirmations, payment failures, refund notifications, upcoming
              renewals, and membership cancelations/expirations. When disabled, the platform
              is responsible for handling these communications. This is defaulted to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/companies",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "parent_company_id": parent_company_id,
                    "title": title,
                    "business_type": business_type,
                    "industry_type": industry_type,
                    "metadata": metadata,
                    "send_customer_emails": send_customer_emails,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
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
    ) -> Company:
        """
        Retrieves an company by ID or its url route

        Required permissions:

        - `company:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/companies/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    async def update(
        self,
        id: str,
        *,
        banner_image: Optional[company_update_params.BannerImage] | Omit = omit,
        business_type: Optional[BusinessTypes] | Omit = omit,
        industry_type: Optional[IndustryTypes] | Omit = omit,
        logo: Optional[company_update_params.Logo] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """Update an existing company.

        Either a regular company, platform company, or one
        of a platform's connected accounts

        Required permissions:

        - `company:update`
        - `company:basic:read`

        Args:
          banner_image: The banner image for the company in png or jpeg format

          business_type: The different business types a company can be.

          industry_type: The different industry types a company can be in.

          logo: The logo for the company in png, jpeg, or gif format

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Includes: order confirmations, payment failures, refund notifications, upcoming
              renewals, and membership cancelations/expirations. When disabled, the platform
              is responsible for handling these communications.

          title: The title of the company

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/companies/{id}",
            body=await async_maybe_transform(
                {
                    "banner_image": banner_image,
                    "business_type": business_type,
                    "industry_type": industry_type,
                    "logo": logo,
                    "send_customer_emails": send_customer_emails,
                    "title": title,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )

    def list(
        self,
        *,
        parent_company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompanyListResponse, AsyncCursorPage[CompanyListResponse]]:
        """
        Lists companies the current user has access to

        Required permissions:

        - `company:basic:read`

        Args:
          parent_company_id: The ID of the parent company to list connected accounts for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/companies",
            page=AsyncCursorPage[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "parent_company_id": parent_company_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
