# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import access_token_create_params
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
from .._base_client import make_request_options
from ..types.access_token_create_response import AccessTokenCreateResponse

__all__ = ["AccessTokensResource", "AsyncAccessTokensResource"]


class AccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AccessTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        scoped_actions: Optional[SequenceNotStr[str]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenCreateResponse:
        """Create a short-lived access token for authenticating API requests.

        When using
        API key authentication, provide company_id or user_id. When using OAuth, the
        user is derived from the token. Use this token with Whop's web and mobile
        embedded components.

        Args:
          company_id: The unique identifier of the company to generate the token for, starting with
              'biz\\__'. The API key must have permission to access this company.

          expires_at: The expiration timestamp for the access token. Defaults to 1 hour from now, with
              a maximum of 3 hours.

          scoped_actions: An array of permission scopes to grant to the access token. If empty or omitted,
              all permissions from the authenticating credential are inherited. Must be a
              subset of the credential's permissions.

          user_id: The unique identifier of the user to generate the token for, starting with
              'user\\__'. The API key must have permission to access this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/access_tokens",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "expires_at": expires_at,
                    "scoped_actions": scoped_actions,
                    "user_id": user_id,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenCreateResponse,
        )


class AsyncAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAccessTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        scoped_actions: Optional[SequenceNotStr[str]] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenCreateResponse:
        """Create a short-lived access token for authenticating API requests.

        When using
        API key authentication, provide company_id or user_id. When using OAuth, the
        user is derived from the token. Use this token with Whop's web and mobile
        embedded components.

        Args:
          company_id: The unique identifier of the company to generate the token for, starting with
              'biz\\__'. The API key must have permission to access this company.

          expires_at: The expiration timestamp for the access token. Defaults to 1 hour from now, with
              a maximum of 3 hours.

          scoped_actions: An array of permission scopes to grant to the access token. If empty or omitted,
              all permissions from the authenticating credential are inherited. Must be a
              subset of the credential's permissions.

          user_id: The unique identifier of the user to generate the token for, starting with
              'user\\__'. The API key must have permission to access this user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/access_tokens",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "expires_at": expires_at,
                    "scoped_actions": scoped_actions,
                    "user_id": user_id,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessTokenCreateResponse,
        )


class AccessTokensResourceWithRawResponse:
    def __init__(self, access_tokens: AccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = to_raw_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensResourceWithRawResponse:
    def __init__(self, access_tokens: AsyncAccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = async_to_raw_response_wrapper(
            access_tokens.create,
        )


class AccessTokensResourceWithStreamingResponse:
    def __init__(self, access_tokens: AccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = to_streamed_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensResourceWithStreamingResponse:
    def __init__(self, access_tokens: AsyncAccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = async_to_streamed_response_wrapper(
            access_tokens.create,
        )
