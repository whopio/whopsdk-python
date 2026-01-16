# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["FriendlyReceiptStatus"]

FriendlyReceiptStatus: TypeAlias = Literal[
    "drafted",
    "succeeded",
    "incomplete",
    "refunded",
    "price_too_low",
    "uncollectible",
    "canceled",
    "partially_refunded",
    "failed",
    "open_dispute",
    "past_due",
    "auto_refunded",
    "dispute_warning",
    "unresolved",
    "open_resolution",
    "pending",
    "dispute_needs_response",
    "dispute_warning_needs_response",
    "dispute_under_review",
    "dispute_warning_under_review",
    "dispute_lost",
    "dispute_won",
    "dispute_closed",
    "dispute_warning_closed",
]
