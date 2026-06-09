# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    identity_profile_list_params,
    identity_profile_delete_params,
    identity_profile_list_verifications_params,
)
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
from ..types.identity_profile import IdentityProfile
from ..types.identity_profile_list_response import IdentityProfileListResponse
from ..types.identity_profile_list_verifications_response import IdentityProfileListVerificationsResponse

__all__ = ["IdentityProfilesResource", "AsyncIdentityProfilesResource"]


class IdentityProfilesResource(SyncAPIResource):
    """Identity profiles"""

    @cached_property
    def with_raw_response(self) -> IdentityProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return IdentityProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return IdentityProfilesResourceWithStreamingResponse(self)

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
    ) -> IdentityProfile:
        """
        Retrieves the details of an existing identity profile.

        Required permissions:

        - `identity:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/identity_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityProfile,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        profile_type: Optional[Literal["individual", "business"]] | Omit = omit,
        status: Optional[Literal["not_started", "pending", "approved", "rejected"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[IdentityProfileListResponse]:
        """Returns a paginated list of identity profiles.

        When company_id is provided,
        lists IPs currently linked to that company's ledger. When omitted, lists IPs
        linked to any ledger the actor can read (including child companies under a
        parent).

        Required permissions:

        - `identity:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of the company to filter to. When omitted, returns IPs
              across all ledgers the actor can read.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          profile_type: The kind of identity profile (individual vs business).

          status: Derived verification status for an identity profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/identity_profiles",
            page=SyncCursorPage[IdentityProfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "first": first,
                        "last": last,
                        "profile_type": profile_type,
                        "status": status,
                    },
                    identity_profile_list_params.IdentityProfileListParams,
                ),
            ),
            model=IdentityProfileListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        ledger_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityProfile:
        """
        Unlinks an IdentityProfile from a LedgerAccount (flips the matching link to
        is_current=false).

        Args:
          ledger_account_id: The ID of the LedgerAccount to unlink the identity profile from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/identity_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ledger_account_id": ledger_account_id}, identity_profile_delete_params.IdentityProfileDeleteParams
                ),
            ),
            cast_to=IdentityProfile,
        )

    def list_verifications(
        self,
        id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[IdentityProfileListVerificationsResponse]:
        """
        Returns a list of verifications attached to an identity profile, ordered by most
        recent first.

        Required permissions:

        - `identity:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/identity_profiles/{id}/verifications", id=id),
            page=SyncCursorPage[IdentityProfileListVerificationsResponse],
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
                    },
                    identity_profile_list_verifications_params.IdentityProfileListVerificationsParams,
                ),
            ),
            model=IdentityProfileListVerificationsResponse,
        )


class AsyncIdentityProfilesResource(AsyncAPIResource):
    """Identity profiles"""

    @cached_property
    def with_raw_response(self) -> AsyncIdentityProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentityProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncIdentityProfilesResourceWithStreamingResponse(self)

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
    ) -> IdentityProfile:
        """
        Retrieves the details of an existing identity profile.

        Required permissions:

        - `identity:read`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/identity_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityProfile,
        )

    def list(
        self,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        profile_type: Optional[Literal["individual", "business"]] | Omit = omit,
        status: Optional[Literal["not_started", "pending", "approved", "rejected"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[IdentityProfileListResponse, AsyncCursorPage[IdentityProfileListResponse]]:
        """Returns a paginated list of identity profiles.

        When company_id is provided,
        lists IPs currently linked to that company's ledger. When omitted, lists IPs
        linked to any ledger the actor can read (including child companies under a
        parent).

        Required permissions:

        - `identity:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          company_id: The unique identifier of the company to filter to. When omitted, returns IPs
              across all ledgers the actor can read.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          profile_type: The kind of identity profile (individual vs business).

          status: Derived verification status for an identity profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/identity_profiles",
            page=AsyncCursorPage[IdentityProfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "company_id": company_id,
                        "first": first,
                        "last": last,
                        "profile_type": profile_type,
                        "status": status,
                    },
                    identity_profile_list_params.IdentityProfileListParams,
                ),
            ),
            model=IdentityProfileListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        ledger_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityProfile:
        """
        Unlinks an IdentityProfile from a LedgerAccount (flips the matching link to
        is_current=false).

        Args:
          ledger_account_id: The ID of the LedgerAccount to unlink the identity profile from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/identity_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ledger_account_id": ledger_account_id}, identity_profile_delete_params.IdentityProfileDeleteParams
                ),
            ),
            cast_to=IdentityProfile,
        )

    def list_verifications(
        self,
        id: str,
        *,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        first: Optional[int] | Omit = omit,
        last: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        IdentityProfileListVerificationsResponse, AsyncCursorPage[IdentityProfileListVerificationsResponse]
    ]:
        """
        Returns a list of verifications attached to an identity profile, ordered by most
        recent first.

        Required permissions:

        - `identity:read`

        Args:
          after: Returns the elements in the list that come after the specified cursor.

          before: Returns the elements in the list that come before the specified cursor.

          first: Returns the first _n_ elements from the list.

          last: Returns the last _n_ elements from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/identity_profiles/{id}/verifications", id=id),
            page=AsyncCursorPage[IdentityProfileListVerificationsResponse],
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
                    },
                    identity_profile_list_verifications_params.IdentityProfileListVerificationsParams,
                ),
            ),
            model=IdentityProfileListVerificationsResponse,
        )


class IdentityProfilesResourceWithRawResponse:
    def __init__(self, identity_profiles: IdentityProfilesResource) -> None:
        self._identity_profiles = identity_profiles

        self.retrieve = to_raw_response_wrapper(
            identity_profiles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            identity_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            identity_profiles.delete,
        )
        self.list_verifications = to_raw_response_wrapper(
            identity_profiles.list_verifications,
        )


class AsyncIdentityProfilesResourceWithRawResponse:
    def __init__(self, identity_profiles: AsyncIdentityProfilesResource) -> None:
        self._identity_profiles = identity_profiles

        self.retrieve = async_to_raw_response_wrapper(
            identity_profiles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            identity_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            identity_profiles.delete,
        )
        self.list_verifications = async_to_raw_response_wrapper(
            identity_profiles.list_verifications,
        )


class IdentityProfilesResourceWithStreamingResponse:
    def __init__(self, identity_profiles: IdentityProfilesResource) -> None:
        self._identity_profiles = identity_profiles

        self.retrieve = to_streamed_response_wrapper(
            identity_profiles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            identity_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            identity_profiles.delete,
        )
        self.list_verifications = to_streamed_response_wrapper(
            identity_profiles.list_verifications,
        )


class AsyncIdentityProfilesResourceWithStreamingResponse:
    def __init__(self, identity_profiles: AsyncIdentityProfilesResource) -> None:
        self._identity_profiles = identity_profiles

        self.retrieve = async_to_streamed_response_wrapper(
            identity_profiles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            identity_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            identity_profiles.delete,
        )
        self.list_verifications = async_to_streamed_response_wrapper(
            identity_profiles.list_verifications,
        )
