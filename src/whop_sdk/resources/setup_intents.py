# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import overload

import httpx

from ..types import setup_intent_list_params, setup_intent_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ..types.setup_intent import SetupIntent
from ..types.shared.currency import Currency
from ..types.shared.direction import Direction
from ..types.setup_intent_list_response import SetupIntentListResponse
from ..types.setup_intent_retrieve_status_response import SetupIntentRetrieveStatusResponse

__all__ = ["SetupIntentsResource", "AsyncSetupIntentsResource"]


class SetupIntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SetupIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return SetupIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SetupIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return SetupIntentsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        company_id: str,
        confirmation_token: str,
        currency: Optional[Currency] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntent:
        """Save a buyer's payment method for later without charging it.

        Provide a
        confirmation token for a method the buyer just supplied, or an existing payment
        method to re-verify. The buyer may still have a step to complete — 3D Secure, a
        hosted enrollment, linking a bank account — so poll the setup intent's status
        endpoint for what to do next.

        Required permissions:

        - `payment:charge`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to save the payment method for.

          confirmation_token: A confirmation token ID (ctok\\__) describing a payment method the buyer just
              supplied. Provide this or payment_method_id, not both.

          currency: The available currencies on the platform

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the method belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the setup intent.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials, at most 2,048 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        company_id: str,
        payment_method_id: str,
        currency: Optional[Currency] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntent:
        """Save a buyer's payment method for later without charging it.

        Provide a
        confirmation token for a method the buyer just supplied, or an existing payment
        method to re-verify. The buyer may still have a step to complete — 3D Secure, a
        hosted enrollment, linking a bank account — so poll the setup intent's status
        endpoint for what to do next.

        Required permissions:

        - `payment:charge`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to save the payment method for.

          payment_method_id: An existing payment method (payt\\__) to re-verify and save. Provide this or
              confirmation_token, not both.

          currency: The available currencies on the platform

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the method belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the setup intent.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials, at most 2,048 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["company_id", "confirmation_token"], ["company_id", "payment_method_id"])
    def create(
        self,
        *,
        company_id: str,
        confirmation_token: str | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        payment_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntent:
        return self._post(
            "/setup_intents",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "confirmation_token": confirmation_token,
                    "currency": currency,
                    "email": email,
                    "metadata": metadata,
                    "return_url": return_url,
                    "payment_method_id": payment_method_id,
                },
                setup_intent_create_params.SetupIntentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntent,
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
    ) -> SetupIntent:
        """
        Retrieves the details of an existing setup intent.

        Required permissions:

        - `payment:setup_intent:read`
        - `member:basic:read`
        - `member:email:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/setup_intents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntent,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[SetupIntentListResponse]:
        """
        Returns a paginated list of setup intents for a company, with optional filtering
        by creation date. A setup intent securely collects and stores a member's payment
        method for future use without charging them immediately.

        Required permissions:

        - `payment:setup_intent:read`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The unique identifier of the company to list setup intents for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return setup intents created after this timestamp.

          created_before: Only return setup intents created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/setup_intents",
            page=SyncCursorPage[SetupIntentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    setup_intent_list_params.SetupIntentListParams,
                ),
            ),
            model=SetupIntentListResponse,
        )

    def retrieve_status(
        self,
        setup_intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntentRetrieveStatusResponse:
        """
        Retrieves how far a setup has got and what the buyer must do next, if anything.
        Collection runs in the background, so poll this rather than reading the create
        response. Accepts either a secret key or the setup's own `client_secret`, so the
        surface collecting the payment method can poll it directly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not setup_intent_id:
            raise ValueError(f"Expected a non-empty value for `setup_intent_id` but received {setup_intent_id!r}")
        return self._get(
            path_template("/setup_intents/{setup_intent_id}/status", setup_intent_id=setup_intent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntentRetrieveStatusResponse,
        )


class AsyncSetupIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSetupIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSetupIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSetupIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncSetupIntentsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        company_id: str,
        confirmation_token: str,
        currency: Optional[Currency] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntent:
        """Save a buyer's payment method for later without charging it.

        Provide a
        confirmation token for a method the buyer just supplied, or an existing payment
        method to re-verify. The buyer may still have a step to complete — 3D Secure, a
        hosted enrollment, linking a bank account — so poll the setup intent's status
        endpoint for what to do next.

        Required permissions:

        - `payment:charge`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to save the payment method for.

          confirmation_token: A confirmation token ID (ctok\\__) describing a payment method the buyer just
              supplied. Provide this or payment_method_id, not both.

          currency: The available currencies on the platform

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the method belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the setup intent.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials, at most 2,048 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        company_id: str,
        payment_method_id: str,
        currency: Optional[Currency] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntent:
        """Save a buyer's payment method for later without charging it.

        Provide a
        confirmation token for a method the buyer just supplied, or an existing payment
        method to re-verify. The buyer may still have a step to complete — 3D Secure, a
        hosted enrollment, linking a bank account — so poll the setup intent's status
        endpoint for what to do next.

        Required permissions:

        - `payment:charge`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to save the payment method for.

          payment_method_id: An existing payment method (payt\\__) to re-verify and save. Provide this or
              confirmation_token, not both.

          currency: The available currencies on the platform

          email: Overrides the buyer email carried on the confirmation token, resolving or
              creating the Whop user the method belongs to. Ignored when the confirmation
              token was created by a signed-in buyer, and unless confirmation_token is
              provided.

          metadata: Custom metadata to attach to the setup intent.

          return_url: Where the buyer continues after completing an off-site step. Must be an absolute
              https URL without credentials, at most 2,048 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["company_id", "confirmation_token"], ["company_id", "payment_method_id"])
    async def create(
        self,
        *,
        company_id: str,
        confirmation_token: str | Omit = omit,
        currency: Optional[Currency] | Omit = omit,
        email: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        return_url: Optional[str] | Omit = omit,
        payment_method_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntent:
        return await self._post(
            "/setup_intents",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "confirmation_token": confirmation_token,
                    "currency": currency,
                    "email": email,
                    "metadata": metadata,
                    "return_url": return_url,
                    "payment_method_id": payment_method_id,
                },
                setup_intent_create_params.SetupIntentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntent,
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
    ) -> SetupIntent:
        """
        Retrieves the details of an existing setup intent.

        Required permissions:

        - `payment:setup_intent:read`
        - `member:basic:read`
        - `member:email:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/setup_intents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntent,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SetupIntentListResponse, AsyncCursorPage[SetupIntentListResponse]]:
        """
        Returns a paginated list of setup intents for a company, with optional filtering
        by creation date. A setup intent securely collects and stores a member's payment
        method for future use without charging them immediately.

        Required permissions:

        - `payment:setup_intent:read`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The unique identifier of the company to list setup intents for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: Only return setup intents created after this timestamp.

          created_before: Only return setup intents created before this timestamp.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/setup_intents",
            page=AsyncCursorPage[SetupIntentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                    },
                    setup_intent_list_params.SetupIntentListParams,
                ),
            ),
            model=SetupIntentListResponse,
        )

    async def retrieve_status(
        self,
        setup_intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupIntentRetrieveStatusResponse:
        """
        Retrieves how far a setup has got and what the buyer must do next, if anything.
        Collection runs in the background, so poll this rather than reading the create
        response. Accepts either a secret key or the setup's own `client_secret`, so the
        surface collecting the payment method can poll it directly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not setup_intent_id:
            raise ValueError(f"Expected a non-empty value for `setup_intent_id` but received {setup_intent_id!r}")
        return await self._get(
            path_template("/setup_intents/{setup_intent_id}/status", setup_intent_id=setup_intent_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntentRetrieveStatusResponse,
        )


class SetupIntentsResourceWithRawResponse:
    def __init__(self, setup_intents: SetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.create = to_raw_response_wrapper(
            setup_intents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            setup_intents.list,
        )
        self.retrieve_status = to_raw_response_wrapper(
            setup_intents.retrieve_status,
        )


class AsyncSetupIntentsResourceWithRawResponse:
    def __init__(self, setup_intents: AsyncSetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.create = async_to_raw_response_wrapper(
            setup_intents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            setup_intents.list,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            setup_intents.retrieve_status,
        )


class SetupIntentsResourceWithStreamingResponse:
    def __init__(self, setup_intents: SetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.create = to_streamed_response_wrapper(
            setup_intents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            setup_intents.list,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            setup_intents.retrieve_status,
        )


class AsyncSetupIntentsResourceWithStreamingResponse:
    def __init__(self, setup_intents: AsyncSetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.create = async_to_streamed_response_wrapper(
            setup_intents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            setup_intents.list,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            setup_intents.retrieve_status,
        )
