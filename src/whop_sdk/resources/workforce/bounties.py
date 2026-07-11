# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.workforce import bounty_list_params
from ...types.workforce.workforce_bounty import WorkforceBounty
from ...types.workforce.workforce_bounty_list_item import WorkforceBountyListItem

__all__ = ["BountiesResource", "AsyncBountiesResource"]


class BountiesResource(SyncAPIResource):
    """A Workforce Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
    """

    @cached_property
    def with_raw_response(self) -> BountiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return BountiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BountiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return BountiesResourceWithStreamingResponse(self)

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
    ) -> WorkforceBounty:
        """Retrieves one workforce bounty by ID.

        The bounty must be visible to the
        credential; bounties outside the caller's scope return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/workforce/bounties/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkforceBounty,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "gross_paid_out_amount"] | Omit = omit,
        query: str | Omit = omit,
        status: Literal["scheduled", "open", "closed", "completed", "canceled"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[WorkforceBountyListItem]:
        """Lists workforce bounties visible to the credential.

        Account API keys return the
        account's bounties, scheduled drafts included; user tokens return the bounties
        the user can see and work. Pass account_id to view one account's bounties as a
        team member (or a connected account of the caller's), or user_id (your own) to
        list the bounties you participated in.

        Args:
          account_id: Scope the list to this account (`biz_` tag). Requires read access to the
              account; account API keys may pass their own account or a connected account.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only bounties created after this ISO 8601 timestamp.

          created_before: Only bounties created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of bounties to return from the start of the window.

          last: Number of bounties to return from the end of the window.

          order: Sort field.

          query: Substring match on the bounty title or ID.

          status: Filter by lifecycle state.

          user_id: List the bounties this user participated in (`user_` tag). Must be the
              authenticated user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/workforce/bounties",
            page=SyncCursorPage[WorkforceBountyListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "query": query,
                        "status": status,
                        "user_id": user_id,
                    },
                    bounty_list_params.BountyListParams,
                ),
            ),
            model=WorkforceBountyListItem,
        )


class AsyncBountiesResource(AsyncAPIResource):
    """A Workforce Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Workforce Bounties API to list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBountiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBountiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBountiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncBountiesResourceWithStreamingResponse(self)

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
    ) -> WorkforceBounty:
        """Retrieves one workforce bounty by ID.

        The bounty must be visible to the
        credential; bounties outside the caller's scope return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/workforce/bounties/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkforceBounty,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "gross_paid_out_amount"] | Omit = omit,
        query: str | Omit = omit,
        status: Literal["scheduled", "open", "closed", "completed", "canceled"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkforceBountyListItem, AsyncCursorPage[WorkforceBountyListItem]]:
        """Lists workforce bounties visible to the credential.

        Account API keys return the
        account's bounties, scheduled drafts included; user tokens return the bounties
        the user can see and work. Pass account_id to view one account's bounties as a
        team member (or a connected account of the caller's), or user_id (your own) to
        list the bounties you participated in.

        Args:
          account_id: Scope the list to this account (`biz_` tag). Requires read access to the
              account; account API keys may pass their own account or a connected account.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only bounties created after this ISO 8601 timestamp.

          created_before: Only bounties created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of bounties to return from the start of the window.

          last: Number of bounties to return from the end of the window.

          order: Sort field.

          query: Substring match on the bounty title or ID.

          status: Filter by lifecycle state.

          user_id: List the bounties this user participated in (`user_` tag). Must be the
              authenticated user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/workforce/bounties",
            page=AsyncCursorPage[WorkforceBountyListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "after": after,
                        "before": before,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "query": query,
                        "status": status,
                        "user_id": user_id,
                    },
                    bounty_list_params.BountyListParams,
                ),
            ),
            model=WorkforceBountyListItem,
        )


class BountiesResourceWithRawResponse:
    def __init__(self, bounties: BountiesResource) -> None:
        self._bounties = bounties

        self.retrieve = to_raw_response_wrapper(
            bounties.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bounties.list,
        )


class AsyncBountiesResourceWithRawResponse:
    def __init__(self, bounties: AsyncBountiesResource) -> None:
        self._bounties = bounties

        self.retrieve = async_to_raw_response_wrapper(
            bounties.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bounties.list,
        )


class BountiesResourceWithStreamingResponse:
    def __init__(self, bounties: BountiesResource) -> None:
        self._bounties = bounties

        self.retrieve = to_streamed_response_wrapper(
            bounties.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bounties.list,
        )


class AsyncBountiesResourceWithStreamingResponse:
    def __init__(self, bounties: AsyncBountiesResource) -> None:
        self._bounties = bounties

        self.retrieve = async_to_streamed_response_wrapper(
            bounties.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bounties.list,
        )
