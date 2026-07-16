# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .account_social_link import AccountSocialLink

__all__ = ["Account", "Balance", "Capabilities", "RecommendedAction", "RequiredAction", "Wallet"]


class Balance(BaseModel):
    """Account holdings, each with USD value. Empty when `total_usd` is `null`."""

    balance: str
    """Total amount held in native units, as a decimal string."""

    breakdown: object
    """
    Balance split into available, pending, and reserve amounts, as native-unit
    decimal strings. On-chain crypto is entirely available; good_funds and fiat cash
    can have pending or reserve portions.
    """

    icon_url: Optional[str] = None
    """Holding icon URL."""

    name: str
    """The holding's display name"""

    price_usd: Optional[float] = None
    """USD price per unit, or `null` when no exchange rate is available."""

    symbol: str
    """Holding display symbol, such as `USDT`, `cbBTC`, or `EUR`."""

    value_usd: Optional[str] = None
    """Holding USD value, or `null` when no exchange rate is available."""


class Capabilities(BaseModel):
    """
    Payment rails enabled for this account, each `active`, `inactive`, or `pending` (onboarding or review in progress). Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    accept_bank_payments: Literal["active", "inactive", "pending"]
    """Bank payins: debits, transfers, and local bank rails"""

    accept_bnpl_payments: Literal["active", "inactive", "pending"]
    """Buy-now-pay-later payins; requires approval"""

    accept_card_payments: Literal["active", "inactive", "pending"]
    """Card payins, including Apple Pay and Google Pay"""

    bank_deposit: Literal["active", "inactive", "pending"]
    """Deposits by bank wire or ACH to the account's virtual bank account"""

    card_deposit: Literal["active", "inactive", "pending"]
    """Balance top-ups by charging a stored payment method"""

    card_issuing: Literal["active", "inactive", "pending"]
    """Issuing Whop cards; requires card application approval"""

    crypto_deposit: Literal["active", "inactive", "pending"]
    """On-chain deposits to the account's crypto wallet"""

    crypto_payout: Literal["active", "inactive", "pending"]
    """On-chain payouts to a crypto wallet"""

    instant_payout: Literal["active", "inactive", "pending"]
    """Instant payouts to an eligible payout destination"""

    standard_payout: Literal["active", "inactive", "pending"]
    """Standard payouts to an external payout destination"""

    transfer: Literal["active", "inactive", "pending"]
    """Transfers to other accounts"""


class RecommendedAction(BaseModel):
    """
    Deprecated: use the `GET /accounts/{account_id}/recommend_actions` endpoint instead. Optional actions that unlock capabilities or grow the account, same shape as `required_actions`. Computed only on `retrieve` and `me`; `null` otherwise.
    """

    action: Literal[
        "theme_business",
        "create_product",
        "create_plan",
        "verify_identity",
        "connect_affiliate_program",
        "create_promotion",
        "setup_tracking_pixel",
        "migrate_from_stripe",
        "accept_first_payment",
        "launch_first_ad",
        "launch_draft_campaign",
        "increase_ad_budget",
        "refresh_ad_creatives",
        "fix_ad_billing",
        "exclude_customers_from_ads",
        "retarget_abandoned_checkouts",
        "invite_team_member",
        "enable_tax_collection",
        "create_card",
        "join_whop_university",
        "apply_for_financing",
    ]
    """
    The recommendation; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: str
    """The URL the call-to-action links to"""

    cta_label: str
    """Button label"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """Illustration icon URL, or `null`"""

    impact_score: Optional[int] = None
    """Estimated impact from 0-100, or `null` when not ranked"""

    reasoning: Optional[str] = None
    """Why this action was recommended, or `null`"""

    status: Literal["optional"]
    """Always optional — never blocking"""

    title: str
    """Headline for the recommendation"""


class RequiredAction(BaseModel):
    """
    Actions the account owner must take to unblock capabilities like payouts and card spend, ordered by display priority. Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    action: Literal["deposit_funds", "submit_information_request", "verify_identity", "connect_fulfillment_tracker"]
    """
    What the holder must do; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: Optional[str] = None
    """The URL the call-to-action links to, or null when there is no button"""

    cta_label: str
    """Button label, or empty when there is no button"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """The URL of the action's illustration icon, or null if it has none"""

    status: Literal["required", "pending"]
    """required (act now) or pending (under review)"""

    title: str
    """Headline for the action"""


