# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    ForumPostVisibilityType,
    forum_post_list_params,
    forum_post_create_params,
    forum_post_update_params,
)
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
from ..types.shared.currency import Currency
from ..types.shared.forum_post import ForumPost
from ..types.forum_post_list_response import ForumPostListResponse
from ..types.forum_post_visibility_type import ForumPostVisibilityType

__all__ = ["ForumPostsResource", "AsyncForumPostsResource"]


class ForumPostsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForumPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ForumPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForumPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ForumPostsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        experience_id: str,
        attachments: Optional[Iterable[forum_post_create_params.Attachment]] | Omit = omit,
        content: Optional[str] | Omit = omit,
        is_mention: Optional[bool] | Omit = omit,
        parent_id: Optional[str] | Omit = omit,
        paywall_amount: Optional[float] | Omit = omit,
        paywall_currency: Optional[Currency] | Omit = omit,
        pinned: Optional[bool] | Omit = omit,
        poll: Optional[forum_post_create_params.Poll] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[ForumPostVisibilityType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ForumPost:
        """
        Create a new forum post

        Required permissions:

        - `forum:post:create`

        Args:
          experience_id: The experience to create this post in

          attachments: The attachments for this post

          content: This is the main body of the post in Markdown format. Hidden if paywalled and
              user hasn't purchased access to it.

          is_mention: This is used to determine if the post should be sent as a 'mention' notification
              to all of the users who are in the experience. This means that anyone with
              'mentions' enabled will receive a notification about this post.

          parent_id: The ID of the parent post. Set it to the ID of the post you want to comment on
              or don't include it if its a top level post.

          paywall_amount: The amount to paywall this post by. A paywalled post requires the user to
              purchase it in order to view its content.

          paywall_currency: The available currencies on the platform

          pinned: Whether the post should be pinned

          poll: The poll for this post

          title: The title of the post. Only visible if paywalled.

          visibility: The visibility types for forum posts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/forum_posts",
            body=maybe_transform(
                {
                    "experience_id": experience_id,
                    "attachments": attachments,
                    "content": content,
                    "is_mention": is_mention,
                    "parent_id": parent_id,
                    "paywall_amount": paywall_amount,
                    "paywall_currency": paywall_currency,
                    "pinned": pinned,
                    "poll": poll,
                    "title": title,
                    "visibility": visibility,
                },
                forum_post_create_params.ForumPostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForumPost,
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
    ) -> ForumPost:
        """
        Retrieves a forum post by ID

        Required permissions:

        - `forum:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/forum_posts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForumPost,
        )

    def update(
        self,
        id: str,
        *,
        attachments: Optional[Iterable[forum_post_update_params.Attachment]] | Omit = omit,
        content: Optional[str] | Omit = omit,
        is_pinned: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[ForumPostVisibilityType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ForumPost:
        """
        Update an existing forum post

        Args:
          attachments: The attachments for this post

          content: This is the main body of the post in Markdown format. Hidden if paywalled and
              user hasn't purchased access to it.

          is_pinned: Whether the post is pinned. You can only pin a top level posts (not comments).

          title: The title of the post. Only visible if paywalled.

          visibility: The visibility types for forum posts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/forum_posts/{id}",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "content": content,
                    "is_pinned": is_pinned,
                    "title": title,
                    "visibility": visibility,
                },
                forum_post_update_params.ForumPostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForumPost,
        )

    def list(
        self,
        *,
        experience_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        parent_id: Optional[str] | Omit = omit,
        pinned: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ForumPostListResponse]:
        """
        Lists forum posts

        Required permissions:

        - `forum:read`

        Args:
          experience_id: The ID of the experience to list forum posts for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          parent_id: The ID of the parent post to list forum post comments for

          pinned: Set to true to only return pinned posts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/forum_posts",
            page=SyncCursorPage[ForumPostListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "experience_id": experience_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                        "parent_id": parent_id,
                        "pinned": pinned,
                    },
                    forum_post_list_params.ForumPostListParams,
                ),
            ),
            model=ForumPostListResponse,
        )


class AsyncForumPostsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForumPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncForumPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForumPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncForumPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        experience_id: str,
        attachments: Optional[Iterable[forum_post_create_params.Attachment]] | Omit = omit,
        content: Optional[str] | Omit = omit,
        is_mention: Optional[bool] | Omit = omit,
        parent_id: Optional[str] | Omit = omit,
        paywall_amount: Optional[float] | Omit = omit,
        paywall_currency: Optional[Currency] | Omit = omit,
        pinned: Optional[bool] | Omit = omit,
        poll: Optional[forum_post_create_params.Poll] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[ForumPostVisibilityType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ForumPost:
        """
        Create a new forum post

        Required permissions:

        - `forum:post:create`

        Args:
          experience_id: The experience to create this post in

          attachments: The attachments for this post

          content: This is the main body of the post in Markdown format. Hidden if paywalled and
              user hasn't purchased access to it.

          is_mention: This is used to determine if the post should be sent as a 'mention' notification
              to all of the users who are in the experience. This means that anyone with
              'mentions' enabled will receive a notification about this post.

          parent_id: The ID of the parent post. Set it to the ID of the post you want to comment on
              or don't include it if its a top level post.

          paywall_amount: The amount to paywall this post by. A paywalled post requires the user to
              purchase it in order to view its content.

          paywall_currency: The available currencies on the platform

          pinned: Whether the post should be pinned

          poll: The poll for this post

          title: The title of the post. Only visible if paywalled.

          visibility: The visibility types for forum posts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/forum_posts",
            body=await async_maybe_transform(
                {
                    "experience_id": experience_id,
                    "attachments": attachments,
                    "content": content,
                    "is_mention": is_mention,
                    "parent_id": parent_id,
                    "paywall_amount": paywall_amount,
                    "paywall_currency": paywall_currency,
                    "pinned": pinned,
                    "poll": poll,
                    "title": title,
                    "visibility": visibility,
                },
                forum_post_create_params.ForumPostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForumPost,
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
    ) -> ForumPost:
        """
        Retrieves a forum post by ID

        Required permissions:

        - `forum:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/forum_posts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForumPost,
        )

    async def update(
        self,
        id: str,
        *,
        attachments: Optional[Iterable[forum_post_update_params.Attachment]] | Omit = omit,
        content: Optional[str] | Omit = omit,
        is_pinned: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        visibility: Optional[ForumPostVisibilityType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ForumPost:
        """
        Update an existing forum post

        Args:
          attachments: The attachments for this post

          content: This is the main body of the post in Markdown format. Hidden if paywalled and
              user hasn't purchased access to it.

          is_pinned: Whether the post is pinned. You can only pin a top level posts (not comments).

          title: The title of the post. Only visible if paywalled.

          visibility: The visibility types for forum posts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/forum_posts/{id}",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "content": content,
                    "is_pinned": is_pinned,
                    "title": title,
                    "visibility": visibility,
                },
                forum_post_update_params.ForumPostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ForumPost,
        )

    def list(
        self,
        *,
        experience_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        parent_id: Optional[str] | Omit = omit,
        pinned: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ForumPostListResponse, AsyncCursorPage[ForumPostListResponse]]:
        """
        Lists forum posts

        Required permissions:

        - `forum:read`

        Args:
          experience_id: The ID of the experience to list forum posts for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          parent_id: The ID of the parent post to list forum post comments for

          pinned: Set to true to only return pinned posts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/forum_posts",
            page=AsyncCursorPage[ForumPostListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "experience_id": experience_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                        "parent_id": parent_id,
                        "pinned": pinned,
                    },
                    forum_post_list_params.ForumPostListParams,
                ),
            ),
            model=ForumPostListResponse,
        )


