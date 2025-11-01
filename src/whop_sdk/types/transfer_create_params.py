# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared.currency import Currency

__all__ = ["TransferCreateParams"]


class TransferCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to withdraw"""

    currency: Required[Currency]
    """The currency that is being withdrawn."""

    destination_id: Required[str]
    """
    The ID of the destination account which will receive the funds (either a User
    ID, Company ID, or LedgerAccount ID)
    """

    origin_id: Required[str]
    """
    The ID of the origin account which will send the funds (either a User ID,
    Company ID, or LedgerAccount ID)
    """

    idempotence_key: Optional[str]
    """A unique key to ensure idempotence. Use a UUID or similar."""

    metadata: Optional[Dict[str, object]]
    """A hash of metadata to attach to the transfer."""

    notes: Optional[str]
    """Notes for the transfer. Maximum of 50 characters."""
