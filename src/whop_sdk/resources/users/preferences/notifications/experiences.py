# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.users.preferences.notifications import experience_list_params
from .....types.users.preferences.notifications.experience_list_response import ExperienceListResponse

__all__ = ["ExperiencesResource", "AsyncExperiencesResource"]


class ExperiencesResource(SyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def with_raw_response(self) -> ExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ExperiencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ExperienceListResponse]:
        """Lists the authenticated user's per-experience notification levels.

        Experiences
        the user never set a level for are omitted — their effective level is `all`.

        Args:
          after: A cursor; returns preferences after this position.

          first: The number of preferences to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/preferences/notifications/experiences",
            page=SyncCursorPage[ExperienceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    experience_list_params.ExperienceListParams,
                ),
            ),
            model=ExperienceListResponse,
        )


class AsyncExperiencesResource(AsyncAPIResource):
    """A User represents a person on Whop.

    Users have a public profile and can buy products, join accounts, and access experiences.

    Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncExperiencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        first: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExperienceListResponse, AsyncCursorPage[ExperienceListResponse]]:
        """Lists the authenticated user's per-experience notification levels.

        Experiences
        the user never set a level for are omitted — their effective level is `all`.

        Args:
          after: A cursor; returns preferences after this position.

          first: The number of preferences to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/users/me/preferences/notifications/experiences",
            page=AsyncCursorPage[ExperienceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "first": first,
                    },
                    experience_list_params.ExperienceListParams,
                ),
            ),
            model=ExperienceListResponse,
        )


class ExperiencesResourceWithRawResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.list = to_raw_response_wrapper(
            experiences.list,
        )


class AsyncExperiencesResourceWithRawResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.list = async_to_raw_response_wrapper(
            experiences.list,
        )


class ExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.list = to_streamed_response_wrapper(
            experiences.list,
        )


class AsyncExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.list = async_to_streamed_response_wrapper(
            experiences.list,
        )
