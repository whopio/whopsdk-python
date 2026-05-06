# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .card_brands import CardBrands
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "AdCampaignCreateResponse",
    "BillingLedgerAccount",
    "Config",
    "CreatedByUser",
    "PaymentMethod",
    "PaymentMethodBasePaymentMethod",
    "PaymentMethodCardPaymentMethod",
    "PaymentMethodCardPaymentMethodCard",
    "PaymentMethodUsBankAccountPaymentMethod",
    "PaymentMethodUsBankAccountPaymentMethodUsBankAccount",
    "PaymentMethodCashappPaymentMethod",
    "PaymentMethodCashappPaymentMethodCashapp",
    "PaymentMethodIdealPaymentMethod",
    "PaymentMethodIdealPaymentMethodIdeal",
    "PaymentMethodSepaDebitPaymentMethod",
    "PaymentMethodSepaDebitPaymentMethodSepaDebit",
    "Product",
]


class BillingLedgerAccount(BaseModel):
    """
    The ledger account being charged for platform balance billing (null if using card)
    """

    id: str
    """The unique identifier for the ledger account."""


class Config(BaseModel):
    """Meta campaign configuration (objective, budget, bidding, etc.).

    Null for non-Meta campaigns — use `tiktokConfig` for TikTok.
    """

    bid_amount: Optional[int] = None
    """Bid cap amount in cents. Only used when bid_strategy is bid_cap."""

    bid_strategy: Optional[Literal["lowest_cost", "bid_cap", "cost_cap"]] = None
    """The bidding strategy used to optimize spend for this campaign."""

    budget_optimization: Optional[bool] = None
    """
    Whether campaign budget optimization (CBO) is enabled, allowing the platform to
    distribute budget across ad groups.
    """

    end_time: Optional[str] = None
    """The scheduled end time of the campaign (ISO8601)."""

    objective: Optional[Literal["awareness", "traffic", "engagement", "leads", "sales"]] = None
    """The campaign objective that determines how Meta optimizes delivery."""

    special_categories: Optional[List[str]] = None
    """
    Special ad categories required by the platform (e.g., housing, employment,
    credit).
    """

    start_time: Optional[str] = None
    """The scheduled start time of the campaign (ISO8601)."""

    status: Optional[Literal["active", "paused"]] = None
    """The campaign status as set by the advertiser (active or paused)."""


class CreatedByUser(BaseModel):
    """The user who created the campaign"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class PaymentMethodBasePaymentMethod(BaseModel):
    """A saved payment method with no type-specific details available."""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["BasePaymentMethod"]
    """The typename of this object"""


class PaymentMethodCardPaymentMethodCard(BaseModel):
    """
    The card-specific details for this payment method, including brand, last four digits, and expiration.
    """

    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """The two-digit expiration month of the card (1-12). Null if not available."""

    exp_year: Optional[int] = None
    """The two-digit expiration year of the card (e.g., 27 for 2027).

    Null if not available.
    """

    last4: Optional[str] = None
    """The last four digits of the card number. Null if not available."""


class PaymentMethodCardPaymentMethod(BaseModel):
    """
    A saved card payment method, including brand, last four digits, and expiration details.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    card: PaymentMethodCardPaymentMethodCard
    """
    The card-specific details for this payment method, including brand, last four
    digits, and expiration.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["CardPaymentMethod"]
    """The typename of this object"""


class PaymentMethodUsBankAccountPaymentMethodUsBankAccount(BaseModel):
    """
    The bank account-specific details for this payment method, including bank name and last four digits.
    """

    account_type: str
    """The type of bank account (e.g., checking, savings)."""

    bank_name: str
    """The name of the financial institution holding the account."""

    last4: str
    """The last four digits of the bank account number."""


class PaymentMethodUsBankAccountPaymentMethod(BaseModel):
    """
    A saved US bank account payment method, including bank name, last four digits, and account type.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["UsBankAccountPaymentMethod"]
    """The typename of this object"""

    us_bank_account: PaymentMethodUsBankAccountPaymentMethodUsBankAccount
    """
    The bank account-specific details for this payment method, including bank name
    and last four digits.
    """


class PaymentMethodCashappPaymentMethodCashapp(BaseModel):
    """
    The Cash App-specific details for this payment method, including cashtag and buyer ID.
    """

    buyer_id: Optional[str] = None
    """The unique and immutable identifier assigned by Cash App to the buyer.

    Null if not available.
    """

    cashtag: Optional[str] = None
    """The public cashtag handle of the buyer on Cash App. Null if not available."""


class PaymentMethodCashappPaymentMethod(BaseModel):
    """
    A saved Cash App payment method, including the buyer's cashtag and unique identifier.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    cashapp: PaymentMethodCashappPaymentMethodCashapp
    """
    The Cash App-specific details for this payment method, including cashtag and
    buyer ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["CashappPaymentMethod"]
    """The typename of this object"""


