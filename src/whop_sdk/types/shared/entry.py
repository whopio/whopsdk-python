# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .entry_status import EntryStatus

__all__ = ["Entry", "CustomFieldResponse", "Plan", "Product", "User"]


class CustomFieldResponse(BaseModel):
    """The response from a custom field on checkout"""

    id: str
    """The unique identifier for the custom field response."""

    answer: str
    """The response a user gave to the specific question or field."""

    question: str
    """The question asked by the custom field"""


class Plan(BaseModel):
    """The waitlist plan the entry if for."""

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product tied to this entry, if there is one."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user who created the entry."""

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


class Entry(BaseModel):
    """An entry represents a user's signup for a waitlisted plan."""

    id: str
    """The unique identifier for the entry."""

    created_at: Optional[datetime] = None
    """The datetime the entry was created."""

    custom_field_responses: Optional[List[CustomFieldResponse]] = None
    """Responses collected from the user when submitting their entry."""

    plan: Optional[Plan] = None
    """The waitlist plan the entry if for."""

    product: Optional[Product] = None
    """The product tied to this entry, if there is one."""

    status: EntryStatus
    """The status of the entry."""

    user: User
    """The user who created the entry."""
