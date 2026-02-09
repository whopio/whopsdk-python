# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .bot_token_transaction_types import BotTokenTransactionTypes

__all__ = ["CompanyTokenTransaction", "Company", "Member", "User"]


class Company(BaseModel):
    """The company"""

    id: str
    """The unique identifier for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class Member(BaseModel):
    """The member"""

    id: str
    """The unique identifier for the company member."""


class User(BaseModel):
    """The user whose balance changed"""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class CompanyTokenTransaction(BaseModel):
    """A token transaction within a company"""

    id: str
    """The unique identifier for the company token transaction."""

    amount: float
    """The transaction amount (always positive)"""

    company: Company
    """The company"""

    created_at: datetime
    """The datetime the company token transaction was created."""

    description: Optional[str] = None
    """Optional description"""

    idempotency_key: Optional[str] = None
    """Optional idempotency key to prevent duplicate transactions"""

    linked_transaction_id: Optional[str] = None
    """For transfers, the ID of the linked transaction"""

    member: Member
    """The member"""

    transaction_type: BotTokenTransactionTypes
    """The type of transaction"""

    user: User
    """The user whose balance changed"""
