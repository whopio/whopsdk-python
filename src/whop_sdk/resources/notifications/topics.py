# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.notifications import topic_list_params
from ...types.notifications.notification_topic import NotificationTopic

__all__ = ["TopicsResource", "AsyncTopicsResource"]


class TopicsResource(SyncAPIResource):
    """
    A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

    Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

    Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
    """

    @cached_property
    def with_raw_response(self) -> TopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return TopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return TopicsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        first: int | Omit = omit,
        topic_type: Literal["user", "account_team"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[NotificationTopic]:
        """
        Lists the platform's visible notification topics — the categories users can set
        notification preferences on. App-created topics are internal and not returned.

        Args:
          after: A cursor; returns topics after this position.

          first: The number of topics to return (default 20, max 100).

          topic_type: Only return topics of this scope: `user` (member notifications) or
              `account_team` (team notifications).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notifications/topics",
            page=SyncCursorPage[NotificationTopic],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                        "topic_type": topic_type,
                    },
                    topic_list_params.TopicListParams,
                ),
            ),
            model=NotificationTopic,
        )


class AsyncTopicsResource(AsyncAPIResource):
    """
    A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

    Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

    Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncTopicsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        first: int | Omit = omit,
        topic_type: Literal["user", "account_team"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NotificationTopic, AsyncCursorPage[NotificationTopic]]:
        """
        Lists the platform's visible notification topics — the categories users can set
        notification preferences on. App-created topics are internal and not returned.

        Args:
          after: A cursor; returns topics after this position.

          first: The number of topics to return (default 20, max 100).

          topic_type: Only return topics of this scope: `user` (member notifications) or
              `account_team` (team notifications).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notifications/topics",
            page=AsyncCursorPage[NotificationTopic],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                        "topic_type": topic_type,
                    },
                    topic_list_params.TopicListParams,
                ),
            ),
            model=NotificationTopic,
        )


class TopicsResourceWithRawResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.list = to_raw_response_wrapper(
            topics.list,
        )


class AsyncTopicsResourceWithRawResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.list = async_to_raw_response_wrapper(
            topics.list,
        )


class TopicsResourceWithStreamingResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.list = to_streamed_response_wrapper(
            topics.list,
        )


class AsyncTopicsResourceWithStreamingResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.list = async_to_streamed_response_wrapper(
            topics.list,
        )
