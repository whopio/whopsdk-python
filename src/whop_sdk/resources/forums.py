# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import forum_list_params, forum_update_params
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
from ..types.shared.forum import Forum
from ..types.forum_list_response import ForumListResponse
from ..types.shared.who_can_post_types import WhoCanPostTypes
from ..types.shared.who_can_comment_types import WhoCanCommentTypes
from ..types.shared.email_notification_preferences import EmailNotificationPreferences

__all__ = ["ForumsResource", "AsyncForumsResource"]


class ForumsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ForumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ForumsResourceWithStreamingResponse(self)

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
    ) -> Forum:
        """
        Retrieves a forum

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
            f"/forums/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Forum,
        )

    def update(
        self,
        id: str,
        *,
        email_notification_preference: Optional[EmailNotificationPreferences] | Omit = omit,
        who_can_comment: Optional[WhoCanCommentTypes] | Omit = omit,
        who_can_post: Optional[WhoCanPostTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Forum:
        """
        Updates a forum

        Required permissions:

        - `forum:moderate`

        Args:
          email_notification_preference: Email notification preference option for a forum feed

          who_can_comment: Who can comment on a forum feed

          who_can_post: Who can post on a forum feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/forums/{id}",
            body=maybe_transform(
                {
                    "email_notification_preference": email_notification_preference,
                    "who_can_comment": who_can_comment,
                    "who_can_post": who_can_post,
                },
                forum_update_params.ForumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Forum,
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
    ) -> SyncCursorPage[ForumListResponse]:
        """
        Lists forums inside a company

        Required permissions:

        - `forum:read`

        Args:
          company_id: The ID of the company to list forums for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_id: If provided, only forums connected to this product are returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/forums",
            page=SyncCursorPage[ForumListResponse],
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
                    forum_list_params.ForumListParams,
                ),
            ),
            model=ForumListResponse,
        )


class AsyncForumsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncForumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncForumsResourceWithStreamingResponse(self)

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
    ) -> Forum:
        """
        Retrieves a forum

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
            f"/forums/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Forum,
        )

    async def update(
        self,
        id: str,
        *,
        email_notification_preference: Optional[EmailNotificationPreferences] | Omit = omit,
        who_can_comment: Optional[WhoCanCommentTypes] | Omit = omit,
        who_can_post: Optional[WhoCanPostTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Forum:
        """
        Updates a forum

        Required permissions:

        - `forum:moderate`

        Args:
          email_notification_preference: Email notification preference option for a forum feed

          who_can_comment: Who can comment on a forum feed

          who_can_post: Who can post on a forum feed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/forums/{id}",
            body=await async_maybe_transform(
                {
                    "email_notification_preference": email_notification_preference,
                    "who_can_comment": who_can_comment,
                    "who_can_post": who_can_post,
                },
                forum_update_params.ForumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Forum,
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
    ) -> AsyncPaginator[ForumListResponse, AsyncCursorPage[ForumListResponse]]:
        """
        Lists forums inside a company

        Required permissions:

        - `forum:read`

        Args:
          company_id: The ID of the company to list forums for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          product_id: If provided, only forums connected to this product are returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/forums",
            page=AsyncCursorPage[ForumListResponse],
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
                    forum_list_params.ForumListParams,
                ),
            ),
            model=ForumListResponse,
        )


class ForumsResourceWithRawResponse:
    def __init__(self, forums: ForumsResource) -> None:
        self._forums = forums

        self.retrieve = to_raw_response_wrapper(
            forums.retrieve,
        )
        self.update = to_raw_response_wrapper(
            forums.update,
        )
        self.list = to_raw_response_wrapper(
            forums.list,
        )


class AsyncForumsResourceWithRawResponse:
    def __init__(self, forums: AsyncForumsResource) -> None:
        self._forums = forums

        self.retrieve = async_to_raw_response_wrapper(
            forums.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            forums.update,
        )
        self.list = async_to_raw_response_wrapper(
            forums.list,
        )


class ForumsResourceWithStreamingResponse:
    def __init__(self, forums: ForumsResource) -> None:
        self._forums = forums

        self.retrieve = to_streamed_response_wrapper(
            forums.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            forums.update,
        )
        self.list = to_streamed_response_wrapper(
            forums.list,
        )


class AsyncForumsResourceWithStreamingResponse:
    def __init__(self, forums: AsyncForumsResource) -> None:
        self._forums = forums

        self.retrieve = async_to_streamed_response_wrapper(
            forums.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            forums.update,
        )
        self.list = async_to_streamed_response_wrapper(
            forums.list,
        )
