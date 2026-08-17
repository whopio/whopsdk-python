# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import app_deployment_create_params
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
from ..types.app_deployment_create_response import AppDeploymentCreateResponse
from ..types.app_deployment_retrieve_response import AppDeploymentRetrieveResponse

__all__ = ["AppDeploymentsResource", "AsyncAppDeploymentsResource"]


class AppDeploymentsResource(SyncAPIResource):
    """A Deployment builds an app's current source and ships it, producing an App Build.

    It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

    Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
    """

    @cached_property
    def with_raw_response(self) -> AppDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AppDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AppDeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: str,
        *,
        draft: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AppDeploymentCreateResponse:
        """Starts deploying the app's current source.

        Returns immediately with the same
        shape as a retrieve, so the caller can render progress from this response and
        then poll. Only one deployment runs per app at a time — calling this while one
        is in flight reports that run rather than starting a second.

        Args:
          draft: Upload the build without making it live. Defaults to `false`, which deploys and
              promotes in one step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            path_template("/apps/{app_id}/deployment", app_id=app_id),
            body=maybe_transform({"draft": draft}, app_deployment_create_params.AppDeploymentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AppDeploymentCreateResponse,
        )

    def retrieve(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppDeploymentRetrieveResponse:
        """
        Reports whether the app has changes that have not been deployed, and how a
        deployment already in progress is going. Poll this while `status` is
        `publishing` to follow it to completion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template("/apps/{app_id}/deployment", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppDeploymentRetrieveResponse,
        )


class AsyncAppDeploymentsResource(AsyncAPIResource):
    """A Deployment builds an app's current source and ships it, producing an App Build.

    It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

    Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAppDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAppDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: str,
        *,
        draft: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AppDeploymentCreateResponse:
        """Starts deploying the app's current source.

        Returns immediately with the same
        shape as a retrieve, so the caller can render progress from this response and
        then poll. Only one deployment runs per app at a time — calling this while one
        is in flight reports that run rather than starting a second.

        Args:
          draft: Upload the build without making it live. Defaults to `false`, which deploys and
              promotes in one step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            path_template("/apps/{app_id}/deployment", app_id=app_id),
            body=await async_maybe_transform({"draft": draft}, app_deployment_create_params.AppDeploymentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AppDeploymentCreateResponse,
        )

    async def retrieve(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppDeploymentRetrieveResponse:
        """
        Reports whether the app has changes that have not been deployed, and how a
        deployment already in progress is going. Poll this while `status` is
        `publishing` to follow it to completion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template("/apps/{app_id}/deployment", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppDeploymentRetrieveResponse,
        )


class AppDeploymentsResourceWithRawResponse:
    def __init__(self, app_deployments: AppDeploymentsResource) -> None:
        self._app_deployments = app_deployments

        self.create = to_raw_response_wrapper(
            app_deployments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            app_deployments.retrieve,
        )


class AsyncAppDeploymentsResourceWithRawResponse:
    def __init__(self, app_deployments: AsyncAppDeploymentsResource) -> None:
        self._app_deployments = app_deployments

        self.create = async_to_raw_response_wrapper(
            app_deployments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            app_deployments.retrieve,
        )


class AppDeploymentsResourceWithStreamingResponse:
    def __init__(self, app_deployments: AppDeploymentsResource) -> None:
        self._app_deployments = app_deployments

        self.create = to_streamed_response_wrapper(
            app_deployments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            app_deployments.retrieve,
        )


class AsyncAppDeploymentsResourceWithStreamingResponse:
    def __init__(self, app_deployments: AsyncAppDeploymentsResource) -> None:
        self._app_deployments = app_deployments

        self.create = async_to_streamed_response_wrapper(
            app_deployments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            app_deployments.retrieve,
        )
