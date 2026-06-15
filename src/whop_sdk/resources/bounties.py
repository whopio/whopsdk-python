# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import bounty_list_params, bounty_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.shared.currency import Currency
from ..types.shared.direction import Direction
from ..types.bounty_list_response import BountyListResponse
from ..types.bounty_create_response import BountyCreateResponse
from ..types.bounty_retrieve_response import BountyRetrieveResponse

__all__ = ["BountiesResource", "AsyncBountiesResource"]


class BountiesResource(SyncAPIResource):
    """Bounties"""

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
        base_unit_amount: float,
        currency: Currency,
        description: str,
        title: str,
        accepted_submissions_limit: Optional[int] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        business_goal_type: Optional[
            Literal["clipping", "post_engagement", "owned_account_growth", "ugc_content", "local_activation", "other"]
        ]
        | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        origin_account_id: Optional[str] | Omit = omit,
        post_markdown_content: Optional[str] | Omit = omit,
        post_title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BountyCreateResponse:
        """
        Create a new workforce bounty by funding a dedicated bounty pool.

        Required permissions:

        - `bounty:create`

        Args:
          base_unit_amount: The amount paid to each approved submission. The total bounty pool funded is
              this amount times accepted_submissions_limit.

          currency: The currency for the bounty pool funding amount.

          description: The description of the bounty.

          title: The title of the bounty.

          accepted_submissions_limit: The number of submissions that can be approved before the bounty closes.
              Defaults to 1.

          allowed_country_codes: The ISO3166 country codes where this bounty should be visible. Empty means
              globally visible.

          business_goal_type: What the poster is trying to accomplish with a workforce bounty. Used for
              product taxonomy and analytics, separate from the bounty's implementation type.

          experience_id: An optional experience to scope the bounty to.

          origin_account_id: The user (user*\\**) or company (biz*\\**) tag whose balance funds this bounty pool.
              Defaults to the requester's personal balance when omitted. The requester must be
              the user themself or an owner/admin of the company.

          post_markdown_content: Optional markdown body for the anchor forum post. Falls back to the bounty
              description when omitted.

          post_title: Optional title for the anchor forum post. Falls back to the bounty title when
              omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/bounties",
            body=maybe_transform(
                {
                    "base_unit_amount": base_unit_amount,
                    "currency": currency,
                    "description": description,
                    "title": title,
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "allowed_country_codes": allowed_country_codes,
                    "business_goal_type": business_goal_type,
                    "experience_id": experience_id,
                    "origin_account_id": origin_account_id,
                    "post_markdown_content": post_markdown_content,
                    "post_title": post_title,
                },
                bounty_create_params.BountyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BountyCreateResponse,
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
    ) -> BountyRetrieveResponse:
        """
        Retrieves a workforce bounty for the current authenticated user.

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
            cast_to=BountyRetrieveResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        status: Optional[Literal["published", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BountyListResponse]:
        """Returns a paginated list of workforce bounties.

        When experienceId is provided,
        returns bounties scoped to that experience. When omitted, returns bounties with
        no experience.

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          experience_id: The experience to list bounties for. When omitted, returns bounties with no
              experience.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          status: The available bounty statuses to choose from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bounties",
            page=SyncCursorPage[BountyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "experience_id": experience_id,
                        "first": first,
                        "last": last,
                        "status": status,
                    },
                    bounty_list_params.BountyListParams,
                ),
            ),
            model=BountyListResponse,
        )


class AsyncBountiesResource(AsyncAPIResource):
    """Bounties"""

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
        base_unit_amount: float,
        currency: Currency,
        description: str,
        title: str,
        accepted_submissions_limit: Optional[int] | Omit = omit,
        allowed_country_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        business_goal_type: Optional[
            Literal["clipping", "post_engagement", "owned_account_growth", "ugc_content", "local_activation", "other"]
        ]
        | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        origin_account_id: Optional[str] | Omit = omit,
        post_markdown_content: Optional[str] | Omit = omit,
        post_title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BountyCreateResponse:
        """
        Create a new workforce bounty by funding a dedicated bounty pool.

        Required permissions:

        - `bounty:create`

        Args:
          base_unit_amount: The amount paid to each approved submission. The total bounty pool funded is
              this amount times accepted_submissions_limit.

          currency: The currency for the bounty pool funding amount.

          description: The description of the bounty.

          title: The title of the bounty.

          accepted_submissions_limit: The number of submissions that can be approved before the bounty closes.
              Defaults to 1.

          allowed_country_codes: The ISO3166 country codes where this bounty should be visible. Empty means
              globally visible.

          business_goal_type: What the poster is trying to accomplish with a workforce bounty. Used for
              product taxonomy and analytics, separate from the bounty's implementation type.

          experience_id: An optional experience to scope the bounty to.

          origin_account_id: The user (user*\\**) or company (biz*\\**) tag whose balance funds this bounty pool.
              Defaults to the requester's personal balance when omitted. The requester must be
              the user themself or an owner/admin of the company.

          post_markdown_content: Optional markdown body for the anchor forum post. Falls back to the bounty
              description when omitted.

          post_title: Optional title for the anchor forum post. Falls back to the bounty title when
              omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/bounties",
            body=await async_maybe_transform(
                {
                    "base_unit_amount": base_unit_amount,
                    "currency": currency,
                    "description": description,
                    "title": title,
                    "accepted_submissions_limit": accepted_submissions_limit,
                    "allowed_country_codes": allowed_country_codes,
                    "business_goal_type": business_goal_type,
                    "experience_id": experience_id,
                    "origin_account_id": origin_account_id,
                    "post_markdown_content": post_markdown_content,
                    "post_title": post_title,
                },
                bounty_create_params.BountyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BountyCreateResponse,
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
    ) -> BountyRetrieveResponse:
        """
        Retrieves a workforce bounty for the current authenticated user.

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
            cast_to=BountyRetrieveResponse,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        experience_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        status: Optional[Literal["published", "archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BountyListResponse, AsyncCursorPage[BountyListResponse]]:
        """Returns a paginated list of workforce bounties.

        When experienceId is provided,
        returns bounties scoped to that experience. When omitted, returns bounties with
        no experience.

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          direction: The direction of the sort.

          experience_id: The experience to list bounties for. When omitted, returns bounties with no
              experience.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          status: The available bounty statuses to choose from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bounties",
            page=AsyncCursorPage[BountyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "experience_id": experience_id,
                        "first": first,
                        "last": last,
                        "status": status,
                    },
                    bounty_list_params.BountyListParams,
                ),
            ),
            model=BountyListResponse,
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
