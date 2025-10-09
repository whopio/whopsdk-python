# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["FriendlyReceiptStatus"]

FriendlyReceiptStatus: TypeAlias = Literal[
    "auto_refunded",
    "refunded",
    "partially_refunded",
    "dispute_warning",
    "open_resolution",
    "open_dispute",
    "failed",
    "price_too_low",
    "succeeded",
    "drafted",
    "uncollectible",
    "unresolved",
    "past_due",
    "pending",
    "incomplete",
    "canceled",
]
