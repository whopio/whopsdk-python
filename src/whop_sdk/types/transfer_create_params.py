# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared.currency import Currency

__all__ = ["TransferCreateParams"]


class TransferCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to transfer in the specified currency.

    For example, 25.00 for $25.00 USD.
    """

    currency: Required[Currency]
    """The currency of the transfer amount, such as 'usd'."""

    destination_id: Required[str]
    """The identifier of the account receiving the funds.

    Accepts a user ID ('user_xxx'), company ID ('biz_xxx'), or ledger account ID
    ('ldgr_xxx').
    """

    origin_id: Required[str]
    """The identifier of the account sending the funds.

    Accepts a user ID ('user_xxx'), company ID ('biz_xxx'), or ledger account ID
    ('ldgr_xxx').
    """

    idempotence_key: Optional[str]
    """A unique key to prevent duplicate transfers.

    Use a UUID or similar unique string.
    """

    metadata: Optional[Dict[str, object]]
    """
    A JSON object of custom metadata to attach to the transfer for tracking
    purposes.
    """

    notes: Optional[str]
    """A short note describing the transfer, up to 50 characters."""
