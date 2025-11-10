# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import overload

import httpx

from ..types import notification_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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

    @overload
    def create(
        self,
        *,
        company_id: str,
        content: str,
        title: str,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
        """
        Queues a notification to be sent to users in an experience or company team

        Args:
          company_id: The id of the company to target. Only team members of this company will receive
              the notification. When clicked will take the user to your dashboard app view.

          content: The content of the notification

          title: The title of the notification

          icon_user_id: Optional: ID of a Whop user whose profile picture will be used as the
              notification icon. If not provided, defaults to the experience or company
              avatar.

          rest_path: The rest path to append to the generated deep link that opens your app. Use
              [restPath] in your app path in the dashboard to read this parameter.

          subtitle: The subtitle of the notification

          user_ids: If provided, this will only send to these users if they are also in the main
              scope (experience or company)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        content: str,
        experience_id: str,
        title: str,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
        """
        Queues a notification to be sent to users in an experience or company team

        Args:
          content: The content of the notification

          experience_id: The id of the experience to target. All users with access to this experience
              (customers and admins) will receive the notification. When clicked, open your
              experience view.

          title: The title of the notification

          icon_user_id: Optional: ID of a Whop user whose profile picture will be used as the
              notification icon. If not provided, defaults to the experience or company
              avatar.

          rest_path: The rest path to append to the generated deep link that opens your app. Use
              [restPath] in your app path in the dashboard to read this parameter.

          subtitle: The subtitle of the notification

          user_ids: If provided, this will only send to these users if they are also in the main
              scope (experience or company)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["company_id", "content", "title"], ["content", "experience_id", "title"])
    def create(
        self,
        *,
        company_id: str | Omit = omit,
        content: str,
        title: str,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        experience_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
        return self._post(
            "/notifications",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "content": content,
                    "title": title,
                    "icon_user_id": icon_user_id,
                    "rest_path": rest_path,
                    "subtitle": subtitle,
                    "user_ids": user_ids,
                    "experience_id": experience_id,
                },
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
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

    @overload
    async def create(
        self,
        *,
        company_id: str,
        content: str,
        title: str,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
        """
        Queues a notification to be sent to users in an experience or company team

        Args:
          company_id: The id of the company to target. Only team members of this company will receive
              the notification. When clicked will take the user to your dashboard app view.

          content: The content of the notification

          title: The title of the notification

          icon_user_id: Optional: ID of a Whop user whose profile picture will be used as the
              notification icon. If not provided, defaults to the experience or company
              avatar.

          rest_path: The rest path to append to the generated deep link that opens your app. Use
              [restPath] in your app path in the dashboard to read this parameter.

          subtitle: The subtitle of the notification

          user_ids: If provided, this will only send to these users if they are also in the main
              scope (experience or company)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        content: str,
        experience_id: str,
        title: str,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
        """
        Queues a notification to be sent to users in an experience or company team

        Args:
          content: The content of the notification

          experience_id: The id of the experience to target. All users with access to this experience
              (customers and admins) will receive the notification. When clicked, open your
              experience view.

          title: The title of the notification

          icon_user_id: Optional: ID of a Whop user whose profile picture will be used as the
              notification icon. If not provided, defaults to the experience or company
              avatar.

          rest_path: The rest path to append to the generated deep link that opens your app. Use
              [restPath] in your app path in the dashboard to read this parameter.

          subtitle: The subtitle of the notification

          user_ids: If provided, this will only send to these users if they are also in the main
              scope (experience or company)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["company_id", "content", "title"], ["content", "experience_id", "title"])
    async def create(
        self,
        *,
        company_id: str | Omit = omit,
        content: str,
        title: str,
        icon_user_id: Optional[str] | Omit = omit,
        rest_path: Optional[str] | Omit = omit,
        subtitle: Optional[str] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        experience_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
        return await self._post(
            "/notifications",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "content": content,
                    "title": title,
                    "icon_user_id": icon_user_id,
                    "rest_path": rest_path,
                    "subtitle": subtitle,
                    "user_ids": user_ids,
                    "experience_id": experience_id,
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
