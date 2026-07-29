# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MethodCreateResponse", "PayoutDestination"]


class PayoutDestination(BaseModel):
    delivery_type: Literal[
        "cash_pickup",
        "bank_deposit",
        "home_delivery",
        "mobile_wallet",
        "masspay_card",
        "paper_check",
        "bill",
        "cryptocurrency",
        "unknown",
    ]
    """How funds are delivered."""

    icon_url: Optional[str] = None

    name: Optional[str] = None

    supports_instant_delivery: bool

    supports_standard_delivery: bool


class MethodCreateResponse(BaseModel):
    id: str
    """Payout method ID, usable as payout_method_id on POST /payouts."""

    account_reference: Optional[str] = None
    """Masked identifier for the destination."""

    created_at: datetime

    destination_currency: str

    estimated_arrival: Optional[object] = None
    """Null on create. List payout methods to retrieve arrival estimates."""

    fee_structure: Optional[object] = None
    """Null on create. List payout methods to retrieve the configured fee terms."""

    institution_name: Optional[str] = None

    is_default: bool

    nickname: Optional[str] = None

    object: Literal["payout_method"]

    payer_name: Optional[str] = None

    payout_destination: Optional[PayoutDestination] = None

    quote: Optional[builtins.object] = None
    """Always null on create."""

    status: Literal["created", "active", "broken"]
