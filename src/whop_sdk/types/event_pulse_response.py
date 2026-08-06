# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventPulseResponse", "Data", "DataUser", "PageInfo"]


class DataUser(BaseModel):
    """Coarse location, shaped like the event `user` block.

    It belongs to the owner of the wallet the money moved into or out of — the party the event is about, never their counterparty. Omitted entirely when nothing is known.
    """

    city: Optional[str] = None
    """City name. Omitted when unknown."""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country code. Omitted when unknown."""


class Data(BaseModel):
    event_name: Literal["ledger_line.created"]
    """The underlying event recorded.

    Every movement on this feed is a ledger line, so switch on `type` rather than
    this.
    """

    event_time: datetime
    """When the event happened, coarsened to the start of the minute."""

    type: Literal[
        "purchase",
        "affiliate_commission",
        "card_spend",
        "ad_spend",
        "app_revenue",
        "off_platform_sale",
        "deposit",
        "card_load",
        "airdrop_claim",
        "transfer",
        "referral_bonus",
    ]
    """
    What moved: a purchase, an affiliate commission, Whop card spend, ad spend, app
    revenue, an off-platform sale, a wallet deposit, a card load, a claimed drop, a
    transfer between accounts, or a referral bonus.
    """

    total_usd_amount: Optional[float] = None
    """The USD amount of the event."""

    user: Optional[DataUser] = None
    """Coarse location, shaped like the event `user` block.

    It belongs to the owner of the wallet the money moved into or out of — the party
    the event is about, never their counterparty. Omitted entirely when nothing is
    known.
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
