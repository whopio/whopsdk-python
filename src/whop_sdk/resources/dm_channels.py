# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import dm_channel_list_params, dm_channel_create_params, dm_channel_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.dm_channel import DmChannel
from ..types.dm_channel_list_response import DmChannelListResponse
from ..types.dm_channel_delete_response import DmChannelDeleteResponse

__all__ = ["DmChannelsResource", "AsyncDmChannelsResource"]


class DmChannelsResource(SyncAPIResource):
    """Dm channels"""

    @cached_property
    def with_raw_response(self) -> DmChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return DmChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DmChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return DmChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        with_user_ids: SequenceNotStr[str],
        company_id: Optional[str] | Omit = omit,
        custom_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmChannel:
        """
        Create a new DM channel between two or more users, optionally scoped to a
        specific company. Returns the existing channel if one already exists.

        Args:
          with_user_ids: The list of user identifiers to include in the DM channel. Each entry can be an
              email, username, or user ID (e.g. 'user_xxxxx').

          company_id: The unique identifier of the company to scope this DM channel to. When set, the
              channel is visible only within that company context.

          custom_name: A custom display name for the DM channel. For example, 'Project Discussion'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dm_channels",
            body=maybe_transform(
                {
                    "with_user_ids": with_user_ids,
                    "company_id": company_id,
                    "custom_name": custom_name,
                },
                dm_channel_create_params.DmChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannel,
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
    ) -> DmChannel:
        """
        Retrieves the details of an existing DM channel.

        Required permissions:

        - `dms:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/dm_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannel,
        )

    def update(
        self,
        id: str,
        *,
        custom_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmChannel:
        """Update the settings of an existing DM channel, such as its display name.

        Only an
        admin of the channel can perform this action.

        Required permissions:

        - `dms:channel:manage`

        Args:
          custom_name: A new custom display name for the DM channel. For example, 'Project Discussion'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/dm_channels/{id}",
            body=maybe_transform({"custom_name": custom_name}, dm_channel_update_params.DmChannelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannel,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[DmChannelListResponse]:
        """
        Returns a paginated list of DM channels for the currently authenticated user,
        sorted by most recently active.

        Required permissions:

        - `dms:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of a company to filter DM channels by. Only returns
              channels scoped to this company.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dm_channels",
            page=SyncCursorPage[DmChannelListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "first": first,
                        "last": last,
                    },
                    dm_channel_list_params.DmChannelListParams,
                ),
            ),
            model=DmChannelListResponse,
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
    ) -> DmChannelDeleteResponse:
        """Permanently delete a DM channel and all of its messages.

        Only an admin of the
        channel can perform this action.

        Required permissions:

        - `dms:channel:manage`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/dm_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannelDeleteResponse,
        )


class AsyncDmChannelsResource(AsyncAPIResource):
    """Dm channels"""

    @cached_property
    def with_raw_response(self) -> AsyncDmChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDmChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDmChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncDmChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        with_user_ids: SequenceNotStr[str],
        company_id: Optional[str] | Omit = omit,
        custom_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmChannel:
        """
        Create a new DM channel between two or more users, optionally scoped to a
        specific company. Returns the existing channel if one already exists.

        Args:
          with_user_ids: The list of user identifiers to include in the DM channel. Each entry can be an
              email, username, or user ID (e.g. 'user_xxxxx').

          company_id: The unique identifier of the company to scope this DM channel to. When set, the
              channel is visible only within that company context.

          custom_name: A custom display name for the DM channel. For example, 'Project Discussion'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dm_channels",
            body=await async_maybe_transform(
                {
                    "with_user_ids": with_user_ids,
                    "company_id": company_id,
                    "custom_name": custom_name,
                },
                dm_channel_create_params.DmChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannel,
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
    ) -> DmChannel:
        """
        Retrieves the details of an existing DM channel.

        Required permissions:

        - `dms:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/dm_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannel,
        )

    async def update(
        self,
        id: str,
        *,
        custom_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmChannel:
        """Update the settings of an existing DM channel, such as its display name.

        Only an
        admin of the channel can perform this action.

        Required permissions:

        - `dms:channel:manage`

        Args:
          custom_name: A new custom display name for the DM channel. For example, 'Project Discussion'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/dm_channels/{id}",
            body=await async_maybe_transform(
                {"custom_name": custom_name}, dm_channel_update_params.DmChannelUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannel,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DmChannelListResponse, AsyncCursorPage[DmChannelListResponse]]:
        """
        Returns a paginated list of DM channels for the currently authenticated user,
        sorted by most recently active.

        Required permissions:

        - `dms:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of a company to filter DM channels by. Only returns
              channels scoped to this company.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dm_channels",
            page=AsyncCursorPage[DmChannelListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "first": first,
                        "last": last,
                    },
                    dm_channel_list_params.DmChannelListParams,
                ),
            ),
            model=DmChannelListResponse,
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
    ) -> DmChannelDeleteResponse:
        """Permanently delete a DM channel and all of its messages.

        Only an admin of the
        channel can perform this action.

        Required permissions:

        - `dms:channel:manage`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/dm_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmChannelDeleteResponse,
        )


class DmChannelsResourceWithRawResponse:
    def __init__(self, dm_channels: DmChannelsResource) -> None:
        self._dm_channels = dm_channels

        self.create = to_raw_response_wrapper(
            dm_channels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dm_channels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dm_channels.update,
        )
        self.list = to_raw_response_wrapper(
            dm_channels.list,
        )
        self.delete = to_raw_response_wrapper(
            dm_channels.delete,
        )


class AsyncDmChannelsResourceWithRawResponse:
    def __init__(self, dm_channels: AsyncDmChannelsResource) -> None:
        self._dm_channels = dm_channels

        self.create = async_to_raw_response_wrapper(
            dm_channels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dm_channels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dm_channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            dm_channels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dm_channels.delete,
        )


class DmChannelsResourceWithStreamingResponse:
    def __init__(self, dm_channels: DmChannelsResource) -> None:
        self._dm_channels = dm_channels

        self.create = to_streamed_response_wrapper(
            dm_channels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dm_channels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dm_channels.update,
        )
        self.list = to_streamed_response_wrapper(
            dm_channels.list,
        )
        self.delete = to_streamed_response_wrapper(
            dm_channels.delete,
        )


class AsyncDmChannelsResourceWithStreamingResponse:
    def __init__(self, dm_channels: AsyncDmChannelsResource) -> None:
        self._dm_channels = dm_channels

        self.create = async_to_streamed_response_wrapper(
            dm_channels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dm_channels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dm_channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dm_channels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dm_channels.delete,
        )
