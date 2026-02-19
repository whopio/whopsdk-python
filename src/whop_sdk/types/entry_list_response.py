# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.entry_status import EntryStatus

__all__ = ["EntryListResponse", "Plan", "Product", "User"]


class Plan(BaseModel):
    """The waitlisted plan that this entry is a signup for."""

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product associated with this entry's waitlisted plan.

    Null if the plan is not tied to a product.
    """

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user who submitted this waitlist entry."""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class EntryListResponse(BaseModel):
    """An entry represents a user's signup for a waitlisted plan."""

    id: str
    """The unique identifier for the entry."""

    created_at: Optional[datetime] = None
    """The datetime the entry was created."""

    plan: Optional[Plan] = None
    """The waitlisted plan that this entry is a signup for."""

    product: Optional[Product] = None
    """The product associated with this entry's waitlisted plan.

    Null if the plan is not tied to a product.
    """

    status: EntryStatus
    """
    The current status of the waitlist entry (e.g., drafted, pending, approved,
    denied).
    """

    user: User
    """The user who submitted this waitlist entry."""
