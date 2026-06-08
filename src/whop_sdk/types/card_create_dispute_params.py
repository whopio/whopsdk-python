# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardCreateDisputeParams"]


class CardCreateDisputeParams(TypedDict, total=False):
    dispute_type: Required[
        Literal["fraud", "credit_not_processed", "service_not_received", "merchandise_issue", "other"]
    ]
    """The reason category for the dispute."""

    text_evidence: Required[str]
    """The cardholder's written evidence for the dispute."""

    transaction_id: Required[str]
    """The ID of the card transaction being disputed. Must belong to this card."""

    dispute_amount_cents: int
    """Optional disputed amount in cents.

    Defaults to the full transaction amount. Must not exceed the transaction amount.
    """
