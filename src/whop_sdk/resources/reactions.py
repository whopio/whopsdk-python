# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import reaction_list_params, reaction_create_params, reaction_delete_params
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
from ..types.shared.reaction import Reaction
from ..types.reaction_list_response import ReactionListResponse
from ..types.reaction_delete_response import ReactionDeleteResponse

__all__ = ["ReactionsResource", "AsyncReactionsResource"]


class ReactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ReactionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        resource_id: str,
        emoji: Optional[str] | Omit = omit,
        poll_option_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Reaction:
        """Add an emoji reaction or poll vote to a message or forum post.

        In forums, the
        reaction is always a like.

        Required permissions:

        - `chat:read`

        Args:
          resource_id: The unique identifier of the message or forum post to react to.

          emoji: The emoji to react with, in shortcode or unicode format. For example, ':heart:'
              or a unicode emoji. Ignored in forums where reactions are always likes.

          poll_option_id: The unique identifier of a poll option to vote for. Only valid when the target
              message or post contains a poll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/reactions",
            body=maybe_transform(
                {
                    "resource_id": resource_id,
                    "emoji": emoji,
                    "poll_option_id": poll_option_id,
                },
                reaction_create_params.ReactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reaction,
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
    ) -> Reaction:
        """
        Retrieves the details of an existing reaction.

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
            f"/reactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reaction,
        )

    def list(
        self,
        *,
        resource_id: str,
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
    ) -> SyncCursorPage[ReactionListResponse]:
        """
        Returns a paginated list of emoji reactions on a specific message or forum post,
        sorted by most recent.

        Required permissions:

        - `chat:read`

        Args:
          resource_id: The unique identifier of the message or forum post to list reactions for.

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
            "/reactions",
            page=SyncCursorPage[ReactionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    reaction_list_params.ReactionListParams,
                ),
            ),
            model=ReactionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        emoji: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReactionDeleteResponse:
        """Remove an emoji reaction from a message or forum post.

        Only the reaction author
        or a channel admin can remove a reaction.

        Required permissions:

        - `chat:read`

        Args:
          emoji: The emoji to remove, in shortcode or unicode format. For example, ':heart:' or a
              unicode emoji. Required when the id refers to a message or post instead of a
              reaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/reactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"emoji": emoji}, reaction_delete_params.ReactionDeleteParams),
            ),
            cast_to=ReactionDeleteResponse,
        )


class AsyncReactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncReactionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        resource_id: str,
        emoji: Optional[str] | Omit = omit,
        poll_option_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Reaction:
        """Add an emoji reaction or poll vote to a message or forum post.

        In forums, the
        reaction is always a like.

        Required permissions:

        - `chat:read`

        Args:
          resource_id: The unique identifier of the message or forum post to react to.

          emoji: The emoji to react with, in shortcode or unicode format. For example, ':heart:'
              or a unicode emoji. Ignored in forums where reactions are always likes.

          poll_option_id: The unique identifier of a poll option to vote for. Only valid when the target
              message or post contains a poll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/reactions",
            body=await async_maybe_transform(
                {
                    "resource_id": resource_id,
                    "emoji": emoji,
                    "poll_option_id": poll_option_id,
                },
                reaction_create_params.ReactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reaction,
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
    ) -> Reaction:
        """
        Retrieves the details of an existing reaction.

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
            f"/reactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reaction,
        )

    def list(
        self,
        *,
        resource_id: str,
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
    ) -> AsyncPaginator[ReactionListResponse, AsyncCursorPage[ReactionListResponse]]:
        """
        Returns a paginated list of emoji reactions on a specific message or forum post,
        sorted by most recent.

        Required permissions:

        - `chat:read`

        Args:
          resource_id: The unique identifier of the message or forum post to list reactions for.

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
            "/reactions",
            page=AsyncCursorPage[ReactionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    reaction_list_params.ReactionListParams,
                ),
            ),
            model=ReactionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        emoji: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReactionDeleteResponse:
        """Remove an emoji reaction from a message or forum post.

        Only the reaction author
        or a channel admin can remove a reaction.

        Required permissions:

        - `chat:read`

        Args:
          emoji: The emoji to remove, in shortcode or unicode format. For example, ':heart:' or a
              unicode emoji. Required when the id refers to a message or post instead of a
              reaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/reactions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"emoji": emoji}, reaction_delete_params.ReactionDeleteParams),
            ),
            cast_to=ReactionDeleteResponse,
        )


class ReactionsResourceWithRawResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.create = to_raw_response_wrapper(
            reactions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            reactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            reactions.list,
        )
        self.delete = to_raw_response_wrapper(
            reactions.delete,
        )


class AsyncReactionsResourceWithRawResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.create = async_to_raw_response_wrapper(
            reactions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            reactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            reactions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            reactions.delete,
        )


class ReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.create = to_streamed_response_wrapper(
            reactions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            reactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            reactions.list,
        )
        self.delete = to_streamed_response_wrapper(
            reactions.delete,
        )


class AsyncReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.create = async_to_streamed_response_wrapper(
            reactions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            reactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            reactions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            reactions.delete,
        )
