# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import recommended_action_run_params, recommended_action_list_params, recommended_action_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.recommended_action_run_response import RecommendedActionRunResponse
from ..types.recommended_action_list_response import RecommendedActionListResponse
from ..types.recommended_action_retrieve_response import RecommendedActionRetrieveResponse

__all__ = ["RecommendedActionsResource", "AsyncRecommendedActionsResource"]


class RecommendedActionsResource(SyncAPIResource):
    """
    A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

    Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
    """

    @cached_property
    def with_raw_response(self) -> RecommendedActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return RecommendedActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecommendedActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return RecommendedActionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        chain_id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecommendedActionRetrieveResponse:
        """
        Retrieves a recommended action chain by id, including chains that have already
        been run. Seeded chains are reconstructed from their preset; generated chains
        are read from the account's stored chain, with each step's filled-in input.

        Args:
          account_id: Account ID, prefixed `biz_`. Defaults to the API key's own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        return self._get(
            path_template("/recommended_actions/{chain_id}", chain_id=chain_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, recommended_action_retrieve_params.RecommendedActionRetrieveParams
                ),
            ),
            cast_to=RecommendedActionRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecommendedActionListResponse:
        """
        Lists the recommended action chains for an account — short sequences of actions
        (create a product, price it, publish it) the account should run next, gated on
        what it already has.

        Args:
          account_id: Account ID, prefixed `biz_`. Defaults to the API key's own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/recommended_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"account_id": account_id}, recommended_action_list_params.RecommendedActionListParams
                ),
            ),
            cast_to=RecommendedActionListResponse,
        )

    def run(
        self,
        chain_id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RecommendedActionRunResponse:
        """Records that the caller ran a recommended action chain.

        Nothing is executed
        server-side yet — the client follows the chain's step CTAs itself; this writes
        the `recommended_action_chain.executed` analytics event.

        Args:
          account_id: Account ID, prefixed `biz_`. Defaults to the API key's own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        return self._post(
            path_template("/recommended_actions/{chain_id}", chain_id=chain_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {"account_id": account_id}, recommended_action_run_params.RecommendedActionRunParams
                ),
            ),
            cast_to=RecommendedActionRunResponse,
        )


class AsyncRecommendedActionsResource(AsyncAPIResource):
    """
    A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

    Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRecommendedActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecommendedActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecommendedActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncRecommendedActionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        chain_id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecommendedActionRetrieveResponse:
        """
        Retrieves a recommended action chain by id, including chains that have already
        been run. Seeded chains are reconstructed from their preset; generated chains
        are read from the account's stored chain, with each step's filled-in input.

        Args:
          account_id: Account ID, prefixed `biz_`. Defaults to the API key's own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        return await self._get(
            path_template("/recommended_actions/{chain_id}", chain_id=chain_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, recommended_action_retrieve_params.RecommendedActionRetrieveParams
                ),
            ),
            cast_to=RecommendedActionRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecommendedActionListResponse:
        """
        Lists the recommended action chains for an account — short sequences of actions
        (create a product, price it, publish it) the account should run next, gated on
        what it already has.

        Args:
          account_id: Account ID, prefixed `biz_`. Defaults to the API key's own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/recommended_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, recommended_action_list_params.RecommendedActionListParams
                ),
            ),
            cast_to=RecommendedActionListResponse,
        )

    async def run(
        self,
        chain_id: str,
        *,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RecommendedActionRunResponse:
        """Records that the caller ran a recommended action chain.

        Nothing is executed
        server-side yet — the client follows the chain's step CTAs itself; this writes
        the `recommended_action_chain.executed` analytics event.

        Args:
          account_id: Account ID, prefixed `biz_`. Defaults to the API key's own account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        return await self._post(
            path_template("/recommended_actions/{chain_id}", chain_id=chain_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=await async_maybe_transform(
                    {"account_id": account_id}, recommended_action_run_params.RecommendedActionRunParams
                ),
            ),
            cast_to=RecommendedActionRunResponse,
        )


class RecommendedActionsResourceWithRawResponse:
    def __init__(self, recommended_actions: RecommendedActionsResource) -> None:
        self._recommended_actions = recommended_actions

        self.retrieve = to_raw_response_wrapper(
            recommended_actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            recommended_actions.list,
        )
        self.run = to_raw_response_wrapper(
            recommended_actions.run,
        )


class AsyncRecommendedActionsResourceWithRawResponse:
    def __init__(self, recommended_actions: AsyncRecommendedActionsResource) -> None:
        self._recommended_actions = recommended_actions

        self.retrieve = async_to_raw_response_wrapper(
            recommended_actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            recommended_actions.list,
        )
        self.run = async_to_raw_response_wrapper(
            recommended_actions.run,
        )


class RecommendedActionsResourceWithStreamingResponse:
    def __init__(self, recommended_actions: RecommendedActionsResource) -> None:
        self._recommended_actions = recommended_actions

        self.retrieve = to_streamed_response_wrapper(
            recommended_actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            recommended_actions.list,
        )
        self.run = to_streamed_response_wrapper(
            recommended_actions.run,
        )


class AsyncRecommendedActionsResourceWithStreamingResponse:
    def __init__(self, recommended_actions: AsyncRecommendedActionsResource) -> None:
        self._recommended_actions = recommended_actions

        self.retrieve = async_to_streamed_response_wrapper(
            recommended_actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            recommended_actions.list,
        )
        self.run = async_to_streamed_response_wrapper(
            recommended_actions.run,
        )
