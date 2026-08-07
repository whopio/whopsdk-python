# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .topics import (
    TopicsResource,
    AsyncTopicsResource,
    TopicsResourceWithRawResponse,
    AsyncTopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
    AsyncTopicsResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .experiences import (
    ExperiencesResource,
    AsyncExperiencesResource,
    ExperiencesResourceWithRawResponse,
    AsyncExperiencesResourceWithRawResponse,
    ExperiencesResourceWithStreamingResponse,
    AsyncExperiencesResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.users.preferences import notification_set_params
from .....types.users.preferences.notification_set_response import NotificationSetResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def topics(self) -> TopicsResource:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return TopicsResource(self._client)

    @cached_property
    def experiences(self) -> ExperiencesResource:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return ExperiencesResource(self._client)

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

    def set(
        self,
        *,
        preferences: Iterable[notification_set_params.Preference],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NotificationSetResponse:
        """Sets the authenticated user's notification preferences.

        Each preference is
        addressed by `scope`, not by id, so a scope read back from either list endpoint
        can be sent straight here.

        A scope naming an experience with no topic sets that experience's level, and
        accepts all three levels. Any other scope sets a topic override, which is binary
        — `all` or `nothing` — and requires a `channel`.

        `level: null` clears the preference. Preferences are stored as overrides, so
        clearing one means the scope inherits its default again rather than being
        switched off.

        The batch is applied in one transaction: if any entry is rejected, none are
        written. Experience levels are applied before topic overrides, because setting a
        level replaces every topic preference for that experience — so an override sent
        alongside a level wins. The response reports what each scope now resolves to, in
        the order the entries were sent.

        Args:
          preferences: The preferences to set, at most 100 per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            "/users/me/preferences/notifications",
            body=maybe_transform({"preferences": preferences}, notification_set_params.NotificationSetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NotificationSetResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def topics(self) -> AsyncTopicsResource:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncTopicsResource(self._client)

    @cached_property
    def experiences(self) -> AsyncExperiencesResource:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncExperiencesResource(self._client)

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

    async def set(
        self,
        *,
        preferences: Iterable[notification_set_params.Preference],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NotificationSetResponse:
        """Sets the authenticated user's notification preferences.

        Each preference is
        addressed by `scope`, not by id, so a scope read back from either list endpoint
        can be sent straight here.

        A scope naming an experience with no topic sets that experience's level, and
        accepts all three levels. Any other scope sets a topic override, which is binary
        — `all` or `nothing` — and requires a `channel`.

        `level: null` clears the preference. Preferences are stored as overrides, so
        clearing one means the scope inherits its default again rather than being
        switched off.

        The batch is applied in one transaction: if any entry is rejected, none are
        written. Experience levels are applied before topic overrides, because setting a
        level replaces every topic preference for that experience — so an override sent
        alongside a level wins. The response reports what each scope now resolves to, in
        the order the entries were sent.

        Args:
          preferences: The preferences to set, at most 100 per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            "/users/me/preferences/notifications",
            body=await async_maybe_transform(
                {"preferences": preferences}, notification_set_params.NotificationSetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NotificationSetResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.set = to_raw_response_wrapper(
            notifications.set,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return TopicsResourceWithRawResponse(self._notifications.topics)

    @cached_property
    def experiences(self) -> ExperiencesResourceWithRawResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return ExperiencesResourceWithRawResponse(self._notifications.experiences)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.set = async_to_raw_response_wrapper(
            notifications.set,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncTopicsResourceWithRawResponse(self._notifications.topics)

    @cached_property
    def experiences(self) -> AsyncExperiencesResourceWithRawResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncExperiencesResourceWithRawResponse(self._notifications.experiences)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.set = to_streamed_response_wrapper(
            notifications.set,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return TopicsResourceWithStreamingResponse(self._notifications.topics)

    @cached_property
    def experiences(self) -> ExperiencesResourceWithStreamingResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return ExperiencesResourceWithStreamingResponse(self._notifications.experiences)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.set = async_to_streamed_response_wrapper(
            notifications.set,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncTopicsResourceWithStreamingResponse(self._notifications.topics)

    @cached_property
    def experiences(self) -> AsyncExperiencesResourceWithStreamingResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncExperiencesResourceWithStreamingResponse(self._notifications.experiences)
