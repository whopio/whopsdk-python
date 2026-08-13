# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FinancialActivityListParams"]


class FinancialActivityListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    available_after: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Only include rows whose funds became withdrawable on or after this `YYYY-MM-DD`
    settlement date (UTC), distinct from posted_at. Requires currency.
    """

    available_before: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Only include rows whose funds became withdrawable on or before this `YYYY-MM-DD`
    settlement date (UTC). Set equal to available_after for a single day. Requires
    currency.
    """

    currency: str
    """Optional currency code filter, for example `usd`."""

    cursor: str
    """Cursor returned by the previous page."""

    include_owned_accounts: bool
    """
    When true, aggregates the authenticated user's personal ledger with the
    businesses they own (owner role with balance read) into one feed. Requires
    user_id to be the authenticated user; cannot be combined with account_id or the
    settlement-date filters. Each returned row includes the owning `account`.
    """

    include_resource: bool
    """Whether to include the `resource` field in the response or not.

    Consider passing `false` if you need a fast response without as many rich
    details.
    """

    limit: int
    """Maximum number of rows to return."""

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
    """Optional ledger line categories to include.

    Some categories (for example `onchain_deposit`, which covers inbound crypto
    deposits such as MoonPay onramps) are only returned when explicitly requested
    here.
    """

    posted_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include rows posted after this ISO 8601 timestamp."""

    posted_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include rows posted before this ISO 8601 timestamp."""

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
