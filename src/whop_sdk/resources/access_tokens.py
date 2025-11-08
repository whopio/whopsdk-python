# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

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
        scoped_actions: SequenceNotStr[str],
        target_resource_id: str,
        target_resource_type: Literal["company", "product", "experience", "app", "user"],
        expires_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenCreateResponse:
        """Creates an access token for a user to access a specific resource.

        These access
        tokens are designed to be used with Whop's embedded components.

        Args:
          scoped_actions: Array of desired scoped actions for the access token. This list must be a subset
              of the API keys's existing permissions. Otherwise, an error will be raised.

          target_resource_id: The ID of the target resource (Company, User, etc.) for which the access token
              is being created.

          target_resource_type: The type of the target resource (company, user, product, experience, etc.).

          expires_at: The expiration timestamp for the access token. If not provided, a default
              expiration time of 1 hour will be used. The expiration can be set to a maximum
              of 3 hours from the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/access_tokens",
            body=maybe_transform(
                {
                    "scoped_actions": scoped_actions,
                    "target_resource_id": target_resource_id,
                    "target_resource_type": target_resource_type,
                    "expires_at": expires_at,
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
        scoped_actions: SequenceNotStr[str],
        target_resource_id: str,
        target_resource_type: Literal["company", "product", "experience", "app", "user"],
        expires_at: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessTokenCreateResponse:
        """Creates an access token for a user to access a specific resource.

        These access
        tokens are designed to be used with Whop's embedded components.

        Args:
          scoped_actions: Array of desired scoped actions for the access token. This list must be a subset
              of the API keys's existing permissions. Otherwise, an error will be raised.

          target_resource_id: The ID of the target resource (Company, User, etc.) for which the access token
              is being created.

          target_resource_type: The type of the target resource (company, user, product, experience, etc.).

          expires_at: The expiration timestamp for the access token. If not provided, a default
              expiration time of 1 hour will be used. The expiration can be set to a maximum
              of 3 hours from the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/access_tokens",
            body=await async_maybe_transform(
                {
                    "scoped_actions": scoped_actions,
                    "target_resource_id": target_resource_id,
                    "target_resource_type": target_resource_type,
                    "expires_at": expires_at,
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
