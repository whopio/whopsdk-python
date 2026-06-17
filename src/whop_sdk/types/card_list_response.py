# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardListResponse", "Data", "DataBilling", "DataLimit", "DataSecrets"]


class DataBilling(BaseModel):
    """The billing address."""

    city: Optional[str] = None

    country_code: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    region: Optional[str] = None


class DataLimit(BaseModel):
    """The spending limit configuration."""

    amount: int
    """The limit amount in cents."""

    frequency: str
    """The limit window, for example per24HourPeriod or perAuthorization."""


class DataSecrets(BaseModel):
    """The card's sensitive details.

    Only present on GET /cards/:card_id (retrieve); null for cards that are not active or whose details could not be retrieved.
    """

    card_number: str
    """The full card number."""

    cvc: str
    """The card verification code."""

    name_on_card: Optional[str] = None
    """The cardholder name printed on the card."""


class Data(BaseModel):
    id: str
    """The icrd\\__ identifier of the card."""

    billing: Optional[DataBilling] = None
    """The billing address."""

    canceled_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    expiration_month: Optional[str] = None

    expiration_year: Optional[str] = None

    last4: Optional[str] = None
    """The last 4 digits of the card number. Null for pending invitation cards."""

    limit: Optional[DataLimit] = None
    """The spending limit configuration."""

    name: Optional[str] = None

    object: Literal["card"]

    spent_last_month: Optional[int] = None
    """Total spend in the last 30 days, in cents."""

    status: Optional[Literal["active", "frozen", "canceled", "invited"]] = None
    """The card status."""

    type: Optional[Literal["virtual", "physical"]] = None
    """The card type."""

    user_id: Optional[str] = None
    """The user\\__ identifier of the cardholder, when assigned."""

    secrets: Optional[DataSecrets] = None
    """The card's sensitive details.

    Only present on GET /cards/:card_id (retrieve); null for cards that are not
    active or whose details could not be retrieved.
    """


class CardListResponse(BaseModel):
    data: List[Data]
