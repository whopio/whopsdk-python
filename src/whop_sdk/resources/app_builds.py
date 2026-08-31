# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

import httpx

from ..types import app_build_list_params, app_build_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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

__all__ = ["AppBuildsResource", "AsyncAppBuildsResource"]


class AppBuildsResource(SyncAPIResource):
    """
    An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

    Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
    """

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
        platform: Literal["ios", "android", "web"],
        ai_prompt_id: str | Omit = omit,
        app_id: str | Omit = omit,
        source_attachment: app_build_create_params.SourceAttachment | Omit = omit,
        supported_app_view_types: List[
            Literal["hub", "discover", "dash", "dashboard", "analytics", "skills", "openapi"]
        ]
        | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """Uploads a new build artifact for an app.

        Upload the file first (POST /files or a
        direct upload), then reference it here; iOS and Android take a .zip bundle, web
        takes a JavaScript file or a .zip archive of the hosted site.

        Args:
          attachment: The uploaded build file: `{ id }` for an existing file or `{ direct_upload_id }`
              for a completed direct upload.

          checksum: A client-generated checksum of the build file, used to verify file integrity
              when unpacked.

          platform: The target platform for the build.

          ai_prompt_id: The AI prompt that generated this build, if applicable.

          app_id: The app to create the build for, prefixed `app_`. Defaults to the app behind the
              presented credential.

          source_attachment: An optional compressed archive (.zip or .gz) of the source code that produced
              this build, stored alongside the build so it can be downloaded later. Referenced
              like `attachment`, and must be a different file.

          supported_app_view_types: The view types this build supports. Only list the ones its code implements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/app_builds",
            body=maybe_transform(
                {
                    "attachment": attachment,
                    "checksum": checksum,
                    "platform": platform,
                    "ai_prompt_id": ai_prompt_id,
                    "app_id": app_id,
                    "source_attachment": source_attachment,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """
        Retrieves the details of an existing app build.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/app_builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )

    def list(
        self,
        *,
        app_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[int, str] | Omit = omit,
        created_before: Union[int, str] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        platform: Literal["ios", "android", "web"] | Omit = omit,
        status: Literal["draft", "pending", "approved", "rejected"] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AppBuild]:
        """
        Returns a paginated list of build artifacts for an app, newest first, with
        optional platform, status, and creation-date filters.

        Args:
          app_id: The app to list builds for, prefixed `app_`.

          after: A cursor; returns builds after this position.

          before: A cursor; returns builds before this position.

          created_after: Only return builds created after this ISO 8601 timestamp.

          created_before: Only return builds created before this ISO 8601 timestamp.

          first: The number of builds to return (default 20, max 100).

          last: The number of builds to return from the end of the range.

          platform: Filter builds by target platform.

          status: Filter builds by review status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/app_builds",
            page=SyncCursorPage[AppBuild],
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
            model=AppBuild,
        )

    def promote(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """
        Promotes a draft or approved app build to production so it becomes the active
        version served to users. Draft builds enter review first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/app_builds/{id}/promote", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )


class AsyncAppBuildsResource(AsyncAPIResource):
    """
    An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

    Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
    """

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
        platform: Literal["ios", "android", "web"],
        ai_prompt_id: str | Omit = omit,
        app_id: str | Omit = omit,
        source_attachment: app_build_create_params.SourceAttachment | Omit = omit,
        supported_app_view_types: List[
            Literal["hub", "discover", "dash", "dashboard", "analytics", "skills", "openapi"]
        ]
        | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """Uploads a new build artifact for an app.

        Upload the file first (POST /files or a
        direct upload), then reference it here; iOS and Android take a .zip bundle, web
        takes a JavaScript file or a .zip archive of the hosted site.

        Args:
          attachment: The uploaded build file: `{ id }` for an existing file or `{ direct_upload_id }`
              for a completed direct upload.

          checksum: A client-generated checksum of the build file, used to verify file integrity
              when unpacked.

          platform: The target platform for the build.

          ai_prompt_id: The AI prompt that generated this build, if applicable.

          app_id: The app to create the build for, prefixed `app_`. Defaults to the app behind the
              presented credential.

          source_attachment: An optional compressed archive (.zip or .gz) of the source code that produced
              this build, stored alongside the build so it can be downloaded later. Referenced
              like `attachment`, and must be a different file.

          supported_app_view_types: The view types this build supports. Only list the ones its code implements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/app_builds",
            body=await async_maybe_transform(
                {
                    "attachment": attachment,
                    "checksum": checksum,
                    "platform": platform,
                    "ai_prompt_id": ai_prompt_id,
                    "app_id": app_id,
                    "source_attachment": source_attachment,
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
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """
        Retrieves the details of an existing app build.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/app_builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppBuild,
        )

    def list(
        self,
        *,
        app_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[int, str] | Omit = omit,
        created_before: Union[int, str] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        platform: Literal["ios", "android", "web"] | Omit = omit,
        status: Literal["draft", "pending", "approved", "rejected"] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AppBuild, AsyncCursorPage[AppBuild]]:
        """
        Returns a paginated list of build artifacts for an app, newest first, with
        optional platform, status, and creation-date filters.

        Args:
          app_id: The app to list builds for, prefixed `app_`.

          after: A cursor; returns builds after this position.

          before: A cursor; returns builds before this position.

          created_after: Only return builds created after this ISO 8601 timestamp.

          created_before: Only return builds created before this ISO 8601 timestamp.

          first: The number of builds to return (default 20, max 100).

          last: The number of builds to return from the end of the range.

          platform: Filter builds by target platform.

          status: Filter builds by review status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/app_builds",
            page=AsyncCursorPage[AppBuild],
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
            model=AppBuild,
        )

    async def promote(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppBuild:
        """
        Promotes a draft or approved app build to production so it becomes the active
        version served to users. Draft builds enter review first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/app_builds/{id}/promote", id=id),
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
