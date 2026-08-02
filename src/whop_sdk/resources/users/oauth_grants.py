# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ...types.users import oauth_grant_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.users.oauth_grant import OAuthGrant

__all__ = ["OAuthGrantsResource", "AsyncOAuthGrantsResource"]


class OAuthGrantsResource(SyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def with_raw_response(self) -> OAuthGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return OAuthGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return OAuthGrantsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        app_id: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[OAuthGrant]:
        """
        Lists the authenticated user's own OAuth grants — one per app they have
        authorized, per account they authorized it for. The list is always the caller's
        own; there is no parameter for reading another user's grants. Requires a user
        session: an API key or an OAuth token is refused, so an app can never enumerate
        the other apps a user has authorized.

        Args:
          after: A cursor; returns grants after this position.

          app_id: Only return grants for this app, prefixed `app_`. An app the user has never
              authorized returns an empty list.

          before: A cursor; returns grants before this position.

          direction: Sort direction.

          first: The number of grants to return (default 20, max 100).

          last: The number of grants to return from the end of the range.

          order: The field to sort grants by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/oauth_grants",
            page=SyncCursorPage[OAuthGrant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "app_id": app_id,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    oauth_grant_list_params.OAuthGrantListParams,
                ),
            ),
            model=OAuthGrant,
        )


class AsyncOAuthGrantsResource(AsyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOAuthGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncOAuthGrantsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        app_id: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OAuthGrant, AsyncCursorPage[OAuthGrant]]:
        """
        Lists the authenticated user's own OAuth grants — one per app they have
        authorized, per account they authorized it for. The list is always the caller's
        own; there is no parameter for reading another user's grants. Requires a user
        session: an API key or an OAuth token is refused, so an app can never enumerate
        the other apps a user has authorized.

        Args:
          after: A cursor; returns grants after this position.

          app_id: Only return grants for this app, prefixed `app_`. An app the user has never
              authorized returns an empty list.

          before: A cursor; returns grants before this position.

          direction: Sort direction.

          first: The number of grants to return (default 20, max 100).

          last: The number of grants to return from the end of the range.

          order: The field to sort grants by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/oauth_grants",
            page=AsyncCursorPage[OAuthGrant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "app_id": app_id,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    oauth_grant_list_params.OAuthGrantListParams,
                ),
            ),
            model=OAuthGrant,
        )


class OAuthGrantsResourceWithRawResponse:
    def __init__(self, oauth_grants: OAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.list = to_raw_response_wrapper(
            oauth_grants.list,
        )


class AsyncOAuthGrantsResourceWithRawResponse:
    def __init__(self, oauth_grants: AsyncOAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.list = async_to_raw_response_wrapper(
            oauth_grants.list,
        )


class OAuthGrantsResourceWithStreamingResponse:
    def __init__(self, oauth_grants: OAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.list = to_streamed_response_wrapper(
            oauth_grants.list,
        )


class AsyncOAuthGrantsResourceWithStreamingResponse:
    def __init__(self, oauth_grants: AsyncOAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.list = async_to_streamed_response_wrapper(
            oauth_grants.list,
        )
