# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["BountyRetrieveResponse"]


class BountyRetrieveResponse(BaseModel):
    """A privately accessible bounty."""

    id: str
    """The unique identifier for the bounty."""

    bounty_type: Literal["classic", "user_funded", "workforce"]
    """The underlying bounty implementation type."""

    created_at: datetime
    """The datetime the bounty was created."""

    currency: Currency
    """The currency used for the bounty funds."""

    description: str
    """The description of the bounty."""

    status: Literal["published", "archived"]
    """The current lifecycle status of the bounty."""

    title: str
    """The title of the bounty."""

    total_available: float
    """The total amount currently funded in the bounty pool for payout."""

    total_paid: float
    """The total amount paid out for this bounty."""

    updated_at: datetime
    """The datetime the bounty was last updated."""

    vote_threshold: int
    """The number of watcher votes required before the submission can resolve."""
