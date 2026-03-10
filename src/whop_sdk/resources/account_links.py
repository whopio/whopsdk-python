# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import account_link_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.account_link_create_response import AccountLinkCreateResponse

__all__ = ["AccountLinksResource", "AsyncAccountLinksResource"]


class AccountLinksResource(SyncAPIResource):
    """Account links"""

    @cached_property
    def with_raw_response(self) -> AccountLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AccountLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        refresh_url: str,
        return_url: str,
        use_case: Literal["account_onboarding", "payouts_portal"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountLinkCreateResponse:
        """
        Generate a URL that directs a sub-merchant to their account portal, such as the
        hosted payouts dashboard or the KYC onboarding flow.

        Args:
          company_id: The unique identifier of the company to generate the link for, starting with
              'biz\\__'. Must be a sub-merchant of the API key's company.

          refresh_url: The URL to redirect the user to if the session expires and needs to be
              re-authenticated, such as 'https://example.com/refresh'.

          return_url: The URL to redirect the user to when they want to return to your site, such as
              'https://example.com/return'.

          use_case: The purpose of the account link, such as hosted payouts portal or hosted KYC
              onboarding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/account_links",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "refresh_url": refresh_url,
                    "return_url": return_url,
                    "use_case": use_case,
                },
                account_link_create_params.AccountLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountLinkCreateResponse,
        )


class AsyncAccountLinksResource(AsyncAPIResource):
    """Account links"""

    @cached_property
    def with_raw_response(self) -> AsyncAccountLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAccountLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        refresh_url: str,
        return_url: str,
        use_case: Literal["account_onboarding", "payouts_portal"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountLinkCreateResponse:
        """
        Generate a URL that directs a sub-merchant to their account portal, such as the
        hosted payouts dashboard or the KYC onboarding flow.

        Args:
          company_id: The unique identifier of the company to generate the link for, starting with
              'biz\\__'. Must be a sub-merchant of the API key's company.

          refresh_url: The URL to redirect the user to if the session expires and needs to be
              re-authenticated, such as 'https://example.com/refresh'.

          return_url: The URL to redirect the user to when they want to return to your site, such as
              'https://example.com/return'.

          use_case: The purpose of the account link, such as hosted payouts portal or hosted KYC
              onboarding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/account_links",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "refresh_url": refresh_url,
                    "return_url": return_url,
                    "use_case": use_case,
                },
                account_link_create_params.AccountLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountLinkCreateResponse,
        )


class AccountLinksResourceWithRawResponse:
    def __init__(self, account_links: AccountLinksResource) -> None:
        self._account_links = account_links

        self.create = to_raw_response_wrapper(
            account_links.create,
        )


class AsyncAccountLinksResourceWithRawResponse:
    def __init__(self, account_links: AsyncAccountLinksResource) -> None:
        self._account_links = account_links

        self.create = async_to_raw_response_wrapper(
            account_links.create,
        )


class AccountLinksResourceWithStreamingResponse:
    def __init__(self, account_links: AccountLinksResource) -> None:
        self._account_links = account_links

        self.create = to_streamed_response_wrapper(
            account_links.create,
        )


class AsyncAccountLinksResourceWithStreamingResponse:
    def __init__(self, account_links: AsyncAccountLinksResource) -> None:
        self._account_links = account_links

        self.create = async_to_streamed_response_wrapper(
            account_links.create,
        )