class PaymentMethodIdealPaymentMethodIdeal(BaseModel):
    """
    The iDEAL-specific details for this payment method, including bank name and BIC.
    """

    bank: Optional[str] = None
    """The name of the customer's bank used for the iDEAL transaction.

    Null if not available.
    """

    bic: Optional[str] = None
    """The Bank Identifier Code (BIC/SWIFT) of the customer's bank.

    Null if not available.
    """


class PaymentMethodIdealPaymentMethod(BaseModel):
    """A saved iDEAL payment method, including the customer's bank name and BIC code."""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    ideal: PaymentMethodIdealPaymentMethodIdeal
    """
    The iDEAL-specific details for this payment method, including bank name and BIC.
    """

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["IdealPaymentMethod"]
    """The typename of this object"""


class PaymentMethodSepaDebitPaymentMethodSepaDebit(BaseModel):
    """
    The SEPA Direct Debit-specific details for this payment method, including bank code and last four IBAN digits.
    """

    bank_code: Optional[str] = None
    """The bank code of the financial institution associated with this SEPA account.

    Null if not available.
    """

    branch_code: Optional[str] = None
    """The branch code of the financial institution associated with this SEPA account.

    Null if not available.
    """

    country: Optional[str] = None
    """The two-letter ISO country code where the bank account is located.

    Null if not available.
    """

    last4: Optional[str] = None
    """The last four digits of the IBAN associated with this SEPA account.

    Null if not available.
    """


class PaymentMethodSepaDebitPaymentMethod(BaseModel):
    """
    A saved SEPA Direct Debit payment method, including the bank code, country, and last four IBAN digits.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    sepa_debit: PaymentMethodSepaDebitPaymentMethodSepaDebit
    """
    The SEPA Direct Debit-specific details for this payment method, including bank
    code and last four IBAN digits.
    """

    typename: Literal["SepaDebitPaymentMethod"]
    """The typename of this object"""


PaymentMethod: TypeAlias = Annotated[
    Union[
        Optional[PaymentMethodBasePaymentMethod],
        Optional[PaymentMethodCardPaymentMethod],
        Optional[PaymentMethodUsBankAccountPaymentMethod],
        Optional[PaymentMethodCashappPaymentMethod],
        Optional[PaymentMethodIdealPaymentMethod],
        Optional[PaymentMethodSepaDebitPaymentMethod],
    ],
    PropertyInfo(discriminator="typename"),
]


class Product(BaseModel):
    """The access pass being promoted.

    Null for campaigns that don't target a specific product.
    """

    id: str
    """The unique identifier for the product."""

    route: str
    """
    The URL slug used in the product's public link (e.g., 'my-product' in
    whop.com/company/my-product).
    """

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class AdCampaignCreateResponse(BaseModel):
    """An advertising campaign running on an external platform or within Whop."""

    id: str
    """The unique identifier for the ad campaign."""

    available_budget: float
    """
    Available budget in dollars, capped at daily budget minus today's spend for
    daily campaigns
    """

    billing_ledger_account: Optional[BillingLedgerAccount] = None
    """
    The ledger account being charged for platform balance billing (null if using
    card)
    """

    clicks_count: int
    """Number of clicks"""

    config: Optional[Config] = None
    """Meta campaign configuration (objective, budget, bidding, etc.).

    Null for non-Meta campaigns — use `tiktokConfig` for TikTok.
    """

    created_at: datetime
    """The datetime the ad campaign was created."""

    created_by_user: CreatedByUser
    """The user who created the campaign"""

    daily_budget: Optional[float] = None
    """
    Effective daily budget in dollars — sum of ad group budgets when set, otherwise
    campaign-level daily budget
    """

    impressions_count: int
    """Number of impressions (views)"""

    paused_until: Optional[datetime] = None
    """If temporarily paused, the timestamp when the campaign will auto-resume"""

    payment_method: PaymentMethod
    """The payment method used for daily billing (null if using platform balance)"""

    platform: Optional[Literal["meta", "tiktok"]] = None
    """The platforms where an ad campaign can run."""

    product: Optional[Product] = None
    """The access pass being promoted.

    Null for campaigns that don't target a specific product.
    """

    purchases_count: int
    """Number of purchases"""

    remaining_balance: float
    """Remaining balance in dollars"""

    return_on_ad_spend: float
    """Return on Ad Spend (ROAS) percentage - revenue generated divided by ad spend"""

    revenue: float
    """Total revenue generated from users who converted through this campaign"""

    status: Literal[
        "active",
        "paused",
        "inactive",
        "stale",
        "pending_refund",
        "payment_failed",
        "draft",
        "in_review",
        "flagged",
        "importing",
    ]
    """Current status of the campaign (active, paused, or inactive)"""

    target_country_codes: List[str]
    """Array of ISO3166 country codes for territory targeting"""

    title: str
    """The title of the ad campaign"""

    todays_spend: float
    """Amount spent today in dollars"""

    total_credits: float
    """Total credits added to the campaign in dollars"""

    total_spend: float
    """Total amount spent on conversions in dollars"""

    updated_at: datetime
    """The datetime the ad campaign was last updated."""
