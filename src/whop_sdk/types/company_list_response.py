# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CompanyListResponse", "Logo", "OwnerUser"]


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


class CompanyListResponse(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

    created_at: datetime
    """The datetime the company was created."""

    description: Optional[str] = None
    """
    A promotional pitch written by the company creator, displayed to potential
    customers on the store page.
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

    title: str
    """The display name of the company shown to customers."""

    updated_at: datetime
    """The datetime the company was last updated."""

    verified: bool
    """Whether this company has been verified by Whop's trust and safety team."""
