# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import account_list_params, account_create_params, account_update_params, account_register_llc_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.account import Account
from ...types.account_register_llc_response import AccountRegisterLlcResponse
from ...types.account_recommend_actions_response import AccountRecommendActionsResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    """
    An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

    Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
    """

    @cached_property
    def preferences(self) -> PreferencesResource:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        return PreferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country: str | Omit = omit,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        title: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Creates an account.

        User tokens create business accounts; business account API
        keys create connected accounts. Tax fields (`tax_remitted_by`,
        `product_tax_code_id`, `business_address`, `tax_identifiers`) are configured
        with Update Account, not at creation.

        Args:
          country: The ISO 3166-1 alpha-2 country code where the account's business is located
              (e.g. `US`). Defaults to the parent account's country for connected accounts.

          email: The email address of the account owner. Required for business account API key
              requests.

          metadata: Arbitrary key/value metadata to store on the account.

          title: The display name of the account. Defaults to `metadata.external_id` or the
              owner's email when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "country": country,
                    "email": email,
                    "metadata": metadata,
                    "title": title,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

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
    ) -> Account:
        """
        Retrieves a single account visible to the credential, including its crypto
        wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def update(
        self,
        account_id: str,
        *,
        affiliate_application_required: bool | Omit = omit,
        affiliate_instructions: Optional[str] | Omit = omit,
        banner_image: Optional[Dict[str, object]] | Omit = omit,
        business_address: account_update_params.BusinessAddress | Omit = omit,
        business_type: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        featured_affiliate_product_id: Optional[str] | Omit = omit,
        home_preferences: SequenceNotStr[str] | Omit = omit,
        industry_group: Optional[str] | Omit = omit,
        industry_type: Optional[str] | Omit = omit,
        invoice_prefix: Optional[str] | Omit = omit,
        logo: Optional[Dict[str, object]] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        onboarding_type: Optional[str] | Omit = omit,
        opengraph_image: Optional[Dict[str, object]] | Omit = omit,
        opengraph_image_variant: Optional[str] | Omit = omit,
        other_business_description: Optional[str] | Omit = omit,
        other_industry_description: Optional[str] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        require_2fa: bool | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_customer_emails: bool | Omit = omit,
        show_joined_whops: bool | Omit = omit,
        show_reviews_dtc: bool | Omit = omit,
        show_user_directory: bool | Omit = omit,
        social_links: Iterable[Dict[str, object]] | Omit = omit,
        store_page_config: Optional[Dict[str, object]] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        tax_collection_enabled_states: List[
            Literal[
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY",
            ]
        ]
        | Omit = omit,
        tax_identifiers: Iterable[account_update_params.TaxIdentifier] | Omit = omit,
        tax_remitted_by: Literal["whop", "self", "none"] | Omit = omit,
        title: Optional[str] | Omit = omit,
        use_logo_as_opengraph_image_fallback: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Updates an account.

        User tokens can update business accounts; business account
        API keys can update connected accounts.

        Args:
          affiliate_application_required: Whether prospective affiliates must submit an application before promoting this
              account.

          affiliate_instructions: Guidelines shown to affiliates promoting this account.

          banner_image: Attachment input for the account banner image.

          business_address: Account business address used to calculate tax. A complete address in a
              supported country is required when `tax_remitted_by` is `self`.

          business_type: High-level business category for the account.

          country: Country where the account is located.

          description: Account promotional description.

          featured_affiliate_product_id: The ID of the product to feature for affiliates. Pass `null` to clear.

          home_preferences: Public account home page preferences.

          industry_group: Account industry group.

          industry_type: Specific industry vertical for the account.

          invoice_prefix: Prefix used for account invoices.

          logo: Attachment input for the account logo.

          metadata: Arbitrary key/value metadata to store on the account.

          onboarding_type: The type of onboarding the account has completed.

          opengraph_image: Attachment input for the account Open Graph image.

          opengraph_image_variant: The account Open Graph image variant.

          other_business_description: The description of the business type when business_type is other.

          other_industry_description: The description of the industry type when industry_type is other.

          product_tax_code_id: ID of the tax classification code applied by default to the account's products.
              See the available
              [product categories](https://docs.numeral.com/essentials/product-categories).

          require_2fa: Whether the account requires authorized users to have two-factor authentication
              enabled.

          route: The unique URL slug for the account.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this account.

          show_joined_whops: Whether the account appears in joined whops on other accounts.

          show_reviews_dtc: Whether reviews are displayed on direct-to-consumer product pages.

          show_user_directory: Whether the account shows users in the user directory.

          social_links: The full list of social links to display for the account.

          store_page_config: Account store page display configuration.

          target_audience: The target audience for this account.

          tax_collection_enabled_states: US state codes (50 states plus `DC`) where the account collects tax. Replaces
              the full set on update. Only settable when `tax_remitted_by` is `self`.

          tax_identifiers: Account tax/VAT registrations to add or update. When `tax_remitted_by` is
              `self`, tax is calculated and collected only in the countries where the account
              holds a registration.

          tax_remitted_by: Who calculates and remits tax for the account: `whop` (Whop calculates and
              remits), `self` (Whop calculates; the account collects and remits), or `none`
              (neither; the account is responsible). `self` requires a `business_address` in a
              supported country.

          title: The display name of the account.

          use_logo_as_opengraph_image_fallback: Whether the account uses its logo as the fallback Open Graph image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=maybe_transform(
                {
                    "affiliate_application_required": affiliate_application_required,
                    "affiliate_instructions": affiliate_instructions,
                    "banner_image": banner_image,
                    "business_address": business_address,
                    "business_type": business_type,
                    "country": country,
                    "description": description,
                    "featured_affiliate_product_id": featured_affiliate_product_id,
                    "home_preferences": home_preferences,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "invoice_prefix": invoice_prefix,
                    "logo": logo,
                    "metadata": metadata,
                    "onboarding_type": onboarding_type,
                    "opengraph_image": opengraph_image,
                    "opengraph_image_variant": opengraph_image_variant,
                    "other_business_description": other_business_description,
                    "other_industry_description": other_industry_description,
                    "product_tax_code_id": product_tax_code_id,
                    "require_2fa": require_2fa,
                    "route": route,
                    "send_customer_emails": send_customer_emails,
                    "show_joined_whops": show_joined_whops,
                    "show_reviews_dtc": show_reviews_dtc,
                    "show_user_directory": show_user_directory,
                    "social_links": social_links,
                    "store_page_config": store_page_config,
                    "target_audience": target_audience,
                    "tax_collection_enabled_states": tax_collection_enabled_states,
                    "tax_identifiers": tax_identifiers,
                    "tax_remitted_by": tax_remitted_by,
                    "title": title,
                    "use_logo_as_opengraph_image_fallback": use_logo_as_opengraph_image_fallback,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Account]:
        """Lists accounts visible to the credential.

        User tokens return the user's business
        accounts; business account API keys return the requesting business account and
        its connected accounts.

        Args:
          after: A cursor; returns accounts after this position.

          before: A cursor; returns accounts before this position.

          direction: Sort direction.

          first: The number of accounts to return (default 10, max 50).

          last: The number of accounts to return from the end of the range.

          order: The field to sort accounts by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=SyncCursorPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves the business account associated with the current business account API
        key.
        """
        return self._get(
            "/accounts/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def recommend_actions(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRecommendActionsResponse:
        """
        Lists the recommended actions computed for the account — the same set embedded
        on the account resource, served on their own so a caller can fetch just the
        recommendations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/recommend_actions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRecommendActionsResponse,
        )

    def register_llc(
        self,
        account_id: str,
        *,
        business_info: account_register_llc_params.BusinessInfo,
        founders: Iterable[account_register_llc_params.Founder],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRegisterLlcResponse:
        """Starts an LLC formation for a business account.

        On submission, the application
        is validated and the response returns a hosted checkout URL. Once paid, the
        filing is submitted. Track progress through the account's
        [`llc_formation`](/api-reference/beta/accounts/retrieve-account) field on
        Retrieve Account.

        Args:
          business_info: The company to form.

          founders: The company's founders. Exactly one must be marked `is_primary` — the
              responsible party for the filing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/accounts/{account_id}/llc", account_id=account_id),
            body=maybe_transform(
                {
                    "business_info": business_info,
                    "founders": founders,
                },
                account_register_llc_params.AccountRegisterLlcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRegisterLlcResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    """
    An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

    Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
    """

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        return AsyncPreferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country: str | Omit = omit,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        title: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Creates an account.

        User tokens create business accounts; business account API
        keys create connected accounts. Tax fields (`tax_remitted_by`,
        `product_tax_code_id`, `business_address`, `tax_identifiers`) are configured
        with Update Account, not at creation.

        Args:
          country: The ISO 3166-1 alpha-2 country code where the account's business is located
              (e.g. `US`). Defaults to the parent account's country for connected accounts.

          email: The email address of the account owner. Required for business account API key
              requests.

          metadata: Arbitrary key/value metadata to store on the account.

          title: The display name of the account. Defaults to `metadata.external_id` or the
              owner's email when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/accounts",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "email": email,
                    "metadata": metadata,
                    "title": title,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

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
    ) -> Account:
        """
        Retrieves a single account visible to the credential, including its crypto
        wallet.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def update(
        self,
        account_id: str,
        *,
        affiliate_application_required: bool | Omit = omit,
        affiliate_instructions: Optional[str] | Omit = omit,
        banner_image: Optional[Dict[str, object]] | Omit = omit,
        business_address: account_update_params.BusinessAddress | Omit = omit,
        business_type: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        featured_affiliate_product_id: Optional[str] | Omit = omit,
        home_preferences: SequenceNotStr[str] | Omit = omit,
        industry_group: Optional[str] | Omit = omit,
        industry_type: Optional[str] | Omit = omit,
        invoice_prefix: Optional[str] | Omit = omit,
        logo: Optional[Dict[str, object]] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        onboarding_type: Optional[str] | Omit = omit,
        opengraph_image: Optional[Dict[str, object]] | Omit = omit,
        opengraph_image_variant: Optional[str] | Omit = omit,
        other_business_description: Optional[str] | Omit = omit,
        other_industry_description: Optional[str] | Omit = omit,
        product_tax_code_id: Optional[str] | Omit = omit,
        require_2fa: bool | Omit = omit,
        route: Optional[str] | Omit = omit,
        send_customer_emails: bool | Omit = omit,
        show_joined_whops: bool | Omit = omit,
        show_reviews_dtc: bool | Omit = omit,
        show_user_directory: bool | Omit = omit,
        social_links: Iterable[Dict[str, object]] | Omit = omit,
        store_page_config: Optional[Dict[str, object]] | Omit = omit,
        target_audience: Optional[str] | Omit = omit,
        tax_collection_enabled_states: List[
            Literal[
                "AL",
                "AK",
                "AZ",
                "AR",
                "CA",
                "CO",
                "CT",
                "DE",
                "DC",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "IA",
                "KS",
                "KY",
                "LA",
                "ME",
                "MD",
                "MA",
                "MI",
                "MN",
                "MS",
                "MO",
                "MT",
                "NE",
                "NV",
                "NH",
                "NJ",
                "NM",
                "NY",
                "NC",
                "ND",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VT",
                "VA",
                "WA",
                "WV",
                "WI",
                "WY",
            ]
        ]
        | Omit = omit,
        tax_identifiers: Iterable[account_update_params.TaxIdentifier] | Omit = omit,
        tax_remitted_by: Literal["whop", "self", "none"] | Omit = omit,
        title: Optional[str] | Omit = omit,
        use_logo_as_opengraph_image_fallback: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """Updates an account.

        User tokens can update business accounts; business account
        API keys can update connected accounts.

        Args:
          affiliate_application_required: Whether prospective affiliates must submit an application before promoting this
              account.

          affiliate_instructions: Guidelines shown to affiliates promoting this account.

          banner_image: Attachment input for the account banner image.

          business_address: Account business address used to calculate tax. A complete address in a
              supported country is required when `tax_remitted_by` is `self`.

          business_type: High-level business category for the account.

          country: Country where the account is located.

          description: Account promotional description.

          featured_affiliate_product_id: The ID of the product to feature for affiliates. Pass `null` to clear.

          home_preferences: Public account home page preferences.

          industry_group: Account industry group.

          industry_type: Specific industry vertical for the account.

          invoice_prefix: Prefix used for account invoices.

          logo: Attachment input for the account logo.

          metadata: Arbitrary key/value metadata to store on the account.

          onboarding_type: The type of onboarding the account has completed.

          opengraph_image: Attachment input for the account Open Graph image.

          opengraph_image_variant: The account Open Graph image variant.

          other_business_description: The description of the business type when business_type is other.

          other_industry_description: The description of the industry type when industry_type is other.

          product_tax_code_id: ID of the tax classification code applied by default to the account's products.
              See the available
              [product categories](https://docs.numeral.com/essentials/product-categories).

          require_2fa: Whether the account requires authorized users to have two-factor authentication
              enabled.

          route: The unique URL slug for the account.

          send_customer_emails: Whether Whop sends transactional emails to customers on behalf of this account.

          show_joined_whops: Whether the account appears in joined whops on other accounts.

          show_reviews_dtc: Whether reviews are displayed on direct-to-consumer product pages.

          show_user_directory: Whether the account shows users in the user directory.

          social_links: The full list of social links to display for the account.

          store_page_config: Account store page display configuration.

          target_audience: The target audience for this account.

          tax_collection_enabled_states: US state codes (50 states plus `DC`) where the account collects tax. Replaces
              the full set on update. Only settable when `tax_remitted_by` is `self`.

          tax_identifiers: Account tax/VAT registrations to add or update. When `tax_remitted_by` is
              `self`, tax is calculated and collected only in the countries where the account
              holds a registration.

          tax_remitted_by: Who calculates and remits tax for the account: `whop` (Whop calculates and
              remits), `self` (Whop calculates; the account collects and remits), or `none`
              (neither; the account is responsible). `self` requires a `business_address` in a
              supported country.

          title: The display name of the account.

          use_logo_as_opengraph_image_fallback: Whether the account uses its logo as the fallback Open Graph image.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "affiliate_application_required": affiliate_application_required,
                    "affiliate_instructions": affiliate_instructions,
                    "banner_image": banner_image,
                    "business_address": business_address,
                    "business_type": business_type,
                    "country": country,
                    "description": description,
                    "featured_affiliate_product_id": featured_affiliate_product_id,
                    "home_preferences": home_preferences,
                    "industry_group": industry_group,
                    "industry_type": industry_type,
                    "invoice_prefix": invoice_prefix,
                    "logo": logo,
                    "metadata": metadata,
                    "onboarding_type": onboarding_type,
                    "opengraph_image": opengraph_image,
                    "opengraph_image_variant": opengraph_image_variant,
                    "other_business_description": other_business_description,
                    "other_industry_description": other_industry_description,
                    "product_tax_code_id": product_tax_code_id,
                    "require_2fa": require_2fa,
                    "route": route,
                    "send_customer_emails": send_customer_emails,
                    "show_joined_whops": show_joined_whops,
                    "show_reviews_dtc": show_reviews_dtc,
                    "show_user_directory": show_user_directory,
                    "social_links": social_links,
                    "store_page_config": store_page_config,
                    "target_audience": target_audience,
                    "tax_collection_enabled_states": tax_collection_enabled_states,
                    "tax_identifiers": tax_identifiers,
                    "tax_remitted_by": tax_remitted_by,
                    "title": title,
                    "use_logo_as_opengraph_image_fallback": use_logo_as_opengraph_image_fallback,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        first: int | Omit = omit,
        last: int | Omit = omit,
        order: Literal["created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Account, AsyncCursorPage[Account]]:
        """Lists accounts visible to the credential.

        User tokens return the user's business
        accounts; business account API keys return the requesting business account and
        its connected accounts.

        Args:
          after: A cursor; returns accounts after this position.

          before: A cursor; returns accounts before this position.

          direction: Sort direction.

          first: The number of accounts to return (default 10, max 50).

          last: The number of accounts to return from the end of the range.

          order: The field to sort accounts by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=AsyncCursorPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "first": first,
                        "last": last,
                        "order": order,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves the business account associated with the current business account API
        key.
        """
        return await self._get(
            "/accounts/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def recommend_actions(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRecommendActionsResponse:
        """
        Lists the recommended actions computed for the account — the same set embedded
        on the account resource, served on their own so a caller can fetch just the
        recommendations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/recommend_actions", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRecommendActionsResponse,
        )

    async def register_llc(
        self,
        account_id: str,
        *,
        business_info: account_register_llc_params.BusinessInfo,
        founders: Iterable[account_register_llc_params.Founder],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRegisterLlcResponse:
        """Starts an LLC formation for a business account.

        On submission, the application
        is validated and the response returns a hosted checkout URL. Once paid, the
        filing is submitted. Track progress through the account's
        [`llc_formation`](/api-reference/beta/accounts/retrieve-account) field on
        Retrieve Account.

        Args:
          business_info: The company to form.

          founders: The company's founders. Exactly one must be marked `is_primary` — the
              responsible party for the filing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/accounts/{account_id}/llc", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "business_info": business_info,
                    "founders": founders,
                },
                account_register_llc_params.AccountRegisterLlcParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRegisterLlcResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.me = to_raw_response_wrapper(
            accounts.me,
        )
        self.recommend_actions = to_raw_response_wrapper(
            accounts.recommend_actions,
        )
        self.register_llc = to_raw_response_wrapper(
            accounts.register_llc,
        )

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        return PreferencesResourceWithRawResponse(self._accounts.preferences)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.me = async_to_raw_response_wrapper(
            accounts.me,
        )
        self.recommend_actions = async_to_raw_response_wrapper(
            accounts.recommend_actions,
        )
        self.register_llc = async_to_raw_response_wrapper(
            accounts.register_llc,
        )

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        return AsyncPreferencesResourceWithRawResponse(self._accounts.preferences)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.me = to_streamed_response_wrapper(
            accounts.me,
        )
        self.recommend_actions = to_streamed_response_wrapper(
            accounts.recommend_actions,
        )
        self.register_llc = to_streamed_response_wrapper(
            accounts.register_llc,
        )

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        return PreferencesResourceWithStreamingResponse(self._accounts.preferences)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.me = async_to_streamed_response_wrapper(
            accounts.me,
        )
        self.recommend_actions = async_to_streamed_response_wrapper(
            accounts.recommend_actions,
        )
        self.register_llc = async_to_streamed_response_wrapper(
            accounts.register_llc,
        )

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        return AsyncPreferencesResourceWithStreamingResponse(self._accounts.preferences)
