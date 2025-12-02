# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import setup_intent_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.shared.direction import Direction
from ..types.setup_intent_list_response import SetupIntentListResponse

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
        A setup intent is an object used to securely collect and store a member’s
        payment method for future use without charging them immediately. It handles
        authentication steps up front so future off-session payments can be completed
        smoothly. This ensures the payment method is verified and ready for later
        billing.

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
            f"/setup_intents/{id}",
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
        A setup intent is an object used to securely collect and store a member’s
        payment method for future use without charging them immediately. It handles
        authentication steps up front so future off-session payments can be completed
        smoothly. This ensures the payment method is verified and ready for later
        billing.

        Required permissions:

        - `payment:setup_intent:read`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to list setup intents for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

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
        A setup intent is an object used to securely collect and store a member’s
        payment method for future use without charging them immediately. It handles
        authentication steps up front so future off-session payments can be completed
        smoothly. This ensures the payment method is verified and ready for later
        billing.

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
            f"/setup_intents/{id}",
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
        A setup intent is an object used to securely collect and store a member’s
        payment method for future use without charging them immediately. It handles
        authentication steps up front so future off-session payments can be completed
        smoothly. This ensures the payment method is verified and ready for later
        billing.

        Required permissions:

        - `payment:setup_intent:read`
        - `member:basic:read`
        - `member:email:read`

        Args:
          company_id: The ID of the company to list setup intents for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

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
