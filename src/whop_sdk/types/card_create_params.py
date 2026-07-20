# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardCreateParams"]


class CardCreateParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    assigned_user_id: str
    """The company member (a user\\__ identifier) to assign the card to.

    Required for company (business) card issuing accounts.
    """

    name: str
    """A display name for the card."""

    spend_limit: float
    """Spending limit amount, in dollars."""

    spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"]
    """The spending limit window."""

    transaction_limit: float
    """Per-transaction limit amount, in dollars."""

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
