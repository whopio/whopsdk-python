# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentListFeesResponse", "Data", "DataAmount", "DataSettlementAmount", "PageInfo"]


class DataAmount(BaseModel):
    """The fee in the currency it was collected in."""

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class DataSettlementAmount(BaseModel):
    """
    The fee converted to the payment's settlement currency, so lines can be totalled against the payment.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


class Data(BaseModel):
    amount: DataAmount
    """The fee in the currency it was collected in."""

    collected_at: Optional[str] = None
    """
    When the fee was collected, as an ISO 8601 timestamp, or null when it has not
    been.
    """

    description: Optional[str] = None
    """A longer explanation of the fee, when there is one."""

    label: str
    """The name the dashboard shows for this fee."""

    origin: Literal[
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
        "dispute_representment_fee",
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
        "high_risk_merchant_fee",
    ]
    """
    The specific fee this line is, such as `payment_processing_percentage_fee` or
    `revshare_percentage_fee`.
    """

    settlement_amount: DataSettlementAmount
    """
    The fee converted to the payment's settlement currency, so lines can be totalled
    against the payment.
    """

    type: Literal["whop_fee", "processing_fee", "affiliate_program_fee", "other_fee"]
    """
    The family the fee belongs to: `whop_fee`, `processing_fee`,
    `affiliate_program_fee`, or `other_fee`.
    """


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class PaymentListFeesResponse(BaseModel):
    data: List[Data]

    page_info: PageInfo
