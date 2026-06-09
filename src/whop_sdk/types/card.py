# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Card"]


class Card(BaseModel):
    id: Optional[str] = None
    """The card ID."""

    object: Literal["card"]

    status: Optional[Literal["pending", "active", "frozen", "canceled"]] = None
    """The card lifecycle status."""

    assigned_user_id: Optional[str] = None
    """The user the card is assigned to."""

    card_type: Optional[Literal["virtual", "physical"]] = None

    created_at: Optional[str] = None
    """ISO 8601 creation timestamp."""

    expiration_month: Optional[str] = None

    expiration_year: Optional[str] = None

    last4: Optional[str] = None
    """The last 4 digits of the card number."""

    name: Optional[str] = None
    """The display name of the card."""

    spend_limit: Optional[str] = None
    """Recurring spend limit in dollars."""

    spend_limit_frequency: Optional[Literal["daily", "weekly", "monthly", "one_time"]] = None

    spent_last_month_cents: Optional[int] = None
    """Amount spent on this card in the last 30 days, in integer cents."""

    transaction_limit: Optional[str] = None
    """Per-authorization limit in dollars."""
