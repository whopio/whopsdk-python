# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.users import preference_update_params
from ...._base_client import make_request_options
from .notifications.notifications import (
    NotificationsResource,
    AsyncNotificationsResource,
    NotificationsResourceWithRawResponse,
    AsyncNotificationsResourceWithRawResponse,
    NotificationsResourceWithStreamingResponse,
    AsyncNotificationsResourceWithStreamingResponse,
)
from ....types.users.preference_update_response import PreferenceUpdateResponse
from ....types.users.preference_retrieve_response import PreferenceRetrieveResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def notifications(self) -> NotificationsResource:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return NotificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """Retrieves the authenticated user's settings document.

        Addressed only as `me` —
        the document always belongs to the session user.
        """
        return self._get(
            "/users/me/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    def update(
        self,
        *,
        investigation_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateResponse:
        """Updates the authenticated user's settings document.

        Replaces the top-level keys
        it is given and leaves the rest untouched.

        Args:
          investigation_enabled: Whether investigation mode is enabled for the user. Only meaningful for staff
              users with investigation access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/users/me/preferences",
            body=maybe_transform(
                {"investigation_enabled": investigation_enabled}, preference_update_params.PreferenceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpdateResponse,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncNotificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """Retrieves the authenticated user's settings document.

        Addressed only as `me` —
        the document always belongs to the session user.
        """
        return await self._get(
            "/users/me/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    async def update(
        self,
        *,
        investigation_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateResponse:
        """Updates the authenticated user's settings document.

        Replaces the top-level keys
        it is given and leaves the rest untouched.

        Args:
          investigation_enabled: Whether investigation mode is enabled for the user. Only meaningful for staff
              users with investigation access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/users/me/preferences",
            body=await async_maybe_transform(
                {"investigation_enabled": investigation_enabled}, preference_update_params.PreferenceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpdateResponse,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            preferences.update,
        )

    @cached_property
    def notifications(self) -> NotificationsResourceWithRawResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return NotificationsResourceWithRawResponse(self._preferences.notifications)


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            preferences.update,
        )

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithRawResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncNotificationsResourceWithRawResponse(self._preferences.notifications)


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            preferences.update,
        )

    @cached_property
    def notifications(self) -> NotificationsResourceWithStreamingResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return NotificationsResourceWithStreamingResponse(self._preferences.notifications)


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            preferences.update,
        )

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        return AsyncNotificationsResourceWithStreamingResponse(self._preferences.notifications)
