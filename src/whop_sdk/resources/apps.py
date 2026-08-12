# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    app_list_params,
    app_logs_params,
    app_create_params,
    app_update_params,
    app_update_permissions_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.shared.app import App
from ..types.app_list_response import AppListResponse
from ..types.app_logs_response import AppLogsResponse
from ..types.app_delete_response import AppDeleteResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    """An App is software you build on Whop.

    It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

    Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
    """

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
        name: str,
        account_id: str | Omit = omit,
        app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        icon: app_create_params.Icon | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> App:
        """Registers a new app on the Whop developer platform.

        Apps provide custom
        experiences that can be added to products.

        Args:
          name: The display name for the app, shown to users on the app store and product pages.

          account_id: The account to create the app for (`biz_` tag). Defaults to the account behind
              the presented credential.

          app_type: The type of app to create. Defaults to `b2c_app`.

          base_url: The base production URL where the app is hosted, such as
              `https://myapp.example.com`.

          icon: The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded
              file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new
              direct upload.

          redirect_uris: The whitelisted OAuth callback URLs that users are redirected to after
              authorizing the app.

          route: The subdomain route where the app's hosted web builds are served, such as
              `myapp` for myapp.whop.app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/apps",
            body=maybe_transform(
                {
                    "name": name,
                    "account_id": account_id,
                    "app_type": app_type,
                    "base_url": base_url,
                    "icon": icon,
                    "redirect_uris": redirect_uris,
                    "route": route,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        """Retrieves an app by ID, claimed route, or proxy domain id.

        Credential fields
        (api_key, default_api_key, secrets) render `null` unless the caller has the
        corresponding developer permission on the owning account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    def update(
        self,
        id: str,
        *,
        app_store_description: str | Omit = omit,
        app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        dashboard_path: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        discover_path: Optional[str] | Omit = omit,
        experience_path: Optional[str] | Omit = omit,
        icon: app_update_params.Icon | Omit = omit,
        name: str | Omit = omit,
        oauth_client_type: Literal["public", "confidential"] | Omit = omit,
        openapi_path: Optional[str] | Omit = omit,
        production_android_build_id: Optional[str] | Omit = omit,
        production_ios_build_id: Optional[str] | Omit = omit,
        production_web_build_id: Optional[str] | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        required_scopes: SequenceNotStr[str] | Omit = omit,
        route: str | Omit = omit,
        secrets: object | Omit = omit,
        skills_path: Optional[str] | Omit = omit,
        status: Literal["live", "unlisted", "hidden"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> App:
        """Updates the settings, metadata, or status of an app.

        Fields that are omitted
        keep their current value.

        Args:
          app_store_description: The detailed description shown on the app store's in-depth app view page.

          app_type: The type of end-user the app is built for. Cannot be changed on an app whose
              type is already `website`.

          base_url: The base production URL where the app is hosted. Set to `null` to take the app
              proxy offline.

          dashboard_path: The URL path for the account dashboard view.

          description: A short description of the app shown in listings and search results.

          discover_path: The URL path for the discover view.

          experience_path: The URL path for the member-facing hub view, such as
              `/experiences/[experienceId]`.

          icon: The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded
              file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new
              direct upload.

          name: The display name for the app, shown to users on the app store and product pages.

          oauth_client_type: How the app authenticates at the OAuth token endpoint.

          openapi_path: The URL path to the app's OpenAPI spec file (requires the ai_chat capability).

          production_android_build_id: The app build (`abld_` tag) to serve as the Android production build, or `null`
              to unassign it. Same rules as `production_web_build_id`.

          production_ios_build_id: The app build (`abld_` tag) to serve as the iOS production build, or `null` to
              unassign it. Same rules as `production_web_build_id`.

          production_web_build_id: The app build (`abld_` tag) to serve as the web production build, or `null` to
              unassign it. The build must belong to this app, target web, and be in the draft
              or approved status; a draft build is queued for approval and takes over once
              approved. Requires the `developer:manage_builds` scope.

          redirect_uris: The whitelisted OAuth callback URLs users are redirected to after authorizing
              the app.

          required_scopes: The OAuth scopes the app requests from users when they install it.

          route: The subdomain route where the app's hosted web builds are served.

          secrets: Secrets to add or overwrite on the app, as an object of string values. Keys not
              included are left untouched; pass null or an empty string as the value to delete
              a secret. Encrypted at rest and injected into the app's hosted server runtime.

          skills_path: The URL path to the app's skills directory (requires the ai_chat capability).

          status: Controls whether the app is published on Whop discovery or accessible only
              through its direct link. Publishing requires a name, icon, and description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/apps/{id}", id=id),
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
                    "oauth_client_type": oauth_client_type,
                    "openapi_path": openapi_path,
                    "production_android_build_id": production_android_build_id,
                    "production_ios_build_id": production_ios_build_id,
                    "production_web_build_id": production_web_build_id,
                    "redirect_uris": redirect_uris,
                    "required_scopes": required_scopes,
                    "route": route,
                    "secrets": secrets,
                    "skills_path": skills_path,
                    "status": status,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=App,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"] | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "discoverable_at", "total_installs_last_30_days", "total_installs_last_7_days"]
        | Omit = omit,
        query: str | Omit = omit,
        verified_apps_only: bool | Omit = omit,
        view_type: Literal["hub", "discover", "dash", "dashboard", "analytics", "skills", "openapi"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AppListResponse]:
        """
        Lists apps on the Whop platform: the app store's live apps, or — with
        `account_id` and developer access to that account — every app the account owns.

        Args:
          account_id: Only return apps created by this account (`biz_` tag). With developer access to
              the account this includes its unlisted and hidden apps.

          after: A cursor; returns apps after this position.

          app_type: Filter apps by the type of end-user they are built for. Apps of type `website`
              are left out unless you ask for them by name.

          before: A cursor; returns apps before this position.

          direction: Sort direction.

          first: The number of apps to return (default 20, max 100).

          last: The number of apps to return from the end of the range.

          order: The field to sort apps by. Defaults to discoverable_at, showing the most
              recently published apps first.

          query: A search string matched against app names.

          verified_apps_only: Whether to only return apps verified by Whop.

          view_type: Only return apps supporting this view type, such as `dashboard` or `hub`.

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
                        "account_id": account_id,
                        "after": after,
                        "app_type": app_type,
                        "before": before,
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

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AppDeleteResponse:
        """Deletes an app.

        The app stops resolving within seconds — a website's site stops
        serving, and any claimed subdomain is reserved for a month before it can be
        claimed again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AppDeleteResponse,
        )

    def logs(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        app_build_id: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        first: int | Omit = omit,
        level: Literal["log", "debug", "info", "warn", "error"] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppLogsResponse:
        """
        Lists a hosted app's server runtime logs, most recent first: console output,
        uncaught exceptions, and failed-request summaries captured on whop.app hosting.
        Logs are retained for 7 days.

        Args:
          after: A cursor for fetching logs after a previous page.

          app_build_id: Only return logs from this build.

          before: A cursor for fetching logs before a later page.

          created_after: Start of the time window as an ISO 8601 timestamp. Defaults to 7 days before
              created_before.

          created_before: End of the time window as an ISO 8601 timestamp. Defaults to now.

          first: The number of log lines to return (max 500).

          level: Only return console lines of this level.

          query: Only return logs whose message contains this text (case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/apps/{id}/logs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "app_build_id": app_build_id,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "level": level,
                        "query": query,
                    },
                    app_logs_params.AppLogsParams,
                ),
            ),
            cast_to=AppLogsResponse,
        )

    def update_permissions(
        self,
        id: str,
        *,
        requested_permissions: Iterable[app_update_permissions_params.RequestedPermission],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> App:
        """Replaces the set of permissions the app requests from users when they install
        it.

        Requires a user session: the `developer:update_app_authorization` scope
        cannot be delegated to API keys.

        Args:
          requested_permissions: The full set of permissions the app requests on install; permissions not listed
              are removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/apps/{id}/permissions", id=id),
            body=maybe_transform(
                {"requested_permissions": requested_permissions},
                app_update_permissions_params.AppUpdatePermissionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=App,
        )


class AsyncAppsResource(AsyncAPIResource):
    """An App is software you build on Whop.

    It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

    Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
    """

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
        name: str,
        account_id: str | Omit = omit,
        app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        icon: app_create_params.Icon | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        route: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> App:
        """Registers a new app on the Whop developer platform.

        Apps provide custom
        experiences that can be added to products.

        Args:
          name: The display name for the app, shown to users on the app store and product pages.

          account_id: The account to create the app for (`biz_` tag). Defaults to the account behind
              the presented credential.

          app_type: The type of app to create. Defaults to `b2c_app`.

          base_url: The base production URL where the app is hosted, such as
              `https://myapp.example.com`.

          icon: The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded
              file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new
              direct upload.

          redirect_uris: The whitelisted OAuth callback URLs that users are redirected to after
              authorizing the app.

          route: The subdomain route where the app's hosted web builds are served, such as
              `myapp` for myapp.whop.app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/apps",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "account_id": account_id,
                    "app_type": app_type,
                    "base_url": base_url,
                    "icon": icon,
                    "redirect_uris": redirect_uris,
                    "route": route,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        """Retrieves an app by ID, claimed route, or proxy domain id.

        Credential fields
        (api_key, default_api_key, secrets) render `null` unless the caller has the
        corresponding developer permission on the owning account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    async def update(
        self,
        id: str,
        *,
        app_store_description: str | Omit = omit,
        app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"] | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        dashboard_path: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        discover_path: Optional[str] | Omit = omit,
        experience_path: Optional[str] | Omit = omit,
        icon: app_update_params.Icon | Omit = omit,
        name: str | Omit = omit,
        oauth_client_type: Literal["public", "confidential"] | Omit = omit,
        openapi_path: Optional[str] | Omit = omit,
        production_android_build_id: Optional[str] | Omit = omit,
        production_ios_build_id: Optional[str] | Omit = omit,
        production_web_build_id: Optional[str] | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        required_scopes: SequenceNotStr[str] | Omit = omit,
        route: str | Omit = omit,
        secrets: object | Omit = omit,
        skills_path: Optional[str] | Omit = omit,
        status: Literal["live", "unlisted", "hidden"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> App:
        """Updates the settings, metadata, or status of an app.

        Fields that are omitted
        keep their current value.

        Args:
          app_store_description: The detailed description shown on the app store's in-depth app view page.

          app_type: The type of end-user the app is built for. Cannot be changed on an app whose
              type is already `website`.

          base_url: The base production URL where the app is hosted. Set to `null` to take the app
              proxy offline.

          dashboard_path: The URL path for the account dashboard view.

          description: A short description of the app shown in listings and search results.

          discover_path: The URL path for the discover view.

          experience_path: The URL path for the member-facing hub view, such as
              `/experiences/[experienceId]`.

          icon: The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded
              file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new
              direct upload.

          name: The display name for the app, shown to users on the app store and product pages.

          oauth_client_type: How the app authenticates at the OAuth token endpoint.

          openapi_path: The URL path to the app's OpenAPI spec file (requires the ai_chat capability).

          production_android_build_id: The app build (`abld_` tag) to serve as the Android production build, or `null`
              to unassign it. Same rules as `production_web_build_id`.

          production_ios_build_id: The app build (`abld_` tag) to serve as the iOS production build, or `null` to
              unassign it. Same rules as `production_web_build_id`.

          production_web_build_id: The app build (`abld_` tag) to serve as the web production build, or `null` to
              unassign it. The build must belong to this app, target web, and be in the draft
              or approved status; a draft build is queued for approval and takes over once
              approved. Requires the `developer:manage_builds` scope.

          redirect_uris: The whitelisted OAuth callback URLs users are redirected to after authorizing
              the app.

          required_scopes: The OAuth scopes the app requests from users when they install it.

          route: The subdomain route where the app's hosted web builds are served.

          secrets: Secrets to add or overwrite on the app, as an object of string values. Keys not
              included are left untouched; pass null or an empty string as the value to delete
              a secret. Encrypted at rest and injected into the app's hosted server runtime.

          skills_path: The URL path to the app's skills directory (requires the ai_chat capability).

          status: Controls whether the app is published on Whop discovery or accessible only
              through its direct link. Publishing requires a name, icon, and description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/apps/{id}", id=id),
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
                    "oauth_client_type": oauth_client_type,
                    "openapi_path": openapi_path,
                    "production_android_build_id": production_android_build_id,
                    "production_ios_build_id": production_ios_build_id,
                    "production_web_build_id": production_web_build_id,
                    "redirect_uris": redirect_uris,
                    "required_scopes": required_scopes,
                    "route": route,
                    "secrets": secrets,
                    "skills_path": skills_path,
                    "status": status,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=App,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"] | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "discoverable_at", "total_installs_last_30_days", "total_installs_last_7_days"]
        | Omit = omit,
        query: str | Omit = omit,
        verified_apps_only: bool | Omit = omit,
        view_type: Literal["hub", "discover", "dash", "dashboard", "analytics", "skills", "openapi"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AppListResponse, AsyncCursorPage[AppListResponse]]:
        """
        Lists apps on the Whop platform: the app store's live apps, or — with
        `account_id` and developer access to that account — every app the account owns.

        Args:
          account_id: Only return apps created by this account (`biz_` tag). With developer access to
              the account this includes its unlisted and hidden apps.

          after: A cursor; returns apps after this position.

          app_type: Filter apps by the type of end-user they are built for. Apps of type `website`
              are left out unless you ask for them by name.

          before: A cursor; returns apps before this position.

          direction: Sort direction.

          first: The number of apps to return (default 20, max 100).

          last: The number of apps to return from the end of the range.

          order: The field to sort apps by. Defaults to discoverable_at, showing the most
              recently published apps first.

          query: A search string matched against app names.

          verified_apps_only: Whether to only return apps verified by Whop.

          view_type: Only return apps supporting this view type, such as `dashboard` or `hub`.

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
                        "account_id": account_id,
                        "after": after,
                        "app_type": app_type,
                        "before": before,
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

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> AppDeleteResponse:
        """Deletes an app.

        The app stops resolving within seconds — a website's site stops
        serving, and any claimed subdomain is reserved for a month before it can be
        claimed again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AppDeleteResponse,
        )

    async def logs(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        app_build_id: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        first: int | Omit = omit,
        level: Literal["log", "debug", "info", "warn", "error"] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppLogsResponse:
        """
        Lists a hosted app's server runtime logs, most recent first: console output,
        uncaught exceptions, and failed-request summaries captured on whop.app hosting.
        Logs are retained for 7 days.

        Args:
          after: A cursor for fetching logs after a previous page.

          app_build_id: Only return logs from this build.

          before: A cursor for fetching logs before a later page.

          created_after: Start of the time window as an ISO 8601 timestamp. Defaults to 7 days before
              created_before.

          created_before: End of the time window as an ISO 8601 timestamp. Defaults to now.

          first: The number of log lines to return (max 500).

          level: Only return console lines of this level.

          query: Only return logs whose message contains this text (case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/apps/{id}/logs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "app_build_id": app_build_id,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "first": first,
                        "level": level,
                        "query": query,
                    },
                    app_logs_params.AppLogsParams,
                ),
            ),
            cast_to=AppLogsResponse,
        )

    async def update_permissions(
        self,
        id: str,
        *,
        requested_permissions: Iterable[app_update_permissions_params.RequestedPermission],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> App:
        """Replaces the set of permissions the app requests from users when they install
        it.

        Requires a user session: the `developer:update_app_authorization` scope
        cannot be delegated to API keys.

        Args:
          requested_permissions: The full set of permissions the app requests on install; permissions not listed
              are removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/apps/{id}/permissions", id=id),
            body=await async_maybe_transform(
                {"requested_permissions": requested_permissions},
                app_update_permissions_params.AppUpdatePermissionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=App,
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
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.logs = to_raw_response_wrapper(
            apps.logs,
        )
        self.update_permissions = to_raw_response_wrapper(
            apps.update_permissions,
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
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.logs = async_to_raw_response_wrapper(
            apps.logs,
        )
        self.update_permissions = async_to_raw_response_wrapper(
            apps.update_permissions,
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
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.logs = to_streamed_response_wrapper(
            apps.logs,
        )
        self.update_permissions = to_streamed_response_wrapper(
            apps.update_permissions,
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
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.logs = async_to_streamed_response_wrapper(
            apps.logs,
        )
        self.update_permissions = async_to_streamed_response_wrapper(
            apps.update_permissions,
        )
