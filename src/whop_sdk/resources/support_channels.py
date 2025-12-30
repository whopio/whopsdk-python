# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import support_channel_list_params, support_channel_create_params
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
from ..types.shared.direction import Direction
from ..types.shared.support_channel import SupportChannel
from ..types.support_channel_list_response import SupportChannelListResponse

__all__ = ["SupportChannelsResource", "AsyncSupportChannelsResource"]


class SupportChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupportChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return SupportChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return SupportChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SupportChannel:
        """Create a new support channel for a user in a company.

        If one already exists, it
        will return the existing one.

        Required permissions:

        - `support_chat:create`

        Args:
          company_id: The ID of the company to create the support chat in

          user_id: The ID (user_xxx) or username of the user to create the support chat for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/support_channels",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "user_id": user_id,
                },
                support_channel_create_params.SupportChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportChannel,
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
    ) -> SupportChannel:
        """
        Retrieves a support channel

        Required permissions:

        - `support_chat:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/support_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportChannel,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        open: Optional[bool] | Omit = omit,
        order: Optional[Literal["created_at", "last_post_sent_at"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[SupportChannelListResponse]:
        """
        Lists chat channels inside a company

        Required permissions:

        - `support_chat:read`

        Args:
          company_id: The ID of the company to list chat channels for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          open: Filter for tickets where customer sent the last message (needs response) AND not
              resolved. Set to true to only return open channels, false to only return
              resolved channels.

          order: Sort options for message channels

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/support_channels",
            page=SyncCursorPage[SupportChannelListResponse],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "open": open,
                        "order": order,
                    },
                    support_channel_list_params.SupportChannelListParams,
                ),
            ),
            model=SupportChannelListResponse,
        )


class AsyncSupportChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupportChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncSupportChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SupportChannel:
        """Create a new support channel for a user in a company.

        If one already exists, it
        will return the existing one.

        Required permissions:

        - `support_chat:create`

        Args:
          company_id: The ID of the company to create the support chat in

          user_id: The ID (user_xxx) or username of the user to create the support chat for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/support_channels",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "user_id": user_id,
                },
                support_channel_create_params.SupportChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportChannel,
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
    ) -> SupportChannel:
        """
        Retrieves a support channel

        Required permissions:

        - `support_chat:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/support_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportChannel,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        open: Optional[bool] | Omit = omit,
        order: Optional[Literal["created_at", "last_post_sent_at"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SupportChannelListResponse, AsyncCursorPage[SupportChannelListResponse]]:
        """
        Lists chat channels inside a company

        Required permissions:

        - `support_chat:read`

        Args:
          company_id: The ID of the company to list chat channels for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          open: Filter for tickets where customer sent the last message (needs response) AND not
              resolved. Set to true to only return open channels, false to only return
              resolved channels.

          order: Sort options for message channels

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/support_channels",
            page=AsyncCursorPage[SupportChannelListResponse],
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
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "open": open,
                        "order": order,
                    },
                    support_channel_list_params.SupportChannelListParams,
                ),
            ),
            model=SupportChannelListResponse,
        )


class SupportChannelsResourceWithRawResponse:
    def __init__(self, support_channels: SupportChannelsResource) -> None:
        self._support_channels = support_channels

        self.create = to_raw_response_wrapper(
            support_channels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            support_channels.retrieve,
        )
        self.list = to_raw_response_wrapper(
            support_channels.list,
        )


class AsyncSupportChannelsResourceWithRawResponse:
    def __init__(self, support_channels: AsyncSupportChannelsResource) -> None:
        self._support_channels = support_channels

        self.create = async_to_raw_response_wrapper(
            support_channels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            support_channels.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            support_channels.list,
        )


class SupportChannelsResourceWithStreamingResponse:
    def __init__(self, support_channels: SupportChannelsResource) -> None:
        self._support_channels = support_channels

        self.create = to_streamed_response_wrapper(
            support_channels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            support_channels.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            support_channels.list,
        )


class AsyncSupportChannelsResourceWithStreamingResponse:
    def __init__(self, support_channels: AsyncSupportChannelsResource) -> None:
        self._support_channels = support_channels

        self.create = async_to_streamed_response_wrapper(
            support_channels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            support_channels.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            support_channels.list,
        )
