# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import payment_method_domain_list_params, payment_method_domain_create_params
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.payment_method_domain import PaymentMethodDomain
from ..types.payment_method_domain_delete_response import PaymentMethodDomainDeleteResponse

__all__ = ["PaymentMethodDomainsResource", "AsyncPaymentMethodDomainsResource"]


class PaymentMethodDomainsResource(SyncAPIResource):
    """
    A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

    Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
    """

    @cached_property
    def with_raw_response(self) -> PaymentMethodDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PaymentMethodDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentMethodDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PaymentMethodDomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        hostname: str,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentMethodDomain:
        """
        Registers a hostname with the wallet provider and attempts verification inline.
        Returns `verified` when the provider fetched the domain-association file (for
        Apple Pay, `/.well-known/apple-developer-merchantid-domain-association`), or
        `pending` when it could not — host the file, then retry with the verify
        endpoint.

        Args:
          hostname: Hostname to register (e.g. `checkout.shinetime.example`).

          account_id: Account to register the domain for (`biz_` tag). Defaults to the caller's
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/payment_method_domains",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "account_id": account_id,
                },
                payment_method_domain_create_params.PaymentMethodDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentMethodDomain,
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
    ) -> PaymentMethodDomain:
        """
        Retrieves a payment method domain to check its verification status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/payment_method_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethodDomain,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        hostname: str | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        provider: Literal["apple"] | Omit = omit,
        status: Literal["pending", "verified"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaymentMethodDomain]:
        """Lists payment method domains.

        Without `account_id`, returns the caller's own
        domains and those of every connected account.

        Args:
          account_id: Only domains registered for this account (`biz_` tag). Defaults to the caller's
              account plus its connected accounts.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only domains created after this ISO 8601 timestamp.

          created_before: Only domains created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of domains to return from the start of the window.

          hostname: Only the domain with this exact hostname.

          last: Number of domains to return from the end of the window.

          order: Sort field.

          provider: Only domains registered with this wallet provider.

          status: Only domains with this verification status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payment_method_domains",
            page=SyncCursorPage[PaymentMethodDomain],
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
                        "hostname": hostname,
                        "last": last,
                        "order": order,
                        "provider": provider,
                        "status": status,
                    },
                    payment_method_domain_list_params.PaymentMethodDomainListParams,
                ),
            ),
            model=PaymentMethodDomain,
        )

    def delete(
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
    ) -> PaymentMethodDomainDeleteResponse:
        """
        Unregisters a payment method domain so its wallet payment methods stop rendering
        there.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/payment_method_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentMethodDomainDeleteResponse,
        )

    def verify(
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
    ) -> PaymentMethodDomain:
        """
        Re-attempts provider verification of a pending domain once the association file
        is hosted. Fails with a `bad_request` explaining what to fix; verifying an
        already `verified` domain is a no-op.

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
            path_template("/payment_method_domains/{id}/verify", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentMethodDomain,
        )


class AsyncPaymentMethodDomainsResource(AsyncAPIResource):
    """
    A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

    Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPaymentMethodDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentMethodDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentMethodDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPaymentMethodDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        hostname: str,
        account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentMethodDomain:
        """
        Registers a hostname with the wallet provider and attempts verification inline.
        Returns `verified` when the provider fetched the domain-association file (for
        Apple Pay, `/.well-known/apple-developer-merchantid-domain-association`), or
        `pending` when it could not — host the file, then retry with the verify
        endpoint.

        Args:
          hostname: Hostname to register (e.g. `checkout.shinetime.example`).

          account_id: Account to register the domain for (`biz_` tag). Defaults to the caller's
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/payment_method_domains",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "account_id": account_id,
                },
                payment_method_domain_create_params.PaymentMethodDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentMethodDomain,
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
    ) -> PaymentMethodDomain:
        """
        Retrieves a payment method domain to check its verification status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/payment_method_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethodDomain,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        hostname: str | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        provider: Literal["apple"] | Omit = omit,
        status: Literal["pending", "verified"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentMethodDomain, AsyncCursorPage[PaymentMethodDomain]]:
        """Lists payment method domains.

        Without `account_id`, returns the caller's own
        domains and those of every connected account.

        Args:
          account_id: Only domains registered for this account (`biz_` tag). Defaults to the caller's
              account plus its connected accounts.

          after: Cursor to paginate forwards from.

          before: Cursor to paginate backwards from.

          created_after: Only domains created after this ISO 8601 timestamp.

          created_before: Only domains created before this ISO 8601 timestamp.

          direction: Sort direction.

          first: Number of domains to return from the start of the window.

          hostname: Only the domain with this exact hostname.

          last: Number of domains to return from the end of the window.

          order: Sort field.

          provider: Only domains registered with this wallet provider.

          status: Only domains with this verification status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payment_method_domains",
            page=AsyncCursorPage[PaymentMethodDomain],
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
                        "hostname": hostname,
                        "last": last,
                        "order": order,
                        "provider": provider,
                        "status": status,
                    },
                    payment_method_domain_list_params.PaymentMethodDomainListParams,
                ),
            ),
            model=PaymentMethodDomain,
        )

    async def delete(
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
    ) -> PaymentMethodDomainDeleteResponse:
        """
        Unregisters a payment method domain so its wallet payment methods stop rendering
        there.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/payment_method_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentMethodDomainDeleteResponse,
        )

    async def verify(
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
    ) -> PaymentMethodDomain:
        """
        Re-attempts provider verification of a pending domain once the association file
        is hosted. Fails with a `bad_request` explaining what to fix; verifying an
        already `verified` domain is a no-op.

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
            path_template("/payment_method_domains/{id}/verify", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentMethodDomain,
        )


class PaymentMethodDomainsResourceWithRawResponse:
    def __init__(self, payment_method_domains: PaymentMethodDomainsResource) -> None:
        self._payment_method_domains = payment_method_domains

        self.create = to_raw_response_wrapper(
            payment_method_domains.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payment_method_domains.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payment_method_domains.list,
        )
        self.delete = to_raw_response_wrapper(
            payment_method_domains.delete,
        )
        self.verify = to_raw_response_wrapper(
            payment_method_domains.verify,
        )


class AsyncPaymentMethodDomainsResourceWithRawResponse:
    def __init__(self, payment_method_domains: AsyncPaymentMethodDomainsResource) -> None:
        self._payment_method_domains = payment_method_domains

        self.create = async_to_raw_response_wrapper(
            payment_method_domains.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payment_method_domains.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payment_method_domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            payment_method_domains.delete,
        )
        self.verify = async_to_raw_response_wrapper(
            payment_method_domains.verify,
        )


class PaymentMethodDomainsResourceWithStreamingResponse:
    def __init__(self, payment_method_domains: PaymentMethodDomainsResource) -> None:
        self._payment_method_domains = payment_method_domains

        self.create = to_streamed_response_wrapper(
            payment_method_domains.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_method_domains.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payment_method_domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            payment_method_domains.delete,
        )
        self.verify = to_streamed_response_wrapper(
            payment_method_domains.verify,
        )


class AsyncPaymentMethodDomainsResourceWithStreamingResponse:
    def __init__(self, payment_method_domains: AsyncPaymentMethodDomainsResource) -> None:
        self._payment_method_domains = payment_method_domains

        self.create = async_to_streamed_response_wrapper(
            payment_method_domains.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_method_domains.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_method_domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            payment_method_domains.delete,
        )
        self.verify = async_to_streamed_response_wrapper(
            payment_method_domains.verify,
        )
