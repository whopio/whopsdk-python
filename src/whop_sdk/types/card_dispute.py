# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardDispute"]


class CardDispute(BaseModel):
    id: str
    """The card dispute ID."""

    attachment_count: int
    """The number of evidence files attached to the dispute."""

    created_at: str
    """ISO 8601 timestamp of when the dispute was created."""

    currency: str
    """The ISO 4217 currency code for the disputed amount."""

    dispute_amount_cents: int
    """The disputed amount in the smallest currency unit (cents)."""

    dispute_type: Literal["fraud", "credit_not_processed", "service_not_received", "merchandise_issue", "other"]
    """The reason category for the dispute."""

    has_file_evidence: bool
    """Whether evidence files have been attached to the dispute."""

    object: Literal["card_dispute"]

    status: Literal["pending", "in_review", "accepted", "rejected", "canceled", "resolved_by_merchant"]
    """The dispute lifecycle status."""

    resolved_at: Optional[str] = None
    """ISO 8601 timestamp of when the provider resolved the dispute.

    Null if unresolved.
    """

    text_evidence: Optional[str] = None
    """The cardholder's written evidence for the dispute."""

    transaction_id: Optional[str] = None
    """The ID of the card transaction the dispute was filed against."""
