# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import ai_chat_list_params, ai_chat_create_params, ai_chat_update_params
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
from ..types.ai_chat import AIChat
from ..types.ai_chat_list_response import AIChatListResponse
from ..types.ai_chat_delete_response import AIChatDeleteResponse

__all__ = ["AIChatsResource", "AsyncAIChatsResource"]


class AIChatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AIChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AIChatsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message_text: str,
        current_company_id: Optional[str] | Omit = omit,
        message_attachments: Optional[Iterable[ai_chat_create_params.MessageAttachment]] | Omit = omit,
        message_source: Optional[Literal["manual", "suggestion", "link"]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIChat:
        """
        Create a new AI chat thread and send the first message to the AI agent.

        Required permissions:

        - `ai_chat:create`

        Args:
          message_text: The text content of the first message to send to the AI agent.

          current_company_id: The unique identifier of the company to set as context for the AI chat (e.g.,
              "biz_XXXXX").

          message_attachments: A list of previously uploaded file attachments to include with the first
              message.

          message_source: The source of an AI chat message

          title: An optional display title for the AI chat thread (e.g., "Help with billing").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai_chats",
            body=maybe_transform(
                {
                    "message_text": message_text,
                    "current_company_id": current_company_id,
                    "message_attachments": message_attachments,
                    "message_source": message_source,
                    "title": title,
                },
                ai_chat_create_params.AIChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChat,
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
    ) -> AIChat:
        """
        Retrieves the details of an existing AI chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ai_chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChat,
        )

    def update(
        self,
        id: str,
        *,
        current_company_id: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIChat:
        """
        Update an AI chat's title or associated company context.

        Required permissions:

        - `ai_chat:update`

        Args:
          current_company_id: The unique identifier of the company to set as context for the AI chat (e.g.,
              "biz_XXXXX").

          title: The new display title for the AI chat thread (e.g., "Help with billing").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/ai_chats/{id}",
            body=maybe_transform(
                {
                    "current_company_id": current_company_id,
                    "title": title,
                },
                ai_chat_update_params.AIChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChat,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AIChatListResponse]:
        """
        Returns a paginated list of AI chat threads for the current authenticated user.

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai_chats",
            page=SyncCursorPage[AIChatListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    ai_chat_list_params.AIChatListParams,
                ),
            ),
            model=AIChatListResponse,
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
    ) -> AIChatDeleteResponse:
        """
        Delete an AI chat thread so it no longer appears in the user's chat list.

        Required permissions:

        - `ai_chat:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/ai_chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChatDeleteResponse,
        )


class AsyncAIChatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAIChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message_text: str,
        current_company_id: Optional[str] | Omit = omit,
        message_attachments: Optional[Iterable[ai_chat_create_params.MessageAttachment]] | Omit = omit,
        message_source: Optional[Literal["manual", "suggestion", "link"]] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIChat:
        """
        Create a new AI chat thread and send the first message to the AI agent.

        Required permissions:

        - `ai_chat:create`

        Args:
          message_text: The text content of the first message to send to the AI agent.

          current_company_id: The unique identifier of the company to set as context for the AI chat (e.g.,
              "biz_XXXXX").

          message_attachments: A list of previously uploaded file attachments to include with the first
              message.

          message_source: The source of an AI chat message

          title: An optional display title for the AI chat thread (e.g., "Help with billing").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai_chats",
            body=await async_maybe_transform(
                {
                    "message_text": message_text,
                    "current_company_id": current_company_id,
                    "message_attachments": message_attachments,
                    "message_source": message_source,
                    "title": title,
                },
                ai_chat_create_params.AIChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChat,
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
    ) -> AIChat:
        """
        Retrieves the details of an existing AI chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ai_chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChat,
        )

    async def update(
        self,
        id: str,
        *,
        current_company_id: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIChat:
        """
        Update an AI chat's title or associated company context.

        Required permissions:

        - `ai_chat:update`

        Args:
          current_company_id: The unique identifier of the company to set as context for the AI chat (e.g.,
              "biz_XXXXX").

          title: The new display title for the AI chat thread (e.g., "Help with billing").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/ai_chats/{id}",
            body=await async_maybe_transform(
                {
                    "current_company_id": current_company_id,
                    "title": title,
                },
                ai_chat_update_params.AIChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChat,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AIChatListResponse, AsyncCursorPage[AIChatListResponse]]:
        """
        Returns a paginated list of AI chat threads for the current authenticated user.

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai_chats",
            page=AsyncCursorPage[AIChatListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    ai_chat_list_params.AIChatListParams,
                ),
            ),
            model=AIChatListResponse,
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
    ) -> AIChatDeleteResponse:
        """
        Delete an AI chat thread so it no longer appears in the user's chat list.

        Required permissions:

        - `ai_chat:delete`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/ai_chats/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIChatDeleteResponse,
        )


class AIChatsResourceWithRawResponse:
    def __init__(self, ai_chats: AIChatsResource) -> None:
        self._ai_chats = ai_chats

        self.create = to_raw_response_wrapper(
            ai_chats.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ai_chats.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ai_chats.update,
        )
        self.list = to_raw_response_wrapper(
            ai_chats.list,
        )
        self.delete = to_raw_response_wrapper(
            ai_chats.delete,
        )


class AsyncAIChatsResourceWithRawResponse:
    def __init__(self, ai_chats: AsyncAIChatsResource) -> None:
        self._ai_chats = ai_chats

        self.create = async_to_raw_response_wrapper(
            ai_chats.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ai_chats.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ai_chats.update,
        )
        self.list = async_to_raw_response_wrapper(
            ai_chats.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ai_chats.delete,
        )


class AIChatsResourceWithStreamingResponse:
    def __init__(self, ai_chats: AIChatsResource) -> None:
        self._ai_chats = ai_chats

        self.create = to_streamed_response_wrapper(
            ai_chats.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ai_chats.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ai_chats.update,
        )
        self.list = to_streamed_response_wrapper(
            ai_chats.list,
        )
        self.delete = to_streamed_response_wrapper(
            ai_chats.delete,
        )


class AsyncAIChatsResourceWithStreamingResponse:
    def __init__(self, ai_chats: AsyncAIChatsResource) -> None:
        self._ai_chats = ai_chats

        self.create = async_to_streamed_response_wrapper(
            ai_chats.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ai_chats.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ai_chats.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ai_chats.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ai_chats.delete,
        )
