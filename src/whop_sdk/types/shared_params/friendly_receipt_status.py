# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["FriendlyReceiptStatus"]

FriendlyReceiptStatus: TypeAlias = Literal[
    "succeeded",
    "failed",
    "past_due",
    "canceled",
    "price_too_low",
    "uncollectible",
    "refunded",
    "auto_refunded",
    "partially_refunded",
    "open_resolution",
    "dispute_warning",
    "open_dispute",
    "dispute_needs_response",
    "dispute_warning_needs_response",
    "dispute_under_review",
    "dispute_warning_under_review",
    "dispute_won",
    "dispute_lost",
    "dispute_closed",
    "dispute_warning_closed",
    "drafted",
    "incomplete",
    "unresolved",
    "pending",
]
