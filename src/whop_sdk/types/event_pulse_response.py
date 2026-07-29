# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventPulseResponse", "Data", "DataUser", "PageInfo"]


class DataUser(BaseModel):
    """Coarse location, shaped like the event `user` block.

    The buyer on a purchase; on a payout it is the paying side — the poster for a bounty, the paying company for an affiliate commission, which resolves to a country with no city. Omitted entirely when nothing is known.
    """

    city: Optional[str] = None
    """City name. Omitted when unknown."""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country code. Omitted when unknown."""


class Data(BaseModel):
    event_name: Literal["payment.completed", "bounty.payout.completed", "affiliate.payout.completed"]
    """
    The event recorded, matching the [event](/api-reference/beta/events/event) of
    the same name: a purchase, a bounty payout, or an affiliate commission payout.
    """

    event_time: datetime
    """When the event happened, coarsened to the start of the minute."""

    total_usd_amount: Optional[float] = None
    """The USD amount of the event."""

    user: Optional[DataUser] = None
    """Coarse location, shaped like the event `user` block.

    The buyer on a purchase; on a payout it is the paying side — the poster for a
    bounty, the paying company for an affiliate commission, which resolves to a
    country with no city. Omitted entirely when nothing is known.
    """


class PageInfo(BaseModel):
    has_next_page: bool

    has_previous_page: bool

    end_cursor: Optional[str] = None

    start_cursor: Optional[str] = None


class EventPulseResponse(BaseModel):
    data: List[Data]
    """Recent anonymized purchase events, newest first."""

    page_info: PageInfo
