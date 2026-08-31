# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import resolution_center_case_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given
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
from ..types.resolution_center_case_list_response import ResolutionCenterCaseListResponse
from ..types.resolution_center_case_retrieve_response import ResolutionCenterCaseRetrieveResponse

__all__ = ["ResolutionCenterCasesResource", "AsyncResolutionCenterCasesResource"]


class ResolutionCenterCasesResource(SyncAPIResource):
    """
    A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

    Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
    """

    @cached_property
    def with_raw_response(self) -> ResolutionCenterCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return ResolutionCenterCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResolutionCenterCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return ResolutionCenterCasesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseRetrieveResponse:
        """
        Retrieves a single resolution center case with its full event timeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get(
            path_template("/resolution_center_cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRetrieveResponse,
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
        order: Literal["created_at", "response_due_at"] | Omit = omit,
        outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]] | Omit = omit,
        reason: List[
            Literal[
                "fraudulent",
                "product_not_received",
                "not_as_described",
                "product_unacceptable",
                "subscription_canceled",
            ]
        ]
        | Omit = omit,
        status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]] | Omit = omit,
        user_id: str | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ResolutionCenterCaseListResponse]:
        """Lists resolution center cases.

        Without `account_id` you get every case you can
        read — the ones you opened as a buyer and every account you are a team member
        of; the filters narrow that list.

        Args:
          account_id: Only cases filed against this account (`biz_` tag). With read access to the
              account this lists its whole queue; without, only the cases you opened against
              it.

          after: A cursor; returns cases after this position.

          before: A cursor; returns cases before this position.

          created_after: Only cases created after this ISO 8601 timestamp.

          created_before: Only cases created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of cases to return (default 20, max 100).

          last: The number of cases to return from the end of the range.

          order: The field to sort cases by.

          outcome: Only closed cases that ended these ways. Repeat the parameter to pass several.

          reason: Only cases opened for these reasons. Repeat the parameter to pass several.

          status: Only cases in these statuses. Repeat the parameter to pass several — one
              paginated list covers all of them.

          user_id: Only cases opened by this customer — a `user_` tag, or `me` for the calling
              user. It narrows what you can already read, so `me` lists the cases you opened
              without the ones on accounts you are a team member of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/resolution_center_cases",
            page=SyncCursorPage[ResolutionCenterCaseListResponse],
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
                        "outcome": outcome,
                        "reason": reason,
                        "status": status,
                        "user_id": user_id,
                    },
                    resolution_center_case_list_params.ResolutionCenterCaseListParams,
                ),
            ),
            model=ResolutionCenterCaseListResponse,
        )


class AsyncResolutionCenterCasesResource(AsyncAPIResource):
    """
    A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

    Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResolutionCenterCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResolutionCenterCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResolutionCenterCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncResolutionCenterCasesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolutionCenterCaseRetrieveResponse:
        """
        Retrieves a single resolution center case with its full event timeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._get(
            path_template("/resolution_center_cases/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolutionCenterCaseRetrieveResponse,
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
        order: Literal["created_at", "response_due_at"] | Omit = omit,
        outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]] | Omit = omit,
        reason: List[
            Literal[
                "fraudulent",
                "product_not_received",
                "not_as_described",
                "product_unacceptable",
                "subscription_canceled",
            ]
        ]
        | Omit = omit,
        status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]] | Omit = omit,
        user_id: str | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResolutionCenterCaseListResponse, AsyncCursorPage[ResolutionCenterCaseListResponse]]:
        """Lists resolution center cases.

        Without `account_id` you get every case you can
        read — the ones you opened as a buyer and every account you are a team member
        of; the filters narrow that list.

        Args:
          account_id: Only cases filed against this account (`biz_` tag). With read access to the
              account this lists its whole queue; without, only the cases you opened against
              it.

          after: A cursor; returns cases after this position.

          before: A cursor; returns cases before this position.

          created_after: Only cases created after this ISO 8601 timestamp.

          created_before: Only cases created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: The number of cases to return (default 20, max 100).

          last: The number of cases to return from the end of the range.

          order: The field to sort cases by.

          outcome: Only closed cases that ended these ways. Repeat the parameter to pass several.

          reason: Only cases opened for these reasons. Repeat the parameter to pass several.

          status: Only cases in these statuses. Repeat the parameter to pass several — one
              paginated list covers all of them.

          user_id: Only cases opened by this customer — a `user_` tag, or `me` for the calling
              user. It narrows what you can already read, so `me` lists the cases you opened
              without the ones on accounts you are a team member of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/resolution_center_cases",
            page=AsyncCursorPage[ResolutionCenterCaseListResponse],
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
                        "outcome": outcome,
                        "reason": reason,
                        "status": status,
                        "user_id": user_id,
                    },
                    resolution_center_case_list_params.ResolutionCenterCaseListParams,
                ),
            ),
            model=ResolutionCenterCaseListResponse,
        )


class ResolutionCenterCasesResourceWithRawResponse:
    def __init__(self, resolution_center_cases: ResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = to_raw_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            resolution_center_cases.list,
        )


class AsyncResolutionCenterCasesResourceWithRawResponse:
    def __init__(self, resolution_center_cases: AsyncResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = async_to_raw_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            resolution_center_cases.list,
        )


class ResolutionCenterCasesResourceWithStreamingResponse:
    def __init__(self, resolution_center_cases: ResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = to_streamed_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            resolution_center_cases.list,
        )


class AsyncResolutionCenterCasesResourceWithStreamingResponse:
    def __init__(self, resolution_center_cases: AsyncResolutionCenterCasesResource) -> None:
        self._resolution_center_cases = resolution_center_cases

        self.retrieve = async_to_streamed_response_wrapper(
            resolution_center_cases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            resolution_center_cases.list,
        )
