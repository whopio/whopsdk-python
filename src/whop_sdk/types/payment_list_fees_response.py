# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["PaymentListFeesResponse"]


class PaymentListFeesResponse(BaseModel):
    """Represents a fee related to a payment"""

    amount: float
    """The value or amount to display for the fee."""

    currency: Currency
    """The currency of the fee."""

    name: str
    """The label to display for the fee."""

    type: Literal[
        "stripe_domestic_processing_fee",
        "stripe_international_processing_fee",
        "stripe_fixed_processing_fee",
        "stripe_billing_fee",
        "stripe_radar_fee",
        "sales_tax_remittance",
        "sales_tax_remittance_reversal",
        "stripe_sales_tax_fee",
        "whop_processing_fee",
        "marketplace_affiliate_fee",
        "affiliate_fee",
        "crypto_fee",
        "stripe_standard_processing_fee",
        "paypal_fee",
        "stripe_payout_fee",
        "dispute_fee",
        "dispute_alert_fee",
        "apple_processing_fee",
        "buyer_fee",
        "sezzle_processing_fee",
        "splitit_processing_fee",
        "platform_balance_processing_fee",
        "payment_processing_percentage_fee",
        "payment_processing_fixed_fee",
        "cross_border_percentage_fee",
        "fx_percentage_fee",
        "orchestration_percentage_fee",
        "three_ds_fixed_fee",
        "billing_percentage_fee",
        "revshare_percentage_fee",
        "application_fee",
    ]
    """The specific origin of the fee, if applicable."""
