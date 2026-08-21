# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncCursorPage, AsyncCursorPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.users.preferences.notifications import topic_list_params
from .....types.users.preferences.notifications.topic_list_response import TopicListResponse

__all__ = ["TopicsResource", "AsyncTopicsResource"]


class TopicsResource(SyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
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
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        channel: Literal["in_app", "mobile"] | Omit = omit,
        experience_id: str | Omit = omit,
        first: int | Omit = omit,
        team_account_id: str | Omit = omit,
        topic_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[TopicListResponse]:
        """
        Lists the authenticated user's topic-scoped notification preferences, plus
        user-agnostic platform defaults. Each filter matches preferences scoped to its
        value or not narrowed on that dimension. Per-experience levels are listed
        separately, by `GET /users/me/preferences/notifications/experiences`.

        Args:
          account_id: Only return preferences scoped to this account's member notifications (`biz_`
              tag).

          after: A cursor; returns preferences after this position.

          channel: Only return preferences for this delivery channel (or not narrowed to a
              channel).

          experience_id: Only return preferences scoped to this experience (`exp_` tag).

          first: The number of preferences to return.

          team_account_id: Only return preferences scoped to this account's team notifications (`biz_`
              tag).

          topic_id: Only return preferences scoped to this notification topic (`topic_` tag).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/preferences/notifications/topics",
            page=SyncCursorPage[TopicListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "channel": channel,
                        "experience_id": experience_id,
                        "first": first,
                        "team_account_id": team_account_id,
                        "topic_id": topic_id,
                    },
                    topic_list_params.TopicListParams,
                ),
            ),
            model=TopicListResponse,
        )


class AsyncTopicsResource(AsyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
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
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        channel: Literal["in_app", "mobile"] | Omit = omit,
        experience_id: str | Omit = omit,
        first: int | Omit = omit,
        team_account_id: str | Omit = omit,
        topic_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TopicListResponse, AsyncCursorPage[TopicListResponse]]:
        """
        Lists the authenticated user's topic-scoped notification preferences, plus
        user-agnostic platform defaults. Each filter matches preferences scoped to its
        value or not narrowed on that dimension. Per-experience levels are listed
        separately, by `GET /users/me/preferences/notifications/experiences`.

        Args:
          account_id: Only return preferences scoped to this account's member notifications (`biz_`
              tag).

          after: A cursor; returns preferences after this position.

          channel: Only return preferences for this delivery channel (or not narrowed to a
              channel).

          experience_id: Only return preferences scoped to this experience (`exp_` tag).

          first: The number of preferences to return.

          team_account_id: Only return preferences scoped to this account's team notifications (`biz_`
              tag).

          topic_id: Only return preferences scoped to this notification topic (`topic_` tag).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/preferences/notifications/topics",
            page=AsyncCursorPage[TopicListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "channel": channel,
                        "experience_id": experience_id,
                        "first": first,
                        "team_account_id": team_account_id,
                        "topic_id": topic_id,
                    },
                    topic_list_params.TopicListParams,
                ),
            ),
            model=TopicListResponse,
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
