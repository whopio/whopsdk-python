# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import chat_channel_list_params, chat_channel_update_params
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
from ..types.shared.chat_channel import ChatChannel
from ..types.shared.who_can_post import WhoCanPost
from ..types.shared.who_can_react import WhoCanReact
from ..types.chat_channel_list_response import ChatChannelListResponse

__all__ = ["ChatChannelsResource", "AsyncChatChannelsResource"]


class ChatChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ChatChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ChatChannelsResourceWithStreamingResponse(self)

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
    ) -> ChatChannel:
        """
        Retrieves the details of an existing chat channel.

        Required permissions:

        - `chat:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/chat_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatChannel,
        )

    def update(
        self,
        id: str,
        *,
        ban_media: Optional[bool] | Omit = omit,
        ban_urls: Optional[bool] | Omit = omit,
        banned_words: Optional[SequenceNotStr[str]] | Omit = omit,
        user_posts_cooldown_seconds: Optional[int] | Omit = omit,
        who_can_post: Optional[WhoCanPost] | Omit = omit,
        who_can_react: Optional[WhoCanReact] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatChannel:
        """
        Update moderation settings for a chat channel, such as who can post, banned
        words, and media restrictions.

        Required permissions:

        - `chat:moderate`

        Args:
          ban_media: Whether media uploads such as images and videos are banned in this chat channel.

          ban_urls: Whether URLs and links are banned from being posted in this chat channel.

          banned_words: A list of words that are automatically blocked from messages in this chat
              channel. For example, ['spam', 'scam'].

          user_posts_cooldown_seconds: The minimum number of seconds a user must wait between sending messages in this
              chat channel.

          who_can_post: Who can post on a chat feed

          who_can_react: Who can react on a chat feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/chat_channels/{id}",
            body=maybe_transform(
                {
                    "ban_media": ban_media,
                    "ban_urls": ban_urls,
                    "banned_words": banned_words,
                    "user_posts_cooldown_seconds": user_posts_cooldown_seconds,
                    "who_can_post": who_can_post,
                    "who_can_react": who_can_react,
                },
                chat_channel_update_params.ChatChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatChannel,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ChatChannelListResponse]:
        """
        Returns a paginated list of chat channels within a specific company, with
        optional filtering by product.

        Required permissions:

        - `chat:read`

        Args:
          company_id: The unique identifier of the company to list chat channels for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_id: The unique identifier of a product to filter by. When set, only chat channels
              connected to this product are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/chat_channels",
            page=SyncCursorPage[ChatChannelListResponse],
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
                        "first": first,
                        "last": last,
                        "product_id": product_id,
                    },
                    chat_channel_list_params.ChatChannelListParams,
                ),
            ),
            model=ChatChannelListResponse,
        )


class AsyncChatChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncChatChannelsResourceWithStreamingResponse(self)

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
    ) -> ChatChannel:
        """
        Retrieves the details of an existing chat channel.

        Required permissions:

        - `chat:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/chat_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatChannel,
        )

    async def update(
        self,
        id: str,
        *,
        ban_media: Optional[bool] | Omit = omit,
        ban_urls: Optional[bool] | Omit = omit,
        banned_words: Optional[SequenceNotStr[str]] | Omit = omit,
        user_posts_cooldown_seconds: Optional[int] | Omit = omit,
        who_can_post: Optional[WhoCanPost] | Omit = omit,
        who_can_react: Optional[WhoCanReact] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatChannel:
        """
        Update moderation settings for a chat channel, such as who can post, banned
        words, and media restrictions.

        Required permissions:

        - `chat:moderate`

        Args:
          ban_media: Whether media uploads such as images and videos are banned in this chat channel.

          ban_urls: Whether URLs and links are banned from being posted in this chat channel.

          banned_words: A list of words that are automatically blocked from messages in this chat
              channel. For example, ['spam', 'scam'].

          user_posts_cooldown_seconds: The minimum number of seconds a user must wait between sending messages in this
              chat channel.

          who_can_post: Who can post on a chat feed

          who_can_react: Who can react on a chat feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/chat_channels/{id}",
            body=await async_maybe_transform(
                {
                    "ban_media": ban_media,
                    "ban_urls": ban_urls,
                    "banned_words": banned_words,
                    "user_posts_cooldown_seconds": user_posts_cooldown_seconds,
                    "who_can_post": who_can_post,
                    "who_can_react": who_can_react,
                },
                chat_channel_update_params.ChatChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatChannel,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChatChannelListResponse, AsyncCursorPage[ChatChannelListResponse]]:
        """
        Returns a paginated list of chat channels within a specific company, with
        optional filtering by product.

        Required permissions:

        - `chat:read`

        Args:
          company_id: The unique identifier of the company to list chat channels for.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_id: The unique identifier of a product to filter by. When set, only chat channels
              connected to this product are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/chat_channels",
            page=AsyncCursorPage[ChatChannelListResponse],
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
                        "first": first,
                        "last": last,
                        "product_id": product_id,
                    },
                    chat_channel_list_params.ChatChannelListParams,
                ),
            ),
            model=ChatChannelListResponse,
        )


class ChatChannelsResourceWithRawResponse:
    def __init__(self, chat_channels: ChatChannelsResource) -> None:
        self._chat_channels = chat_channels

        self.retrieve = to_raw_response_wrapper(
            chat_channels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            chat_channels.update,
        )
        self.list = to_raw_response_wrapper(
            chat_channels.list,
        )


class AsyncChatChannelsResourceWithRawResponse:
    def __init__(self, chat_channels: AsyncChatChannelsResource) -> None:
        self._chat_channels = chat_channels

        self.retrieve = async_to_raw_response_wrapper(
            chat_channels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            chat_channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            chat_channels.list,
        )


class ChatChannelsResourceWithStreamingResponse:
    def __init__(self, chat_channels: ChatChannelsResource) -> None:
        self._chat_channels = chat_channels

        self.retrieve = to_streamed_response_wrapper(
            chat_channels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            chat_channels.update,
        )
        self.list = to_streamed_response_wrapper(
            chat_channels.list,
        )


class AsyncChatChannelsResourceWithStreamingResponse:
    def __init__(self, chat_channels: AsyncChatChannelsResource) -> None:
        self._chat_channels = chat_channels

        self.retrieve = async_to_streamed_response_wrapper(
            chat_channels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            chat_channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            chat_channels.list,
        )
