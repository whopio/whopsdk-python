# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts import preference_update_params
from ...types.accounts.preference_update_response import PreferenceUpdateResponse
from ...types.accounts.preference_retrieve_response import PreferenceRetrieveResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    """
    An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

    Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
    """

    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """
        Retrieves the account's preferences: a singleton settings document keyed by
        preference name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/preferences", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    def update(
        self,
        account_id: str,
        *,
        ads_payment_methods: preference_update_params.AdsPaymentMethods | Omit = omit,
        ads_reporting_currency: str | Omit = omit,
        ads_scheduling_timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateResponse:
        """Updates the account's preferences.

        Each top-level key present in the body is
        replaced as a whole; omitted keys are left untouched. `ads_payment_methods`
        always requires a `primary` entry. `backup` is optional and any pairing is
        allowed — two cards, `card`+`platform_balance`, or a single method — so a
        card-only advertiser can fund ads without a platform balance. The `primary` and
        `backup` must be different sources. A `platform_balance` entry may omit `id` to
        use the account's default Whop balance. Configuring a `card` requires a user
        token; account API keys can set up platform-balance billing only.

        Args:
          ads_payment_methods: How the account pays for Whop Ads spend. `primary` is charged first; `backup`
              covers the charge when the primary fails.

          ads_reporting_currency: Lowercase ISO currency code, such as `usd` or `eur`, used to display ad spend
              and stats. Defaults to `usd`.

          ads_scheduling_timezone: IANA timezone (e.g. `America/New_York`) used to interpret campaign start/end
              times and to bucket reports. Cannot be cleared once set — pass a new value to
              change it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template("/accounts/{account_id}/preferences", account_id=account_id),
            body=maybe_transform(
                {
                    "ads_payment_methods": ads_payment_methods,
                    "ads_reporting_currency": ads_reporting_currency,
                    "ads_scheduling_timezone": ads_scheduling_timezone,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpdateResponse,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    """
    An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

    Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """
        Retrieves the account's preferences: a singleton settings document keyed by
        preference name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/preferences", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    async def update(
        self,
        account_id: str,
        *,
        ads_payment_methods: preference_update_params.AdsPaymentMethods | Omit = omit,
        ads_reporting_currency: str | Omit = omit,
        ads_scheduling_timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateResponse:
        """Updates the account's preferences.

        Each top-level key present in the body is
        replaced as a whole; omitted keys are left untouched. `ads_payment_methods`
        always requires a `primary` entry. `backup` is optional and any pairing is
        allowed — two cards, `card`+`platform_balance`, or a single method — so a
        card-only advertiser can fund ads without a platform balance. The `primary` and
        `backup` must be different sources. A `platform_balance` entry may omit `id` to
        use the account's default Whop balance. Configuring a `card` requires a user
        token; account API keys can set up platform-balance billing only.

        Args:
          ads_payment_methods: How the account pays for Whop Ads spend. `primary` is charged first; `backup`
              covers the charge when the primary fails.

          ads_reporting_currency: Lowercase ISO currency code, such as `usd` or `eur`, used to display ad spend
              and stats. Defaults to `usd`.

          ads_scheduling_timezone: IANA timezone (e.g. `America/New_York`) used to interpret campaign start/end
              times and to bucket reports. Cannot be cleared once set — pass a new value to
              change it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}/preferences", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "ads_payment_methods": ads_payment_methods,
                    "ads_reporting_currency": ads_reporting_currency,
                    "ads_scheduling_timezone": ads_scheduling_timezone,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceUpdateResponse,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            preferences.update,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            preferences.update,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            preferences.update,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            preferences.update,
        )
