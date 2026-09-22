# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import setup_intent_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given
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

__all__ = ["SetupIntentsResource", "AsyncSetupIntentsResource"]


class SetupIntentsResource(SyncAPIResource):
    """A Setup Intent saves a buyer's payment method for later without taking money now.

    Create one from a confirmation token the payment elements collected in setup mode, or from a payment method already on file to re-verify it. It runs the same collection flow a payment does, so the buyer may still owe a step: 3D Secure on a card, a hosted enrollment, or linking a bank account.

    The create response is the setup intent as created, not its outcome. Hand its `client_secret` to the elements' `handleNextAction`, or poll [Retrieve status](/api-reference/beta/setup-intents/retrieve-setup-status) for how far the setup has gone and what is outstanding. Once it reaches `succeeded`, `payment_method_id` names the saved method and Create Payment charges it.
    """

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
    ) -> SetupIntent:
        """Returns one setup intent.

        Related records are ids — once `status` is
        `succeeded`, `payment_method_id` is the saved method to charge or retrieve. The
        buyer's own token may retrieve a setup intent that belongs to it.

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
            path_template("/setup_intents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntent,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        status: Literal["processing", "succeeded", "canceled", "requires_action"] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[SetupIntent]:
        """Lists setup intents newest first.

        An account API key lists its own account; a
        user token lists every account it can read, or one account with `account_id`.
        `client_secret` is always null on list rows — retrieve the setup intent for it.

        Args:
          account_id: Only setup intents for this account, prefixed `biz_`.

          after: Return results after this cursor. Use `page_info.end_cursor` from the previous
              response to fetch the next page.

          before: Return results before this cursor. Use `page_info.start_cursor` from the
              previous response to fetch the previous page.

          created_after: Only setup intents created after this ISO 8601 timestamp.

          created_before: Only setup intents created before this ISO 8601 timestamp.

          direction: The sort direction.

          first: Number of results to return from the start of the range.

          last: Number of results to return from the end of the range.

          order: The field to sort by.

          status: Only setup intents in this state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/setup_intents",
            page=SyncCursorPage[SetupIntent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    setup_intent_list_params.SetupIntentListParams,
                ),
            ),
            model=SetupIntent,
        )


class AsyncSetupIntentsResource(AsyncAPIResource):
    """A Setup Intent saves a buyer's payment method for later without taking money now.

    Create one from a confirmation token the payment elements collected in setup mode, or from a payment method already on file to re-verify it. It runs the same collection flow a payment does, so the buyer may still owe a step: 3D Secure on a card, a hosted enrollment, or linking a bank account.

    The create response is the setup intent as created, not its outcome. Hand its `client_secret` to the elements' `handleNextAction`, or poll [Retrieve status](/api-reference/beta/setup-intents/retrieve-setup-status) for how far the setup has gone and what is outstanding. Once it reaches `succeeded`, `payment_method_id` names the saved method and Create Payment charges it.
    """

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
    ) -> SetupIntent:
        """Returns one setup intent.

        Related records are ids — once `status` is
        `succeeded`, `payment_method_id` is the saved method to charge or retrieve. The
        buyer's own token may retrieve a setup intent that belongs to it.

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
            path_template("/setup_intents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupIntent,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        status: Literal["processing", "succeeded", "canceled", "requires_action"] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SetupIntent, AsyncCursorPage[SetupIntent]]:
        """Lists setup intents newest first.

        An account API key lists its own account; a
        user token lists every account it can read, or one account with `account_id`.
        `client_secret` is always null on list rows — retrieve the setup intent for it.

        Args:
          account_id: Only setup intents for this account, prefixed `biz_`.

          after: Return results after this cursor. Use `page_info.end_cursor` from the previous
              response to fetch the next page.

          before: Return results before this cursor. Use `page_info.start_cursor` from the
              previous response to fetch the previous page.

          created_after: Only setup intents created after this ISO 8601 timestamp.

          created_before: Only setup intents created before this ISO 8601 timestamp.

          direction: The sort direction.

          first: Number of results to return from the start of the range.

          last: Number of results to return from the end of the range.

          order: The field to sort by.

          status: Only setup intents in this state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/setup_intents",
            page=AsyncCursorPage[SetupIntent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "status": status,
                    },
                    setup_intent_list_params.SetupIntentListParams,
                ),
            ),
            model=SetupIntent,
        )


class SetupIntentsResourceWithRawResponse:
    def __init__(self, setup_intents: SetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.retrieve = to_raw_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            setup_intents.list,
        )


class AsyncSetupIntentsResourceWithRawResponse:
    def __init__(self, setup_intents: AsyncSetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.retrieve = async_to_raw_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            setup_intents.list,
        )


class SetupIntentsResourceWithStreamingResponse:
    def __init__(self, setup_intents: SetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.retrieve = to_streamed_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            setup_intents.list,
        )


class AsyncSetupIntentsResourceWithStreamingResponse:
    def __init__(self, setup_intents: AsyncSetupIntentsResource) -> None:
        self._setup_intents = setup_intents

        self.retrieve = async_to_streamed_response_wrapper(
            setup_intents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            setup_intents.list,
        )
