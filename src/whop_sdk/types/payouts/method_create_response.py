# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MethodCreateResponse", "SupportedPayoutMethod"]


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

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-3 country the destination pays out to."""

    supports_plaid: Optional[bool] = None
    """
    Whether the payer can link this method by signing in to their bank instead of
    typing account details.
    """


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
    """User-defined label for the payout method."""

    object: Literal["payout_method"]

    payer_name: Optional[str] = None

    quote: Optional[builtins.object] = None
    """Always null on create."""

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

    bank_verification_state: Optional[Literal["checking", "verified", "no_data", "warning", "broken"]] = None
    """
    Lifecycle trust state: `checking` (verification still running), `verified` (bank
    confirmed ownership or a payout already completed to it), `no_data`
    (verification unavailable or bank returned no ownership data), `warning` (bank
    could not confirm the destination's owner), `broken` (payouts failed with a
    permanent account error), `null` (never checked).
    """

    is_clone: Optional[bool] = None
    """Whether this method is a copy of one saved on another of the payer's accounts."""

    linked_via_plaid: Optional[bool] = None
    """
    Whether the payer added this method by signing in to their bank rather than
    typing account details.
    """

    needs_plaid_reconnect: Optional[bool] = None
    """
    Whether the bank sign-in behind this method has expired and must be redone
    before it counts as linked.
    """
