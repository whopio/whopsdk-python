# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import Status, affiliate_list_params, affiliate_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .overrides import (
    OverridesResource,
    AsyncOverridesResource,
    OverridesResourceWithRawResponse,
    AsyncOverridesResourceWithRawResponse,
    OverridesResourceWithStreamingResponse,
    AsyncOverridesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.status import Status
from ...types.affiliate import Affiliate
from ...types.shared.direction import Direction
from ...types.affiliate_list_response import AffiliateListResponse
from ...types.affiliate_archive_response import AffiliateArchiveResponse
from ...types.affiliate_unarchive_response import AffiliateUnarchiveResponse

__all__ = ["AffiliatesResource", "AsyncAffiliatesResource"]


class AffiliatesResource(SyncAPIResource):
    """Affiliates"""

    @cached_property
    def overrides(self) -> OverridesResource:
        """Affiliates"""
        return OverridesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AffiliatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AffiliatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AffiliatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AffiliatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        user_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Affiliate:
        """
        Creates or finds an affiliate for a company and user.

        Required permissions:

        - `affiliate:create`

        Args:
          company_id: The ID of the company to create the affiliate for.

          user_identifier: The user identifier (username, email, user ID, or Discord ID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/affiliates",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "user_identifier": user_identifier,
                },
                affiliate_create_params.AffiliateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Affiliate,
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
    ) -> Affiliate:
        """
        Retrieves the details of an existing affiliate.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/affiliates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Affiliate,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "cached_total_referrals", "cached_total_rewards"]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[Status] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AffiliateListResponse]:
        """
        Returns a paginated list of affiliates for the actor in context, with optional
        filtering by status, search, and sorting.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          company_id: The unique identifier of the company to list affiliates for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          query: Search affiliates by username.

          status: Statuses for resources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/affiliates",
            page=SyncCursorPage[AffiliateListResponse],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "query": query,
                        "status": status,
                    },
                    affiliate_list_params.AffiliateListParams,
                ),
            ),
            model=AffiliateListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AffiliateArchiveResponse:
        """
        Archives an existing Affiliate

        Required permissions:

        - `affiliate:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/affiliates/{id}/archive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AffiliateArchiveResponse,
        )

    def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AffiliateUnarchiveResponse:
        """
        Unarchives an existing Affiliate

        Required permissions:

        - `affiliate:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/affiliates/{id}/unarchive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AffiliateUnarchiveResponse,
        )


class AsyncAffiliatesResource(AsyncAPIResource):
    """Affiliates"""

    @cached_property
    def overrides(self) -> AsyncOverridesResource:
        """Affiliates"""
        return AsyncOverridesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAffiliatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAffiliatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAffiliatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAffiliatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        user_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Affiliate:
        """
        Creates or finds an affiliate for a company and user.

        Required permissions:

        - `affiliate:create`

        Args:
          company_id: The ID of the company to create the affiliate for.

          user_identifier: The user identifier (username, email, user ID, or Discord ID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/affiliates",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "user_identifier": user_identifier,
                },
                affiliate_create_params.AffiliateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Affiliate,
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
    ) -> Affiliate:
        """
        Retrieves the details of an existing affiliate.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/affiliates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Affiliate,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "cached_total_referrals", "cached_total_rewards"]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[Status] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AffiliateListResponse, AsyncCursorPage[AffiliateListResponse]]:
        """
        Returns a paginated list of affiliates for the actor in context, with optional
        filtering by status, search, and sorting.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          company_id: The unique identifier of the company to list affiliates for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          query: Search affiliates by username.

          status: Statuses for resources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/affiliates",
            page=AsyncCursorPage[AffiliateListResponse],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "query": query,
                        "status": status,
                    },
                    affiliate_list_params.AffiliateListParams,
                ),
            ),
            model=AffiliateListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AffiliateArchiveResponse:
        """
        Archives an existing Affiliate

        Required permissions:

        - `affiliate:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/affiliates/{id}/archive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AffiliateArchiveResponse,
        )

    async def unarchive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AffiliateUnarchiveResponse:
        """
        Unarchives an existing Affiliate

        Required permissions:

        - `affiliate:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/affiliates/{id}/unarchive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AffiliateUnarchiveResponse,
        )


class AffiliatesResourceWithRawResponse:
    def __init__(self, affiliates: AffiliatesResource) -> None:
        self._affiliates = affiliates

        self.create = to_raw_response_wrapper(
            affiliates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            affiliates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            affiliates.list,
        )
        self.archive = to_raw_response_wrapper(
            affiliates.archive,
        )
        self.unarchive = to_raw_response_wrapper(
            affiliates.unarchive,
        )

    @cached_property
    def overrides(self) -> OverridesResourceWithRawResponse:
        """Affiliates"""
        return OverridesResourceWithRawResponse(self._affiliates.overrides)


class AsyncAffiliatesResourceWithRawResponse:
    def __init__(self, affiliates: AsyncAffiliatesResource) -> None:
        self._affiliates = affiliates

        self.create = async_to_raw_response_wrapper(
            affiliates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            affiliates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            affiliates.list,
        )
        self.archive = async_to_raw_response_wrapper(
            affiliates.archive,
        )
        self.unarchive = async_to_raw_response_wrapper(
            affiliates.unarchive,
        )

    @cached_property
    def overrides(self) -> AsyncOverridesResourceWithRawResponse:
        """Affiliates"""
        return AsyncOverridesResourceWithRawResponse(self._affiliates.overrides)


class AffiliatesResourceWithStreamingResponse:
    def __init__(self, affiliates: AffiliatesResource) -> None:
        self._affiliates = affiliates

        self.create = to_streamed_response_wrapper(
            affiliates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            affiliates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            affiliates.list,
        )
        self.archive = to_streamed_response_wrapper(
            affiliates.archive,
        )
        self.unarchive = to_streamed_response_wrapper(
            affiliates.unarchive,
        )

    @cached_property
    def overrides(self) -> OverridesResourceWithStreamingResponse:
        """Affiliates"""
        return OverridesResourceWithStreamingResponse(self._affiliates.overrides)


class AsyncAffiliatesResourceWithStreamingResponse:
    def __init__(self, affiliates: AsyncAffiliatesResource) -> None:
        self._affiliates = affiliates

        self.create = async_to_streamed_response_wrapper(
            affiliates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            affiliates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            affiliates.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            affiliates.archive,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            affiliates.unarchive,
        )

    @cached_property
    def overrides(self) -> AsyncOverridesResourceWithStreamingResponse:
        """Affiliates"""
        return AsyncOverridesResourceWithStreamingResponse(self._affiliates.overrides)
