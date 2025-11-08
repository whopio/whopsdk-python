# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import member_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform
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
from ..types.shared.direction import Direction
from ..types.shared.access_level import AccessLevel
from ..types.member_list_response import MemberListResponse
from ..types.shared.member_statuses import MemberStatuses
from ..types.member_retrieve_response import MemberRetrieveResponse
from ..types.shared.member_most_recent_actions import MemberMostRecentActions

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

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
    ) -> MemberRetrieveResponse:
        """
        Retrieves a member of a company by ID

        Required permissions:

        - `member:basic:read`
        - `member:email:read`
        - `member:phone:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/members/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        access_level: Optional[AccessLevel] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        most_recent_actions: Optional[List[MemberMostRecentActions]] | Omit = omit,
        order: Optional[Literal["id", "usd_total_spent", "created_at", "joined_at", "most_recent_action"]]
        | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        promo_code_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        statuses: Optional[List[MemberStatuses]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MemberListResponse]:
        """
        List the members of a company

        Required permissions:

        - `member:basic:read`
        - `member:email:read`
        - `member:phone:read`

        Args:
          company_id: The ID of the company to list members for

          access_level: The access level a given user (or company) has to a product or company.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          most_recent_actions: The most recent actions to filter the members by

          order: Which columns can be used to sort.

          plan_ids: The plan IDs to filter the members by

          product_ids: The product IDs to filter the members by

          promo_code_ids: The promo code IDs to filter the members by

          query: The name, username, or email to filter the members by. The email filter will
              only apply if the current actor has the `member:email:read` permission.

          statuses: The statuses to filter the members by

          user_ids: The user IDs to filter the members by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/members",
            page=SyncCursorPage[MemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "access_level": access_level,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "most_recent_actions": most_recent_actions,
                        "order": order,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "promo_code_ids": promo_code_ids,
                        "query": query,
                        "statuses": statuses,
                        "user_ids": user_ids,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MemberListResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

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
    ) -> MemberRetrieveResponse:
        """
        Retrieves a member of a company by ID

        Required permissions:

        - `member:basic:read`
        - `member:email:read`
        - `member:phone:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/members/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        access_level: Optional[AccessLevel] | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        most_recent_actions: Optional[List[MemberMostRecentActions]] | Omit = omit,
        order: Optional[Literal["id", "usd_total_spent", "created_at", "joined_at", "most_recent_action"]]
        | Omit = omit,
        plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        promo_code_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        statuses: Optional[List[MemberStatuses]] | Omit = omit,
        user_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MemberListResponse, AsyncCursorPage[MemberListResponse]]:
        """
        List the members of a company

        Required permissions:

        - `member:basic:read`
        - `member:email:read`
        - `member:phone:read`

        Args:
          company_id: The ID of the company to list members for

          access_level: The access level a given user (or company) has to a product or company.

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          most_recent_actions: The most recent actions to filter the members by

          order: Which columns can be used to sort.

          plan_ids: The plan IDs to filter the members by

          product_ids: The product IDs to filter the members by

          promo_code_ids: The promo code IDs to filter the members by

          query: The name, username, or email to filter the members by. The email filter will
              only apply if the current actor has the `member:email:read` permission.

          statuses: The statuses to filter the members by

          user_ids: The user IDs to filter the members by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/members",
            page=AsyncCursorPage[MemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "access_level": access_level,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "most_recent_actions": most_recent_actions,
                        "order": order,
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "promo_code_ids": promo_code_ids,
                        "query": query,
                        "statuses": statuses,
                        "user_ids": user_ids,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MemberListResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.retrieve = to_raw_response_wrapper(
            members.retrieve,
        )
        self.list = to_raw_response_wrapper(
            members.list,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.retrieve = async_to_raw_response_wrapper(
            members.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            members.list,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.retrieve = to_streamed_response_wrapper(
            members.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            members.list,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.retrieve = async_to_streamed_response_wrapper(
            members.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
