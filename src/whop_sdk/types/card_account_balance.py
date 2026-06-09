# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardAccountBalance"]


class CardAccountBalance(BaseModel):
    available_balance: str
    """The available spending power in dollars."""

    currency: str
    """The currency of the balance."""

    object: Literal["card_account_balance"]

    spending_power: str
    """Spending power in dollars."""

    balance_due: Optional[str] = None
    """Balance due in dollars."""

    credit_limit: Optional[str] = None
    """Credit limit in dollars."""

    has_activity: Optional[bool] = None
    """Whether this card account has any card transactions."""

    pending_charges: Optional[str] = None
    """Pending charges in dollars."""

    pending_deposit_amount: Optional[str] = None
    """
    Dollar amount of in-flight deposits routed to the card that have not yet
    settled.
    """

    posted_charges: Optional[str] = None
    """Posted charges in dollars."""
