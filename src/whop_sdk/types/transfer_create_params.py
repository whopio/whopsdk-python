# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferCreateParams"]


class TransferCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to move, in the transfer currency. For example 25.00."""

    origin_id: Required[str]
    """The account sending the funds.

    A user ID (user_xxx), company ID (biz_xxx), or ledger account ID (ldgr_xxx).
    """

    currency: str
    """The currency, such as usd. Required for ledger transfers."""

    destination_id: str
    """The recipient.

    Required for ledger and wallet*send (a user*/biz*/ldgr* ID, or — for sends — an
    email). Omit for claim_link.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """claim_link only.

    Link expiry as an ISO 8601 timestamp. Defaults to 24 hours from creation.
    """

    idempotence_key: Optional[str]
    """Ledger transfers only. A unique key to prevent duplicate transfers."""

    metadata: Optional[Dict[str, object]]
    """Ledger transfers only. Custom key-value pairs attached to the transfer."""

    notes: Optional[str]
    """Ledger transfers only. A short note describing the transfer."""

    redeemable_count: int
    """claim_link only. How many different users can claim the link. Defaults to 1."""

    type: Literal["ledger", "wallet_send", "claim_link"]
    """The kind of money movement. Defaults to ledger."""
