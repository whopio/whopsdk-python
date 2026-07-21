# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .account_social_link import AccountSocialLink

__all__ = [
    "Account",
    "Balance",
    "Capabilities",
    "LlcFormation",
    "LlcFormationDocument",
    "LlcFormationSignatures",
    "LlcFormationSignaturesForm8821",
    "LlcFormationSignaturesSs4",
    "PaymentControls",
    "PaymentControlsDisputeAlertAutoRefund",
    "PaymentControlsReserve",
    "PaymentControlsResolutionCenterAutoRefund",
    "RecommendedAction",
    "RequiredAction",
    "Wallet",
]


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


class LlcFormationDocument(BaseModel):
    """
    Formation documents available for download, such as the Articles of Organization and the EIN confirmation letter. Present once `status` leaves `draft`.
    """

    id: str
    """Document ID, prefixed `file_`."""

    name: str
    """Human-readable document name, such as `Articles of Organization`."""

    type: str
    """
    Document category: `articles_of_organization`, `operating_agreement`,
    `ein_letter`, `signed_ss4`, `signed_form8821`, or `mail` for postal
    correspondence received on the company's behalf.
    """

    url: str
    """CDN URL for downloading the document."""


class LlcFormationSignaturesForm8821(BaseModel):
    """Signature state for IRS Form 8821, the tax information authorization.

    Present only while the form still needs the founder's action.
    """

    status: Literal["pending", "unknown"]
    """
    `pending` when a signing session is ready for the founder; `unknown` when the
    signature state could not be determined.
    """

    expires_at: Optional[str] = None
    """When the signing URL expires, as an ISO 8601 timestamp.

    Present while `status` is `pending`.
    """

    url: Optional[str] = None
    """Hosted signing URL where the founder completes the form.

    Present while `status` is `pending`.
    """


class LlcFormationSignaturesSs4(BaseModel):
    """Signature state for IRS Form SS-4, the EIN application.

    Present only while the form still needs the founder's action.
    """

    status: Literal["pending", "unknown"]
    """
    `pending` when a signing session is ready for the founder; `unknown` when the
    signature state could not be determined.
    """

    expires_at: Optional[str] = None
    """When the signing URL expires, as an ISO 8601 timestamp.

    Present while `status` is `pending`.
    """

    url: Optional[str] = None
    """Hosted signing URL where the founder completes the form.

    Present while `status` is `pending`.
    """


class LlcFormationSignatures(BaseModel):
    """IRS forms still awaiting a founder's signature, each with a hosted signing URL.

    Present once `status` leaves `draft`; empty when nothing needs signing.
    """

    form8821: Optional[LlcFormationSignaturesForm8821] = None
    """Signature state for IRS Form 8821, the tax information authorization.

    Present only while the form still needs the founder's action.
    """

    ss4: Optional[LlcFormationSignaturesSs4] = None
    """Signature state for IRS Form SS-4, the EIN application.

    Present only while the form still needs the founder's action.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class LlcFormation(BaseModel):
    """
    LLC formation state for the account, managed through [Register LLC](/api-reference/beta/accounts/register-llc). A `draft` `status` until the formation checkout is paid, then filing progress with downloadable documents and signatures awaiting action. Empty when the formation state is temporarily unavailable.
    """

    documents: Optional[List[LlcFormationDocument]] = None

    ein_registered: Optional[bool] = None
    """Whether the company's EIN has been issued by the IRS.

    Present once `status` leaves `draft`.
    """

    legal_name: Optional[str] = None
    """Registered company name including the entity ending, for example `Acme, LLC`.

    Present once `status` leaves `draft`.
    """

    signatures: Optional[LlcFormationSignatures] = None
    """IRS forms still awaiting a founder's signature, each with a hosted signing URL.

    Present once `status` leaves `draft`; empty when nothing needs signing.
    """

    state_registered: Optional[bool] = None
    """Whether the state formation filing is complete.

    Present once `status` leaves `draft`.
    """

    status: Optional[Literal["draft", "processing", "filed", "rejected", "completed"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class PaymentControlsDisputeAlertAutoRefund(BaseModel):
    """Automatic refund settings for pre-chargeback dispute alerts."""

    locked: bool
    """Whether the account owner is prevented from changing this threshold."""

    threshold_usd: Optional[float] = None
    """Maximum dispute alert amount automatically refunded in USD.

    `null` when automatic refunds are disabled.
    """


class PaymentControlsReserve(BaseModel):
    """Reserve currently applied to incoming payment volume."""

    hold_period_days: int
    """Number of days reserved funds are held before release."""

    percentage: Optional[float] = None
    """Percentage of incoming payment volume held in reserve.

    `null` when no reserve is applied.
    """


class PaymentControlsResolutionCenterAutoRefund(BaseModel):
    """Automatic refund settings for resolution center cases."""

    card_threshold_usd: Optional[float] = None
    """Maximum card-funded resolution center case amount automatically refunded in USD.

    `null` when automatic refunds are disabled for cards.
    """

    financing_threshold_usd: Optional[float] = None
    """
    Maximum financing-funded resolution center case amount automatically refunded in
    USD. `null` when automatic refunds are disabled for financing.
    """

    locked: bool
    """Whether the account owner is prevented from changing these thresholds."""

    paypal_threshold_usd: Optional[float] = None
    """
    Maximum PayPal-funded resolution center case amount automatically refunded in
    USD. `null` when automatic refunds are disabled for PayPal.
    """


class PaymentControls(BaseModel):
    """Payment health controls currently applied to the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    dispute_alert_auto_refund: PaymentControlsDisputeAlertAutoRefund
    """Automatic refund settings for pre-chargeback dispute alerts."""

    dispute_alert_fee_usd: Optional[float] = None
    """Fee charged for each dispute alert in USD. `null` when unavailable."""

    financing_disabled: bool
    """Whether payment health controls explicitly disable financing.

    This is independent of financing approval in
    `capabilities.accept_bnpl_payments`.
    """

    high_risk_processing_fee_percentage: float
    """Additional processing fee percentage for high-risk processing.

    Currently `0` for all accounts.
    """

    pending_balance_delay_days: int
    """Additional days payments remain pending before becoming available."""

    reserve: PaymentControlsReserve
    """Reserve currently applied to incoming payment volume."""

    resolution_center_auto_refund: PaymentControlsResolutionCenterAutoRefund
    """Automatic refund settings for resolution center cases."""


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

    action: Literal[
        "deposit_funds",
        "submit_information_request",
        "verify_identity",
        "connect_fulfillment_tracker",
        "setup_apple_pay_domains",
    ]
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

    llc_formation: LlcFormation
    """
    LLC formation state for the account, managed through
    [Register LLC](/api-reference/beta/accounts/register-llc). A `draft` `status`
    until the formation checkout is paid, then filing progress with downloadable
    documents and signatures awaiting action. Empty when the formation state is
    temporarily unavailable.
    """

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

    payment_controls: Optional[PaymentControls] = None
    """Payment health controls currently applied to the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read`
    scope; `null` otherwise.
    """

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
