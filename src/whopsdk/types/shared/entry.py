# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .entry_status import EntryStatus

__all__ = ["Entry", "CustomFieldResponse", "Plan", "Product", "User"]


class CustomFieldResponse(BaseModel):
    id: str
    """The ID of the custom field item"""

    answer: str
    """The response a user gave to the specific question or field."""

    question: str
    """The question asked by the custom field"""


class Plan(BaseModel):
    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    id: str
    """The internal ID of the public access pass."""

    title: str
    """The title of the access pass. Use for Whop 4.0."""


class User(BaseModel):
    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Entry(BaseModel):
    id: str
    """The internal ID of the entry."""

    created_at: Optional[int] = None
    """When the entry was created."""

    custom_field_responses: Optional[List[CustomFieldResponse]] = None
    """Responses collected from the user when submitting their entry."""

    plan: Optional[Plan] = None
    """The waitlist plan the entry if for."""

    product: Optional[Product] = None
    """The access pass tied to this entry, if there is one."""

    status: Optional[EntryStatus] = None
    """The status of an entry to a waitlist."""

    user: User
    """The user who created the entry."""
