# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompanyTokenTransactionListResponse", "Company", "Member", "User"]


class Company(BaseModel):
    """The company"""

    id: str
    """The ID of the company"""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class Member(BaseModel):
    """The member"""

    id: str
    """The ID of the member"""


class User(BaseModel):
    """The user whose balance changed"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class CompanyTokenTransactionListResponse(BaseModel):
    """A token transaction within a company"""

    id: str
    """The ID of the transaction"""

    amount: float
    """The transaction amount (always positive)"""

    company: Company
    """The company"""

    created_at: datetime
    """When the transaction was created"""

    description: Optional[str] = None
    """Optional description"""

    idempotency_key: Optional[str] = None
    """Optional idempotency key to prevent duplicate transactions"""

    linked_transaction_id: Optional[str] = None
    """For transfers, the ID of the linked transaction"""

    member: Member
    """The member"""

    transaction_type: Literal["add", "subtract", "transfer"]
    """The type of transaction"""

    user: User
    """The user whose balance changed"""
