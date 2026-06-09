# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import verification_create_params, verification_update_params
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
from ..types.verification_create_response import VerificationCreateResponse
from ..types.verification_delete_response import VerificationDeleteResponse
from ..types.verification_update_response import VerificationUpdateResponse
from ..types.verification_retrieve_response import VerificationRetrieveResponse

__all__ = ["VerificationsResource", "AsyncVerificationsResource"]


class VerificationsResource(SyncAPIResource):
    """Verifications"""

    @cached_property
    def with_raw_response(self) -> VerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return VerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return VerificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        address: Dict[str, object] | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual", "business"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        restart: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """
        Creates or resumes a verification session for an account.

        Args:
          account_id: The account ID to verify (biz\\__ tag).

          address: Pre-fill address (line1, city, state, postal_code).

          country: Pre-fill the country.

          date_of_birth: Pre-fill the date of birth.

          first_name: Pre-fill the first name.

          kind: The verification type. Defaults to individual.

          last_name: Pre-fill the last name.

          phone: Pre-fill the phone number.

          restart: Whether to restart an in-flight verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verifications",
            body=maybe_transform(
                {
                    "address": address,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "kind": kind,
                    "last_name": last_name,
                    "phone": phone,
                    "restart": restart,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_id": account_id}, verification_create_params.VerificationCreateParams),
            ),
            cast_to=VerificationCreateResponse,
        )

    def retrieve(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationRetrieveResponse:
        """Lists identity verification profiles for an account.

        Pass a biz\\__ tag.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._get(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
        )

    def update(
        self,
        verification_id: str,
        *,
        business_address: Dict[str, object] | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        personal_address: Dict[str, object] | Omit = omit,
        rfis: Iterable[verification_update_params.Rfi] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates fields on an identity verification profile, or responds to outstanding
        RFIs.

        Args:
          business_address: The business address.

          business_name: The business name.

          business_structure: The business structure.

          country: The country code.

          date_of_birth: The date of birth.

          first_name: The first name on the verification.

          last_name: The last name on the verification.

          personal_address: The personal address.

          rfis: RFI responses. Each entry must include id and a value, address, or files
              payload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._patch(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            body=maybe_transform(
                {
                    "business_address": business_address,
                    "business_name": business_name,
                    "business_structure": business_structure,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "personal_address": personal_address,
                    "rfis": rfis,
                },
                verification_update_params.VerificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationUpdateResponse,
        )

    def delete(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationDeleteResponse:
        """
        Soft-deletes an identity verification profile and unlinks it from all accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._delete(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationDeleteResponse,
        )


class AsyncVerificationsResource(AsyncAPIResource):
    """Verifications"""

    @cached_property
    def with_raw_response(self) -> AsyncVerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncVerificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        address: Dict[str, object] | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual", "business"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        restart: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """
        Creates or resumes a verification session for an account.

        Args:
          account_id: The account ID to verify (biz\\__ tag).

          address: Pre-fill address (line1, city, state, postal_code).

          country: Pre-fill the country.

          date_of_birth: Pre-fill the date of birth.

          first_name: Pre-fill the first name.

          kind: The verification type. Defaults to individual.

          last_name: Pre-fill the last name.

          phone: Pre-fill the phone number.

          restart: Whether to restart an in-flight verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verifications",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "kind": kind,
                    "last_name": last_name,
                    "phone": phone,
                    "restart": restart,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_id": account_id}, verification_create_params.VerificationCreateParams
                ),
            ),
            cast_to=VerificationCreateResponse,
        )

    async def retrieve(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationRetrieveResponse:
        """Lists identity verification profiles for an account.

        Pass a biz\\__ tag.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._get(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
        )

    async def update(
        self,
        verification_id: str,
        *,
        business_address: Dict[str, object] | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        personal_address: Dict[str, object] | Omit = omit,
        rfis: Iterable[verification_update_params.Rfi] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates fields on an identity verification profile, or responds to outstanding
        RFIs.

        Args:
          business_address: The business address.

          business_name: The business name.

          business_structure: The business structure.

          country: The country code.

          date_of_birth: The date of birth.

          first_name: The first name on the verification.

          last_name: The last name on the verification.

          personal_address: The personal address.

          rfis: RFI responses. Each entry must include id and a value, address, or files
              payload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._patch(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            body=await async_maybe_transform(
                {
                    "business_address": business_address,
                    "business_name": business_name,
                    "business_structure": business_structure,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "personal_address": personal_address,
                    "rfis": rfis,
                },
                verification_update_params.VerificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationUpdateResponse,
        )

    async def delete(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationDeleteResponse:
        """
        Soft-deletes an identity verification profile and unlinks it from all accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._delete(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationDeleteResponse,
        )


class VerificationsResourceWithRawResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.create = to_raw_response_wrapper(
            verifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            verifications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            verifications.update,
        )
        self.delete = to_raw_response_wrapper(
            verifications.delete,
        )


class AsyncVerificationsResourceWithRawResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.create = async_to_raw_response_wrapper(
            verifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            verifications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            verifications.update,
        )
        self.delete = async_to_raw_response_wrapper(
            verifications.delete,
        )


class VerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.create = to_streamed_response_wrapper(
            verifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            verifications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            verifications.update,
        )
        self.delete = to_streamed_response_wrapper(
            verifications.delete,
        )


class AsyncVerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.create = async_to_streamed_response_wrapper(
            verifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            verifications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            verifications.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            verifications.delete,
        )
