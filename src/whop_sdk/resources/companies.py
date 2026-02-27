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

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    """Companies"""

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
        title: str,
        description: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        logo: Optional[company_create_params.Logo] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """Create a new company.

        Pass parent_company_id to create a connected account under
        a platform, or omit it to create a company for the current user.

        Required permissions:

        - `company:create`
        - `company:basic:read`

        Args:
          title: The display name of the company shown to customers.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          email: The email address of the user who will own the connected account. Required when
              parent_company_id is provided.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          metadata: A key-value JSON object of custom metadata to store on the company.

          parent_company_id: The unique identifier of the parent platform company. When provided, creates a
              connected account under that platform. Omit to create a company for the current
              user.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Only applies when creating a connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/companies",
            body=maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "email": email,
                    "logo": logo,
                    "metadata": metadata,
                    "parent_company_id": parent_company_id,
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
        Retrieves the details of an existing company.

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
        description: Optional[str] | Omit = omit,
        logo: Optional[company_update_params.Logo] | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Update a company's title, description, logo, and other settings.

        Required permissions:

        - `company:update`
        - `company:basic:read`

        Args:
          banner_image: The company's banner image. Accepts PNG or JPEG format.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          route: The unique URL slug for the company's store page. Must be lowercase and can
              include hyphens (e.g., 'my-company'). If not provided, the route will remain
              unchanged.

          send_customer_emails: Whether Whop sends transactional emails (receipts, renewals, cancelations) to
              customers on behalf of this company.

          target_audience: The target audience for this company (e.g., 'beginner day traders aged 18-25
              looking to learn options').

          title: The display name of the company shown to customers.

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
                    "description": description,
                    "logo": logo,
                    "route": route,
                    "send_customer_emails": send_customer_emails,
                    "target_audience": target_audience,
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
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CompanyListResponse]:
        """Returns a paginated list of companies.

        When parent_company_id is provided, lists
        connected accounts under that platform. When omitted, lists companies the
        current user has access to.

        Required permissions:

        - `company:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return companies created after this timestamp.

          created_before: Only return companies created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          parent_company_id: The unique identifier of the parent platform company. When provided, lists
              connected accounts under that platform. Omit to list the current user's own
              companies.

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
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "parent_company_id": parent_company_id,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    """Companies"""

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
        title: str,
        description: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        logo: Optional[company_create_params.Logo] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """Create a new company.

        Pass parent_company_id to create a connected account under
        a platform, or omit it to create a company for the current user.

        Required permissions:

        - `company:create`
        - `company:basic:read`

        Args:
          title: The display name of the company shown to customers.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          email: The email address of the user who will own the connected account. Required when
              parent_company_id is provided.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          metadata: A key-value JSON object of custom metadata to store on the company.

          parent_company_id: The unique identifier of the parent platform company. When provided, creates a
              connected account under that platform. Omit to create a company for the current
              user.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this company.
              Only applies when creating a connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/companies",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "email": email,
                    "logo": logo,
                    "metadata": metadata,
                    "parent_company_id": parent_company_id,
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
        Retrieves the details of an existing company.

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
        description: Optional[str] | Omit = omit,
        logo: Optional[company_update_params.Logo] | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_customer_emails: Optional[bool] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Company:
        """
        Update a company's title, description, logo, and other settings.

        Required permissions:

        - `company:update`
        - `company:basic:read`

        Args:
          banner_image: The company's banner image. Accepts PNG or JPEG format.

          description: A promotional pitch displayed to potential customers on the company's store
              page.

          logo: The company's logo image. Accepts PNG, JPEG, or GIF format.

          route: The unique URL slug for the company's store page. Must be lowercase and can
              include hyphens (e.g., 'my-company'). If not provided, the route will remain
              unchanged.

          send_customer_emails: Whether Whop sends transactional emails (receipts, renewals, cancelations) to
              customers on behalf of this company.

          target_audience: The target audience for this company (e.g., 'beginner day traders aged 18-25
              looking to learn options').

          title: The display name of the company shown to customers.

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
                    "description": description,
                    "logo": logo,
                    "route": route,
                    "send_customer_emails": send_customer_emails,
                    "target_audience": target_audience,
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
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        parent_company_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompanyListResponse, AsyncCursorPage[CompanyListResponse]]:
        """Returns a paginated list of companies.

        When parent_company_id is provided, lists
        connected accounts under that platform. When omitted, lists companies the
        current user has access to.

        Required permissions:

        - `company:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return companies created after this timestamp.

          created_before: Only return companies created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          parent_company_id: The unique identifier of the parent platform company. When provided, lists
              connected accounts under that platform. Omit to list the current user's own
              companies.

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
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "parent_company_id": parent_company_id,
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
