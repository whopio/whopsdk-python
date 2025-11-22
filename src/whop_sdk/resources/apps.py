# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import AppType, app_list_params, app_create_params, app_update_params
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
from ..types.app_type import AppType
from ..types.shared.app import App
from ..types.shared.direction import Direction
from ..types.app_list_response import AppListResponse
from ..types.shared.app_statuses import AppStatuses
from ..types.shared.app_view_type import AppViewType

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        name: str,
        base_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> App:
        """
        Create a new App

        Required permissions:

        - `developer:create_app`
        - `developer:manage_api_key`

        Args:
          company_id: The ID of the company to create the app for

          name: The name of the app to be created

          base_url: The base URL of the app to be created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/apps",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "name": name,
                    "base_url": base_url,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
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
    ) -> App:
        """
        Retrieves an app by ID

        Required permissions:

        - `developer:manage_api_key`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/apps/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    def update(
        self,
        id: str,
        *,
        app_store_description: Optional[str] | Omit = omit,
        app_type: Optional[AppType] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        dashboard_path: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        discover_path: Optional[str] | Omit = omit,
        experience_path: Optional[str] | Omit = omit,
        icon: Optional[app_update_params.Icon] | Omit = omit,
        name: Optional[str] | Omit = omit,
        required_scopes: Optional[List[Literal["read_user"]]] | Omit = omit,
        status: Optional[AppStatuses] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> App:
        """
        Update an existing App

        Required permissions:

        - `developer:update_app`
        - `developer:manage_api_key`

        Args:
          app_store_description: The description of the app for the app store in-depth app view.

          app_type: The type of end-user an app is built for

          base_url: The base production url of the app

          dashboard_path: The path for the dashboard view of the app

          description: The description of the app

          discover_path: The path for the discover view of the app

          experience_path: The path for the hub view of the app

          icon: The icon for the app

          name: The name of the app

          required_scopes: The scopes that the app will request off of users when a user installs the app.

          status: The status of an experience interface

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/apps/{id}",
            body=maybe_transform(
                {
                    "app_store_description": app_store_description,
                    "app_type": app_type,
                    "base_url": base_url,
                    "dashboard_path": dashboard_path,
                    "description": description,
                    "discover_path": discover_path,
                    "experience_path": experience_path,
                    "icon": icon,
                    "name": name,
                    "required_scopes": required_scopes,
                    "status": status,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        app_type: Optional[AppType] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[
            Literal[
                "discoverable_at",
                "total_installs_last_30_days",
                "total_installs_last_7_days",
                "time_spent",
                "time_spent_last_24_hours",
                "daily_active_users",
            ]
        ]
        | Omit = omit,
        query: Optional[str] | Omit = omit,
        verified_apps_only: Optional[bool] | Omit = omit,
        view_type: Optional[AppViewType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AppListResponse]:
        """
        Fetches a list of apps

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          app_type: The type of end-user an app is built for

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the company to filter apps by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The order to fetch the apps in for discovery.

          query: The query to search for apps by name.

          verified_apps_only: If true, you will only get apps that are verified by Whop. Use this to populate
              a 'featured apps' section on the app store.

          view_type: The different types of an app view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/apps",
            page=SyncCursorPage[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "app_type": app_type,
                        "before": before,
                        "company_id": company_id,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "query": query,
                        "verified_apps_only": verified_apps_only,
                        "view_type": view_type,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=AppListResponse,
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        name: str,
        base_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> App:
        """
        Create a new App

        Required permissions:

        - `developer:create_app`
        - `developer:manage_api_key`

        Args:
          company_id: The ID of the company to create the app for

          name: The name of the app to be created

          base_url: The base URL of the app to be created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/apps",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "name": name,
                    "base_url": base_url,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
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
    ) -> App:
        """
        Retrieves an app by ID

        Required permissions:

        - `developer:manage_api_key`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/apps/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    async def update(
        self,
        id: str,
        *,
        app_store_description: Optional[str] | Omit = omit,
        app_type: Optional[AppType] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        dashboard_path: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        discover_path: Optional[str] | Omit = omit,
        experience_path: Optional[str] | Omit = omit,
        icon: Optional[app_update_params.Icon] | Omit = omit,
        name: Optional[str] | Omit = omit,
        required_scopes: Optional[List[Literal["read_user"]]] | Omit = omit,
        status: Optional[AppStatuses] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> App:
        """
        Update an existing App

        Required permissions:

        - `developer:update_app`
        - `developer:manage_api_key`

        Args:
          app_store_description: The description of the app for the app store in-depth app view.

          app_type: The type of end-user an app is built for

          base_url: The base production url of the app

          dashboard_path: The path for the dashboard view of the app

          description: The description of the app

          discover_path: The path for the discover view of the app

          experience_path: The path for the hub view of the app

          icon: The icon for the app

          name: The name of the app

          required_scopes: The scopes that the app will request off of users when a user installs the app.

          status: The status of an experience interface

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/apps/{id}",
            body=await async_maybe_transform(
                {
                    "app_store_description": app_store_description,
                    "app_type": app_type,
                    "base_url": base_url,
                    "dashboard_path": dashboard_path,
                    "description": description,
                    "discover_path": discover_path,
                    "experience_path": experience_path,
                    "icon": icon,
                    "name": name,
                    "required_scopes": required_scopes,
                    "status": status,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        app_type: Optional[AppType] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[
            Literal[
                "discoverable_at",
                "total_installs_last_30_days",
                "total_installs_last_7_days",
                "time_spent",
                "time_spent_last_24_hours",
                "daily_active_users",
            ]
        ]
        | Omit = omit,
        query: Optional[str] | Omit = omit,
        verified_apps_only: Optional[bool] | Omit = omit,
        view_type: Optional[AppViewType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AppListResponse, AsyncCursorPage[AppListResponse]]:
        """
        Fetches a list of apps

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          app_type: The type of end-user an app is built for

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The ID of the company to filter apps by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: The order to fetch the apps in for discovery.

          query: The query to search for apps by name.

          verified_apps_only: If true, you will only get apps that are verified by Whop. Use this to populate
              a 'featured apps' section on the app store.

          view_type: The different types of an app view

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/apps",
            page=AsyncCursorPage[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "app_type": app_type,
                        "before": before,
                        "company_id": company_id,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "query": query,
                        "verified_apps_only": verified_apps_only,
                        "view_type": view_type,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=AppListResponse,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_raw_response_wrapper(
            apps.create,
        )
        self.retrieve = to_raw_response_wrapper(
            apps.retrieve,
        )
        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_raw_response_wrapper(
            apps.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            apps.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_streamed_response_wrapper(
            apps.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            apps.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_streamed_response_wrapper(
            apps.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            apps.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
