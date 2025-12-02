# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..types import invoice_list_params, invoice_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
from ..types.shared.invoice import Invoice
from ..types.shared.direction import Direction
from ..types.invoice_void_response import InvoiceVoidResponse
from ..types.shared.invoice_status import InvoiceStatus
from ..types.shared.collection_method import CollectionMethod
from ..types.shared.invoice_list_item import InvoiceListItem

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        member_id: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDPlan,
        product: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDProduct,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          member_id: The member ID to create this invoice for. Include this if you want to create an
              invoice for an existing member. If you do not have a member ID, you must provide
              an email_address and customer_name.

          plan: The properties of the plan to create for this invoice.

          product: The properties of the product to create for this invoice. Include this if you
              want to create an invoice for a new product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        email_address: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressPlan,
        product: invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressProduct,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          email_address: The email address to create this invoice for. This is required if you want to
              create an invoice for a user who does not have a member of your company yet.

          plan: The properties of the plan to create for this invoice.

          product: The properties of the product to create for this invoice. Include this if you
              want to create an invoice for a new product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        member_id: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductIDAndMemberIDPlan,
        product_id: str,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          member_id: The member ID to create this invoice for. Include this if you want to create an
              invoice for an existing member. If you do not have a member ID, you must provide
              an email_address and customer_name.

          plan: The properties of the plan to create for this invoice.

          product_id: The product ID to create this invoice for. Include this if you want to create an
              invoice for an existing product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        email_address: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductIDAndEmailAddressPlan,
        product_id: str,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          email_address: The email address to create this invoice for. This is required if you want to
              create an invoice for a user who does not have a member of your company yet.

          plan: The properties of the plan to create for this invoice.

          product_id: The product ID to create this invoice for. Include this if you want to create an
              invoice for an existing product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["collection_method", "company_id", "due_date", "member_id", "plan", "product"],
        ["collection_method", "company_id", "due_date", "email_address", "plan", "product"],
        ["collection_method", "company_id", "due_date", "member_id", "plan", "product_id"],
        ["collection_method", "company_id", "due_date", "email_address", "plan", "product_id"],
    )
    def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        member_id: str | Omit = omit,
        plan: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDPlan
        | invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressPlan
        | invoice_create_params.CreateInvoiceInputWithProductIDAndMemberIDPlan
        | invoice_create_params.CreateInvoiceInputWithProductIDAndEmailAddressPlan,
        product: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDProduct
        | invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressProduct
        | Omit = omit,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        email_address: str | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        return self._post(
            "/invoices",
            body=maybe_transform(
                {
                    "collection_method": collection_method,
                    "company_id": company_id,
                    "due_date": due_date,
                    "member_id": member_id,
                    "plan": plan,
                    "product": product,
                    "charge_buyer_fee": charge_buyer_fee,
                    "customer_name": customer_name,
                    "payment_method_id": payment_method_id,
                    "payment_token_id": payment_token_id,
                    "email_address": email_address,
                    "product_id": product_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
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
    ) -> Invoice:
        """
        Retrieves an invoice by ID or token

        Required permissions:

        - `invoice:basic:read`
        - `plan:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        collection_methods: Optional[List[CollectionMethod]] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "due_date"]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[InvoiceStatus]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[InvoiceListItem]:
        """
        Lists invoices

        Required permissions:

        - `invoice:basic:read`
        - `plan:basic:read`

        Args:
          company_id: The ID of the company to list invoices for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          collection_methods: Filter invoices by their collection method

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          product_ids: Return only invoices created for these specific product ids

          statuses: The statuses to filter the invoices by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/invoices",
            page=SyncCursorPage[InvoiceListItem],
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
                        "collection_methods": collection_methods,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "product_ids": product_ids,
                        "statuses": statuses,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=InvoiceListItem,
        )

    def void(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceVoidResponse:
        """
        Void an invoice

        Required permissions:

        - `invoice:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/invoices/{id}/void",
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

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        member_id: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDPlan,
        product: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDProduct,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          member_id: The member ID to create this invoice for. Include this if you want to create an
              invoice for an existing member. If you do not have a member ID, you must provide
              an email_address and customer_name.

          plan: The properties of the plan to create for this invoice.

          product: The properties of the product to create for this invoice. Include this if you
              want to create an invoice for a new product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        email_address: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressPlan,
        product: invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressProduct,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          email_address: The email address to create this invoice for. This is required if you want to
              create an invoice for a user who does not have a member of your company yet.

          plan: The properties of the plan to create for this invoice.

          product: The properties of the product to create for this invoice. Include this if you
              want to create an invoice for a new product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        member_id: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductIDAndMemberIDPlan,
        product_id: str,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          member_id: The member ID to create this invoice for. Include this if you want to create an
              invoice for an existing member. If you do not have a member ID, you must provide
              an email_address and customer_name.

          plan: The properties of the plan to create for this invoice.

          product_id: The product ID to create this invoice for. Include this if you want to create an
              invoice for an existing product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        email_address: str,
        plan: invoice_create_params.CreateInvoiceInputWithProductIDAndEmailAddressPlan,
        product_id: str,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        Creates an invoice

        Required permissions:

        - `invoice:create`
        - `plan:basic:read`

        Args:
          collection_method: The method of collection for this invoice. If using charge_automatically, you
              must provide a payment_token.

          company_id: The company ID to create this invoice for.

          due_date: The date the invoice is due, if applicable.

          email_address: The email address to create this invoice for. This is required if you want to
              create an invoice for a user who does not have a member of your company yet.

          plan: The properties of the plan to create for this invoice.

          product_id: The product ID to create this invoice for. Include this if you want to create an
              invoice for an existing product.

          charge_buyer_fee: Whether or not to charge the customer a buyer fee.

          customer_name: The name of the customer to create this invoice for. This is required if you
              want to create an invoice for a customer who does not have a member of your
              company yet.

          payment_method_id: The payment method ID to use for this invoice. If using charge_automatically,
              you must provide a payment_method_id.

          payment_token_id: The payment token ID to use for this invoice. If using charge_automatically, you
              must provide a payment_token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["collection_method", "company_id", "due_date", "member_id", "plan", "product"],
        ["collection_method", "company_id", "due_date", "email_address", "plan", "product"],
        ["collection_method", "company_id", "due_date", "member_id", "plan", "product_id"],
        ["collection_method", "company_id", "due_date", "email_address", "plan", "product_id"],
    )
    async def create(
        self,
        *,
        collection_method: CollectionMethod,
        company_id: str,
        due_date: Union[str, datetime],
        member_id: str | Omit = omit,
        plan: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDPlan
        | invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressPlan
        | invoice_create_params.CreateInvoiceInputWithProductIDAndMemberIDPlan
        | invoice_create_params.CreateInvoiceInputWithProductIDAndEmailAddressPlan,
        product: invoice_create_params.CreateInvoiceInputWithProductAndMemberIDProduct
        | invoice_create_params.CreateInvoiceInputWithProductAndEmailAddressProduct
        | Omit = omit,
        charge_buyer_fee: Optional[bool] | Omit = omit,
        customer_name: Optional[str] | Omit = omit,
        payment_method_id: Optional[str] | Omit = omit,
        payment_token_id: Optional[str] | Omit = omit,
        email_address: str | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        return await self._post(
            "/invoices",
            body=await async_maybe_transform(
                {
                    "collection_method": collection_method,
                    "company_id": company_id,
                    "due_date": due_date,
                    "member_id": member_id,
                    "plan": plan,
                    "product": product,
                    "charge_buyer_fee": charge_buyer_fee,
                    "customer_name": customer_name,
                    "payment_method_id": payment_method_id,
                    "payment_token_id": payment_token_id,
                    "email_address": email_address,
                    "product_id": product_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
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
    ) -> Invoice:
        """
        Retrieves an invoice by ID or token

        Required permissions:

        - `invoice:basic:read`
        - `plan:basic:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        company_id: str,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        collection_methods: Optional[List[CollectionMethod]] | Omit = omit,
        created_after: Union[str, datetime, None] | Omit = omit,
        created_before: Union[str, datetime, None] | Omit = omit,
        direction: Optional[Direction] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        order: Optional[Literal["id", "created_at", "due_date"]] | Omit = omit,
        product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[InvoiceStatus]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InvoiceListItem, AsyncCursorPage[InvoiceListItem]]:
        """
        Lists invoices

        Required permissions:

        - `invoice:basic:read`
        - `plan:basic:read`

        Args:
          company_id: The ID of the company to list invoices for

          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          collection_methods: Filter invoices by their collection method

          created_after: The minimum creation date to filter by

          created_before: The maximum creation date to filter by

          direction: The direction of the sort.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          order: Which columns can be used to sort.

          product_ids: Return only invoices created for these specific product ids

          statuses: The statuses to filter the invoices by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/invoices",
            page=AsyncCursorPage[InvoiceListItem],
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
                        "collection_methods": collection_methods,
                        "created_after": created_after,
                        "created_before": created_before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                        "product_ids": product_ids,
                        "statuses": statuses,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=InvoiceListItem,
        )

    async def void(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceVoidResponse:
        """
        Void an invoice

        Required permissions:

        - `invoice:update`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/invoices/{id}/void",
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