class ForumPostsResourceWithRawResponse:
    def __init__(self, forum_posts: ForumPostsResource) -> None:
        self._forum_posts = forum_posts

        self.create = to_raw_response_wrapper(
            forum_posts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            forum_posts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            forum_posts.update,
        )
        self.list = to_raw_response_wrapper(
            forum_posts.list,
        )


class AsyncForumPostsResourceWithRawResponse:
    def __init__(self, forum_posts: AsyncForumPostsResource) -> None:
        self._forum_posts = forum_posts

        self.create = async_to_raw_response_wrapper(
            forum_posts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            forum_posts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            forum_posts.update,
        )
        self.list = async_to_raw_response_wrapper(
            forum_posts.list,
        )


class ForumPostsResourceWithStreamingResponse:
    def __init__(self, forum_posts: ForumPostsResource) -> None:
        self._forum_posts = forum_posts

        self.create = to_streamed_response_wrapper(
            forum_posts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            forum_posts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            forum_posts.update,
        )
        self.list = to_streamed_response_wrapper(
            forum_posts.list,
        )


class AsyncForumPostsResourceWithStreamingResponse:
    def __init__(self, forum_posts: AsyncForumPostsResource) -> None:
        self._forum_posts = forum_posts

        self.create = async_to_streamed_response_wrapper(
            forum_posts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            forum_posts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            forum_posts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            forum_posts.list,
        )
