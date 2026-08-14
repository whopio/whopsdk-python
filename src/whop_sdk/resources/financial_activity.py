# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import financial_activity_list_params
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
from ..types.financial_activity_list_response import FinancialActivityListResponse

__all__ = ["FinancialActivityResource", "AsyncFinancialActivityResource"]


class FinancialActivityResource(SyncAPIResource):
    """
    A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

    Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
    """

    @cached_property
    def with_raw_response(self) -> FinancialActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return FinancialActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return FinancialActivityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        available_after: Union[str, date] | Omit = omit,
        available_before: Union[str, date] | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        include_owned_accounts: bool | Omit = omit,
        include_resource: bool | Omit = omit,
        limit: int | Omit = omit,
        line_types: List[
            Literal[
                "ad_budget_release",
                "ad_campaign_budget",
                "ad_publisher_payout",
                "ad_publisher_payout_received",
                "ad_spend_charge",
                "affiliate_fee",
                "airdrop",
                "airdrop_link_created",
                "airdrop_link_redeemed",
                "airdrop_link_returned",
                "airdrop_reversal",
                "application_fee",
                "application_fee_payout",
                "bank_transfer",
                "billing_percentage_fee",
                "buyer_fee",
                "card_spend_authorization",
                "card_spend_authorization_void",
                "card_spend_refund",
                "company_referral",
                "cross_border_percentage_fee",
                "currency_conversion_incoming",
                "currency_conversion_outgoing",
                "dispute_alert_fee",
                "dispute_hold_adjustment",
                "dispute_representment_fee",
                "fees",
                "fraud_prevention_fee",
                "fx_percentage_fee",
                "high_risk_merchant_fee",
                "installment_default",
                "internal_balance_transfer_incoming",
                "internal_balance_transfer_outgoing",
                "legacy_crypto_payment",
                "legacy_payment",
                "legacy_payment_refund",
                "license_sale",
                "license_sale_commission",
                "license_sale_revenue",
                "misc_purchase",
                "misc_refund",
                "misc_reversal",
                "onchain_deposit",
                "onchain_swap_target",
                "onchain_wallet_transfer_incoming",
                "onchain_wallet_transfer_outgoing",
                "orchestration_percentage_fee",
                "passthrough_gmv",
                "payment_dispute",
                "payment_dispute_adjustment",
                "payment_dispute_fee",
                "payment_dispute_reversal",
                "payment_gross",
                "payment_gross_reversal",
                "payment_processing_fixed_fee",
                "payment_processing_percentage_fee",
                "payment_referral",
                "payment_referral_reversal",
                "payment_refund",
                "payment_refund_reversal",
                "payment_revshare",
                "payment_revshare_payout",
                "payment_revshare_refund",
                "payment_revshare_reversal",
                "payout_fee",
                "platform_affiliate_payment",
                "platform_affiliate_payment_reversal",
                "platform_balance_payment",
                "platform_balance_payment_refund",
                "platform_balance_transfer_incoming",
                "platform_balance_transfer_outgoing",
                "platform_covered_dispute",
                "promo_reversal",
                "referral_bonus",
                "resolution_center_refund",
                "revshare_percentage_fee",
                "sales_tax_fee",
                "sales_tax_remittance",
                "sales_tax_remittance_reversal",
                "software_rental_revshare",
                "software_rental_transaction",
                "stripe_domestic_processing_fee",
                "stripe_international_processing_fee",
                "three_ds_fixed_fee",
                "topup",
                "topup_fee",
                "topup_reversal",
                "treasury_payin",
                "whop_processing_fee",
                "withdrawal",
                "withdrawal_clawback",
                "withdrawal_clawback_reversal",
                "withdrawal_reclassification",
                "withdrawal_reversal",
            ]
        ]
        | Omit = omit,
        posted_after: Union[str, datetime] | Omit = omit,
        posted_before: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialActivityListResponse:
        """
        Returns an account's or user's activity feed: every movement of money in or out.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          available_after: Only include rows whose funds became withdrawable on or after this `YYYY-MM-DD`
              settlement date (UTC), distinct from posted_at. Requires currency.

          available_before: Only include rows whose funds became withdrawable on or before this `YYYY-MM-DD`
              settlement date (UTC). Set equal to available_after for a single day. Requires
              currency.

          currency: Optional currency code filter, for example `usd`.

          cursor: Cursor returned by the previous page.

          include_owned_accounts: When true, aggregates the authenticated user's personal ledger with the
              businesses they own (owner role with balance read) into one feed. Requires
              user_id to be the authenticated user; cannot be combined with account_id or the
              settlement-date filters. Each returned row includes the owning `account`.

          include_resource: Whether to include the `resource` field in the response or not. Consider passing
              `false` if you need a fast response without as many rich details.

          limit: Maximum number of rows to return.

          line_types: Optional ledger line categories to include. Some categories (for example
              `onchain_deposit`, which covers inbound crypto deposits such as MoonPay onramps)
              are only returned when explicitly requested here.

          posted_after: Only include rows posted after this ISO 8601 timestamp.

          posted_before: Only include rows posted before this ISO 8601 timestamp.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/financial-activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "available_after": available_after,
                        "available_before": available_before,
                        "currency": currency,
                        "cursor": cursor,
                        "include_owned_accounts": include_owned_accounts,
                        "include_resource": include_resource,
                        "limit": limit,
                        "line_types": line_types,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                        "user_id": user_id,
                    },
                    financial_activity_list_params.FinancialActivityListParams,
                ),
            ),
            cast_to=FinancialActivityListResponse,
        )


class AsyncFinancialActivityResource(AsyncAPIResource):
    """
    A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

    Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFinancialActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/whopio/whopsdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFinancialActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/whopio/whopsdk-python#with_streaming_response
        """
        return AsyncFinancialActivityResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        available_after: Union[str, date] | Omit = omit,
        available_before: Union[str, date] | Omit = omit,
        currency: str | Omit = omit,
        cursor: str | Omit = omit,
        include_owned_accounts: bool | Omit = omit,
        include_resource: bool | Omit = omit,
        limit: int | Omit = omit,
        line_types: List[
            Literal[
                "ad_budget_release",
                "ad_campaign_budget",
                "ad_publisher_payout",
                "ad_publisher_payout_received",
                "ad_spend_charge",
                "affiliate_fee",
                "airdrop",
                "airdrop_link_created",
                "airdrop_link_redeemed",
                "airdrop_link_returned",
                "airdrop_reversal",
                "application_fee",
                "application_fee_payout",
                "bank_transfer",
                "billing_percentage_fee",
                "buyer_fee",
                "card_spend_authorization",
                "card_spend_authorization_void",
                "card_spend_refund",
                "company_referral",
                "cross_border_percentage_fee",
                "currency_conversion_incoming",
                "currency_conversion_outgoing",
                "dispute_alert_fee",
                "dispute_hold_adjustment",
                "dispute_representment_fee",
                "fees",
                "fraud_prevention_fee",
                "fx_percentage_fee",
                "high_risk_merchant_fee",
                "installment_default",
                "internal_balance_transfer_incoming",
                "internal_balance_transfer_outgoing",
                "legacy_crypto_payment",
                "legacy_payment",
                "legacy_payment_refund",
                "license_sale",
                "license_sale_commission",
                "license_sale_revenue",
                "misc_purchase",
                "misc_refund",
                "misc_reversal",
                "onchain_deposit",
                "onchain_swap_target",
                "onchain_wallet_transfer_incoming",
                "onchain_wallet_transfer_outgoing",
                "orchestration_percentage_fee",
                "passthrough_gmv",
                "payment_dispute",
                "payment_dispute_adjustment",
                "payment_dispute_fee",
                "payment_dispute_reversal",
                "payment_gross",
                "payment_gross_reversal",
                "payment_processing_fixed_fee",
                "payment_processing_percentage_fee",
                "payment_referral",
                "payment_referral_reversal",
                "payment_refund",
                "payment_refund_reversal",
                "payment_revshare",
                "payment_revshare_payout",
                "payment_revshare_refund",
                "payment_revshare_reversal",
                "payout_fee",
                "platform_affiliate_payment",
                "platform_affiliate_payment_reversal",
                "platform_balance_payment",
                "platform_balance_payment_refund",
                "platform_balance_transfer_incoming",
                "platform_balance_transfer_outgoing",
                "platform_covered_dispute",
                "promo_reversal",
                "referral_bonus",
                "resolution_center_refund",
                "revshare_percentage_fee",
                "sales_tax_fee",
                "sales_tax_remittance",
                "sales_tax_remittance_reversal",
                "software_rental_revshare",
                "software_rental_transaction",
                "stripe_domestic_processing_fee",
                "stripe_international_processing_fee",
                "three_ds_fixed_fee",
                "topup",
                "topup_fee",
                "topup_reversal",
                "treasury_payin",
                "whop_processing_fee",
                "withdrawal",
                "withdrawal_clawback",
                "withdrawal_clawback_reversal",
                "withdrawal_reclassification",
                "withdrawal_reversal",
            ]
        ]
        | Omit = omit,
        posted_after: Union[str, datetime] | Omit = omit,
        posted_before: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialActivityListResponse:
        """
        Returns an account's or user's activity feed: every movement of money in or out.

        Args:
          account_id: The owning account ID (a biz\\__ identifier). Provide this or user_id.

          available_after: Only include rows whose funds became withdrawable on or after this `YYYY-MM-DD`
              settlement date (UTC), distinct from posted_at. Requires currency.

          available_before: Only include rows whose funds became withdrawable on or before this `YYYY-MM-DD`
              settlement date (UTC). Set equal to available_after for a single day. Requires
              currency.

          currency: Optional currency code filter, for example `usd`.

          cursor: Cursor returned by the previous page.

          include_owned_accounts: When true, aggregates the authenticated user's personal ledger with the
              businesses they own (owner role with balance read) into one feed. Requires
              user_id to be the authenticated user; cannot be combined with account_id or the
              settlement-date filters. Each returned row includes the owning `account`.

          include_resource: Whether to include the `resource` field in the response or not. Consider passing
              `false` if you need a fast response without as many rich details.

          limit: Maximum number of rows to return.

          line_types: Optional ledger line categories to include. Some categories (for example
              `onchain_deposit`, which covers inbound crypto deposits such as MoonPay onramps)
              are only returned when explicitly requested here.

          posted_after: Only include rows posted after this ISO 8601 timestamp.

          posted_before: Only include rows posted before this ISO 8601 timestamp.

          user_id: The owning user ID (a user\\__ identifier). Provide this or account_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/financial-activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "available_after": available_after,
                        "available_before": available_before,
                        "currency": currency,
                        "cursor": cursor,
                        "include_owned_accounts": include_owned_accounts,
                        "include_resource": include_resource,
                        "limit": limit,
                        "line_types": line_types,
                        "posted_after": posted_after,
                        "posted_before": posted_before,
                        "user_id": user_id,
                    },
                    financial_activity_list_params.FinancialActivityListParams,
                ),
            ),
            cast_to=FinancialActivityListResponse,
        )


class FinancialActivityResourceWithRawResponse:
    def __init__(self, financial_activity: FinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = to_raw_response_wrapper(
            financial_activity.list,
        )


class AsyncFinancialActivityResourceWithRawResponse:
    def __init__(self, financial_activity: AsyncFinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = async_to_raw_response_wrapper(
            financial_activity.list,
        )


class FinancialActivityResourceWithStreamingResponse:
    def __init__(self, financial_activity: FinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = to_streamed_response_wrapper(
            financial_activity.list,
        )


class AsyncFinancialActivityResourceWithStreamingResponse:
    def __init__(self, financial_activity: AsyncFinancialActivityResource) -> None:
        self._financial_activity = financial_activity

        self.list = async_to_streamed_response_wrapper(
            financial_activity.list,
        )
