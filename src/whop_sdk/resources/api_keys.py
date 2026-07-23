# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from ..types import api_key_list_params, api_key_create_params, api_key_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.api_key import APIKey
from ..types.api_key_delete_response import APIKeyDeleteResponse
from ..types.api_key_list_permissions_response import APIKeyListPermissionsResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    """An API Key is a programmatic credential owned by an account or app.

    Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

    Use the API Keys API to list a company or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
    """

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        permissions: api_key_create_params.Permissions,
        resource_id: str,
        resource_type: Literal["account", "app"],
        expires_at: Optional[str] | Omit = omit,
        ip_allowlist: Optional[SequenceNotStr[str]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Creates an API key for a company or app.

        The response is the only place the full
        `secret_key` is returned — store it immediately. Requires a user session; API
        keys cannot manage API keys.

        Args:
          name: A human-readable name for the API key, such as 'Production API Key'.

          permissions: The permissions policy for the API key: explicit permission statements, or a
              system role to inherit from. Statements without a `resources` array default to
              the owning company (company keys) or every key-addressable resource (app keys).

          resource_id: The company (`biz_`) or app (`app_`) tag to create the API key for.

          resource_type: The type of resource that will own this API key.

          expires_at: When the API key should stop working, as an ISO 8601 timestamp. Omit (or pass
              `null` on update) for a key that never expires.

          ip_allowlist: IPv4/IPv6 CIDR ranges allowed to use this key, for example `["203.0.113.0/24"]`.
              Empty or `null` allows any IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/api_keys",
            body=maybe_transform(
                {
                    "name": name,
                    "permissions": permissions,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                    "expires_at": expires_at,
                    "ip_allowlist": ip_allowlist,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
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
    ) -> APIKey:
        """Retrieves an API key with its effective permission grants.

        The full secret is
        never returned — rotate the key if it was lost.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def update(
        self,
        id: str,
        *,
        expires_at: Optional[str] | Omit = omit,
        ip_allowlist: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        permissions: api_key_update_params.Permissions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Updates an API key's name, permissions, expiration, or IP allowlist.

        Fields that
        are omitted keep their current value; default keys cannot be modified.

        Args:
          expires_at: When the API key should stop working, as an ISO 8601 timestamp. Omit (or pass
              `null` on update) for a key that never expires.

          ip_allowlist: IPv4/IPv6 CIDR ranges allowed to use this key, for example `["203.0.113.0/24"]`.
              Empty or `null` allows any IP.

          name: A new human-readable name for the API key.

          permissions: The permissions policy for the API key: explicit permission statements, or a
              system role to inherit from. Statements without a `resources` array default to
              the owning company (company keys) or every key-addressable resource (app keys).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api_keys/{id}", id=id),
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "ip_allowlist": ip_allowlist,
                    "name": name,
                    "permissions": permissions,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        resource_id: str,
        resource_type: Literal["account", "app"],
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[int, str] | Omit = omit,
        created_before: Union[int, str] | Omit = omit,
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
    ) -> SyncCursorPage[APIKey]:
        """Lists the API keys of a company or app, newest first.

        Responses never include
        the full secret — only its obfuscated form.

        Args:
          resource_id: The company (`biz_`) or app (`app_`) tag to list API keys for.

          resource_type: The type of resource that owns the API keys.

          after: A cursor; returns API keys after this position.

          before: A cursor; returns API keys before this position.

          created_after: Only return API keys created after this ISO 8601 timestamp.

          created_before: Only return API keys created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of API keys to return (default 20, max 100).

          last: The number of API keys to return from the end of the range.

          order: The field to sort API keys by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api_keys",
            page=SyncCursorPage[APIKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            model=APIKey,
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
    ) -> APIKeyDeleteResponse:
        """
        Permanently revokes an API key; requests using its secret stop authenticating
        immediately. Default and agent-backend keys cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyDeleteResponse,
        )

    def list_permissions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListPermissionsResponse:
        """
        Lists the catalog of permission actions that can be granted to users, apps, and
        API keys — the source for the dashboard's permission pickers. Small and returned
        in full on one page.
        """
        return self._get(
            "/api_keys/permissions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyListPermissionsResponse,
        )

    def rotate(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Rotates the API key's secret, invalidating the previous secret immediately.

        The
        response is the only place the new `secret_key` is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/api_keys/{id}/rotate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    """An API Key is a programmatic credential owned by an account or app.

    Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

    Use the API Keys API to list a company or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        permissions: api_key_create_params.Permissions,
        resource_id: str,
        resource_type: Literal["account", "app"],
        expires_at: Optional[str] | Omit = omit,
        ip_allowlist: Optional[SequenceNotStr[str]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Creates an API key for a company or app.

        The response is the only place the full
        `secret_key` is returned — store it immediately. Requires a user session; API
        keys cannot manage API keys.

        Args:
          name: A human-readable name for the API key, such as 'Production API Key'.

          permissions: The permissions policy for the API key: explicit permission statements, or a
              system role to inherit from. Statements without a `resources` array default to
              the owning company (company keys) or every key-addressable resource (app keys).

          resource_id: The company (`biz_`) or app (`app_`) tag to create the API key for.

          resource_type: The type of resource that will own this API key.

          expires_at: When the API key should stop working, as an ISO 8601 timestamp. Omit (or pass
              `null` on update) for a key that never expires.

          ip_allowlist: IPv4/IPv6 CIDR ranges allowed to use this key, for example `["203.0.113.0/24"]`.
              Empty or `null` allows any IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/api_keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "permissions": permissions,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                    "expires_at": expires_at,
                    "ip_allowlist": ip_allowlist,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
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
    ) -> APIKey:
        """Retrieves an API key with its effective permission grants.

        The full secret is
        never returned — rotate the key if it was lost.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def update(
        self,
        id: str,
        *,
        expires_at: Optional[str] | Omit = omit,
        ip_allowlist: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        permissions: api_key_update_params.Permissions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Updates an API key's name, permissions, expiration, or IP allowlist.

        Fields that
        are omitted keep their current value; default keys cannot be modified.

        Args:
          expires_at: When the API key should stop working, as an ISO 8601 timestamp. Omit (or pass
              `null` on update) for a key that never expires.

          ip_allowlist: IPv4/IPv6 CIDR ranges allowed to use this key, for example `["203.0.113.0/24"]`.
              Empty or `null` allows any IP.

          name: A new human-readable name for the API key.

          permissions: The permissions policy for the API key: explicit permission statements, or a
              system role to inherit from. Statements without a `resources` array default to
              the owning company (company keys) or every key-addressable resource (app keys).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api_keys/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "ip_allowlist": ip_allowlist,
                    "name": name,
                    "permissions": permissions,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        resource_id: str,
        resource_type: Literal["account", "app"],
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[int, str] | Omit = omit,
        created_before: Union[int, str] | Omit = omit,
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
    ) -> AsyncPaginator[APIKey, AsyncCursorPage[APIKey]]:
        """Lists the API keys of a company or app, newest first.

        Responses never include
        the full secret — only its obfuscated form.

        Args:
          resource_id: The company (`biz_`) or app (`app_`) tag to list API keys for.

          resource_type: The type of resource that owns the API keys.

          after: A cursor; returns API keys after this position.

          before: A cursor; returns API keys before this position.

          created_after: Only return API keys created after this ISO 8601 timestamp.

          created_before: Only return API keys created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of API keys to return (default 20, max 100).

          last: The number of API keys to return from the end of the range.

          order: The field to sort API keys by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api_keys",
            page=AsyncCursorPage[APIKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            model=APIKey,
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
    ) -> APIKeyDeleteResponse:
        """
        Permanently revokes an API key; requests using its secret stop authenticating
        immediately. Default and agent-backend keys cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyDeleteResponse,
        )

    async def list_permissions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListPermissionsResponse:
        """
        Lists the catalog of permission actions that can be granted to users, apps, and
        API keys — the source for the dashboard's permission pickers. Small and returned
        in full on one page.
        """
        return await self._get(
            "/api_keys/permissions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyListPermissionsResponse,
        )

    async def rotate(
        self,
        id: str,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Rotates the API key's secret, invalidating the previous secret immediately.

        The
        response is the only place the new `secret_key` is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/api_keys/{id}/rotate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )
        self.list_permissions = to_raw_response_wrapper(
            api_keys.list_permissions,
        )
        self.rotate = to_raw_response_wrapper(
            api_keys.rotate,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )
        self.list_permissions = async_to_raw_response_wrapper(
            api_keys.list_permissions,
        )
        self.rotate = async_to_raw_response_wrapper(
            api_keys.rotate,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.list_permissions = to_streamed_response_wrapper(
            api_keys.list_permissions,
        )
        self.rotate = to_streamed_response_wrapper(
            api_keys.rotate,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.list_permissions = async_to_streamed_response_wrapper(
            api_keys.list_permissions,
        )
        self.rotate = async_to_streamed_response_wrapper(
            api_keys.rotate,
        )
