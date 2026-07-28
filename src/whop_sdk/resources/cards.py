# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import card_list_params, card_create_params, card_update_params, card_retrieve_params
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
from .._base_client import make_request_options
from ..types.card_list_response import CardListResponse
from ..types.card_create_response import CardCreateResponse
from ..types.card_update_response import CardUpdateResponse
from ..types.card_retrieve_response import CardRetrieveResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    """
    Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

    Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
    """

    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | Omit = omit,
        assigned_user_id: str | Omit = omit,
        name: str | Omit = omit,
        spend_limit: float | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: float | Omit = omit,
        user_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardCreateResponse:
        """Issues a virtual card.

        For an individual (consumer) card issuing account, the
        card is issued to the account's own cardholder. For a business card issuing
        account, pass assigned*user_id to issue the card to a member of the account; if
        that member is not yet an approved card-issuing user, the card is provisioned
        asynchronously or an onboarding invitation is sent (HTTP 202). If the account
        has never applied for card issuing, a card application is submitted first and
        returned instead of a card (HTTP 202). Track it with capabilities.card_issuing
        on GET /accounts/{account_id}, answer any requested_information on GET
        /verifications/{account_id}, and call this endpoint again once the application
        is approved; calling it earlier returns HTTP 409. An account with an approved
        KYB applies as the business entity; otherwise the application uses the approved
        identity verification of assigned_user_id, falling back to the user the
        credential belongs to. A user credential may only pass its own user id as
        assigned_user_id; an account API key may pass any member of that account, and
        must pass one to submit an application. Pass exactly one of account_id (a biz*
        identifier) or user*id (a user* identifier). Returns the newly created card
        resource.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          assigned_user_id: The account member (a user\\__ identifier) to assign the card to. Required for
              business card issuing accounts.

          name: A display name for the card.

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The spending limit window.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "assigned_user_id": assigned_user_id,
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
        )

    def retrieve(
        self,
        card_id: str,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardRetrieveResponse:
        """
        Retrieves a single card by its icrd\\__ identifier, including its secrets (full
        card number, CVC, and cardholder name) for active cards. The card PIN is
        included only when the request is authenticated as the user the card is assigned
        to.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            path_template("/cards/{card_id}", card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    card_retrieve_params.CardRetrieveParams,
                ),
            ),
            cast_to=CardRetrieveResponse,
        )

    def update(
        self,
        card_id: str,
        *,
        account_id: str | Omit = omit,
        billing: card_update_params.Billing | Omit = omit,
        canceled: bool | Omit = omit,
        frozen: bool | Omit = omit,
        name: str | Omit = omit,
        pin: str | Omit = omit,
        remove_limit: bool | Omit = omit,
        spend_limit: float | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: float | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardUpdateResponse:
        """Updates an issued card.

        All fields are optional; only the fields you pass are
        changed. Updates the card name, billing address, and spending limits in one
        call, sets a new PIN, freezes or unfreezes the card, or cancels it. Pass
        canceled: true alone to cancel the card — cancellation is permanent and a
        canceled card cannot be uncanceled. Pass exactly one of account*id (a biz*
        identifier) or user*id (a user* identifier). Assigned cardholders without the
        payout:account:update scope can update the PIN and freeze state of their own
        card. The PIN can only be changed on a card assigned to the acting user. Returns
        the updated card resource. For a card in the invited status, the invited user
        completes card onboarding by passing only a billing address: their verified
        identity is registered with the card issuer and card provisioning starts (the
        card is returned and can be polled until issued). The invited user must have an
        approved identity verification on their Whop account. No other fields can be
        updated until the card is issued.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          billing: New billing address. Requires line1, city, region, postal_code, and
              country_code. On an invited card, passing billing alone (as the invited user)
              completes onboarding and starts card provisioning.

          canceled: Pass `true` to permanently cancel the card. A canceled card cannot be
              uncanceled. Cannot be combined with other fields.

          frozen: Pass `true` to freeze the card, `false` to unfreeze it.

          name: A display name for the card.

          pin: New 4-digit PIN. Can only be set on a card assigned to the acting user.

          remove_limit: Pass `true` to remove the spending limit (make the card unlimited).

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The spending limit window.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._patch(
            path_template("/cards/{card_id}", card_id=card_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "billing": billing,
                    "canceled": canceled,
                    "frozen": frozen,
                    "name": name,
                    "pin": pin,
                    "remove_limit": remove_limit,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Lists issued Whop virtual cards for an account or user, including pending
        invitation cards that have not been issued by the card provider yet. Pass
        exactly one of account*id (a biz* identifier) or user*id (a user* identifier).
        Non-owner team members only see cards assigned to them. Users without the
        payout:account:read scope can still list cards assigned to them (for example
        moderators or external cardholders). Use GET /cards/:card_id to retrieve a
        single card with its secrets.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    """
    Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

    Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | Omit = omit,
        assigned_user_id: str | Omit = omit,
        name: str | Omit = omit,
        spend_limit: float | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: float | Omit = omit,
        user_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardCreateResponse:
        """Issues a virtual card.

        For an individual (consumer) card issuing account, the
        card is issued to the account's own cardholder. For a business card issuing
        account, pass assigned*user_id to issue the card to a member of the account; if
        that member is not yet an approved card-issuing user, the card is provisioned
        asynchronously or an onboarding invitation is sent (HTTP 202). If the account
        has never applied for card issuing, a card application is submitted first and
        returned instead of a card (HTTP 202). Track it with capabilities.card_issuing
        on GET /accounts/{account_id}, answer any requested_information on GET
        /verifications/{account_id}, and call this endpoint again once the application
        is approved; calling it earlier returns HTTP 409. An account with an approved
        KYB applies as the business entity; otherwise the application uses the approved
        identity verification of assigned_user_id, falling back to the user the
        credential belongs to. A user credential may only pass its own user id as
        assigned_user_id; an account API key may pass any member of that account, and
        must pass one to submit an application. Pass exactly one of account_id (a biz*
        identifier) or user*id (a user* identifier). Returns the newly created card
        resource.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          assigned_user_id: The account member (a user\\__ identifier) to assign the card to. Required for
              business card issuing accounts.

          name: A display name for the card.

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The spending limit window.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/cards",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "assigned_user_id": assigned_user_id,
                    "name": name,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
        )

    async def retrieve(
        self,
        card_id: str,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardRetrieveResponse:
        """
        Retrieves a single card by its icrd\\__ identifier, including its secrets (full
        card number, CVC, and cardholder name) for active cards. The card PIN is
        included only when the request is authenticated as the user the card is assigned
        to.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            path_template("/cards/{card_id}", card_id=card_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    card_retrieve_params.CardRetrieveParams,
                ),
            ),
            cast_to=CardRetrieveResponse,
        )

    async def update(
        self,
        card_id: str,
        *,
        account_id: str | Omit = omit,
        billing: card_update_params.Billing | Omit = omit,
        canceled: bool | Omit = omit,
        frozen: bool | Omit = omit,
        name: str | Omit = omit,
        pin: str | Omit = omit,
        remove_limit: bool | Omit = omit,
        spend_limit: float | Omit = omit,
        spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"] | Omit = omit,
        transaction_limit: float | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardUpdateResponse:
        """Updates an issued card.

        All fields are optional; only the fields you pass are
        changed. Updates the card name, billing address, and spending limits in one
        call, sets a new PIN, freezes or unfreezes the card, or cancels it. Pass
        canceled: true alone to cancel the card — cancellation is permanent and a
        canceled card cannot be uncanceled. Pass exactly one of account*id (a biz*
        identifier) or user*id (a user* identifier). Assigned cardholders without the
        payout:account:update scope can update the PIN and freeze state of their own
        card. The PIN can only be changed on a card assigned to the acting user. Returns
        the updated card resource. For a card in the invited status, the invited user
        completes card onboarding by passing only a billing address: their verified
        identity is registered with the card issuer and card provisioning starts (the
        card is returned and can be polled until issued). The invited user must have an
        approved identity verification on their Whop account. No other fields can be
        updated until the card is issued.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          billing: New billing address. Requires line1, city, region, postal_code, and
              country_code. On an invited card, passing billing alone (as the invited user)
              completes onboarding and starts card provisioning.

          canceled: Pass `true` to permanently cancel the card. A canceled card cannot be
              uncanceled. Cannot be combined with other fields.

          frozen: Pass `true` to freeze the card, `false` to unfreeze it.

          name: A display name for the card.

          pin: New 4-digit PIN. Can only be set on a card assigned to the acting user.

          remove_limit: Pass `true` to remove the spending limit (make the card unlimited).

          spend_limit: Spending limit amount, in dollars.

          spend_limit_frequency: The spending limit window.

          transaction_limit: Per-transaction limit amount, in dollars.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._patch(
            path_template("/cards/{card_id}", card_id=card_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "billing": billing,
                    "canceled": canceled,
                    "frozen": frozen,
                    "name": name,
                    "pin": pin,
                    "remove_limit": remove_limit,
                    "spend_limit": spend_limit,
                    "spend_limit_frequency": spend_limit_frequency,
                    "transaction_limit": transaction_limit,
                    "user_id": user_id,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardUpdateResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Lists issued Whop virtual cards for an account or user, including pending
        invitation cards that have not been issued by the card provider yet. Pass
        exactly one of account*id (a biz* identifier) or user*id (a user* identifier).
        Non-owner team members only see cards assigned to them. Users without the
        payout:account:read scope can still list cards assigned to them (for example
        moderators or external cardholders). Use GET /cards/:card_id to retrieve a
        single card with its secrets.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "user_id": user_id,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            cast_to=CardListResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cards.update,
        )
        self.list = to_raw_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            cards.list,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.create = to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cards.update,
        )
        self.list = to_streamed_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.create = async_to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
