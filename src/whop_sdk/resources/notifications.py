# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import notification_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.notification_create_response import NotificationCreateResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    """
    A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

    Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

    Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
    """

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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    """
    A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

    Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

    Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
    """

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
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_raw_response_wrapper(
            notifications.create,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_raw_response_wrapper(
            notifications.create,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_streamed_response_wrapper(
            notifications.create,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_streamed_response_wrapper(
            notifications.create,
        )
