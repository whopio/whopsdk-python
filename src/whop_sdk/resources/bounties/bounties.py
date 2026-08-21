# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import bounty_list_params, bounty_create_params, bounty_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .submissions import (
    SubmissionsResource,
    AsyncSubmissionsResource,
    SubmissionsResourceWithRawResponse,
    AsyncSubmissionsResourceWithRawResponse,
    SubmissionsResourceWithStreamingResponse,
    AsyncSubmissionsResourceWithStreamingResponse,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.bounty import Bounty
from ...types.bounty_list_item import BountyListItem

__all__ = ["BountiesResource", "AsyncBountiesResource"]


class BountiesResource(SyncAPIResource):
    """A Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
    """

    @cached_property
    def submissions(self) -> SubmissionsResource:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return SubmissionsResource(self._client)

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
        accepted_submissions_per_user_limit: Optional[int] | Omit = omit,
        account_id: Optional[str] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        business_goal_type: Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
        | Omit = omit,
        capture_spec: bounty_create_params.CaptureSpec | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        frequency: Literal["once", "hourly", "daily", "weekly", "monthly"] | Omit = omit,
        publish_at: Optional[str] | Omit = omit,
        publish_at_timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
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

          accepted_submissions_per_user_limit: How many winner slots one worker can win. Defaults to `1`. Wins plus proofs
              awaiting review never exceed this number, and a worker runs one attempt at a
              time. Cannot exceed `accepted_submissions_limit`.

          account_id: Account whose balance funds the bounty pool (`biz_` tag). Defaults to the
              caller's personal balance. Requires permission to move the account's funds.

          allowed_country_codes: Countries whose residents can work the bounty, as ISO 3166 alpha-2 codes. Empty
              means worldwide.

          business_goal_type: What the poster wants the work to achieve, declared once here.

          capture_spec: Per-bounty overrides of the served capture contract. Only accepted when
              `business_goal_type` is `data_capture`; omitted fields keep the platform
              defaults, and the resulting contract is echoed back as `capture_spec` on the
              bounty.

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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/bounties",
            body=maybe_transform(
                {
                    "description": description,
                    "gross_reward_amount": gross_reward_amount,
                    "title": title,
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "accepted_submissions_per_user_limit": accepted_submissions_per_user_limit,
                    "account_id": account_id,
                    "allowed_country_codes": allowed_country_codes,
                    "business_goal_type": business_goal_type,
                    "capture_spec": capture_spec,
                    "experience_id": experience_id,
                    "frequency": frequency,
                    "publish_at": publish_at,
                    "publish_at_timezone": publish_at_timezone,
                },
                bounty_create_params.BountyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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

        Authentication is optional: a request with no
        credential reads the bounty when it is publicly visible — published or
        completed, and not restricted to a private experience's members. Bounties
        outside the caller's scope, and bounties not publicly visible to an anonymous
        caller, return `404`.

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

    def update(
        self,
        id: str,
        *,
        accepted_submissions_limit: Optional[int] | Omit = omit,
        accepted_submissions_per_user_limit: Optional[int] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        business_goal_type: Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
        | Omit = omit,
        description: str | Omit = omit,
        frequency: Literal["once", "hourly", "daily", "weekly", "monthly"] | Omit = omit,
        gross_reward_amount: Optional[float] | Omit = omit,
        publish_at: Optional[str] | Omit = omit,
        publish_at_timezone: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Bounty:
        """Updates a bounty.

        A published bounty accepts title, description, and country
        targeting while it is still open with nothing under review. A scheduled
        (not-yet-published) draft additionally accepts the reward, winner slots, and
        schedule.

        Args:
          accepted_submissions_limit: Scheduled drafts only. Number of submissions that can be accepted (winner
              slots).

          accepted_submissions_per_user_limit: How many winner slots one worker can win. Defaults to `1`. Wins plus proofs
              awaiting review never exceed this number, and a worker runs one attempt at a
              time. Cannot exceed `accepted_submissions_limit`. Editable while the bounty is
              still open with nothing under review.

          allowed_country_codes: Replace the countries whose residents can work the bounty, as ISO 3166 alpha-2
              codes. Empty means worldwide.

          business_goal_type: What the poster wants the work to achieve, declared once here.

          description: New full task instructions.

          frequency: Scheduled drafts only. How often the schedule creates a new bounty.

          gross_reward_amount: Scheduled drafts only. Gross bounty-pool amount (USD) escrowed per accepted
              submission. The escrowed total (this times accepted_submissions_limit) must stay
              at least $5.

          publish_at: Scheduled drafts only. New ISO 8601 time to publish the draft. Must be in the
              future.

          publish_at_timezone: Scheduled drafts only. IANA timezone for recurring occurrences.

          title: New short name of the task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/bounties/{id}", id=id),
            body=maybe_transform(
                {
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "accepted_submissions_per_user_limit": accepted_submissions_per_user_limit,
                    "allowed_country_codes": allowed_country_codes,
                    "business_goal_type": business_goal_type,
                    "description": description,
                    "frequency": frequency,
                    "gross_reward_amount": gross_reward_amount,
                    "publish_at": publish_at,
                    "publish_at_timezone": publish_at_timezone,
                    "title": title,
                },
                bounty_update_params.BountyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Bounty,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        business_goal_type: Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
        | Omit = omit,
        country: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        experience_id: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "gross_paid_out_amount", "gross_reward_amount"] | Omit = omit,
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

          business_goal_type: Filter by the poster's declared goal. Bounties created before the goal taxonomy
              carry no goal and never match this filter.

          country: Only bounties workable from this country, as an ISO 3166-1 alpha-2 code.
              Bounties with no country targeting are workable worldwide and always match.

          created_after: Only bounties created after this ISO 8601 timestamp.

          created_before: Only bounties created before this ISO 8601 timestamp.

          direction: Sort direction.

          experience_id: Only bounties posted to this forum experience, prefixed `exp_`. An unknown
              experience, or one outside the caller's scope, matches nothing.

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
                        "business_goal_type": business_goal_type,
                        "country": country,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "experience_id": experience_id,
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

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Bounty:
        """Cancels a bounty.

        With no in-flight work, it cancels immediately and refunds the
        funder. Otherwise it stops new submissions and cancels once the in-flight work
        resolves and pays out. Repeating the request is a no-op. A bounty that already
        paid out every slot returns `400`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/bounties/{id}/cancel", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Bounty,
        )


class AsyncBountiesResource(AsyncAPIResource):
    """A Bounty is a paid task posted by an account or user.

    The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

    Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
    """

    @cached_property
    def submissions(self) -> AsyncSubmissionsResource:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return AsyncSubmissionsResource(self._client)

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
        accepted_submissions_per_user_limit: Optional[int] | Omit = omit,
        account_id: Optional[str] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        business_goal_type: Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
        | Omit = omit,
        capture_spec: bounty_create_params.CaptureSpec | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        frequency: Literal["once", "hourly", "daily", "weekly", "monthly"] | Omit = omit,
        publish_at: Optional[str] | Omit = omit,
        publish_at_timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
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

          accepted_submissions_per_user_limit: How many winner slots one worker can win. Defaults to `1`. Wins plus proofs
              awaiting review never exceed this number, and a worker runs one attempt at a
              time. Cannot exceed `accepted_submissions_limit`.

          account_id: Account whose balance funds the bounty pool (`biz_` tag). Defaults to the
              caller's personal balance. Requires permission to move the account's funds.

          allowed_country_codes: Countries whose residents can work the bounty, as ISO 3166 alpha-2 codes. Empty
              means worldwide.

          business_goal_type: What the poster wants the work to achieve, declared once here.

          capture_spec: Per-bounty overrides of the served capture contract. Only accepted when
              `business_goal_type` is `data_capture`; omitted fields keep the platform
              defaults, and the resulting contract is echoed back as `capture_spec` on the
              bounty.

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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/bounties",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "gross_reward_amount": gross_reward_amount,
                    "title": title,
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "accepted_submissions_per_user_limit": accepted_submissions_per_user_limit,
                    "account_id": account_id,
                    "allowed_country_codes": allowed_country_codes,
                    "business_goal_type": business_goal_type,
                    "capture_spec": capture_spec,
                    "experience_id": experience_id,
                    "frequency": frequency,
                    "publish_at": publish_at,
                    "publish_at_timezone": publish_at_timezone,
                },
                bounty_create_params.BountyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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

        Authentication is optional: a request with no
        credential reads the bounty when it is publicly visible — published or
        completed, and not restricted to a private experience's members. Bounties
        outside the caller's scope, and bounties not publicly visible to an anonymous
        caller, return `404`.

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

    async def update(
        self,
        id: str,
        *,
        accepted_submissions_limit: Optional[int] | Omit = omit,
        accepted_submissions_per_user_limit: Optional[int] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        business_goal_type: Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
        | Omit = omit,
        description: str | Omit = omit,
        frequency: Literal["once", "hourly", "daily", "weekly", "monthly"] | Omit = omit,
        gross_reward_amount: Optional[float] | Omit = omit,
        publish_at: Optional[str] | Omit = omit,
        publish_at_timezone: Optional[str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Bounty:
        """Updates a bounty.

        A published bounty accepts title, description, and country
        targeting while it is still open with nothing under review. A scheduled
        (not-yet-published) draft additionally accepts the reward, winner slots, and
        schedule.

        Args:
          accepted_submissions_limit: Scheduled drafts only. Number of submissions that can be accepted (winner
              slots).

          accepted_submissions_per_user_limit: How many winner slots one worker can win. Defaults to `1`. Wins plus proofs
              awaiting review never exceed this number, and a worker runs one attempt at a
              time. Cannot exceed `accepted_submissions_limit`. Editable while the bounty is
              still open with nothing under review.

          allowed_country_codes: Replace the countries whose residents can work the bounty, as ISO 3166 alpha-2
              codes. Empty means worldwide.

          business_goal_type: What the poster wants the work to achieve, declared once here.

          description: New full task instructions.

          frequency: Scheduled drafts only. How often the schedule creates a new bounty.

          gross_reward_amount: Scheduled drafts only. Gross bounty-pool amount (USD) escrowed per accepted
              submission. The escrowed total (this times accepted_submissions_limit) must stay
              at least $5.

          publish_at: Scheduled drafts only. New ISO 8601 time to publish the draft. Must be in the
              future.

          publish_at_timezone: Scheduled drafts only. IANA timezone for recurring occurrences.

          title: New short name of the task.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/bounties/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "accepted_submissions_per_user_limit": accepted_submissions_per_user_limit,
                    "allowed_country_codes": allowed_country_codes,
                    "business_goal_type": business_goal_type,
                    "description": description,
                    "frequency": frequency,
                    "gross_reward_amount": gross_reward_amount,
                    "publish_at": publish_at,
                    "publish_at_timezone": publish_at_timezone,
                    "title": title,
                },
                bounty_update_params.BountyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Bounty,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        business_goal_type: Literal[
            "clipping",
            "post_engagement",
            "owned_account_growth",
            "ugc_content",
            "local_activation",
            "data_capture",
            "other",
        ]
        | Omit = omit,
        country: str | Omit = omit,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        experience_id: str | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at", "gross_paid_out_amount", "gross_reward_amount"] | Omit = omit,
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

          business_goal_type: Filter by the poster's declared goal. Bounties created before the goal taxonomy
              carry no goal and never match this filter.

          country: Only bounties workable from this country, as an ISO 3166-1 alpha-2 code.
              Bounties with no country targeting are workable worldwide and always match.

          created_after: Only bounties created after this ISO 8601 timestamp.

          created_before: Only bounties created before this ISO 8601 timestamp.

          direction: Sort direction.

          experience_id: Only bounties posted to this forum experience, prefixed `exp_`. An unknown
              experience, or one outside the caller's scope, matches nothing.

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
                        "business_goal_type": business_goal_type,
                        "country": country,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "experience_id": experience_id,
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

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Bounty:
        """Cancels a bounty.

        With no in-flight work, it cancels immediately and refunds the
        funder. Otherwise it stops new submissions and cancels once the in-flight work
        resolves and pays out. Repeating the request is a no-op. A bounty that already
        paid out every slot returns `400`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/bounties/{id}/cancel", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Bounty,
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
        self.update = to_raw_response_wrapper(
            bounties.update,
        )
        self.list = to_raw_response_wrapper(
            bounties.list,
        )
        self.cancel = to_raw_response_wrapper(
            bounties.cancel,
        )

    @cached_property
    def submissions(self) -> SubmissionsResourceWithRawResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return SubmissionsResourceWithRawResponse(self._bounties.submissions)


class AsyncBountiesResourceWithRawResponse:
    def __init__(self, bounties: AsyncBountiesResource) -> None:
        self._bounties = bounties

        self.create = async_to_raw_response_wrapper(
            bounties.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bounties.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bounties.update,
        )
        self.list = async_to_raw_response_wrapper(
            bounties.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            bounties.cancel,
        )

    @cached_property
    def submissions(self) -> AsyncSubmissionsResourceWithRawResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return AsyncSubmissionsResourceWithRawResponse(self._bounties.submissions)


class BountiesResourceWithStreamingResponse:
    def __init__(self, bounties: BountiesResource) -> None:
        self._bounties = bounties

        self.create = to_streamed_response_wrapper(
            bounties.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bounties.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bounties.update,
        )
        self.list = to_streamed_response_wrapper(
            bounties.list,
        )
        self.cancel = to_streamed_response_wrapper(
            bounties.cancel,
        )

    @cached_property
    def submissions(self) -> SubmissionsResourceWithStreamingResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return SubmissionsResourceWithStreamingResponse(self._bounties.submissions)


class AsyncBountiesResourceWithStreamingResponse:
    def __init__(self, bounties: AsyncBountiesResource) -> None:
        self._bounties = bounties

        self.create = async_to_streamed_response_wrapper(
            bounties.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bounties.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bounties.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bounties.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            bounties.cancel,
        )

    @cached_property
    def submissions(self) -> AsyncSubmissionsResourceWithStreamingResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        return AsyncSubmissionsResourceWithStreamingResponse(self._bounties.submissions)
