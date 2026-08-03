# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ...types.users import oauth_grant_list_params, oauth_grant_create_params
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

    def create(
        self,
        *,
        client_id: str,
        code_challenge: str,
        code_challenge_method: Literal["S256"],
        redirect_uri: str,
        requested_scopes: SequenceNotStr[str],
        account_id: str | Omit = omit,
        consent_shown: bool | Omit = omit,
        nonce: str | Omit = omit,
        response_type: Literal["code"] | Omit = omit,
        state: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthGrant:
        """
        Completes the OAuth authorization step for the authenticated user: records their
        consent for the scopes an app asked for and mints the authorization code to hand
        back to it. Returns the grant, plus a `redirect_url` carrying that code — the
        one and only time it is returned. Exchange the code at `POST /oauth/token` with
        the verifier for `code_challenge`. Requires a user session, because consent has
        to come from the account holder: an API key or an OAuth token is refused, so an
        app can never authorize itself. Send an `Idempotency-Key` to make a retry safe —
        a replay returns the original `redirect_url` and its code rather than issuing a
        second one.

        Args:
          client_id: The app being authorized, prefixed `app_`.

          code_challenge: The PKCE code challenge: the base64url-encoded SHA-256 of your code verifier,
              without padding.

          code_challenge_method: How `code_challenge` was derived. Only `S256` is accepted.

          redirect_uri: Where to send the user once they have consented. Must match one of the app's
              registered redirect URIs exactly — it is compared as a string, not normalized.

          requested_scopes: The permissions the app is asking for, for example `member:basic:read`.
              `GET /api_keys/permissions` names and describes each one. Granting adds to
              whatever the user already granted this app rather than replacing it.

          account_id: Authorize the app for one of the user's accounts rather than for the user alone,
              prefixed `biz_`. The user must have access to it.

          consent_shown: Whether the consent UI listed these scopes for the user. Sending `false`
              succeeds only when the user has already granted every scope requested.

          nonce: OIDC nonce, echoed into the resulting ID token. Required when `requested_scopes`
              includes `openid`.

          response_type: The OAuth response type. Only `code` is accepted; defaults to `code`.

          state: Opaque value appended to `redirect_url` unchanged, for the client to correlate
              the response with its request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/users/me/oauth_grants",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "code_challenge": code_challenge,
                    "code_challenge_method": code_challenge_method,
                    "redirect_uri": redirect_uri,
                    "requested_scopes": requested_scopes,
                    "account_id": account_id,
                    "consent_shown": consent_shown,
                    "nonce": nonce,
                    "response_type": response_type,
                    "state": state,
                },
                oauth_grant_create_params.OAuthGrantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrant,
        )

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

    async def create(
        self,
        *,
        client_id: str,
        code_challenge: str,
        code_challenge_method: Literal["S256"],
        redirect_uri: str,
        requested_scopes: SequenceNotStr[str],
        account_id: str | Omit = omit,
        consent_shown: bool | Omit = omit,
        nonce: str | Omit = omit,
        response_type: Literal["code"] | Omit = omit,
        state: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthGrant:
        """
        Completes the OAuth authorization step for the authenticated user: records their
        consent for the scopes an app asked for and mints the authorization code to hand
        back to it. Returns the grant, plus a `redirect_url` carrying that code — the
        one and only time it is returned. Exchange the code at `POST /oauth/token` with
        the verifier for `code_challenge`. Requires a user session, because consent has
        to come from the account holder: an API key or an OAuth token is refused, so an
        app can never authorize itself. Send an `Idempotency-Key` to make a retry safe —
        a replay returns the original `redirect_url` and its code rather than issuing a
        second one.

        Args:
          client_id: The app being authorized, prefixed `app_`.

          code_challenge: The PKCE code challenge: the base64url-encoded SHA-256 of your code verifier,
              without padding.

          code_challenge_method: How `code_challenge` was derived. Only `S256` is accepted.

          redirect_uri: Where to send the user once they have consented. Must match one of the app's
              registered redirect URIs exactly — it is compared as a string, not normalized.

          requested_scopes: The permissions the app is asking for, for example `member:basic:read`.
              `GET /api_keys/permissions` names and describes each one. Granting adds to
              whatever the user already granted this app rather than replacing it.

          account_id: Authorize the app for one of the user's accounts rather than for the user alone,
              prefixed `biz_`. The user must have access to it.

          consent_shown: Whether the consent UI listed these scopes for the user. Sending `false`
              succeeds only when the user has already granted every scope requested.

          nonce: OIDC nonce, echoed into the resulting ID token. Required when `requested_scopes`
              includes `openid`.

          response_type: The OAuth response type. Only `code` is accepted; defaults to `code`.

          state: Opaque value appended to `redirect_url` unchanged, for the client to correlate
              the response with its request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/users/me/oauth_grants",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "code_challenge": code_challenge,
                    "code_challenge_method": code_challenge_method,
                    "redirect_uri": redirect_uri,
                    "requested_scopes": requested_scopes,
                    "account_id": account_id,
                    "consent_shown": consent_shown,
                    "nonce": nonce,
                    "response_type": response_type,
                    "state": state,
                },
                oauth_grant_create_params.OAuthGrantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrant,
        )

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

        self.create = to_raw_response_wrapper(
            oauth_grants.create,
        )
        self.list = to_raw_response_wrapper(
            oauth_grants.list,
        )


class AsyncOAuthGrantsResourceWithRawResponse:
    def __init__(self, oauth_grants: AsyncOAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.create = async_to_raw_response_wrapper(
            oauth_grants.create,
        )
        self.list = async_to_raw_response_wrapper(
            oauth_grants.list,
        )


class OAuthGrantsResourceWithStreamingResponse:
    def __init__(self, oauth_grants: OAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.create = to_streamed_response_wrapper(
            oauth_grants.create,
        )
        self.list = to_streamed_response_wrapper(
            oauth_grants.list,
        )


class AsyncOAuthGrantsResourceWithStreamingResponse:
    def __init__(self, oauth_grants: AsyncOAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.create = async_to_streamed_response_wrapper(
            oauth_grants.create,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_grants.list,
        )
