# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .entry_status import EntryStatus

__all__ = ["Entry", "CustomFieldResponse", "Plan", "Product", "User"]


class CustomFieldResponse(BaseModel):
    """The response from a custom field on checkout"""

    id: str
    """The ID of the custom field item"""

    answer: str
    """The response a user gave to the specific question or field."""

    question: str
    """The question asked by the custom field"""


class Plan(BaseModel):
    """The waitlist plan the entry if for."""

    id: str
    """The internal ID of the plan."""


class Product(BaseModel):
    """The product tied to this entry, if there is one."""

    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class User(BaseModel):
    """The user who created the entry."""

    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Entry(BaseModel):
    """An object representing an entry in a waitlist."""

    id: str
    """The internal ID of the entry."""

    created_at: Optional[datetime] = None
    """When the entry was created."""

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
