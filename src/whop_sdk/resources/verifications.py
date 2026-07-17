# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import verification_list_params, verification_create_params, verification_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
    """A Verification represents an identity review for a person or business.

    Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

    Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
    """

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

    @overload
    def create(
        self,
        *,
        account_id: str,
        address: verification_create_params.CreateIndividualVerificationAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        document_type: Literal["ID_CARD", "DRIVERS", "RESIDENCE_PERMIT", "PASSPORT"] | Omit = omit,
        documents: verification_create_params.CreateIndividualVerificationDocuments | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
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
        active session when one already exists. Any fields you include in the request
        body are used to prefill the session. Send `documents` (with `document_type`) to
        instead verify the person from identity documents included in this request — no
        hosted session involved. If the account already has an `approved` verification
        the request is rejected; unlink it first to start a new one.

        Args:
          account_id: Account or user ID whose identity you want to verify. Use a `biz_` account ID
              for account verifications, or the caller's `user_` ID for personal verification.

          business_name: Legal business name for a sole proprietor or single-member LLC.

          business_structure: Entity type for sole proprietors, such as `single_member_llc`. Supported values
              vary by country of incorporation — see
              [Business structures](/developer/verification/business-structures).

          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          business_website: Business website URL. Whop store pages are not accepted.

          country: Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`.

          date_of_birth: Formatted as `YYYY-MM-DD`.

          document_type: Identity document being sent, when verifying with `documents`. Decides exactly
              which file slots to send: `ID_CARD` → `id_card_front` + `id_card_back` +
              `selfie`; `DRIVERS` → `drivers_front` + `drivers_back` + `selfie`;
              `RESIDENCE_PERMIT` → `residence_permit_front` + `residence_permit_back` +
              `selfie`; `PASSPORT` → `passport_front` + `selfie`. See
              [Identity documents](/developer/verification/identity-documents).

          documents: Identity document files, each value the file's raw bytes base64-encoded (JPEG,
              PNG, or PDF, up to 5MB per file before encoding). Sending this object verifies
              the person from the files in this request instead of a hosted session —
              individual verifications only, and the request must also carry `document_type`,
              `first_name`, `last_name`, `date_of_birth`, `country`, `phone`,
              `tax_identification_number`, and an `address` with `line1`, `city`, `state`, and
              `postal_code`. Send every slot for your `document_type` — a missing or rejected
              file fails the whole request and nothing is submitted; review starts
              automatically once every document is accepted. See
              [Identity documents](/developer/verification/identity-documents) for a full
              walkthrough.

          kind: Verification type. Defaults to `individual`.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

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
        account_id: str,
        address: verification_create_params.CreateBusinessVerificationAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        kind: Literal["business"] | Omit = omit,
        place_of_incorporation: str | Omit = omit,
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
        active session when one already exists. Any fields you include in the request
        body are used to prefill the session. Send `documents` (with `document_type`) to
        instead verify the person from identity documents included in this request — no
        hosted session involved. If the account already has an `approved` verification
        the request is rejected; unlink it first to start a new one.

        Args:
          account_id: Account or user ID whose identity you want to verify. Use a `biz_` account ID
              for account verifications, or the caller's `user_` ID for personal verification.

          business_name: Legal business name.

          business_structure: Legal entity structure of the business, such as `private_corporation` or
              `sole_proprietorship`. Supported values vary by country of incorporation — see
              [Business structures](/developer/verification/business-structures).

          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          business_website: Business website URL. Whop store pages are not accepted.

          country: Country of incorporation as a two-letter ISO 3166-1 country code.

          kind: Must be `business` to start a KYB verification.

          place_of_incorporation: State or region where the business is incorporated.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    def create(
        self,
        *,
        account_id: str,
        address: verification_create_params.CreateIndividualVerificationAddress
        | verification_create_params.CreateBusinessVerificationAddress
        | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        document_type: Literal["ID_CARD", "DRIVERS", "RESIDENCE_PERMIT", "PASSPORT"] | Omit = omit,
        documents: verification_create_params.CreateIndividualVerificationDocuments | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual"] | Literal["business"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        tax_identification_number: str | Omit = omit,
        place_of_incorporation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        return self._post(
            "/verifications",
            body=maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "business_structure": business_structure,
                    "business_tax_identification_number": business_tax_identification_number,
                    "business_website": business_website,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "document_type": document_type,
                    "documents": documents,
                    "first_name": first_name,
                    "kind": kind,
                    "last_name": last_name,
                    "phone": phone,
                    "tax_identification_number": tax_identification_number,
                    "place_of_incorporation": place_of_incorporation,
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
        Returns verifications for an account, including their status and any required
        actions.

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

    @overload
    def update(
        self,
        verification_id: str,
        *,
        business_tax_identification_number: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        personal_address: verification_update_params.UpdateIndividualVerificationPersonalAddress | Omit = omit,
        requested_information: Iterable[verification_update_params.UpdateIndividualVerificationRequestedInformation]
        | Omit = omit,
        tax_identification_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates editable profile details or submits answers for items returned in
        `requested_information`. Once a verification is `approved` its profile details
        are locked and can no longer be edited.

        Args:
          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          country: Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`.

          date_of_birth: Formatted as `YYYY-MM-DD`.

          personal_address: Personal address for the individual.

          requested_information: Answers to items returned in `requested_information`. Each entry must include
              the requested item `id` and exactly one answer payload matching the item's
              `type`: `value` for `text`, `date`, or `phone`; `address` for `address`; `files`
              for `files`.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        verification_id: str,
        *,
        business_address: verification_update_params.UpdateBusinessVerificationBusinessAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        country: str | Omit = omit,
        requested_information: Iterable[verification_update_params.UpdateBusinessVerificationRequestedInformation]
        | Omit = omit,
        tax_identification_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates editable profile details or submits answers for items returned in
        `requested_information`. Once a verification is `approved` its profile details
        are locked and can no longer be edited.

        Args:
          business_address: Business address.

          business_name: Legal business name.

          business_structure: Legal entity structure of the business, such as `private_corporation` or
              `sole_proprietorship`. Supported values vary by country of incorporation — see
              [Business structures](/developer/verification/business-structures).

          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          country: Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`.

          requested_information: Answers to items returned in `requested_information`. Each entry must include
              the requested item `id` and exactly one answer payload matching the item's
              `type`: `value` for `text`, `date`, or `phone`; `address` for `address`; `files`
              for `files`.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        verification_id: str,
        *,
        business_tax_identification_number: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        personal_address: verification_update_params.UpdateIndividualVerificationPersonalAddress | Omit = omit,
        requested_information: Iterable[verification_update_params.UpdateIndividualVerificationRequestedInformation]
        | Iterable[verification_update_params.UpdateBusinessVerificationRequestedInformation]
        | Omit = omit,
        tax_identification_number: str | Omit = omit,
        business_address: verification_update_params.UpdateBusinessVerificationBusinessAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._patch(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            body=maybe_transform(
                {
                    "business_tax_identification_number": business_tax_identification_number,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "personal_address": personal_address,
                    "requested_information": requested_information,
                    "tax_identification_number": tax_identification_number,
                    "business_address": business_address,
                    "business_name": business_name,
                    "business_structure": business_structure,
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
        Returns verifications for an account, including their status and any required
        actions.

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
    """A Verification represents an identity review for a person or business.

    Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

    Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
    """

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

    @overload
    async def create(
        self,
        *,
        account_id: str,
        address: verification_create_params.CreateIndividualVerificationAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        document_type: Literal["ID_CARD", "DRIVERS", "RESIDENCE_PERMIT", "PASSPORT"] | Omit = omit,
        documents: verification_create_params.CreateIndividualVerificationDocuments | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
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
        active session when one already exists. Any fields you include in the request
        body are used to prefill the session. Send `documents` (with `document_type`) to
        instead verify the person from identity documents included in this request — no
        hosted session involved. If the account already has an `approved` verification
        the request is rejected; unlink it first to start a new one.

        Args:
          account_id: Account or user ID whose identity you want to verify. Use a `biz_` account ID
              for account verifications, or the caller's `user_` ID for personal verification.

          business_name: Legal business name for a sole proprietor or single-member LLC.

          business_structure: Entity type for sole proprietors, such as `single_member_llc`. Supported values
              vary by country of incorporation — see
              [Business structures](/developer/verification/business-structures).

          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          business_website: Business website URL. Whop store pages are not accepted.

          country: Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`.

          date_of_birth: Formatted as `YYYY-MM-DD`.

          document_type: Identity document being sent, when verifying with `documents`. Decides exactly
              which file slots to send: `ID_CARD` → `id_card_front` + `id_card_back` +
              `selfie`; `DRIVERS` → `drivers_front` + `drivers_back` + `selfie`;
              `RESIDENCE_PERMIT` → `residence_permit_front` + `residence_permit_back` +
              `selfie`; `PASSPORT` → `passport_front` + `selfie`. See
              [Identity documents](/developer/verification/identity-documents).

          documents: Identity document files, each value the file's raw bytes base64-encoded (JPEG,
              PNG, or PDF, up to 5MB per file before encoding). Sending this object verifies
              the person from the files in this request instead of a hosted session —
              individual verifications only, and the request must also carry `document_type`,
              `first_name`, `last_name`, `date_of_birth`, `country`, `phone`,
              `tax_identification_number`, and an `address` with `line1`, `city`, `state`, and
              `postal_code`. Send every slot for your `document_type` — a missing or rejected
              file fails the whole request and nothing is submitted; review starts
              automatically once every document is accepted. See
              [Identity documents](/developer/verification/identity-documents) for a full
              walkthrough.

          kind: Verification type. Defaults to `individual`.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

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
        account_id: str,
        address: verification_create_params.CreateBusinessVerificationAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        kind: Literal["business"] | Omit = omit,
        place_of_incorporation: str | Omit = omit,
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
        active session when one already exists. Any fields you include in the request
        body are used to prefill the session. Send `documents` (with `document_type`) to
        instead verify the person from identity documents included in this request — no
        hosted session involved. If the account already has an `approved` verification
        the request is rejected; unlink it first to start a new one.

        Args:
          account_id: Account or user ID whose identity you want to verify. Use a `biz_` account ID
              for account verifications, or the caller's `user_` ID for personal verification.

          business_name: Legal business name.

          business_structure: Legal entity structure of the business, such as `private_corporation` or
              `sole_proprietorship`. Supported values vary by country of incorporation — see
              [Business structures](/developer/verification/business-structures).

          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          business_website: Business website URL. Whop store pages are not accepted.

          country: Country of incorporation as a two-letter ISO 3166-1 country code.

          kind: Must be `business` to start a KYB verification.

          place_of_incorporation: State or region where the business is incorporated.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    async def create(
        self,
        *,
        account_id: str,
        address: verification_create_params.CreateIndividualVerificationAddress
        | verification_create_params.CreateBusinessVerificationAddress
        | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        business_website: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        document_type: Literal["ID_CARD", "DRIVERS", "RESIDENCE_PERMIT", "PASSPORT"] | Omit = omit,
        documents: verification_create_params.CreateIndividualVerificationDocuments | Omit = omit,
        first_name: str | Omit = omit,
        kind: Literal["individual"] | Literal["business"] | Omit = omit,
        last_name: str | Omit = omit,
        phone: str | Omit = omit,
        tax_identification_number: str | Omit = omit,
        place_of_incorporation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        return await self._post(
            "/verifications",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "business_structure": business_structure,
                    "business_tax_identification_number": business_tax_identification_number,
                    "business_website": business_website,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "document_type": document_type,
                    "documents": documents,
                    "first_name": first_name,
                    "kind": kind,
                    "last_name": last_name,
                    "phone": phone,
                    "tax_identification_number": tax_identification_number,
                    "place_of_incorporation": place_of_incorporation,
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
        Returns verifications for an account, including their status and any required
        actions.

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

    @overload
    async def update(
        self,
        verification_id: str,
        *,
        business_tax_identification_number: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        personal_address: verification_update_params.UpdateIndividualVerificationPersonalAddress | Omit = omit,
        requested_information: Iterable[verification_update_params.UpdateIndividualVerificationRequestedInformation]
        | Omit = omit,
        tax_identification_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates editable profile details or submits answers for items returned in
        `requested_information`. Once a verification is `approved` its profile details
        are locked and can no longer be edited.

        Args:
          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          country: Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`.

          date_of_birth: Formatted as `YYYY-MM-DD`.

          personal_address: Personal address for the individual.

          requested_information: Answers to items returned in `requested_information`. Each entry must include
              the requested item `id` and exactly one answer payload matching the item's
              `type`: `value` for `text`, `date`, or `phone`; `address` for `address`; `files`
              for `files`.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        verification_id: str,
        *,
        business_address: verification_update_params.UpdateBusinessVerificationBusinessAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        business_tax_identification_number: str | Omit = omit,
        country: str | Omit = omit,
        requested_information: Iterable[verification_update_params.UpdateBusinessVerificationRequestedInformation]
        | Omit = omit,
        tax_identification_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        """
        Updates editable profile details or submits answers for items returned in
        `requested_information`. Once a verification is `approved` its profile details
        are locked and can no longer be edited.

        Args:
          business_address: Business address.

          business_name: Legal business name.

          business_structure: Legal entity structure of the business, such as `private_corporation` or
              `sole_proprietorship`. Supported values vary by country of incorporation — see
              [Business structures](/developer/verification/business-structures).

          business_tax_identification_number: The business ID number of the company, as appropriate for the company's country.
              Examples are an Employer Identification Number (EIN) in the US, a Business
              Number in Canada, or a Company Number in the UK.

          country: Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`.

          requested_information: Answers to items returned in `requested_information`. Each entry must include
              the requested item `id` and exactly one answer payload matching the item's
              `type`: `value` for `text`, `date`, or `phone`; `address` for `address`; `files`
              for `files`.

          tax_identification_number: The government-issued ID number of the person being verified — the individual
              for a KYC verification, or the business representative for a KYB verification —
              as appropriate for their country. Examples are a Social Security Number (SSN) in
              the US, or a Social Insurance Number in Canada.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        verification_id: str,
        *,
        business_tax_identification_number: str | Omit = omit,
        country: str | Omit = omit,
        date_of_birth: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        personal_address: verification_update_params.UpdateIndividualVerificationPersonalAddress | Omit = omit,
        requested_information: Iterable[verification_update_params.UpdateIndividualVerificationRequestedInformation]
        | Iterable[verification_update_params.UpdateBusinessVerificationRequestedInformation]
        | Omit = omit,
        tax_identification_number: str | Omit = omit,
        business_address: verification_update_params.UpdateBusinessVerificationBusinessAddress | Omit = omit,
        business_name: str | Omit = omit,
        business_structure: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationUpdateResponse:
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._patch(
            path_template("/verifications/{verification_id}", verification_id=verification_id),
            body=await async_maybe_transform(
                {
                    "business_tax_identification_number": business_tax_identification_number,
                    "country": country,
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "personal_address": personal_address,
                    "requested_information": requested_information,
                    "tax_identification_number": tax_identification_number,
                    "business_address": business_address,
                    "business_name": business_name,
                    "business_structure": business_structure,
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
        Returns verifications for an account, including their status and any required
        actions.

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
