# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import invoice_list_params, invoice_void_params, invoice_create_params, invoice_retrieve_params
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
from .._base_client import make_request_options
from ..types.invoice_list_response import InvoiceListResponse
from ..types.invoice_void_response import InvoiceVoidResponse
from ..types.invoice_create_response import InvoiceCreateResponse
from ..types.invoice_retrieve_response import InvoiceRetrieveResponse

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_method: Literal["send_invoice", "charge_automatically"],
        due_date: int,
        plan: invoice_create_params.Plan,
        access_pass: Optional[invoice_create_params.AccessPass] | Omit = omit,
        access_pass_id: Optional[str] | Omit = omit,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        client_mutation_id: Optional[str] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        email_address: Optional[str] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InvoiceCreateResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/invoices",
            body=maybe_transform(
                {
                    "collection_method": collection_method,
                    "due_date": due_date,
                    "plan": plan,
                    "access_pass": access_pass,
                    "access_pass_id": access_pass_id,
                    "charge_buyer_fee": charge_buyer_fee,
                    "client_mutation_id": client_mutation_id,
                    "customer_name": customer_name,
                    "email_address": email_address,
                    "member_id": member_id,
                    "payment_token_id": payment_token_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceCreateResponse,
        )

    def retrieve(
        self,
        path_id: str,
        *,
        query_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._get(
            f"/invoices/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_id": query_id}, invoice_retrieve_params.InvoiceRetrieveParams),
            ),
            cast_to=InvoiceRetrieveResponse,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Literal["asc", "desc"]] | Omit = omit,
        filters: Optional[invoice_list_params.Filters] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "due_date"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/invoices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "filters": filters,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=InvoiceListResponse,
        )

    def void(
        self,
        path_id: str,
        *,
        body_id: str,
        client_mutation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InvoiceVoidResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/invoices/{path_id}/void",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "client_mutation_id": client_mutation_id,
                },
                invoice_void_params.InvoiceVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceVoidResponse,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/whopsdk-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_method: Literal["send_invoice", "charge_automatically"],
        due_date: int,
        plan: invoice_create_params.Plan,
        access_pass: Optional[invoice_create_params.AccessPass] | Omit = omit,
        access_pass_id: Optional[str] | Omit = omit,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        client_mutation_id: Optional[str] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        email_address: Optional[str] | Omit = omit,
        member_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InvoiceCreateResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/invoices",
            body=await async_maybe_transform(
                {
                    "collection_method": collection_method,
                    "due_date": due_date,
                    "plan": plan,
                    "access_pass": access_pass,
                    "access_pass_id": access_pass_id,
                    "charge_buyer_fee": charge_buyer_fee,
                    "client_mutation_id": client_mutation_id,
                    "customer_name": customer_name,
                    "email_address": email_address,
                    "member_id": member_id,
                    "payment_token_id": payment_token_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceCreateResponse,
        )

    async def retrieve(
        self,
        path_id: str,
        *,
        query_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._get(
            f"/invoices/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_id": query_id}, invoice_retrieve_params.InvoiceRetrieveParams
                ),
            ),
            cast_to=InvoiceRetrieveResponse,
        )

    async def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        direction: Optional[Literal["asc", "desc"]] | Omit = omit,
        filters: Optional[invoice_list_params.Filters] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "due_date"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/invoices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company_id": company_id,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "filters": filters,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=InvoiceListResponse,
        )

    async def void(
        self,
        path_id: str,
        *,
        body_id: str,
        client_mutation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InvoiceVoidResponse]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/invoices/{path_id}/void",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "client_mutation_id": client_mutation_id,
                },
                invoice_void_params.InvoiceVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceVoidResponse,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )
        self.void = to_raw_response_wrapper(
            invoices.void,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )
        self.void = async_to_raw_response_wrapper(
            invoices.void,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.void = to_streamed_response_wrapper(
            invoices.void,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.void = async_to_streamed_response_wrapper(
            invoices.void,
        )
