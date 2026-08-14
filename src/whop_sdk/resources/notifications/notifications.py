# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .topics import (
    TopicsResource,
    AsyncTopicsResource,
    TopicsResourceWithRawResponse,
    AsyncTopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
    AsyncTopicsResourceWithStreamingResponse,
)
from ...types import (
    notification_list_params,
    notification_badges_params,
    notification_create_params,
    notification_mark_read_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.notification import Notification
from ...types.notification_badges_response import NotificationBadgesResponse
from ...types.notification_create_response import NotificationCreateResponse
from ...types.notification_mark_read_response import NotificationMarkReadResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    """
    A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

    Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

    Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
    """

    @cached_property
    def topics(self) -> TopicsResource:
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        return TopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        title: str,
        account_id: str | Omit = omit,
        experience_id: str | Omit = omit,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NotificationCreateResponse:
        """
        Queues a notification to every user of an experience or to an account's team,
        processed asynchronously. Every send is attributed to an app: use an app API
        key, or a credential acting on behalf of an app. Narrow the audience with
        `user_ids` to send a mention.

        Args:
          content: Main body text of the notification.

          title: Headline text of the notification.

          account_id: Account whose team members receive the notification (`biz_` tag). Exactly one of
              `experience_id` or `account_id` is required.

          experience_id: Experience whose users receive the notification (`exp_` tag). Exactly one of
              `experience_id` or `account_id` is required.

          icon_user_id: User whose profile picture is used as the notification icon. Defaults to the
              experience or account avatar.

          rest_path: Path segment appended to the generated deep link that opens your app, for
              example `/settings/billing`.

          subtitle: Optional secondary line displayed below the title.

          user_ids: Optional `user_` tags narrowing the audience. When provided, only these users
              are notified (as a mention), provided they are in the targeted experience or
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/notifications",
            body=maybe_transform(
                {
                    "content": content,
                    "title": title,
                    "account_id": account_id,
                    "experience_id": experience_id,
                    "icon_user_id": icon_user_id,
                    "rest_path": rest_path,
                    "subtitle": subtitle,
                    "user_ids": user_ids,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NotificationCreateResponse,
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
    ) -> Notification:
        """
        Retrieves a single notification by id — either an `id` returned by List
        Notifications, or the ephemeral id delivered with a push/websocket event.
        Requires a user credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/notifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notification,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        experience_id: str | Omit = omit,
        first: int | Omit = omit,
        mentions: bool | Omit = omit,
        unread: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Notification]:
        """Lists the authenticated user's notifications, newest first.

        Requires a user
        credential — an account API key has no notification feed. Without filters the
        feed spans every experience the user belongs to plus the teams they are a member
        of.

        Args:
          account_id: Only return team notifications for this account (`biz_` tag).

          after: A cursor (a notification `id` from a previous page); returns notifications older
              than it.

          experience_id: Only return notifications from this experience (`exp_` tag).

          first: The number of notifications to return (default 20, max 100).

          mentions: Only return notifications that mention the user directly.

          unread: Only return notifications created since the user last viewed their source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notifications",
            page=SyncCursorPage[Notification],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "experience_id": experience_id,
                        "first": first,
                        "mentions": mentions,
                        "unread": unread,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            model=Notification,
        )

    def badges(
        self,
        *,
        experience_ids: SequenceNotStr[str] | Omit = omit,
        last_fetched_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationBadgesResponse:
        """Lists the authenticated user's per-experience unread badge state.

        Requires a
        user credential. Returns one row per experience the user belongs to (or per
        requested experience).

        Args:
          experience_ids: Only return badges for these experiences (`exp_` tags).

          last_fetched_at: The client's last fetched-at ISO 8601 timestamp, used to partially refresh
              badges after a websocket message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notifications/badges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "experience_ids": experience_ids,
                        "last_fetched_at": last_fetched_at,
                    },
                    notification_badges_params.NotificationBadgesParams,
                ),
            ),
            cast_to=NotificationBadgesResponse,
        )

    def mark_read(
        self,
        *,
        all: bool | Omit = omit,
        experience_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NotificationMarkReadResponse:
        """
        Marks the authenticated user's notifications as read: one experience's
        (`experience_id`) or everything (`all: true`) — exactly one of the two. Requires
        a user credential. Responds with the refreshed badge rows for the affected
        scope.

        Args:
          all: Pass `true` to mark every notification read. Exactly one of `experience_id` or
              `all` is required.

          experience_id: Experience to mark read (`exp_` tag). Exactly one of `experience_id` or `all` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/notifications/mark_read",
            body=maybe_transform(
                {
                    "all": all,
                    "experience_id": experience_id,
                },
                notification_mark_read_params.NotificationMarkReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NotificationMarkReadResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    """
    A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

    Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

    Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
    """

    @cached_property
    def topics(self) -> AsyncTopicsResource:
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        return AsyncTopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        title: str,
        account_id: str | Omit = omit,
        experience_id: str | Omit = omit,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NotificationCreateResponse:
        """
        Queues a notification to every user of an experience or to an account's team,
        processed asynchronously. Every send is attributed to an app: use an app API
        key, or a credential acting on behalf of an app. Narrow the audience with
        `user_ids` to send a mention.

        Args:
          content: Main body text of the notification.

          title: Headline text of the notification.

          account_id: Account whose team members receive the notification (`biz_` tag). Exactly one of
              `experience_id` or `account_id` is required.

          experience_id: Experience whose users receive the notification (`exp_` tag). Exactly one of
              `experience_id` or `account_id` is required.

          icon_user_id: User whose profile picture is used as the notification icon. Defaults to the
              experience or account avatar.

          rest_path: Path segment appended to the generated deep link that opens your app, for
              example `/settings/billing`.

          subtitle: Optional secondary line displayed below the title.

          user_ids: Optional `user_` tags narrowing the audience. When provided, only these users
              are notified (as a mention), provided they are in the targeted experience or
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/notifications",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "title": title,
                    "account_id": account_id,
                    "experience_id": experience_id,
                    "icon_user_id": icon_user_id,
                    "rest_path": rest_path,
                    "subtitle": subtitle,
                    "user_ids": user_ids,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NotificationCreateResponse,
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
    ) -> Notification:
        """
        Retrieves a single notification by id — either an `id` returned by List
        Notifications, or the ephemeral id delivered with a push/websocket event.
        Requires a user credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/notifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notification,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        experience_id: str | Omit = omit,
        first: int | Omit = omit,
        mentions: bool | Omit = omit,
        unread: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Notification, AsyncCursorPage[Notification]]:
        """Lists the authenticated user's notifications, newest first.

        Requires a user
        credential — an account API key has no notification feed. Without filters the
        feed spans every experience the user belongs to plus the teams they are a member
        of.

        Args:
          account_id: Only return team notifications for this account (`biz_` tag).

          after: A cursor (a notification `id` from a previous page); returns notifications older
              than it.

          experience_id: Only return notifications from this experience (`exp_` tag).

          first: The number of notifications to return (default 20, max 100).

          mentions: Only return notifications that mention the user directly.

          unread: Only return notifications created since the user last viewed their source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notifications",
            page=AsyncCursorPage[Notification],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "experience_id": experience_id,
                        "first": first,
                        "mentions": mentions,
                        "unread": unread,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            model=Notification,
        )

    async def badges(
        self,
        *,
        experience_ids: SequenceNotStr[str] | Omit = omit,
        last_fetched_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationBadgesResponse:
        """Lists the authenticated user's per-experience unread badge state.

        Requires a
        user credential. Returns one row per experience the user belongs to (or per
        requested experience).

        Args:
          experience_ids: Only return badges for these experiences (`exp_` tags).

          last_fetched_at: The client's last fetched-at ISO 8601 timestamp, used to partially refresh
              badges after a websocket message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notifications/badges",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "experience_ids": experience_ids,
                        "last_fetched_at": last_fetched_at,
                    },
                    notification_badges_params.NotificationBadgesParams,
                ),
            ),
            cast_to=NotificationBadgesResponse,
        )

    async def mark_read(
        self,
        *,
        all: bool | Omit = omit,
        experience_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NotificationMarkReadResponse:
        """
        Marks the authenticated user's notifications as read: one experience's
        (`experience_id`) or everything (`all: true`) — exactly one of the two. Requires
        a user credential. Responds with the refreshed badge rows for the affected
        scope.

        Args:
          all: Pass `true` to mark every notification read. Exactly one of `experience_id` or
              `all` is required.

          experience_id: Experience to mark read (`exp_` tag). Exactly one of `experience_id` or `all` is
              required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/notifications/mark_read",
            body=await async_maybe_transform(
                {
                    "all": all,
                    "experience_id": experience_id,
                },
                notification_mark_read_params.NotificationMarkReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NotificationMarkReadResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.badges = to_raw_response_wrapper(
            notifications.badges,
        )
        self.mark_read = to_raw_response_wrapper(
            notifications.mark_read,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        return TopicsResourceWithRawResponse(self._notifications.topics)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.badges = async_to_raw_response_wrapper(
            notifications.badges,
        )
        self.mark_read = async_to_raw_response_wrapper(
            notifications.mark_read,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        return AsyncTopicsResourceWithRawResponse(self._notifications.topics)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.badges = to_streamed_response_wrapper(
            notifications.badges,
        )
        self.mark_read = to_streamed_response_wrapper(
            notifications.mark_read,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        return TopicsResourceWithStreamingResponse(self._notifications.topics)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.badges = async_to_streamed_response_wrapper(
            notifications.badges,
        )
        self.mark_read = async_to_streamed_response_wrapper(
            notifications.mark_read,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        return AsyncTopicsResourceWithStreamingResponse(self._notifications.topics)
