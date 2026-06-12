# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .account_wallet import AccountWallet
from .account_social_link import AccountSocialLink

__all__ = ["Account", "Balance"]


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


class Account(BaseModel):
    id: str
    """The ID of the account, which will look like biz\\__******\\********"""

    balances: List[Balance]

    banner_image_url: Optional[str] = None
    """The URL of the account banner image"""

    business_type: Optional[str] = None
    """The high-level business category for the account"""

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

    require_2fa: bool
    """
    Whether the account requires authorized users to have two-factor authentication
    enabled
    """

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

    store_page_config: object
    """Store page display configuration for the account"""

    target_audience: Optional[str] = None
    """The target audience for this account"""

    title: str
    """The display name of the account"""

    total_usd: Optional[str] = None
    """Total USD value across all balances with a known exchange rate.

    Only computed on single-account reads (retrieve and me); null (with an empty
    balances array) on list responses, on writes, when the caller's token lacks the
    balance-read permission, and when the balance source is unavailable
    """

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image"""

    wallet: Optional[AccountWallet] = None
    """The account's primary crypto wallet, or null if none has been provisioned"""
