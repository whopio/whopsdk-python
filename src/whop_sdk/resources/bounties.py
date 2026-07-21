# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import bounty_list_params, bounty_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.bounty import Bounty
from ..types.bounty_list_item import BountyListItem

__all__ = ["BountiesResource", "AsyncBountiesResource"]


class BountiesResource(SyncAPIResource):
    """A Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
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

    def create(
        self,
        *,
        description: str,
        gross_reward_amount: float,
        title: str,
        accepted_submissions_limit: Optional[int] | Omit = omit,
        account_id: Optional[str] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        frequency: Literal["once", "hourly", "daily", "weekly", "monthly"] | Omit = omit,
        publish_at: Optional[str] | Omit = omit,
        publish_at_timezone: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bounty:
        """Creates a bounty and escrows its reward pool.

        Publishes immediately, or as a
        scheduled draft when you set `publish_at`.

        Args:
          description: Full task instructions shown to workers.

          gross_reward_amount: Gross bounty-pool amount (USD) escrowed per accepted submission, in whole
              dollars. Platform fees and affiliate shares are paid from this amount.

          title: Short name of the task shown to workers.

          accepted_submissions_limit: Number of submissions that can be accepted (winner slots). Defaults to 1. The
              escrowed total is `gross_reward_amount` times this limit and must be at least
              $5.

          account_id: Account whose balance funds the bounty pool (`biz_` tag). Defaults to the
              caller's personal balance. Requires permission to move the account's funds.

          allowed_country_codes: Countries whose residents can work the bounty, as ISO 3166 alpha-2 codes. Empty
              means worldwide.

          experience_id: Experience to host the bounty in (`exp_` tag). Any visibility — public for an
              open bounty, private for an invited one. Required unless account_id is set, in
              which case the bounty anchors in that account's public forum.

          frequency: How often the schedule creates a new bounty. Each occurrence is a separate
              bounty. Defaults to `once`; only applies with `publish_at`.

          publish_at: ISO 8601 time to publish the bounty. When set, the bounty is created as a hidden
              draft and funded + published at this time instead of immediately.

          publish_at_timezone: IANA timezone for recurring occurrences. Required when publish_at is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/bounties",
            body=maybe_transform(
                {
                    "description": description,
                    "gross_reward_amount": gross_reward_amount,
                    "title": title,
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "account_id": account_id,
                    "allowed_country_codes": allowed_country_codes,
                    "experience_id": experience_id,
                    "frequency": frequency,
                    "publish_at": publish_at,
                    "publish_at_timezone": publish_at_timezone,
                },
                bounty_create_params.BountyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bounty,
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
    ) -> Bounty:
        """Retrieves a bounty by ID.

        Bounties outside the caller's scope return `404`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/bounties/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bounty,
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
    ) -> SyncCursorPage[BountyListItem]:
        """
        Lists bounties visible to the credential — for an account API key, the account's
        bounties including scheduled drafts; for a user token, the bounties the user can
        see and work.

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
            "/bounties",
            page=SyncCursorPage[BountyListItem],
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
            model=BountyListItem,
        )


class AsyncBountiesResource(AsyncAPIResource):
    """A Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
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

    async def create(
        self,
        *,
        description: str,
        gross_reward_amount: float,
        title: str,
        accepted_submissions_limit: Optional[int] | Omit = omit,
        account_id: Optional[str] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        frequency: Literal["once", "hourly", "daily", "weekly", "monthly"] | Omit = omit,
        publish_at: Optional[str] | Omit = omit,
        publish_at_timezone: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Bounty:
        """Creates a bounty and escrows its reward pool.

        Publishes immediately, or as a
        scheduled draft when you set `publish_at`.

        Args:
          description: Full task instructions shown to workers.

          gross_reward_amount: Gross bounty-pool amount (USD) escrowed per accepted submission, in whole
              dollars. Platform fees and affiliate shares are paid from this amount.

          title: Short name of the task shown to workers.

          accepted_submissions_limit: Number of submissions that can be accepted (winner slots). Defaults to 1. The
              escrowed total is `gross_reward_amount` times this limit and must be at least
              $5.

          account_id: Account whose balance funds the bounty pool (`biz_` tag). Defaults to the
              caller's personal balance. Requires permission to move the account's funds.

          allowed_country_codes: Countries whose residents can work the bounty, as ISO 3166 alpha-2 codes. Empty
              means worldwide.

          experience_id: Experience to host the bounty in (`exp_` tag). Any visibility — public for an
              open bounty, private for an invited one. Required unless account_id is set, in
              which case the bounty anchors in that account's public forum.

          frequency: How often the schedule creates a new bounty. Each occurrence is a separate
              bounty. Defaults to `once`; only applies with `publish_at`.

          publish_at: ISO 8601 time to publish the bounty. When set, the bounty is created as a hidden
              draft and funded + published at this time instead of immediately.

          publish_at_timezone: IANA timezone for recurring occurrences. Required when publish_at is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/bounties",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "gross_reward_amount": gross_reward_amount,
                    "title": title,
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "account_id": account_id,
                    "allowed_country_codes": allowed_country_codes,
                    "experience_id": experience_id,
                    "frequency": frequency,
                    "publish_at": publish_at,
                    "publish_at_timezone": publish_at_timezone,
                },
                bounty_create_params.BountyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bounty,
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
    ) -> Bounty:
        """Retrieves a bounty by ID.

        Bounties outside the caller's scope return `404`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/bounties/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Bounty,
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
    ) -> AsyncPaginator[BountyListItem, AsyncCursorPage[BountyListItem]]:
        """
        Lists bounties visible to the credential — for an account API key, the account's
        bounties including scheduled drafts; for a user token, the bounties the user can
        see and work.

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
            "/bounties",
            page=AsyncCursorPage[BountyListItem],
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
            model=BountyListItem,
        )


class BountiesResourceWithRawResponse:
    def __init__(self, bounties: BountiesResource) -> None:
        self._bounties = bounties

        self.create = to_raw_response_wrapper(
            bounties.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bounties.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bounties.list,
        )


class AsyncBountiesResourceWithRawResponse:
    def __init__(self, bounties: AsyncBountiesResource) -> None:
        self._bounties = bounties

        self.create = async_to_raw_response_wrapper(
            bounties.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bounties.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bounties.list,
        )


class BountiesResourceWithStreamingResponse:
    def __init__(self, bounties: BountiesResource) -> None:
        self._bounties = bounties

        self.create = to_streamed_response_wrapper(
            bounties.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bounties.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bounties.list,
        )


class AsyncBountiesResourceWithStreamingResponse:
    def __init__(self, bounties: AsyncBountiesResource) -> None:
        self._bounties = bounties

        self.create = async_to_streamed_response_wrapper(
            bounties.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bounties.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bounties.list,
        )
