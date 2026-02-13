# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CompanyTokenTransaction", "Company", "Member", "User"]


class Company(BaseModel):
    """The company whose token balance this transaction affects."""

    id: str
    """The unique identifier for the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The written name of the company."""


class Member(BaseModel):
    """The member whose token balance was affected by this transaction."""

    id: str
    """The unique identifier for the company member."""


class User(BaseModel):
    """The user whose token balance was affected by this transaction."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class CompanyTokenTransaction(BaseModel):
    """
    A token transaction records a credit or debit to a member's token balance within a company, including transfers between members.
    """

    id: str
    """The unique identifier for the company token transaction."""

    amount: float
    """The token amount for this transaction.

    Always a positive value regardless of transaction type.
    """

    company: Company
    """The company whose token balance this transaction affects."""

    created_at: datetime
    """The datetime the company token transaction was created."""

    description: Optional[str] = None
    """Free-text description explaining the reason for this token transaction.

    Null if no description was provided.
    """

    idempotency_key: Optional[str] = None
    """A unique key used to prevent duplicate transactions when retrying API requests.

    Null if no idempotency key was provided.
    """

    linked_transaction_id: Optional[str] = None
    """The ID of the corresponding transaction on the other side of a transfer.

    Null if this is not a transfer transaction.
    """

    member: Member
    """The member whose token balance was affected by this transaction."""

    transaction_type: Literal["add", "subtract", "transfer"]
    """The direction of this token transaction (add, subtract, or transfer)."""

    user: User
    """The user whose token balance was affected by this transaction."""
