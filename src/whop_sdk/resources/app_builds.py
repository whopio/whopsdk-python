# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime

import httpx

from ..types import app_build_list_params, app_build_create_params
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
from ..types.shared.app_build import AppBuild
from ..types.shared.app_view_type import AppViewType
from ..types.app_build_list_response import AppBuildListResponse
from ..types.shared.app_build_statuses import AppBuildStatuses
from ..types.shared.app_build_platforms import AppBuildPlatforms

__all__ = ["AppBuildsResource", "AsyncAppBuildsResource"]


class AppBuildsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppBuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AppBuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppBuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AppBuildsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        attachment: app_build_create_params.Attachment,
        checksum: str,
        platform: AppBuildPlatforms,
        ai_prompt_id: Optional[str] | Omit = omit,
        app_id: Optional[str] | Omit = omit,
        supported_app_view_types: Optional[List[AppViewType]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """Upload a new build artifact for an app.

        The build must include a compiled code
        bundle for the specified platform.

        Required permissions:

        - `developer:manage_builds`

        Args:
          attachment: The build file to upload. For iOS and Android, this should be a .zip archive
              containing a main_js_bundle.hbc file and an optional assets folder. For web,
              this should be a JavaScript file.

          checksum: A client-generated checksum of the build file, used to verify file integrity
              when unpacked on a device.

          platform: The target platform for the build. Accepted values: ios, android, web.

          ai_prompt_id: The identifier of the AI prompt that generated this build, if applicable.

          app_id: The unique identifier of the app to create the build for. Defaults to the app
              associated with the current API key.

          supported_app_view_types: The view types this build supports. A build can support multiple view types but
              should only list the ones its code implements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/app_builds",
            body=maybe_transform(
                {
                    "attachment": attachment,
                    "checksum": checksum,
                    "platform": platform,
                    "ai_prompt_id": ai_prompt_id,
                    "app_id": app_id,
                    "supported_app_view_types": supported_app_view_types,
                },
                app_build_create_params.AppBuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
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
    ) -> AppBuild:
        """
        Retrieves the details of an existing app build.

        Required permissions:

        - `developer:manage_builds`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/app_builds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )

    def list(
        self,
        *,
        app_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        platform: Optional[AppBuildPlatforms] | Omit = omit,
        status: Optional[AppBuildStatuses] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AppBuildListResponse]:
        """
        Returns a paginated list of build artifacts for a given app, with optional
        filtering by platform, status, and creation date.

        Required permissions:

        - `developer:manage_builds`

        Args:
          app_id: The unique identifier of the app to list builds for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return builds created after this timestamp.

          created_before: Only return builds created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          platform: The different platforms an app build can target.

          status: The different statuses an AppBuild can be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/app_builds",
            page=SyncCursorPage[AppBuildListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "platform": platform,
                        "status": status,
                    },
                    app_build_list_params.AppBuildListParams,
                ),
            ),
            model=AppBuildListResponse,
        )

    def promote(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """
        Promote an approved or draft app build to production so it becomes the active
        version served to users.

        Required permissions:

        - `developer:manage_builds`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/app_builds/{id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )


class AsyncAppBuildsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppBuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppBuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppBuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAppBuildsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        attachment: app_build_create_params.Attachment,
        checksum: str,
        platform: AppBuildPlatforms,
        ai_prompt_id: Optional[str] | Omit = omit,
        app_id: Optional[str] | Omit = omit,
        supported_app_view_types: Optional[List[AppViewType]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """Upload a new build artifact for an app.

        The build must include a compiled code
        bundle for the specified platform.

        Required permissions:

        - `developer:manage_builds`

        Args:
          attachment: The build file to upload. For iOS and Android, this should be a .zip archive
              containing a main_js_bundle.hbc file and an optional assets folder. For web,
              this should be a JavaScript file.

          checksum: A client-generated checksum of the build file, used to verify file integrity
              when unpacked on a device.

          platform: The target platform for the build. Accepted values: ios, android, web.

          ai_prompt_id: The identifier of the AI prompt that generated this build, if applicable.

          app_id: The unique identifier of the app to create the build for. Defaults to the app
              associated with the current API key.

          supported_app_view_types: The view types this build supports. A build can support multiple view types but
              should only list the ones its code implements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/app_builds",
            body=await async_maybe_transform(
                {
                    "attachment": attachment,
                    "checksum": checksum,
                    "platform": platform,
                    "ai_prompt_id": ai_prompt_id,
                    "app_id": app_id,
                    "supported_app_view_types": supported_app_view_types,
                },
                app_build_create_params.AppBuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
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
    ) -> AppBuild:
        """
        Retrieves the details of an existing app build.

        Required permissions:

        - `developer:manage_builds`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/app_builds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )

    def list(
        self,
        *,
        app_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        platform: Optional[AppBuildPlatforms] | Omit = omit,
        status: Optional[AppBuildStatuses] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AppBuildListResponse, AsyncCursorPage[AppBuildListResponse]]:
        """
        Returns a paginated list of build artifacts for a given app, with optional
        filtering by platform, status, and creation date.

        Required permissions:

        - `developer:manage_builds`

        Args:
          app_id: The unique identifier of the app to list builds for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return builds created after this timestamp.

          created_before: Only return builds created before this timestamp.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          platform: The different platforms an app build can target.

          status: The different statuses an AppBuild can be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/app_builds",
            page=AsyncCursorPage[AppBuildListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "last": last,
                        "platform": platform,
                        "status": status,
                    },
                    app_build_list_params.AppBuildListParams,
                ),
            ),
            model=AppBuildListResponse,
        )

    async def promote(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """
        Promote an approved or draft app build to production so it becomes the active
        version served to users.

        Required permissions:

        - `developer:manage_builds`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/app_builds/{id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )


class AppBuildsResourceWithRawResponse:
    def __init__(self, app_builds: AppBuildsResource) -> None:
        self._app_builds = app_builds

        self.create = to_raw_response_wrapper(
            app_builds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            app_builds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            app_builds.list,
        )
        self.promote = to_raw_response_wrapper(
            app_builds.promote,
        )


class AsyncAppBuildsResourceWithRawResponse:
    def __init__(self, app_builds: AsyncAppBuildsResource) -> None:
        self._app_builds = app_builds

        self.create = async_to_raw_response_wrapper(
            app_builds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            app_builds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            app_builds.list,
        )
        self.promote = async_to_raw_response_wrapper(
            app_builds.promote,
        )


class AppBuildsResourceWithStreamingResponse:
    def __init__(self, app_builds: AppBuildsResource) -> None:
        self._app_builds = app_builds

        self.create = to_streamed_response_wrapper(
            app_builds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            app_builds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            app_builds.list,
        )
        self.promote = to_streamed_response_wrapper(
            app_builds.promote,
        )


class AsyncAppBuildsResourceWithStreamingResponse:
    def __init__(self, app_builds: AsyncAppBuildsResource) -> None:
        self._app_builds = app_builds

        self.create = async_to_streamed_response_wrapper(
            app_builds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            app_builds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            app_builds.list,
        )
        self.promote = async_to_streamed_response_wrapper(
            app_builds.promote,
        )
