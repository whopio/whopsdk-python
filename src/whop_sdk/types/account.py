# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .account_wallet import AccountWallet
from .account_social_link import AccountSocialLink

__all__ = ["Account"]


class Account(BaseModel):
    id: str
    """The ID of the account, which will look like biz\\__******\\********"""

    banner_image_url: Optional[str] = None
    """The URL of the account banner image"""

    business_type: Optional[str] = None
    """The high-level business category for the account"""

    created_at: str
    """When the account was created, as an ISO 8601 timestamp"""

    description: Optional[str] = None
    """A promotional description for the account"""

    email: Optional[str] = None
    """The email address of the account owner"""

    industry_group: Optional[str] = None
    """The industry group the account belongs to"""

    industry_type: Optional[str] = None
    """The specific industry vertical the account operates in"""

    logo_url: Optional[str] = None
    """The URL of the account logo image"""

    metadata: object
    """Arbitrary key/value metadata supplied when the account was created"""

    parent_account_id: Optional[str] = None
    """The parent account ID for connected accounts"""

    route: str
    """The account's public route identifier"""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account"""

    social_links: List[AccountSocialLink]

    target_audience: Optional[str] = None
    """The target audience for this account"""

    title: str
    """The display name of the account"""

    wallet: Optional[AccountWallet] = None
    """The account's primary crypto wallet, or null if none has been provisioned"""
