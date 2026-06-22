# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .account_social_link import AccountSocialLink

__all__ = ["Account", "Balance", "Capabilities", "RecommendedAction", "RequiredAction", "Wallet"]


class Balance(BaseModel):
    """The account's holdings (crypto and fiat), each with its USD value.

    Empty when total_usd is null (not computed)
    """

    balance: str
    """The total amount held in native units, as a decimal string"""

    breakdown: object
    """
    The holding split into available, pending, and reserve amounts (native-unit
    decimal strings). On-chain crypto is entirely available; good_funds and fiat
    cash can have pending/reserve portions
    """

    icon_url: Optional[str] = None
    """The URL of the holding's icon, when available"""

    name: str
    """The holding's display name"""

    price_usd: Optional[float] = None
    """The USD price per unit, or null when no exchange rate is available"""

    symbol: str
    """The holding's display symbol, e.g. USDT, cbBTC, or EUR"""

    value_usd: Optional[str] = None
    """The total USD value of the holding, or null when no exchange rate is available"""


class Capabilities(BaseModel):
    """
    Each payment rail's status: active, inactive, or pending (pending means onboarding or review is in progress)
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
    Optional actions that unlock capabilities or grow the account, same shape as required_actions
    """

    action: Literal["apply_for_financing", "migrate_from_stripe", "accept_first_payment", "join_whop_university"]
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
    """Illustration icon URL, or null"""

    status: Literal["optional"]
    """Always optional — never blocking"""

    title: str
    """Headline for the recommendation"""


class RequiredAction(BaseModel):
    """
    Actions the account owner must take to unblock capabilities like payouts and card spend, ordered by display priority
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
    """The account's primary crypto wallet, or null if none has been provisioned"""

    id: str
    """The ID of the wallet, which will look like wallet\\__******\\********"""

    address: str
    """The on-chain address of the wallet"""

    network: Literal["solana", "ethereum", "bitcoin"]
    """The blockchain network the wallet lives on"""


class Account(BaseModel):
    id: str
    """The ID of the account, which will look like biz\\__******\\********"""

    balances: List[Balance]

    banner_image_url: Optional[str] = None
    """The URL of the account banner image"""

    business_type: Optional[str] = None
    """The high-level business category for the account"""

    capabilities: Optional[Capabilities] = None
    """
    Each payment rail's status: active, inactive, or pending (pending means
    onboarding or review is in progress)
    """

    country: Optional[str] = None
    """The country the account is located in"""

    created_at: str
    """When the account was created, as an ISO 8601 timestamp"""

    description: Optional[str] = None
    """A promotional description for the account"""

    email: Optional[str] = None
    """The email address of the account owner"""

    home_preferences: List[str]

    industry_group: Optional[str] = None
    """The industry group the account belongs to"""

    industry_type: Optional[str] = None
    """The specific industry vertical the account operates in"""

    invoice_prefix: Optional[str] = None
    """The prefix used for account invoices"""

    logo_url: Optional[str] = None
    """The URL of the account logo image"""

    metadata: object
    """Arbitrary key/value metadata supplied when the account was created"""

    onboarding_type: Optional[str] = None
    """The type of onboarding the account has completed"""

    opengraph_image_url: Optional[str] = None
    """The URL of the account Open Graph image"""

    opengraph_image_variant: Optional[str] = None
    """The account Open Graph image variant"""

    other_business_description: Optional[str] = None
    """The description of the business type when business_type is other"""

    other_industry_description: Optional[str] = None
    """The description of the industry type when industry_type is other"""

    parent_account_id: Optional[str] = None
    """The parent account ID for connected accounts"""

    recommended_actions: Optional[List[RecommendedAction]] = None

    require_2fa: bool
    """
    Whether the account requires authorized users to have two-factor authentication
    enabled
    """

    required_actions: Optional[List[RequiredAction]] = None

    route: str
    """The account's public route identifier"""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account"""

    show_joined_whops: bool
    """Whether the account appears in joined whops on other accounts"""

    show_reviews_dtc: bool
    """Whether reviews are displayed on direct-to-consumer product pages"""

    show_user_directory: bool
    """Whether the account shows users in the user directory"""

    social_links: List[AccountSocialLink]

    status: Optional[str] = None
    """Whether the account can operate on Whop — active or suspended"""

    store_page_config: object
    """Store page display configuration for the account"""

    target_audience: Optional[str] = None
    """The target audience for this account"""

    title: str
    """The display name of the account"""

    total_earned_usd: Optional[float] = None
    """Lifetime sales for the account, normalized to USD"""

    total_usd: Optional[str] = None
    """Total USD value across all balances with a known exchange rate.

    Only computed on single-account reads (retrieve and me); null (with an empty
    balances array) on list responses, on writes, when the caller's token lacks the
    balance-read permission, and when the balance source is unavailable
    """

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image"""

    verification: object
    """The account's identity-verification status.

    `individual` is KYC, `business` is KYB; each is null when that profile has not
    been created, otherwise { status } where status is one of not_started, pending,
    approved, rejected
    """

    wallet: Optional[Wallet] = None
    """The account's primary crypto wallet, or null if none has been provisioned"""
