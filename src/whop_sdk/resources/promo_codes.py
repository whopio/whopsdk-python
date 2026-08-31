# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import promo_code_list_params, promo_code_create_params
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
from ..types.promo_code import PromoCode
from ..types.promo_code_list_response import PromoCodeListResponse
from ..types.promo_code_delete_response import PromoCodeDeleteResponse

__all__ = ["PromoCodesResource", "AsyncPromoCodesResource"]


class PromoCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromoCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PromoCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromoCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PromoCodesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount_off: float,
        base_currency: Literal[
            "usd",
            "sgd",
            "inr",
            "aud",
            "brl",
            "cad",
            "dkk",
            "eur",
            "nok",
            "gbp",
            "sek",
            "chf",
            "hkd",
            "huf",
            "jpy",
            "mxn",
            "myr",
            "pln",
            "czk",
            "nzd",
            "aed",
            "eth",
            "ape",
            "cop",
            "ron",
            "thb",
            "bgn",
            "idr",
            "dop",
            "php",
            "try",
            "krw",
            "twd",
            "vnd",
            "pkr",
            "clp",
            "uyu",
            "ars",
            "zar",
            "dzd",
            "tnd",
            "mad",
            "kes",
            "kwd",
            "jod",
            "all",
            "xcd",
            "amd",
            "bsd",
            "bhd",
            "bob",
            "bam",
            "khr",
            "crc",
            "xof",
            "egp",
            "etb",
            "gmd",
            "ghs",
            "gtq",
            "gyd",
            "ils",
            "jmd",
            "mop",
            "mga",
            "mur",
            "mdl",
            "mnt",
            "nad",
            "ngn",
            "mkd",
            "omr",
            "pyg",
            "pen",
            "qar",
            "rwf",
            "sar",
            "rsd",
            "lkr",
            "tzs",
            "ttd",
            "uzs",
            "rub",
            "btc",
            "cny",
            "usdt",
            "kzt",
            "awg",
            "whop_usd",
            "xau",
        ],
        code: str,
        new_users_only: bool,
        promo_duration_months: int,
        promo_type: Literal["percentage", "flat_amount"],
        churned_users_only: bool | Omit = omit,
        existing_memberships_only: bool | Omit = omit,
        expires_at: Optional[str] | Omit = omit,
        one_per_customer: bool | Omit = omit,
        plan_ids: SequenceNotStr[str] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        unlimited_stock: bool | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromoCode:
        """Creates a promo code for an account.

        First-party sessions may attach an
        affiliate.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/promo_codes",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount_off": amount_off,
                    "base_currency": base_currency,
                    "code": code,
                    "new_users_only": new_users_only,
                    "promo_duration_months": promo_duration_months,
                    "promo_type": promo_type,
                    "churned_users_only": churned_users_only,
                    "existing_memberships_only": existing_memberships_only,
                    "expires_at": expires_at,
                    "one_per_customer": one_per_customer,
                    "plan_ids": plan_ids,
                    "product_id": product_id,
                    "stock": stock,
                    "unlimited_stock": unlimited_stock,
                },
                promo_code_create_params.PromoCodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
        )

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
    ) -> PromoCode:
        """
        Retrieves a promo code by ID.

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
            path_template("/promo_codes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        plan_ids: SequenceNotStr[str] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        status: Literal["active", "inactive", "archived", "expired"] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PromoCodeListResponse]:
        """
        Lists promo codes for an account with cursor pagination, filters, and sorting.

        Args:
          account_id: Account whose promo codes are listed (`biz_` tag).

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only promo codes created after this ISO 8601 timestamp.

          created_before: Only promo codes created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of promo codes to return from the start of the window.

          last: Number of promo codes to return from the end of the window.

          order: Sort field.

          plan_ids: Only promo codes scoped to these plan IDs.

          product_ids: Only promo codes scoped to these product IDs.

          status: Promo-code status. `expired` groups inactive and archived codes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/promo_codes",
            page=SyncCursorPage[PromoCodeListResponse],
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
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "status": status,
                    },
                    promo_code_list_params.PromoCodeListParams,
                ),
            ),
            model=PromoCodeListResponse,
        )

    def delete(
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
    ) -> PromoCodeDeleteResponse:
        """
        Archives a promo code so it cannot be used in future checkouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._delete(
            path_template("/promo_codes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCodeDeleteResponse,
        )


class AsyncPromoCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromoCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromoCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromoCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPromoCodesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount_off: float,
        base_currency: Literal[
            "usd",
            "sgd",
            "inr",
            "aud",
            "brl",
            "cad",
            "dkk",
            "eur",
            "nok",
            "gbp",
            "sek",
            "chf",
            "hkd",
            "huf",
            "jpy",
            "mxn",
            "myr",
            "pln",
            "czk",
            "nzd",
            "aed",
            "eth",
            "ape",
            "cop",
            "ron",
            "thb",
            "bgn",
            "idr",
            "dop",
            "php",
            "try",
            "krw",
            "twd",
            "vnd",
            "pkr",
            "clp",
            "uyu",
            "ars",
            "zar",
            "dzd",
            "tnd",
            "mad",
            "kes",
            "kwd",
            "jod",
            "all",
            "xcd",
            "amd",
            "bsd",
            "bhd",
            "bob",
            "bam",
            "khr",
            "crc",
            "xof",
            "egp",
            "etb",
            "gmd",
            "ghs",
            "gtq",
            "gyd",
            "ils",
            "jmd",
            "mop",
            "mga",
            "mur",
            "mdl",
            "mnt",
            "nad",
            "ngn",
            "mkd",
            "omr",
            "pyg",
            "pen",
            "qar",
            "rwf",
            "sar",
            "rsd",
            "lkr",
            "tzs",
            "ttd",
            "uzs",
            "rub",
            "btc",
            "cny",
            "usdt",
            "kzt",
            "awg",
            "whop_usd",
            "xau",
        ],
        code: str,
        new_users_only: bool,
        promo_duration_months: int,
        promo_type: Literal["percentage", "flat_amount"],
        churned_users_only: bool | Omit = omit,
        existing_memberships_only: bool | Omit = omit,
        expires_at: Optional[str] | Omit = omit,
        one_per_customer: bool | Omit = omit,
        plan_ids: SequenceNotStr[str] | Omit = omit,
        product_id: Optional[str] | Omit = omit,
        stock: Optional[int] | Omit = omit,
        unlimited_stock: bool | Omit = omit,
        api_version_date: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromoCode:
        """Creates a promo code for an account.

        First-party sessions may attach an
        affiliate.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Api-Version-Date": api_version_date,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/promo_codes",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount_off": amount_off,
                    "base_currency": base_currency,
                    "code": code,
                    "new_users_only": new_users_only,
                    "promo_duration_months": promo_duration_months,
                    "promo_type": promo_type,
                    "churned_users_only": churned_users_only,
                    "existing_memberships_only": existing_memberships_only,
                    "expires_at": expires_at,
                    "one_per_customer": one_per_customer,
                    "plan_ids": plan_ids,
                    "product_id": product_id,
                    "stock": stock,
                    "unlimited_stock": unlimited_stock,
                },
                promo_code_create_params.PromoCodeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
        )

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
    ) -> PromoCode:
        """
        Retrieves a promo code by ID.

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
            path_template("/promo_codes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCode,
        )

    def list(
        self,
        *,
        account_id: str,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        plan_ids: SequenceNotStr[str] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        status: Literal["active", "inactive", "archived", "expired"] | Omit = omit,
        api_version_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PromoCodeListResponse, AsyncCursorPage[PromoCodeListResponse]]:
        """
        Lists promo codes for an account with cursor pagination, filters, and sorting.

        Args:
          account_id: Account whose promo codes are listed (`biz_` tag).

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only promo codes created after this ISO 8601 timestamp.

          created_before: Only promo codes created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of promo codes to return from the start of the window.

          last: Number of promo codes to return from the end of the window.

          order: Sort field.

          plan_ids: Only promo codes scoped to these plan IDs.

          product_ids: Only promo codes scoped to these product IDs.

          status: Promo-code status. `expired` groups inactive and archived codes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return self._get_api_list(
            "/promo_codes",
            page=AsyncCursorPage[PromoCodeListResponse],
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
                        "plan_ids": plan_ids,
                        "product_ids": product_ids,
                        "status": status,
                    },
                    promo_code_list_params.PromoCodeListParams,
                ),
            ),
            model=PromoCodeListResponse,
        )

    async def delete(
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
    ) -> PromoCodeDeleteResponse:
        """
        Archives a promo code so it cannot be used in future checkouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Api-Version-Date": api_version_date}), **(extra_headers or {})}
        return await self._delete(
            path_template("/promo_codes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromoCodeDeleteResponse,
        )


class PromoCodesResourceWithRawResponse:
    def __init__(self, promo_codes: PromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = to_raw_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            promo_codes.list,
        )
        self.delete = to_raw_response_wrapper(
            promo_codes.delete,
        )


class AsyncPromoCodesResourceWithRawResponse:
    def __init__(self, promo_codes: AsyncPromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = async_to_raw_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            promo_codes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            promo_codes.delete,
        )


class PromoCodesResourceWithStreamingResponse:
    def __init__(self, promo_codes: PromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = to_streamed_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            promo_codes.list,
        )
        self.delete = to_streamed_response_wrapper(
            promo_codes.delete,
        )


class AsyncPromoCodesResourceWithStreamingResponse:
    def __init__(self, promo_codes: AsyncPromoCodesResource) -> None:
        self._promo_codes = promo_codes

        self.create = async_to_streamed_response_wrapper(
            promo_codes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            promo_codes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            promo_codes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            promo_codes.delete,
        )