class Wallet(BaseModel):
    """Account primary crypto wallet, or `null` if none has been provisioned."""

    id: str
    """Wallet ID, prefixed `wallet_`."""

    address: str
    """The on-chain address of the wallet"""

    network: Literal["solana", "ethereum", "bitcoin"]
    """The blockchain network the wallet lives on"""


class Account(BaseModel):
    id: str
    """Account ID, prefixed `biz_`."""

    balances: List[Balance]

    banner_image_url: Optional[str] = None
    """Account banner image URL."""

    business_address: Optional[object] = None
    """
    Account business address used to calculate tax, with `line1`, `line2`, `city`,
    `state`, `postal_code`, and `country`. `null` when no address is set.
    """

    business_type: Optional[str] = None
    """High-level business category for the account."""

    capabilities: Optional[Capabilities] = None
    """
    Payment rails enabled for this account, each `active`, `inactive`, or `pending`
    (onboarding or review in progress). Computed only on `retrieve` and `me` for
    callers with `company:balance:read` scope; `null` otherwise.
    """

    country: Optional[str] = None
    """Country where the account is located."""

    created_at: str
    """When the account was created, as an ISO 8601 timestamp."""

    description: Optional[str] = None
    """Account promotional description."""

    email: Optional[str] = None
    """Account owner email address."""

    home_preferences: List[str]

    industry_group: Optional[str] = None
    """Account industry group."""

    industry_type: Optional[str] = None
    """Specific industry vertical for the account."""

    invoice_prefix: Optional[str] = None
    """Prefix used for account invoices."""

    logo_url: Optional[str] = None
    """Account logo image URL."""

    metadata: object
    """Arbitrary key/value metadata supplied at account creation."""

    onboarding_type: Optional[str] = None
    """Type of onboarding the account has completed."""

    opengraph_image_url: Optional[str] = None
    """Account Open Graph image URL."""

    opengraph_image_variant: Optional[str] = None
    """Account Open Graph image variant."""

    other_business_description: Optional[str] = None
    """Business type details when business_type is `other`."""

    other_industry_description: Optional[str] = None
    """Industry details when industry_type is `other`."""

    parent_account_id: Optional[str] = None
    """Parent account ID for connected accounts."""

    product_tax_code: Optional[object] = None
    """
    Tax classification code applied by default to the account's products, with `id`,
    `name`, and `product_type`. `null` when no default is set.
    """

    recommended_actions: Optional[List[RecommendedAction]] = None
    """
    DEPRECATED: Use the `GET /accounts/{account_id}/recommend_actions` endpoint
    instead.
    """

    require_2fa: bool
    """Whether authorized users must enable two-factor authentication."""

    required_actions: Optional[List[RequiredAction]] = None

    route: str
    """Account public route identifier."""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account."""

    show_joined_whops: bool
    """Whether the account appears in joined whops on other accounts."""

    show_reviews_dtc: bool
    """Whether reviews are displayed on direct-to-consumer product pages."""

    show_user_directory: bool
    """Whether the account shows users in the user directory."""

    social_links: List[AccountSocialLink]

    status: Optional[str] = None
    """Whether the account can operate on Whop: `active` or `suspended`.

    Computed only on `retrieve` and `me`; `null` otherwise.
    """

    store_page_config: object
    """Account store page display configuration."""

    target_audience: Optional[str] = None
    """Target audience for this account."""

    tax_collection_enabled_states: List[str]

    tax_identifiers: List[object]
    """Account tax/VAT registrations, each with `id`, `tax_id_type`, and
    `tax_id_value`.

    Empty when none are set.
    """

    tax_remitted_by: Optional[str] = None
    """
    Who calculates and remits tax for the account: `whop` (Whop calculates and
    remits), `self` (Whop calculates; the account collects and remits), or `none`
    (neither; the account is responsible). `null` until the account enrolls in the
    Whop tax service.
    """

    title: str
    """Account display name."""

    total_earned_usd: Optional[float] = None
    """Account lifetime sales, normalized to USD.

    Computed only on `retrieve` and `me` for callers with `stats:read` scope; `null`
    otherwise.
    """

    total_usd: Optional[str] = None
    """Total USD value across balances with known exchange rates.

    Computed only on single-account reads (`retrieve` and `me`); `null` on list
    responses, writes, missing balance-read permission, or unavailable balance
    source.
    """

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image."""

    verification: object
    """
    Account identity verification status for the `individual` (KYC) and `business`
    (KYB) profiles. Each is `null` until created, otherwise a `status` of
    `not_started`, `pending`, `approved`, or `rejected`.
    """

    wallet: Optional[Wallet] = None
    """Account primary crypto wallet, or `null` if none has been provisioned."""
