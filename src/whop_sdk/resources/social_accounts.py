# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    social_account_list_params,
    social_account_posts_params,
    social_account_create_params,
    social_account_delete_params,
    social_account_connect_params,
)
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.social_account import SocialAccount
from ..types.social_account_posts_response import SocialAccountPostsResponse
from ..types.social_account_delete_response import SocialAccountDeleteResponse
from ..types.social_account_connect_response import SocialAccountConnectResponse

__all__ = ["SocialAccountsResource", "AsyncSocialAccountsResource"]


class SocialAccountsResource(SyncAPIResource):
    """
    A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

    Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts.
    """

    @cached_property
    def with_raw_response(self) -> SocialAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return SocialAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return SocialAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        platform: Literal["facebook"],
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccount:
        """
        Creates or returns a Whop-managed Facebook page for an account.

        Args:
          platform: The platform to create the social account on.

          account_id: The Account (biz\\__ identifier) to create the social account for. An
              account-scoped API key may omit this to default to its own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/social_accounts",
            body=maybe_transform(
                {
                    "platform": platform,
                    "account_id": account_id,
                },
                social_account_create_params.SocialAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialAccount,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["display_order", "created_at"] | Omit = omit,
        platform: Literal["x", "instagram", "youtube", "tiktok", "facebook"] | Omit = omit,
        scopes: List[Literal["advertise"]] | Omit = omit,
        user_id: str | Omit = omit,
        verified: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[SocialAccount]:
        """
        Lists the social accounts linked to an account or user.

        Args:
          account_id: The Account that the social accounts are connected to. Provide either this or
              user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          direction: Sort direction.

          first: The number of social accounts to return.

          last: The number of social accounts to return from the end of the range.

          order: The field to sort social accounts by.

          platform: Only return social accounts for the platform that is specified.

          scopes: Only return social accounts that have these scopes.

          user_id: The User that the social accounts are connected to. Provide either this or
              account_id.

          verified: Only return social accounts that are verified on the platform.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/social_accounts",
            page=SyncCursorPage[SocialAccount],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "platform": platform,
                        "scopes": scopes,
                        "user_id": user_id,
                        "verified": verified,
                    },
                    social_account_list_params.SocialAccountListParams,
                ),
            ),
            model=SocialAccount,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccountDeleteResponse:
        """
        Disconnects a social account from an account or user without deleting the
        underlying platform account.

        Args:
          account_id: The Account that the social account is connected to. Provide either this or
              user_id.

          user_id: The User that the social account is connected to. Provide either this or
              account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/social_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    social_account_delete_params.SocialAccountDeleteParams,
                ),
            ),
            cast_to=SocialAccountDeleteResponse,
        )

    def connect(
        self,
        *,
        platform: Literal["meta_business", "tiktok"],
        account_id: str | Omit = omit,
        redirect_url: str | Omit = omit,
        scopes: List[Literal["advertise"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccountConnectResponse:
        """
        Starts an OAuth connection flow and returns an authorize_url where the user can
        connect a social account.

        Args:
          platform: The platform to connect the social account on. Supported options are
              `meta_business` and `tiktok`.

          account_id: The Account (biz\\__ identifier) to connect the social account for. An
              account-scoped API key may omit this to default to its own account.

          redirect_url: The Whop URL to redirect the user to after they finish connecting.

          scopes: Capabilities to grant for the connected social account. Use `advertise` when
              connecting a Meta Business or TikTok account for ads.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/social_accounts/connect",
            body=maybe_transform(
                {
                    "platform": platform,
                    "account_id": account_id,
                    "redirect_url": redirect_url,
                    "scopes": scopes,
                },
                social_account_connect_params.SocialAccountConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialAccountConnectResponse,
        )

    def posts(
        self,
        id: str,
        *,
        account_id: str,
        after: str | Omit = omit,
        first: int | Omit = omit,
        post_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccountPostsResponse:
        """
        Lists the existing posts of a connected Facebook page or Instagram account.

        Args:
          account_id: The Account (a biz\\__ identifier) the social account is connected to.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          first: The number of posts to return.

          post_id: Return only the single post with this platform id, instead of the full list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/social_accounts/{id}/posts", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "first": first,
                        "post_id": post_id,
                    },
                    social_account_posts_params.SocialAccountPostsParams,
                ),
            ),
            cast_to=SocialAccountPostsResponse,
        )


class AsyncSocialAccountsResource(AsyncAPIResource):
    """
    A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

    Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSocialAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncSocialAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        platform: Literal["facebook"],
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccount:
        """
        Creates or returns a Whop-managed Facebook page for an account.

        Args:
          platform: The platform to create the social account on.

          account_id: The Account (biz\\__ identifier) to create the social account for. An
              account-scoped API key may omit this to default to its own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/social_accounts",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "account_id": account_id,
                },
                social_account_create_params.SocialAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialAccount,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["display_order", "created_at"] | Omit = omit,
        platform: Literal["x", "instagram", "youtube", "tiktok", "facebook"] | Omit = omit,
        scopes: List[Literal["advertise"]] | Omit = omit,
        user_id: str | Omit = omit,
        verified: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SocialAccount, AsyncCursorPage[SocialAccount]]:
        """
        Lists the social accounts linked to an account or user.

        Args:
          account_id: The Account that the social accounts are connected to. Provide either this or
              user_id.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          before: Cursor to fetch the page before (from page_info.start_cursor).

          direction: Sort direction.

          first: The number of social accounts to return.

          last: The number of social accounts to return from the end of the range.

          order: The field to sort social accounts by.

          platform: Only return social accounts for the platform that is specified.

          scopes: Only return social accounts that have these scopes.

          user_id: The User that the social accounts are connected to. Provide either this or
              account_id.

          verified: Only return social accounts that are verified on the platform.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/social_accounts",
            page=AsyncCursorPage[SocialAccount],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "platform": platform,
                        "scopes": scopes,
                        "user_id": user_id,
                        "verified": verified,
                    },
                    social_account_list_params.SocialAccountListParams,
                ),
            ),
            model=SocialAccount,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccountDeleteResponse:
        """
        Disconnects a social account from an account or user without deleting the
        underlying platform account.

        Args:
          account_id: The Account that the social account is connected to. Provide either this or
              user_id.

          user_id: The User that the social account is connected to. Provide either this or
              account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/social_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    social_account_delete_params.SocialAccountDeleteParams,
                ),
            ),
            cast_to=SocialAccountDeleteResponse,
        )

    async def connect(
        self,
        *,
        platform: Literal["meta_business", "tiktok"],
        account_id: str | Omit = omit,
        redirect_url: str | Omit = omit,
        scopes: List[Literal["advertise"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccountConnectResponse:
        """
        Starts an OAuth connection flow and returns an authorize_url where the user can
        connect a social account.

        Args:
          platform: The platform to connect the social account on. Supported options are
              `meta_business` and `tiktok`.

          account_id: The Account (biz\\__ identifier) to connect the social account for. An
              account-scoped API key may omit this to default to its own account.

          redirect_url: The Whop URL to redirect the user to after they finish connecting.

          scopes: Capabilities to grant for the connected social account. Use `advertise` when
              connecting a Meta Business or TikTok account for ads.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/social_accounts/connect",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "account_id": account_id,
                    "redirect_url": redirect_url,
                    "scopes": scopes,
                },
                social_account_connect_params.SocialAccountConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialAccountConnectResponse,
        )

    async def posts(
        self,
        id: str,
        *,
        account_id: str,
        after: str | Omit = omit,
        first: int | Omit = omit,
        post_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialAccountPostsResponse:
        """
        Lists the existing posts of a connected Facebook page or Instagram account.

        Args:
          account_id: The Account (a biz\\__ identifier) the social account is connected to.

          after: Cursor to fetch the page after (from page_info.end_cursor).

          first: The number of posts to return.

          post_id: Return only the single post with this platform id, instead of the full list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/social_accounts/{id}/posts", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "first": first,
                        "post_id": post_id,
                    },
                    social_account_posts_params.SocialAccountPostsParams,
                ),
            ),
            cast_to=SocialAccountPostsResponse,
        )


class SocialAccountsResourceWithRawResponse:
    def __init__(self, social_accounts: SocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.create = to_raw_response_wrapper(
            social_accounts.create,
        )
        self.list = to_raw_response_wrapper(
            social_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            social_accounts.delete,
        )
        self.connect = to_raw_response_wrapper(
            social_accounts.connect,
        )
        self.posts = to_raw_response_wrapper(
            social_accounts.posts,
        )


class AsyncSocialAccountsResourceWithRawResponse:
    def __init__(self, social_accounts: AsyncSocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.create = async_to_raw_response_wrapper(
            social_accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            social_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            social_accounts.delete,
        )
        self.connect = async_to_raw_response_wrapper(
            social_accounts.connect,
        )
        self.posts = async_to_raw_response_wrapper(
            social_accounts.posts,
        )


class SocialAccountsResourceWithStreamingResponse:
    def __init__(self, social_accounts: SocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.create = to_streamed_response_wrapper(
            social_accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            social_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            social_accounts.delete,
        )
        self.connect = to_streamed_response_wrapper(
            social_accounts.connect,
        )
        self.posts = to_streamed_response_wrapper(
            social_accounts.posts,
        )


class AsyncSocialAccountsResourceWithStreamingResponse:
    def __init__(self, social_accounts: AsyncSocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.create = async_to_streamed_response_wrapper(
            social_accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            social_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            social_accounts.delete,
        )
        self.connect = async_to_streamed_response_wrapper(
            social_accounts.connect,
        )
        self.posts = async_to_streamed_response_wrapper(
            social_accounts.posts,
        )
