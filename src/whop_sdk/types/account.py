# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .account_wallet import AccountWallet
from .account_social_link import AccountSocialLink

__all__ = ["Account", "Balance", "BalanceToken"]


class BalanceToken(BaseModel):
    """The account's per-token holdings"""

    balance: str
    """The token amount in native units, as a decimal string"""

    icon_url: Optional[str] = None
    """The URL of the token icon, when available"""

    name: str
    """The token's display name"""

    price_usd: Optional[float] = None
    """The USD price per token, or null when no exchange rate is available"""

    symbol: str
    """The token's display symbol, e.g. USDT or cbBTC"""

    token_address: Optional[str] = None
    """The token contract address, when the holding maps to a single contract"""

    value_usd: Optional[str] = None
    """The USD value of the holding, or null when no exchange rate is available"""


class Balance(BaseModel):
    """The account's balance by token.

    Only computed on single-account reads (retrieve and me); null on list responses, on writes, when the caller's token lacks the balance-read permission for the account, and when the balance source is unavailable
    """

    tokens: List[BalanceToken]

    total_usd: str
    """The total USD value across all tokens with a known exchange rate"""


class Account(BaseModel):
    id: str
    """The ID of the account, which will look like biz\\__******\\********"""

    balance: Optional[Balance] = None
    """The account's balance by token.

    Only computed on single-account reads (retrieve and me); null on list responses,
    on writes, when the caller's token lacks the balance-read permission for the
    account, and when the balance source is unavailable
    """

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

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image"""

    wallet: Optional[AccountWallet] = None
    """The account's primary crypto wallet, or null if none has been provisioned"""
