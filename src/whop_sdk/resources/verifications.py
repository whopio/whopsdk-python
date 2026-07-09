# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import verification_list_params, verification_create_params, verification_update_params
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
from ..types.verification_list_response import VerificationListResponse
from ..types.verification_create_response import VerificationCreateResponse
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
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual", "business"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        place_of_incorporation: str | Omit = omit,
        restart: bool | Omit = omit,
        tax_identification_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """
        Starts a hosted verification session for an account or user, or returns the
        active session when one already exists.

        Args:
          account_id: Account or user ID whose identity you want to verify. Use a `biz_` account ID
              for account verifications, or the caller's `user_` ID for personal verification.

          address: Address to prefill in the hosted verification session.

          business_name: Legal business name to prefill for a business verification.

          business_structure: Business entity type, such as `llc` or `corporation`.

          business_website: Business website URL used during verification. Whop store pages are not
              accepted.

          country: ISO 3166-1 alpha-2 country code. For businesses, use the country of
              incorporation.

          date_of_birth: Date of birth to prefill in the hosted verification session.

          first_name: First name to prefill in the hosted verification session.

          kind: Verification type. Defaults to `individual`.

          last_name: Last name to prefill in the hosted verification session.

          phone: Phone number to prefill in the hosted verification session.

          place_of_incorporation: State or region where the business is incorporated.

          restart: Set to `true` to abandon the current in-flight session and start a new one.

          tax_identification_number: Tax ID for the individual or business, such as an SSN or EIN. Tokenized in
              transit and never stored raw.

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
                    "business_name": business_name,
                    "business_structure": business_structure,
                    "business_website": business_website,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "kind": kind,
                    "last_name": last_name,
                    "phone": phone,
                    "place_of_incorporation": place_of_incorporation,
                    "restart": restart,
                    "tax_identification_number": tax_identification_number,
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
        """
        Returns a verification profile by its `idpf_` ID.

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
        requested_information: Iterable[verification_update_params.RequestedInformation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates editable profile details or submits answers for items returned in
        `requested_information`.

        Args:
          business_address: Updated business address for a business verification.

          business_name: Updated legal business name for a business verification.

          business_structure: Updated business entity type, such as `llc` or `corporation`.

          country: Updated ISO 3166-1 alpha-2 country code.

          date_of_birth: Updated date of birth for an individual verification.

          first_name: Updated first name for an individual verification.

          last_name: Updated last name for an individual verification.

          personal_address: Updated personal address for an individual verification.

          requested_information: Answers to items returned in `requested_information`. Each entry must include
              the requested item `id` and exactly one answer payload matching the item's
              `type`: `value` for `text`, `date`, or `phone`; `address` for `address`; `files`
              for `files`.

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
                    "requested_information": requested_information,
                },
                verification_update_params.VerificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["updated_at", "created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationListResponse:
        """
        Returns verification profiles for an account or user, including review status
        and any items that still need answers.

        Args:
          account_id: Account or user ID whose verifications you want to list. Use a `biz_` account
              ID, or the caller's `user_` ID for personal verifications.

          direction: Sort direction for returned verifications.

          order: Field used to sort returned verifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/verifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "direction": direction,
                        "order": order,
                    },
                    verification_list_params.VerificationListParams,
                ),
            ),
            cast_to=VerificationListResponse,
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
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual", "business"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        place_of_incorporation: str | Omit = omit,
        restart: bool | Omit = omit,
        tax_identification_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """
        Starts a hosted verification session for an account or user, or returns the
        active session when one already exists.

        Args:
          account_id: Account or user ID whose identity you want to verify. Use a `biz_` account ID
              for account verifications, or the caller's `user_` ID for personal verification.

          address: Address to prefill in the hosted verification session.

          business_name: Legal business name to prefill for a business verification.

          business_structure: Business entity type, such as `llc` or `corporation`.

          business_website: Business website URL used during verification. Whop store pages are not
              accepted.

          country: ISO 3166-1 alpha-2 country code. For businesses, use the country of
              incorporation.

          date_of_birth: Date of birth to prefill in the hosted verification session.

          first_name: First name to prefill in the hosted verification session.

          kind: Verification type. Defaults to `individual`.

          last_name: Last name to prefill in the hosted verification session.

          phone: Phone number to prefill in the hosted verification session.

          place_of_incorporation: State or region where the business is incorporated.

          restart: Set to `true` to abandon the current in-flight session and start a new one.

          tax_identification_number: Tax ID for the individual or business, such as an SSN or EIN. Tokenized in
              transit and never stored raw.

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
                    "business_name": business_name,
                    "business_structure": business_structure,
                    "business_website": business_website,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "kind": kind,
                    "last_name": last_name,
                    "phone": phone,
                    "place_of_incorporation": place_of_incorporation,
                    "restart": restart,
                    "tax_identification_number": tax_identification_number,
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
        """
        Returns a verification profile by its `idpf_` ID.

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
        requested_information: Iterable[verification_update_params.RequestedInformation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates editable profile details or submits answers for items returned in
        `requested_information`.

        Args:
          business_address: Updated business address for a business verification.

          business_name: Updated legal business name for a business verification.

          business_structure: Updated business entity type, such as `llc` or `corporation`.

          country: Updated ISO 3166-1 alpha-2 country code.

          date_of_birth: Updated date of birth for an individual verification.

          first_name: Updated first name for an individual verification.

          last_name: Updated last name for an individual verification.

          personal_address: Updated personal address for an individual verification.

          requested_information: Answers to items returned in `requested_information`. Each entry must include
              the requested item `id` and exactly one answer payload matching the item's
              `type`: `value` for `text`, `date`, or `phone`; `address` for `address`; `files`
              for `files`.

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
                    "requested_information": requested_information,
                },
                verification_update_params.VerificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationUpdateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["updated_at", "created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationListResponse:
        """
        Returns verification profiles for an account or user, including review status
        and any items that still need answers.

        Args:
          account_id: Account or user ID whose verifications you want to list. Use a `biz_` account
              ID, or the caller's `user_` ID for personal verifications.

          direction: Sort direction for returned verifications.

          order: Field used to sort returned verifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/verifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "direction": direction,
                        "order": order,
                    },
                    verification_list_params.VerificationListParams,
                ),
            ),
            cast_to=VerificationListResponse,
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
        self.list = to_raw_response_wrapper(
            verifications.list,
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
        self.list = async_to_raw_response_wrapper(
            verifications.list,
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
        self.list = to_streamed_response_wrapper(
            verifications.list,
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
        self.list = async_to_streamed_response_wrapper(
            verifications.list,
        )
