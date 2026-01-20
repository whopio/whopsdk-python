# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FriendlyReceiptStatus"]

FriendlyReceiptStatus: TypeAlias = Literal[
    "succeeded",
    "pending",
    "failed",
    "past_due",
    "canceled",
    "price_too_low",
    "uncollectible",
    "refunded",
    "auto_refunded",
    "partially_refunded",
    "dispute_warning",
    "dispute_needs_response",
    "dispute_warning_needs_response",
    "resolution_needs_response",
    "dispute_under_review",
    "dispute_warning_under_review",
    "resolution_under_review",
    "dispute_won",
    "dispute_warning_closed",
    "resolution_won",
    "dispute_lost",
    "dispute_closed",
    "resolution_lost",
    "drafted",
    "incomplete",
    "unresolved",
    "open_dispute",
    "open_resolution",
]
