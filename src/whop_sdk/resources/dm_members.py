# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import dm_member_list_params, dm_member_create_params, dm_member_update_params
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
from ..types.dm_member_list_response import DmMemberListResponse
from ..types.dm_member_create_response import DmMemberCreateResponse
from ..types.dm_member_delete_response import DmMemberDeleteResponse
from ..types.dm_member_update_response import DmMemberUpdateResponse
from ..types.dm_member_retrieve_response import DmMemberRetrieveResponse

__all__ = ["DmMembersResource", "AsyncDmMembersResource"]


class DmMembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DmMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return DmMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DmMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return DmMembersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        channel_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmMemberCreateResponse:
        """
        Adds a user to a DM channel

        Required permissions:

        - `dms:channel:manage`

        Args:
          channel_id: The ID of the DM channel to add the member to

          user_id: The ID of the user to add to the channel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dm_members",
            body=maybe_transform(
                {
                    "channel_id": channel_id,
                    "user_id": user_id,
                },
                dm_member_create_params.DmMemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberCreateResponse,
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
    ) -> DmMemberRetrieveResponse:
        """
        Retrieves a DM channel member

        Required permissions:

        - `dms:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/dm_members/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        notification_preference: Optional[Literal["all", "mentions", "none"]] | Omit = omit,
        status: Optional[Literal["requested", "accepted", "hidden", "closed", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmMemberUpdateResponse:
        """
        Updates a DM channel member's settings

        Required permissions:

        - `dms:channel:manage`

        Args:
          notification_preference: The notification preferences for a DMs feed member

          status: The statuses of a DMs feed member

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/dm_members/{id}",
            body=maybe_transform(
                {
                    "notification_preference": notification_preference,
                    "status": status,
                },
                dm_member_update_params.DmMemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberUpdateResponse,
        )

    def list(
        self,
        *,
        channel_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[DmMemberListResponse]:
        """
        Lists members of a DM channel

        Required permissions:

        - `dms:read`

        Args:
          channel_id: The ID of the DM channel to list members for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dm_members",
            page=SyncCursorPage[DmMemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel_id": channel_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    dm_member_list_params.DmMemberListParams,
                ),
            ),
            model=DmMemberListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmMemberDeleteResponse:
        """
        Removes a user from a DM channel

        Required permissions:

        - `dms:channel:manage`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/dm_members/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberDeleteResponse,
        )


class AsyncDmMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDmMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDmMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDmMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncDmMembersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        channel_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmMemberCreateResponse:
        """
        Adds a user to a DM channel

        Required permissions:

        - `dms:channel:manage`

        Args:
          channel_id: The ID of the DM channel to add the member to

          user_id: The ID of the user to add to the channel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dm_members",
            body=await async_maybe_transform(
                {
                    "channel_id": channel_id,
                    "user_id": user_id,
                },
                dm_member_create_params.DmMemberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberCreateResponse,
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
    ) -> DmMemberRetrieveResponse:
        """
        Retrieves a DM channel member

        Required permissions:

        - `dms:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/dm_members/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        notification_preference: Optional[Literal["all", "mentions", "none"]] | Omit = omit,
        status: Optional[Literal["requested", "accepted", "hidden", "closed", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmMemberUpdateResponse:
        """
        Updates a DM channel member's settings

        Required permissions:

        - `dms:channel:manage`

        Args:
          notification_preference: The notification preferences for a DMs feed member

          status: The statuses of a DMs feed member

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/dm_members/{id}",
            body=await async_maybe_transform(
                {
                    "notification_preference": notification_preference,
                    "status": status,
                },
                dm_member_update_params.DmMemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberUpdateResponse,
        )

    def list(
        self,
        *,
        channel_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DmMemberListResponse, AsyncCursorPage[DmMemberListResponse]]:
        """
        Lists members of a DM channel

        Required permissions:

        - `dms:read`

        Args:
          channel_id: The ID of the DM channel to list members for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dm_members",
            page=AsyncCursorPage[DmMemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel_id": channel_id,
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                    },
                    dm_member_list_params.DmMemberListParams,
                ),
            ),
            model=DmMemberListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmMemberDeleteResponse:
        """
        Removes a user from a DM channel

        Required permissions:

        - `dms:channel:manage`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/dm_members/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmMemberDeleteResponse,
        )


class DmMembersResourceWithRawResponse:
    def __init__(self, dm_members: DmMembersResource) -> None:
        self._dm_members = dm_members

        self.create = to_raw_response_wrapper(
            dm_members.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dm_members.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dm_members.update,
        )
        self.list = to_raw_response_wrapper(
            dm_members.list,
        )
        self.delete = to_raw_response_wrapper(
            dm_members.delete,
        )


class AsyncDmMembersResourceWithRawResponse:
    def __init__(self, dm_members: AsyncDmMembersResource) -> None:
        self._dm_members = dm_members

        self.create = async_to_raw_response_wrapper(
            dm_members.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dm_members.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dm_members.update,
        )
        self.list = async_to_raw_response_wrapper(
            dm_members.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dm_members.delete,
        )


class DmMembersResourceWithStreamingResponse:
    def __init__(self, dm_members: DmMembersResource) -> None:
        self._dm_members = dm_members

        self.create = to_streamed_response_wrapper(
            dm_members.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dm_members.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dm_members.update,
        )
        self.list = to_streamed_response_wrapper(
            dm_members.list,
        )
        self.delete = to_streamed_response_wrapper(
            dm_members.delete,
        )


class AsyncDmMembersResourceWithStreamingResponse:
    def __init__(self, dm_members: AsyncDmMembersResource) -> None:
        self._dm_members = dm_members

        self.create = async_to_streamed_response_wrapper(
            dm_members.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dm_members.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dm_members.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dm_members.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dm_members.delete,
        )
