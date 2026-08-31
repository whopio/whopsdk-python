# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DepositSucceededWebhookEvent",
    "Data",
    "DataCurrency",
    "DataResource",
    "DataResourceUnionMember0",
    "DataResourceUnionMember1",
    "DataResourceUnionMember2",
    "DataResourceUnionMember3",
    "DataResourceUnionMember3Owner",
    "DataResourceUnionMember3OwnerUnionMember0",
    "DataResourceUnionMember3OwnerUnionMember1",
    "DataResourceUnionMember4",
    "DataResourceUnionMember4Bank",
    "DataResourceUnionMember4Card",
    "DataResourceUnionMember5",
    "DataResourceUnionMember6",
    "DataSource",
    "DataSourcePaymentAmount",
    "DataSourcePayoutDestination",
    "DataAccount",
    "DataAccountUnionMember0",
    "DataAccountUnionMember1",
    "DataPayment",
    "DataPaymentAmount",
    "DataPaymentPlan",
    "DataPaymentProduct",
    "DataPaymentUser",
]


class DataCurrency(BaseModel):
    """Currency for this ledger activity."""

    code: str
    """Currency code."""

    precision: str
    """Precision factor for the currency, for example `100000000` for USD."""


class DataResourceUnionMember0(BaseModel):
    id: str
    """Account ID."""

    logo_url: Optional[str] = None
    """Account logo URL."""

    object: Literal["account"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class DataResourceUnionMember1(BaseModel):
    id: str
    """User ID."""

    name: Optional[str] = None
    """User display name."""

    object: Literal["user"]

    profile_picture_url: Optional[str] = None
    """User profile image URL."""

    username: Optional[str] = None
    """User's username."""


class DataResourceUnionMember2(BaseModel):
    id: str
    """Bounty ID."""

    object: Literal["bounty"]

    status: str
    """Bounty lifecycle status."""

    title: str
    """Bounty title."""


class DataResourceUnionMember3OwnerUnionMember0(BaseModel):
    id: str
    """Account ID."""

    logo_url: Optional[str] = None
    """Account logo URL."""

    object: Literal["account"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class DataResourceUnionMember3OwnerUnionMember1(BaseModel):
    id: str
    """User ID."""

    name: Optional[str] = None
    """User display name."""

    object: Literal["user"]

    profile_picture_url: Optional[str] = None
    """User profile image URL."""

    username: Optional[str] = None
    """User's username."""


DataResourceUnionMember3Owner: TypeAlias = Union[
    DataResourceUnionMember3OwnerUnionMember0, DataResourceUnionMember3OwnerUnionMember1, None
]


class DataResourceUnionMember3(BaseModel):
    id: str
    """Ledger account ID."""

    object: Literal["ledger_account"]

    owner: Optional[DataResourceUnionMember3Owner] = None


class DataResourceUnionMember4Bank(BaseModel):
    account_name: Optional[str] = None
    """Bank account holder name."""

    account_type: Optional[str] = None
    """Bank account type."""

    bank_name: Optional[str] = None
    """Bank name."""

    last4: Optional[str] = None
    """Last four digits of the bank account."""


class DataResourceUnionMember4Card(BaseModel):
    brand: Optional[str] = None
    """Card brand."""

    exp_month: Optional[int] = None
    """Card expiration month."""

    exp_year: Optional[int] = None
    """Card expiration year."""

    last4: Optional[str] = None
    """Last four digits of the card."""


class DataResourceUnionMember4(BaseModel):
    id: str
    """Payment method ID."""

    bank: Optional[DataResourceUnionMember4Bank] = None

    card: Optional[DataResourceUnionMember4Card] = None

    email_identifier: Optional[str] = None
    """Email identifier for email-based payment methods."""

    gateway_type: Optional[str] = None
    """Payment gateway type."""

    object: Literal["payment_method"]

    payment_method_type: Optional[str] = None
    """Payment method type."""


class DataResourceUnionMember5(BaseModel):
    id: str
    """Payout method ID."""

    account_reference: Optional[str] = None
    """Masked account reference."""

    destination_currency_code: Optional[str] = None
    """Destination currency code."""

    institution_name: Optional[str] = None
    """Payout institution name."""

    nickname: Optional[str] = None
    """Payout method nickname."""

    object: Literal["payout_method"]

    provider: Optional[str] = None
    """Payout provider."""


class DataResourceUnionMember6(BaseModel):
    id: str
    """Card transaction ID."""

    authorized_at: Optional[datetime] = None
    """ISO 8601 timestamp the transaction was authorized."""

    card_id: Optional[str] = None
    """Identifier of the card that the transaction was charged to."""

    cashback_usd: Optional[str] = None
    """Cashback earned on this transaction as a USD decimal string.

    Zero for declined or ineligible transactions; null when cashback has not been
    computed yet.
    """

    declined_reason: Optional[str] = None
    """Reason the transaction was declined (when status is declined)."""

    local_amount: Optional[str] = None
    """Amount the merchant charged in their local currency, as a decimal string.

    Pair with local_currency.
    """

    local_currency: Optional[str] = None
    """ISO 4217 currency code of the merchant-charged amount in local_amount."""

    merchant_category: Optional[str] = None
    """Merchant category."""

    merchant_icon_url: Optional[str] = None
    """Merchant icon URL."""

    merchant_name: Optional[str] = None
    """Merchant display name."""

    object: Literal["card_transaction"]

    posted_at: Optional[datetime] = None
    """ISO 8601 timestamp the transaction was settled by the card network."""

    status: Optional[str] = None
    """Current card transaction status."""

    usd_amount: Optional[str] = None
    """The processor-settled USD amount as a decimal string.

    The ledger's USDT leg is posted 1:1 from this value.
    """


DataResource: TypeAlias = Union[
    DataResourceUnionMember0,
    DataResourceUnionMember1,
    DataResourceUnionMember2,
    DataResourceUnionMember3,
    DataResourceUnionMember4,
    DataResourceUnionMember5,
    DataResourceUnionMember6,
    None,
]


class DataSourcePaymentAmount(BaseModel):
    """Total charged by the payment source."""

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


class DataSourcePayoutDestination(BaseModel):
    """Payout destination display info (payout sources only)."""

    icon_url: Optional[str] = None

    payer_name: Optional[str] = None


class DataSource(BaseModel):
    """Source of this ledger activity."""

    id: str

    object: str

    amount_float: Optional[float] = None
    """
    Payout amount as a decimal number in the destination currency (payout sources
    only; requires payout:withdrawal:read).
    """

    card_brand: Optional[str] = None
    """Card brand used by the payment source."""

    chain: Optional[str] = None
    """
    Chain the deposit landed on, for example plasma (onchain_transaction sources
    only).
    """

    claim_url: Optional[str] = None
    """Public claim URL for the airdrop link (airdrop_link sources only)."""

    created_at: Optional[datetime] = None
    """
    Payout creation time as an ISO 8601 timestamp (payout sources only; requires
    payout:withdrawal:read).
    """

    estimated_arrival: Optional[datetime] = None
    """
    Estimated arrival as an ISO 8601 timestamp (payout sources only; requires
    payout:withdrawal:read).
    """

    from_amount: Optional[str] = None
    """Amount converted out of from_currency as a decimal string (swap sources only)."""

    from_currency: Optional[str] = None
    """Lowercase currency code converted from (swap sources only)."""

    payer_name: Optional[str] = None
    """
    Name of the entity processing the payout (payout sources only; requires
    payout:withdrawal:read).
    """

    payment_amount: Optional[DataSourcePaymentAmount] = None
    """Total charged by the payment source."""

    payment_method_type: Optional[str] = None
    """Payment method used by the payment source."""

    payment_processor: Optional[str] = None
    """Processor used by the payment source."""

    payout_destination: Optional[DataSourcePayoutDestination] = None
    """Payout destination display info (payout sources only)."""

    payout_token_nickname: Optional[str] = None
    """Saved payout destination nickname (payout sources only)."""

    reason: Optional[str] = None
    """Why the activity happened.

    On transfer sources this is the transfer reason, for example pool_top_up or
    bounty_return. On payout sources it explains why the payout was canceled,
    denied, or failed (requires payout:withdrawal:read); null while the payout is
    progressing normally.
    """

    risk_review_hold: Optional[bool] = None
    """
    Whether this payout is currently held for manual risk review (payout sources
    only; requires payout:withdrawal:read).
    """

    sender_address: Optional[str] = None
    """
    Sender wallet address or onramp provider identifier (onchain_transaction sources
    only).
    """

    status: Optional[str] = None
    """Lifecycle status.

    On payout sources this is the payout status (requires payout:withdrawal:read);
    on airdrop_link sources it is the claim-link status (ungated); on payment and
    top-up sources it is the friendly payment status such as
    succeeded/pending/failed (ungated).
    """

    to_amount: Optional[str] = None
    """Amount received in to_currency as a decimal string (swap sources only)."""

    to_currency: Optional[str] = None
    """Lowercase currency code converted to (swap sources only)."""

    tx_hash: Optional[str] = None
    """On-chain transaction hash (onchain_transaction and swap sources only)."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]


class DataAccountUnionMember0(BaseModel):
    id: str
    """Account ID."""

    logo_url: Optional[str] = None
    """Account logo URL."""

    object: Literal["account"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class DataAccountUnionMember1(BaseModel):
    id: str
    """User ID."""

    name: Optional[str] = None
    """User display name."""

    object: Literal["user"]

    profile_picture_url: Optional[str] = None
    """User profile image URL."""

    username: Optional[str] = None
    """User's username."""


DataAccount: TypeAlias = Union[DataAccountUnionMember0, DataAccountUnionMember1]


class DataPaymentAmount(BaseModel):
    """Total charged by the payment."""

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


class DataPaymentPlan(BaseModel):
    """Plan associated with the payment, when applicable."""

    id: str
    """Plan ID, prefixed `plan_`."""

    name: Optional[str] = None
    """Plan name."""


class DataPaymentProduct(BaseModel):
    """Product associated with the payment, when applicable."""

    id: str
    """Product ID, prefixed `prod_`."""

    name: str
    """Product name."""


class DataPaymentUser(BaseModel):
    """Customer associated with the payment. Email requires member:email:read."""

    id: str
    """Customer ID, prefixed `user_`."""

    email: Optional[str] = None
    """Customer email, or null without member:email:read."""

    name: str
    """Customer display name."""


class DataPayment(BaseModel):
    """Payment related to this ledger activity.

    Included when rich resource hydration is enabled and the movement is tied to a payment.
    """

    id: str
    """Payment ID, prefixed `pay_`."""

    amount: Optional[DataPaymentAmount] = None
    """Total charged by the payment."""

    card_brand: Optional[str] = None
    """Card brand, when the customer paid by card."""

    card_last4: Optional[str] = None
    """Last four digits of the card, when the customer paid by card."""

    created_at: datetime
    """When the payment was created."""

    object: Literal["payment"]

    payment_method_type: Optional[str] = None
    """How the customer paid, such as `card` or `paypal`."""

    payment_processor: Optional[str] = None
    """Processor that handled the payment, such as `stripe`."""

    plan: Optional[DataPaymentPlan] = None
    """Plan associated with the payment, when applicable."""

    product: Optional[DataPaymentProduct] = None
    """Product associated with the payment, when applicable."""

    user: Optional[DataPaymentUser] = None
    """Customer associated with the payment. Email requires member:email:read."""


class Data(BaseModel):
    id: str
    """Ledger activity ID."""

    amount: str
    """Signed amount in the currency's smallest precision units."""

    available_at: Optional[datetime] = None
    """
    ISO 8601 timestamp these funds became (or are scheduled to become) withdrawable:
    the posted time for already-settled funds, or 00:00:00 UTC on the scheduled
    release date for pending funds. Present only on inflows entering the balance
    (payments, top-ups, incoming transfers/affiliate); null on payouts, refunds,
    disputes and on-chain rows. The available_after/before filters window on its UTC
    settlement date.
    """

    currency: DataCurrency
    """Currency for this ledger activity."""

    line_type: Literal[
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
        "balance_reservation",
        "balance_reservation_reversal",
        "bank_transfer",
        "billing_percentage_fee",
        "buyer_fee",
        "card_interchange",
        "card_load_deposit",
        "card_load_transfer",
        "card_spend_authorization",
        "card_spend_authorization_void",
        "card_spend_refund",
        "card_unload_deposit",
        "card_unload_transfer",
        "company_referral",
        "connected_account_negative_balance",
        "cross_border_percentage_fee",
        "currency_conversion_incoming",
        "currency_conversion_outgoing",
        "dispute_alert_fee",
        "dispute_hold_adjustment",
        "dispute_representment_fee",
        "external_card_load_deposit",
        "fraud_prevention_fee",
        "fx_percentage_fee",
        "high_risk_merchant_fee",
        "installment_default",
        "internal_balance_transfer_incoming",
        "internal_balance_transfer_outgoing",
        "internal_withdrawal",
        "internal_withdrawal_complete",
        "internal_withdrawal_fee",
        "internal_withdrawal_fee_reversal",
        "internal_withdrawal_in_transit",
        "internal_withdrawal_in_transit_reversal",
        "internal_withdrawal_markup_fee",
        "internal_withdrawal_markup_fee_payout",
        "internal_withdrawal_markup_fee_payout_reversal",
        "internal_withdrawal_markup_fee_reversal",
        "internal_withdrawal_reversal",
        "legacy_crypto_payment",
        "legacy_payment",
        "legacy_payment_refund",
        "license_sale",
        "license_sale_commission",
        "license_sale_revenue",
        "marketplace_affiliate_fee",
        "misc_purchase",
        "misc_refund",
        "misc_reversal",
        "onchain_deposit",
        "onchain_swap_source",
        "onchain_swap_target",
        "onchain_wallet_transfer_incoming",
        "onchain_wallet_transfer_outgoing",
        "onchain_withdrawal",
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
        "payment_referral_refund",
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
        "platform_balance_transfer_fee",
        "platform_balance_transfer_incoming",
        "platform_balance_transfer_outgoing",
        "platform_covered_dispute",
        "platform_earning",
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
        "swap_fee",
        "three_ds_fixed_fee",
        "topup",
        "topup_fee",
        "topup_reversal",
        "treasury_payin",
        "whop_processing_fee",
        "withdrawal",
        "withdrawal_clawback",
        "withdrawal_clawback_reversal",
        "withdrawal_fee",
        "withdrawal_fee_reversal",
        "withdrawal_markup_fee",
        "withdrawal_markup_fee_payout",
        "withdrawal_markup_fee_payout_reversal",
        "withdrawal_markup_fee_reversal",
        "withdrawal_reclassification",
        "withdrawal_reversal",
        "withdrawal_topup_adjustment",
    ]
    """The ledger line category this activity was posted under."""

    object: Literal["ledger_activity"]

    posted_at: datetime
    """When the activity posted to the ledger."""

    resource: Optional[DataResource] = None
    """Resource associated with this ledger activity."""

    source: Optional[DataSource] = None
    """Source of this ledger activity."""

    account: Optional[DataAccount] = None
    """The viewer account that owns this row's ledger.

    Present only when the response aggregates owned accounts
    (include_owned_accounts=true); omitted otherwise.
    """

    ledger_account_id: Optional[str] = None
    """The ledger account (a ldgr\\__ identifier) this row belongs to.

    Present only when the response aggregates owned accounts
    (include_owned_accounts=true); omitted otherwise. Pair it with `account` to
    scope drawers and dashboard links to the owning business.
    """

    payment: Optional[DataPayment] = None
    """Payment related to this ledger activity.

    Included when rich resource hydration is enabled and the movement is tied to a
    payment.
    """

    payment_id: Optional[str] = None
    """Payment ID for any payment-related activity, including refunds and disputes."""

    plan_id: Optional[str] = None
    """ID of the plan associated with the payment, when applicable."""

    plan_name: Optional[str] = None
    """Name of the plan associated with the payment, when applicable."""

    product_id: Optional[str] = None
    """ID of the product associated with the payment, when applicable."""

    product_name: Optional[str] = None
    """Name of the product associated with the payment, when applicable."""

    user_email: Optional[str] = None
    """Email of the customer associated with the payment. Requires member:email:read."""

    user_id: Optional[str] = None
    """ID of the customer associated with the payment."""

    user_name: Optional[str] = None
    """Display name of the customer associated with the payment."""


class DepositSucceededWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["deposit.succeeded"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
