# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventPulseResponse", "Data", "DataUser", "PageInfo"]


class DataUser(BaseModel):
    """Coarse location, shaped like the event `user` block.

    Country only, except on a purchase, which also carries the buyer's city — every other type resolves to the person who received the money, a small enough population that an amount plus a city can name them. Omitted entirely when nothing is known.
    """

    city: Optional[str] = None
    """City name. Present on purchases only, and omitted when unknown."""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country code. Omitted when unknown."""


class Data(BaseModel):
    event_name: Literal[
        "payment.completed", "bounty.payout.completed", "affiliate.payout.completed", "ledger_line.created"
    ]
    """The underlying event recorded.

    Several movements share `ledger_line.created`, so switch on `type` rather than
    this.
    """

    event_time: datetime
    """When the event happened, coarsened to the start of the minute."""

    type: Literal[
        "purchase",
        "bounty",
        "affiliate_commission",
        "withdrawal",
        "card_spend",
        "ad_spend",
        "app_revenue",
        "off_platform_sale",
    ]
    """
    What moved: a purchase, a bounty or affiliate payout, a creator withdrawal, Whop
    card spend, ad spend, app revenue, or an off-platform sale.
    """

    total_usd_amount: Optional[float] = None
    """The USD amount of the event."""

    user: Optional[DataUser] = None
    """Coarse location, shaped like the event `user` block.

    Country only, except on a purchase, which also carries the buyer's city — every
    other type resolves to the person who received the money, a small enough
    population that an amount plus a city can name them. Omitted entirely when
    nothing is known.
    """


class PageInfo(BaseModel):
    has_next_page: bool

    has_previous_page: bool

    end_cursor: Optional[str] = None

    start_cursor: Optional[str] = None


class EventPulseResponse(BaseModel):
    data: List[Data]
    """Recent anonymized money-movement events, newest first."""

    page_info: PageInfo
