# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardRetrieveResponse", "Billing", "Limit", "Secrets"]


class Billing(BaseModel):
    """The billing address."""

    city: Optional[str] = None
    """Billing city."""

    country_code: Optional[str] = None
    """Billing country code."""

    line1: Optional[str] = None
    """Street address line 1."""

    line2: Optional[str] = None
    """Street address line 2."""

    postal_code: Optional[str] = None
    """Billing postal code."""

    region: Optional[str] = None
    """Billing region or state."""


class Limit(BaseModel):
    """The spending limit configuration."""

    amount: float
    """The limit amount in dollars."""

    frequency: str
    """Limit window, for example `per24HourPeriod` or `perAuthorization`."""


class Secrets(BaseModel):
    """Sensitive card details.

    Present only on `GET /cards/:card_id` for active cards; `null` when the card is inactive or details cannot be retrieved.
    """

    card_number: str
    """Full card number."""

    cvc: str
    """Card verification code."""

    name_on_card: Optional[str] = None
    """Cardholder name printed on the card."""


class CardRetrieveResponse(BaseModel):
    id: str
    """Card ID, prefixed `icrd_`."""

    billing: Optional[Billing] = None
    """The billing address."""

    canceled_at: Optional[datetime] = None
    """When the card was canceled."""

    created_at: Optional[datetime] = None
    """When the card was created."""

    expiration_month: Optional[str] = None
    """Card expiration month."""

    expiration_year: Optional[str] = None
    """Card expiration year."""

    last4: Optional[str] = None
    """Last four digits of the card number. `null` for pending invitation cards."""

    limit: Optional[Limit] = None
    """The spending limit configuration."""

    name: Optional[str] = None
    """Card display name."""

    object: Literal["card"]

    spent_last_month: Optional[int] = None
    """Total spend in the last 30 days, in cents."""

    status: Optional[Literal["active", "frozen", "canceled", "invited"]] = None
    """The card status."""

    type: Optional[Literal["virtual", "physical"]] = None
    """The card type."""

    user_id: Optional[str] = None
    """Cardholder user ID, prefixed `user_`, when assigned."""

    secrets: Optional[Secrets] = None
    """Sensitive card details.

    Present only on `GET /cards/:card_id` for active cards; `null` when the card is
    inactive or details cannot be retrieved.
    """
