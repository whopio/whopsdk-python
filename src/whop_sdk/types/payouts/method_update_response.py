# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MethodUpdateResponse", "SupportedPayoutMethod"]


class SupportedPayoutMethod(BaseModel):
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


class MethodUpdateResponse(BaseModel):
    id: str
    """Payout method ID, prefixed `potk_`."""

    account_reference: Optional[str] = None
    """Masked identifier for the destination."""

    bank_verification_state: Optional[Literal["checking", "verified", "no_data", "warning", "broken"]] = None
    """
    Lifecycle trust state: `checking` (verification still running), `verified` (bank
    confirmed ownership or a payout already completed to it), `no_data`
    (verification unavailable or bank returned no ownership data), `warning` (bank
    could not confirm the destination's owner), `broken` (payouts failed with a
    permanent account error), `null` (never checked).
    """

    created_at: datetime

    destination_currency: str

    estimated_arrival: Optional[object] = None
    """`null` after an update. List payout methods to retrieve arrival estimates."""

    fee_structure: Optional[object] = None
    """`null` after an update.

    List payout methods to retrieve the configured fee terms.
    """

    institution_name: Optional[str] = None

    is_default: bool

    nickname: Optional[str] = None
    """User-defined label for the payout method."""

    object: Literal["payout_method"]

    payer_name: Optional[str] = None

    quote: Optional[builtins.object] = None
    """Always `null` after an update."""

    status: Literal["created", "active", "broken"]

    supported_payout_method: Optional[SupportedPayoutMethod] = None

    unavailable_reason: Optional[Literal["destination_retired"]] = None
    """
    Why this method is unavailable: `destination_retired` means the payout provider
    stopped offering the destination. Whop may automatically remap an eligible
    method that was not linked through Plaid to a compatible replacement; otherwise,
    the account owner must re-add it. `null` means no unavailability reason is
    known.
    """
