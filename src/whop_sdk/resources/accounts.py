# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import account_list_params, account_create_params, account_update_params
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
from .._base_client import make_request_options
from ..types.account import Account
from ..types.account_list_response import AccountListResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Creates an account.

        User tokens create business accounts; business account API
        keys create connected accounts.

        Args:
          email: The email address of the account owner. Required for business account API key
              requests.

          metadata: Arbitrary key/value metadata to store on the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "email": email,
                    "metadata": metadata,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves a single account visible to the credential, including its crypto
        wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def update(
        self,
        account_id: str,
        *,
        affiliate_application_required: bool | Omit = omit,
        affiliate_instructions: Optional[str] | Omit = omit,
        banner_image: Optional[Dict[str, object]] | Omit = omit,
        business_type: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        featured_affiliate_product_id: Optional[str] | Omit = omit,
        industry_group: Optional[str] | Omit = omit,
        industry_type: Optional[str] | Omit = omit,
        logo: Optional[Dict[str, object]] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_customer_emails: bool | Omit = omit,
        social_links: Iterable[Dict[str, object]] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Updates an account.

        User tokens can update business accounts; business account
        API keys can update connected accounts.

        Args:
          affiliate_application_required: Whether prospective affiliates must submit an application before promoting this
              account.

          affiliate_instructions: Guidelines shown to affiliates promoting this account.

          banner_image: Attachment input for the account banner image.

          business_type: The high-level business category for the account.

          description: A promotional description for the account.

          featured_affiliate_product_id: The ID of the product to feature for affiliates. Pass null to clear.

          industry_group: The industry group the account belongs to.

          industry_type: The specific industry vertical the account operates in.

          logo: Attachment input for the account logo.

          metadata: Arbitrary key/value metadata to store on the account.

          route: The unique URL slug for the account.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this account.

          social_links: The full list of social links to display for the account.

          target_audience: The target audience for this account.

          title: The display name of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=maybe_transform(
                {
                    "affiliate_application_required": affiliate_application_required,
                    "affiliate_instructions": affiliate_instructions,
                    "banner_image": banner_image,
                    "business_type": business_type,
                    "description": description,
                    "featured_affiliate_product_id": featured_affiliate_product_id,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "logo": logo,
                    "metadata": metadata,
                    "route": route,
                    "send_customer_emails": send_customer_emails,
                    "social_links": social_links,
                    "target_audience": target_audience,
                    "title": title,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListResponse:
        """Lists accounts visible to the credential.

        User tokens return the user's business
        accounts; business account API keys return the requesting business account and
        its connected accounts.

        Args:
          page: The page number to retrieve

          per: The number of resources to return per page. There is a limit of 50 results per
              page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per": per,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves the business account associated with the current business account API
        key.
        """
        return self._get(
            "/accounts/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Creates an account.

        User tokens create business accounts; business account API
        keys create connected accounts.

        Args:
          email: The email address of the account owner. Required for business account API key
              requests.

          metadata: Arbitrary key/value metadata to store on the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "metadata": metadata,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves a single account visible to the credential, including its crypto
        wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def update(
        self,
        account_id: str,
        *,
        affiliate_application_required: bool | Omit = omit,
        affiliate_instructions: Optional[str] | Omit = omit,
        banner_image: Optional[Dict[str, object]] | Omit = omit,
        business_type: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        featured_affiliate_product_id: Optional[str] | Omit = omit,
        industry_group: Optional[str] | Omit = omit,
        industry_type: Optional[str] | Omit = omit,
        logo: Optional[Dict[str, object]] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_customer_emails: bool | Omit = omit,
        social_links: Iterable[Dict[str, object]] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Updates an account.

        User tokens can update business accounts; business account
        API keys can update connected accounts.

        Args:
          affiliate_application_required: Whether prospective affiliates must submit an application before promoting this
              account.

          affiliate_instructions: Guidelines shown to affiliates promoting this account.

          banner_image: Attachment input for the account banner image.

          business_type: The high-level business category for the account.

          description: A promotional description for the account.

          featured_affiliate_product_id: The ID of the product to feature for affiliates. Pass null to clear.

          industry_group: The industry group the account belongs to.

          industry_type: The specific industry vertical the account operates in.

          logo: Attachment input for the account logo.

          metadata: Arbitrary key/value metadata to store on the account.

          route: The unique URL slug for the account.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this account.

          social_links: The full list of social links to display for the account.

          target_audience: The target audience for this account.

          title: The display name of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "affiliate_application_required": affiliate_application_required,
                    "affiliate_instructions": affiliate_instructions,
                    "banner_image": banner_image,
                    "business_type": business_type,
                    "description": description,
                    "featured_affiliate_product_id": featured_affiliate_product_id,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "logo": logo,
                    "metadata": metadata,
                    "route": route,
                    "send_customer_emails": send_customer_emails,
                    "social_links": social_links,
                    "target_audience": target_audience,
                    "title": title,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        per: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListResponse:
        """Lists accounts visible to the credential.

        User tokens return the user's business
        accounts; business account API keys return the requesting business account and
        its connected accounts.

        Args:
          page: The page number to retrieve

          per: The number of resources to return per page. There is a limit of 50 results per
              page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per": per,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves the business account associated with the current business account API
        key.
        """
        return await self._get(
            "/accounts/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.me = to_raw_response_wrapper(
            accounts.me,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.me = async_to_raw_response_wrapper(
            accounts.me,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.me = to_streamed_response_wrapper(
            accounts.me,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.me = async_to_streamed_response_wrapper(
            accounts.me,
        )
