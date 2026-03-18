# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
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
from ...types.affiliates import (
    AffiliatePayoutTypes,
    AffiliateRevenueBases,
    AffiliateOverrideRoles,
    AffiliateAppliesToPayments,
    override_list_params,
    override_create_params,
    override_update_params,
)
from ...types.affiliates.affiliate_payout_types import AffiliatePayoutTypes
from ...types.affiliates.override_list_response import OverrideListResponse
from ...types.affiliates.affiliate_revenue_bases import AffiliateRevenueBases
from ...types.affiliates.affiliate_override_roles import AffiliateOverrideRoles
from ...types.affiliates.override_create_response import OverrideCreateResponse
from ...types.affiliates.override_delete_response import OverrideDeleteResponse
from ...types.affiliates.override_update_response import OverrideUpdateResponse
from ...types.affiliates.override_retrieve_response import OverrideRetrieveResponse
from ...types.affiliates.affiliate_applies_to_payments import AffiliateAppliesToPayments

__all__ = ["OverridesResource", "AsyncOverridesResource"]


class OverridesResource(SyncAPIResource):
    """Affiliates"""

    @cached_property
    def with_raw_response(self) -> OverridesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return OverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverridesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return OverridesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        path_id: str,
        *,
        body_id: str,
        commission_value: float,
        override_type: Literal["standard"],
        plan_id: str,
        applies_to_payments: Optional[AffiliateAppliesToPayments] | Omit = omit,
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideCreateResponse:
        """
        Creates a commission override for an affiliate.

        Required permissions:

        - `affiliate:create`

        Args:
          body_id: The affiliate ID.

          commission_value: The commission value (percentage 1-100 or flat fee).

          plan_id: The plan ID (required for standard overrides).

          applies_to_payments: Whether the affiliate commission applies to the first payment or all payments

          commission_type: The types of payouts an affiliate can have

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        path_id: str,
        *,
        body_id: str,
        commission_value: float,
        override_type: Literal["rev_share"],
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        revenue_basis: Optional[AffiliateRevenueBases] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideCreateResponse:
        """
        Creates a commission override for an affiliate.

        Required permissions:

        - `affiliate:create`

        Args:
          body_id: The affiliate ID.

          commission_value: The commission value (percentage 1-100 or flat fee).

          commission_type: The types of payouts an affiliate can have

          product_id: The product ID (for rev-share overrides, omit for company-wide).

          revenue_basis: The calculation method for affiliate rev-share percentages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["body_id", "commission_value", "override_type", "plan_id"], ["body_id", "commission_value", "override_type"]
    )
    def create(
        self,
        path_id: str,
        *,
        body_id: str,
        commission_value: float,
        override_type: Literal["standard"] | Literal["rev_share"],
        plan_id: str | Omit = omit,
        applies_to_payments: Optional[AffiliateAppliesToPayments] | Omit = omit,
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        revenue_basis: Optional[AffiliateRevenueBases] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideCreateResponse:
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/affiliates/{path_id}/overrides",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "commission_value": commission_value,
                    "override_type": override_type,
                    "plan_id": plan_id,
                    "applies_to_payments": applies_to_payments,
                    "commission_type": commission_type,
                    "product_id": product_id,
                    "revenue_basis": revenue_basis,
                },
                override_create_params.OverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideCreateResponse,
        )

    def retrieve(
        self,
        override_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideRetrieveResponse:
        """
        Retrieves the details of a specific affiliate override.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not override_id:
            raise ValueError(f"Expected a non-empty value for `override_id` but received {override_id!r}")
        return self._get(
            f"/affiliates/{id}/overrides/{override_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideRetrieveResponse,
        )

    def update(
        self,
        override_id: str,
        *,
        id: str,
        applies_to_payments: Optional[AffiliateAppliesToPayments] | Omit = omit,
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        commission_value: Optional[float] | Omit = omit,
        revenue_basis: Optional[AffiliateRevenueBases] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideUpdateResponse:
        """
        Updates an existing affiliate override.

        Required permissions:

        - `affiliate:update`

        Args:
          applies_to_payments: Whether the affiliate commission applies to the first payment or all payments

          commission_type: The types of payouts an affiliate can have

          commission_value: The commission value (percentage 1-100 or flat fee in dollars).

          revenue_basis: The calculation method for affiliate rev-share percentages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not override_id:
            raise ValueError(f"Expected a non-empty value for `override_id` but received {override_id!r}")
        return self._patch(
            f"/affiliates/{id}/overrides/{override_id}",
            body=maybe_transform(
                {
                    "applies_to_payments": applies_to_payments,
                    "commission_type": commission_type,
                    "commission_value": commission_value,
                    "revenue_basis": revenue_basis,
                },
                override_update_params.OverrideUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideUpdateResponse,
        )

    def list(
        self,
        id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        override_type: Optional[AffiliateOverrideRoles] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[OverrideListResponse]:
        """
        Returns a paginated list of overrides for an affiliate.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          override_type: The role of an affiliate override (standard or rev_share)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/affiliates/{id}/overrides",
            page=SyncCursorPage[OverrideListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                        "override_type": override_type,
                    },
                    override_list_params.OverrideListParams,
                ),
            ),
            model=OverrideListResponse,
        )

    def delete(
        self,
        override_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideDeleteResponse:
        """
        Deletes an affiliate override.

        Required permissions:

        - `affiliate:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not override_id:
            raise ValueError(f"Expected a non-empty value for `override_id` but received {override_id!r}")
        return self._delete(
            f"/affiliates/{id}/overrides/{override_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideDeleteResponse,
        )


class AsyncOverridesResource(AsyncAPIResource):
    """Affiliates"""

    @cached_property
    def with_raw_response(self) -> AsyncOverridesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverridesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncOverridesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        path_id: str,
        *,
        body_id: str,
        commission_value: float,
        override_type: Literal["standard"],
        plan_id: str,
        applies_to_payments: Optional[AffiliateAppliesToPayments] | Omit = omit,
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideCreateResponse:
        """
        Creates a commission override for an affiliate.

        Required permissions:

        - `affiliate:create`

        Args:
          body_id: The affiliate ID.

          commission_value: The commission value (percentage 1-100 or flat fee).

          plan_id: The plan ID (required for standard overrides).

          applies_to_payments: Whether the affiliate commission applies to the first payment or all payments

          commission_type: The types of payouts an affiliate can have

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        path_id: str,
        *,
        body_id: str,
        commission_value: float,
        override_type: Literal["rev_share"],
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        revenue_basis: Optional[AffiliateRevenueBases] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideCreateResponse:
        """
        Creates a commission override for an affiliate.

        Required permissions:

        - `affiliate:create`

        Args:
          body_id: The affiliate ID.

          commission_value: The commission value (percentage 1-100 or flat fee).

          commission_type: The types of payouts an affiliate can have

          product_id: The product ID (for rev-share overrides, omit for company-wide).

          revenue_basis: The calculation method for affiliate rev-share percentages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["body_id", "commission_value", "override_type", "plan_id"], ["body_id", "commission_value", "override_type"]
    )
    async def create(
        self,
        path_id: str,
        *,
        body_id: str,
        commission_value: float,
        override_type: Literal["standard"] | Literal["rev_share"],
        plan_id: str | Omit = omit,
        applies_to_payments: Optional[AffiliateAppliesToPayments] | Omit = omit,
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        revenue_basis: Optional[AffiliateRevenueBases] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideCreateResponse:
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/affiliates/{path_id}/overrides",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "commission_value": commission_value,
                    "override_type": override_type,
                    "plan_id": plan_id,
                    "applies_to_payments": applies_to_payments,
                    "commission_type": commission_type,
                    "product_id": product_id,
                    "revenue_basis": revenue_basis,
                },
                override_create_params.OverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideCreateResponse,
        )

    async def retrieve(
        self,
        override_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideRetrieveResponse:
        """
        Retrieves the details of a specific affiliate override.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not override_id:
            raise ValueError(f"Expected a non-empty value for `override_id` but received {override_id!r}")
        return await self._get(
            f"/affiliates/{id}/overrides/{override_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideRetrieveResponse,
        )

    async def update(
        self,
        override_id: str,
        *,
        id: str,
        applies_to_payments: Optional[AffiliateAppliesToPayments] | Omit = omit,
        commission_type: Optional[AffiliatePayoutTypes] | Omit = omit,
        commission_value: Optional[float] | Omit = omit,
        revenue_basis: Optional[AffiliateRevenueBases] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideUpdateResponse:
        """
        Updates an existing affiliate override.

        Required permissions:

        - `affiliate:update`

        Args:
          applies_to_payments: Whether the affiliate commission applies to the first payment or all payments

          commission_type: The types of payouts an affiliate can have

          commission_value: The commission value (percentage 1-100 or flat fee in dollars).

          revenue_basis: The calculation method for affiliate rev-share percentages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not override_id:
            raise ValueError(f"Expected a non-empty value for `override_id` but received {override_id!r}")
        return await self._patch(
            f"/affiliates/{id}/overrides/{override_id}",
            body=await async_maybe_transform(
                {
                    "applies_to_payments": applies_to_payments,
                    "commission_type": commission_type,
                    "commission_value": commission_value,
                    "revenue_basis": revenue_basis,
                },
                override_update_params.OverrideUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideUpdateResponse,
        )

    def list(
        self,
        id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        override_type: Optional[AffiliateOverrideRoles] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OverrideListResponse, AsyncCursorPage[OverrideListResponse]]:
        """
        Returns a paginated list of overrides for an affiliate.

        Required permissions:

        - `affiliate:basic:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          override_type: The role of an affiliate override (standard or rev_share)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/affiliates/{id}/overrides",
            page=AsyncCursorPage[OverrideListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "first": first,
                        "last": last,
                        "override_type": override_type,
                    },
                    override_list_params.OverrideListParams,
                ),
            ),
            model=OverrideListResponse,
        )

    async def delete(
        self,
        override_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverrideDeleteResponse:
        """
        Deletes an affiliate override.

        Required permissions:

        - `affiliate:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not override_id:
            raise ValueError(f"Expected a non-empty value for `override_id` but received {override_id!r}")
        return await self._delete(
            f"/affiliates/{id}/overrides/{override_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverrideDeleteResponse,
        )


class OverridesResourceWithRawResponse:
    def __init__(self, overrides: OverridesResource) -> None:
        self._overrides = overrides

        self.create = to_raw_response_wrapper(
            overrides.create,
        )
        self.retrieve = to_raw_response_wrapper(
            overrides.retrieve,
        )
        self.update = to_raw_response_wrapper(
            overrides.update,
        )
        self.list = to_raw_response_wrapper(
            overrides.list,
        )
        self.delete = to_raw_response_wrapper(
            overrides.delete,
        )


class AsyncOverridesResourceWithRawResponse:
    def __init__(self, overrides: AsyncOverridesResource) -> None:
        self._overrides = overrides

        self.create = async_to_raw_response_wrapper(
            overrides.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            overrides.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            overrides.update,
        )
        self.list = async_to_raw_response_wrapper(
            overrides.list,
        )
        self.delete = async_to_raw_response_wrapper(
            overrides.delete,
        )


class OverridesResourceWithStreamingResponse:
    def __init__(self, overrides: OverridesResource) -> None:
        self._overrides = overrides

        self.create = to_streamed_response_wrapper(
            overrides.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            overrides.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            overrides.update,
        )
        self.list = to_streamed_response_wrapper(
            overrides.list,
        )
        self.delete = to_streamed_response_wrapper(
            overrides.delete,
        )


class AsyncOverridesResourceWithStreamingResponse:
    def __init__(self, overrides: AsyncOverridesResource) -> None:
        self._overrides = overrides

        self.create = async_to_streamed_response_wrapper(
            overrides.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            overrides.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            overrides.update,
        )
        self.list = async_to_streamed_response_wrapper(
            overrides.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            overrides.delete,
        )
