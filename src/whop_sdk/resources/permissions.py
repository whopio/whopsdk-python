# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import permission_list_params
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
from .._base_client import make_request_options
from ..types.permission_list_response import PermissionListResponse

__all__ = ["PermissionsResource", "AsyncPermissionsResource"]


class PermissionsResource(SyncAPIResource):
    """
    A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

    Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
    """

    @cached_property
    def with_raw_response(self) -> PermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PermissionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        resource_id: str,
        actions: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PermissionListResponse:
        """
        Lists permission actions and whether the calling credential is granted each one
        for a resource. Answers for whichever identity authenticated the request — a
        user session, an OAuth token, or an account or app API key — so it never
        describes who else can reach the resource.

        Args:
          resource_id: Tag of the resource to check against: an account (`biz_`), product (`prod_`),
              experience (`exp_`), or app (`app_`). A resource the credential cannot see is
              reported as granted nothing rather than as an error.

          actions: Comma-separated permission actions to check, for example
              `stats:read,payment:basic:read`. Every action is returned when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/permissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "actions": actions,
                    },
                    permission_list_params.PermissionListParams,
                ),
            ),
            cast_to=PermissionListResponse,
        )


class AsyncPermissionsResource(AsyncAPIResource):
    """
    A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

    Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPermissionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        resource_id: str,
        actions: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PermissionListResponse:
        """
        Lists permission actions and whether the calling credential is granted each one
        for a resource. Answers for whichever identity authenticated the request — a
        user session, an OAuth token, or an account or app API key — so it never
        describes who else can reach the resource.

        Args:
          resource_id: Tag of the resource to check against: an account (`biz_`), product (`prod_`),
              experience (`exp_`), or app (`app_`). A resource the credential cannot see is
              reported as granted nothing rather than as an error.

          actions: Comma-separated permission actions to check, for example
              `stats:read,payment:basic:read`. Every action is returned when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/permissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resource_id": resource_id,
                        "actions": actions,
                    },
                    permission_list_params.PermissionListParams,
                ),
            ),
            cast_to=PermissionListResponse,
        )


class PermissionsResourceWithRawResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.list = to_raw_response_wrapper(
            permissions.list,
        )


class AsyncPermissionsResourceWithRawResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.list = async_to_raw_response_wrapper(
            permissions.list,
        )


class PermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.list = to_streamed_response_wrapper(
            permissions.list,
        )


class AsyncPermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.list = async_to_streamed_response_wrapper(
            permissions.list,
        )
