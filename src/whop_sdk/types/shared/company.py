# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..social_link_websites import SocialLinkWebsites

__all__ = ["Company", "FeaturedAffiliateProduct", "Logo", "OwnerUser", "SocialLink"]


class FeaturedAffiliateProduct(BaseModel):
    """The product featured for affiliates to promote on this company's affiliate page.

    Null if none is configured.
    """

    id: str
    """The unique identifier for the product."""

    name: str
    """The display name of the product shown to customers. Maximum 50 characters."""


class Logo(BaseModel):
    """The company's logo."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class OwnerUser(BaseModel):
    """The user who owns and has full administrative control over this company."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class SocialLink(BaseModel):
    """A social link attached to a resource on the site."""

    id: str
    """The unique identifier for the social link."""

    url: str
    """The URL of the social media profile or external link."""

    website: SocialLinkWebsites
    """The website"""


class Company(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

    affiliate_instructions: Optional[str] = None
    """
    Guidelines and instructions provided to affiliates explaining how to promote
    this company's products.
    """

    created_at: datetime
    """The datetime the company was created."""

    description: Optional[str] = None
    """
    A promotional pitch written by the company creator, displayed to potential
    customers on the store page.
    """

    featured_affiliate_product: Optional[FeaturedAffiliateProduct] = None
    """The product featured for affiliates to promote on this company's affiliate page.

    Null if none is configured.
    """

    logo: Optional[Logo] = None
    """The company's logo."""

    member_count: int
    """
    The total number of users who currently hold active memberships across all of
    this company's products.
    """

    metadata: Optional[Dict[str, object]] = None
    """
    A key-value JSON object of custom metadata for this company, managed by the
    platform that created the account.
    """

    owner_user: OwnerUser
    """The user who owns and has full administrative control over this company."""

    published_reviews_count: int
    """
    The total number of published customer reviews across all products for this
    company.
    """

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    send_customer_emails: bool
    """
    Whether Whop sends transactional emails (receipts, updates) to customers on
    behalf of this company.
    """

    social_links: List[SocialLink]
    """
    The list of social media accounts and external links associated with this
    company.
    """

    target_audience: Optional[str] = None
    """The target audience for the company. Null if not set."""

    title: str
    """The display name of the company shown to customers."""

    updated_at: datetime
    """The datetime the company was last updated."""

    verified: bool
    """Whether this company has been verified by Whop's trust and safety team."""
