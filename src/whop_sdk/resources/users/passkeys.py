# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ...types.users import passkey_list_params, passkey_create_params, passkey_delete_params, passkey_challenge_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.users.passkey import Passkey
from ...types.users.passkey_delete_response import PasskeyDeleteResponse
from ...types.users.passkey_challenge_response import PasskeyChallengeResponse

__all__ = ["PasskeysResource", "AsyncPasskeysResource"]


class PasskeysResource(SyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def with_raw_response(self) -> PasskeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PasskeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PasskeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PasskeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        attestation_object: str,
        client_data_json: str,
        credential_id: str,
        nickname: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Passkey:
        """
        Registers a passkey for the authenticated user from the attestation a browser
        produced for a `registration` challenge. Mint that challenge first with
        `POST /users/me/passkeys/challenge`; it is single-use and expires 5 minutes
        after it is issued. Requires a user session.

        Args:
          attestation_object: The `attestationObject` from the WebAuthn attestation response,
              base64url-encoded.

          client_data_json: The `clientDataJSON` from the WebAuthn attestation response, base64url-encoded.

          credential_id: The WebAuthn credential ID the authenticator returned, base64url-encoded.

          nickname: A name for this passkey, usually the device it lives on. 255 characters or
              fewer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/users/me/passkeys",
            body=maybe_transform(
                {
                    "attestation_object": attestation_object,
                    "client_data_json": client_data_json,
                    "credential_id": credential_id,
                    "nickname": nickname,
                },
                passkey_create_params.PasskeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Passkey,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
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
    ) -> SyncCursorPage[Passkey]:
        """Lists the authenticated user's own passkeys, newest first.

        The list is always
        the caller's own; there is no parameter for reading another user's passkeys.
        Requires a user session: an API key or an OAuth token is refused, because a
        passkey confirms the account holder before a sensitive action and no app may
        enumerate one.

        Args:
          after: A cursor; returns passkeys after this position.

          before: A cursor; returns passkeys before this position.

          direction: Sort direction.

          first: The number of passkeys to return (default 20, max 100).

          last: The number of passkeys to return from the end of the range.

          order: The field to sort passkeys by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/passkeys",
            page=SyncCursorPage[Passkey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    passkey_list_params.PasskeyListParams,
                ),
            ),
            model=Passkey,
        )

    def delete(
        self,
        id: str,
        *,
        authenticator_data: str,
        client_data_json: str,
        signature: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PasskeyDeleteResponse:
        """Deletes one of the authenticated user's own passkeys.

        The request body carries a
        WebAuthn assertion from the passkey being deleted, so possession of the
        credential is proven before it is removed: mint a `deletion` challenge for it
        first, run the ceremony with that passkey, and send the result here. Deleting
        the user's last passkey is allowed — their other step-up factors remain.
        Requires a user session.

        Args:
          authenticator_data: The `authenticatorData` from the WebAuthn assertion, base64url-encoded.

          client_data_json: The `clientDataJSON` from the WebAuthn assertion, base64url-encoded.

          signature: The `signature` from the WebAuthn assertion, base64url-encoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/users/me/passkeys/{id}", id=id),
            body=maybe_transform(
                {
                    "authenticator_data": authenticator_data,
                    "client_data_json": client_data_json,
                    "signature": signature,
                },
                passkey_delete_params.PasskeyDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasskeyDeleteResponse,
        )

    def challenge(
        self,
        *,
        challenge_type: Literal["registration", "deletion"],
        passkey_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PasskeyChallengeResponse:
        """
        Mints the challenge a browser needs to run a WebAuthn ceremony against the
        authenticated user's own passkeys. A `registration` challenge enrolls a new
        passkey; a `deletion` challenge is bound to the one passkey named by
        `passkey_id` and proves the user still holds it. Challenges are single-use and
        expire 5 minutes after they are issued, so send a fresh `Idempotency-Key` per
        ceremony — a replayed key returns the original challenge, which may already have
        expired. Requires a user session.

        Args:
          challenge_type: The ceremony this challenge is for.

          passkey_id: The passkey the ceremony targets, prefixed `wcred_`. Required when
              `challenge_type` is `deletion`, ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/users/me/passkeys/challenge",
            body=maybe_transform(
                {
                    "challenge_type": challenge_type,
                    "passkey_id": passkey_id,
                },
                passkey_challenge_params.PasskeyChallengeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasskeyChallengeResponse,
        )


class AsyncPasskeysResource(AsyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPasskeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPasskeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPasskeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPasskeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        attestation_object: str,
        client_data_json: str,
        credential_id: str,
        nickname: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Passkey:
        """
        Registers a passkey for the authenticated user from the attestation a browser
        produced for a `registration` challenge. Mint that challenge first with
        `POST /users/me/passkeys/challenge`; it is single-use and expires 5 minutes
        after it is issued. Requires a user session.

        Args:
          attestation_object: The `attestationObject` from the WebAuthn attestation response,
              base64url-encoded.

          client_data_json: The `clientDataJSON` from the WebAuthn attestation response, base64url-encoded.

          credential_id: The WebAuthn credential ID the authenticator returned, base64url-encoded.

          nickname: A name for this passkey, usually the device it lives on. 255 characters or
              fewer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/users/me/passkeys",
            body=await async_maybe_transform(
                {
                    "attestation_object": attestation_object,
                    "client_data_json": client_data_json,
                    "credential_id": credential_id,
                    "nickname": nickname,
                },
                passkey_create_params.PasskeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Passkey,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
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
    ) -> AsyncPaginator[Passkey, AsyncCursorPage[Passkey]]:
        """Lists the authenticated user's own passkeys, newest first.

        The list is always
        the caller's own; there is no parameter for reading another user's passkeys.
        Requires a user session: an API key or an OAuth token is refused, because a
        passkey confirms the account holder before a sensitive action and no app may
        enumerate one.

        Args:
          after: A cursor; returns passkeys after this position.

          before: A cursor; returns passkeys before this position.

          direction: Sort direction.

          first: The number of passkeys to return (default 20, max 100).

          last: The number of passkeys to return from the end of the range.

          order: The field to sort passkeys by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/passkeys",
            page=AsyncCursorPage[Passkey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    passkey_list_params.PasskeyListParams,
                ),
            ),
            model=Passkey,
        )

    async def delete(
        self,
        id: str,
        *,
        authenticator_data: str,
        client_data_json: str,
        signature: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PasskeyDeleteResponse:
        """Deletes one of the authenticated user's own passkeys.

        The request body carries a
        WebAuthn assertion from the passkey being deleted, so possession of the
        credential is proven before it is removed: mint a `deletion` challenge for it
        first, run the ceremony with that passkey, and send the result here. Deleting
        the user's last passkey is allowed — their other step-up factors remain.
        Requires a user session.

        Args:
          authenticator_data: The `authenticatorData` from the WebAuthn assertion, base64url-encoded.

          client_data_json: The `clientDataJSON` from the WebAuthn assertion, base64url-encoded.

          signature: The `signature` from the WebAuthn assertion, base64url-encoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/users/me/passkeys/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "authenticator_data": authenticator_data,
                    "client_data_json": client_data_json,
                    "signature": signature,
                },
                passkey_delete_params.PasskeyDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasskeyDeleteResponse,
        )

    async def challenge(
        self,
        *,
        challenge_type: Literal["registration", "deletion"],
        passkey_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PasskeyChallengeResponse:
        """
        Mints the challenge a browser needs to run a WebAuthn ceremony against the
        authenticated user's own passkeys. A `registration` challenge enrolls a new
        passkey; a `deletion` challenge is bound to the one passkey named by
        `passkey_id` and proves the user still holds it. Challenges are single-use and
        expire 5 minutes after they are issued, so send a fresh `Idempotency-Key` per
        ceremony — a replayed key returns the original challenge, which may already have
        expired. Requires a user session.

        Args:
          challenge_type: The ceremony this challenge is for.

          passkey_id: The passkey the ceremony targets, prefixed `wcred_`. Required when
              `challenge_type` is `deletion`, ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/users/me/passkeys/challenge",
            body=await async_maybe_transform(
                {
                    "challenge_type": challenge_type,
                    "passkey_id": passkey_id,
                },
                passkey_challenge_params.PasskeyChallengeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PasskeyChallengeResponse,
        )


class PasskeysResourceWithRawResponse:
    def __init__(self, passkeys: PasskeysResource) -> None:
        self._passkeys = passkeys

        self.create = to_raw_response_wrapper(
            passkeys.create,
        )
        self.list = to_raw_response_wrapper(
            passkeys.list,
        )
        self.delete = to_raw_response_wrapper(
            passkeys.delete,
        )
        self.challenge = to_raw_response_wrapper(
            passkeys.challenge,
        )


class AsyncPasskeysResourceWithRawResponse:
    def __init__(self, passkeys: AsyncPasskeysResource) -> None:
        self._passkeys = passkeys

        self.create = async_to_raw_response_wrapper(
            passkeys.create,
        )
        self.list = async_to_raw_response_wrapper(
            passkeys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            passkeys.delete,
        )
        self.challenge = async_to_raw_response_wrapper(
            passkeys.challenge,
        )


class PasskeysResourceWithStreamingResponse:
    def __init__(self, passkeys: PasskeysResource) -> None:
        self._passkeys = passkeys

        self.create = to_streamed_response_wrapper(
            passkeys.create,
        )
        self.list = to_streamed_response_wrapper(
            passkeys.list,
        )
        self.delete = to_streamed_response_wrapper(
            passkeys.delete,
        )
        self.challenge = to_streamed_response_wrapper(
            passkeys.challenge,
        )


class AsyncPasskeysResourceWithStreamingResponse:
    def __init__(self, passkeys: AsyncPasskeysResource) -> None:
        self._passkeys = passkeys

        self.create = async_to_streamed_response_wrapper(
            passkeys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            passkeys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            passkeys.delete,
        )
        self.challenge = async_to_streamed_response_wrapper(
            passkeys.challenge,
        )
