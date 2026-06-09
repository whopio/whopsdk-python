# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardTransaction"]


class CardTransaction(BaseModel):
    id: str
    """The card transaction ID."""

    card_id: str
    """The ID of the card the transaction was made on."""

    created_at: str
    """ISO 8601 timestamp of when the transaction was created."""

    international: bool
    """Whether the purchase was made with a merchant outside the card's home country."""

    object: Literal["card_transaction"]

    status: Literal["pending", "completed", "reversed", "declined"]
    """The transaction lifecycle status."""

    transaction_type: str
    """The type of transaction."""

    authorization_method: Optional[str] = None
    """How the card was presented or authenticated for the purchase."""

    cashback_usd_amount: Optional[str] = None
    """The cashback reward earned on this transaction, in USD."""

    currency: Optional[str] = None
    """The ISO 4217 currency code for the transaction amount."""

    declined_reason: Optional[str] = None
    """The issuer-provided reason the transaction was declined."""

    local_amount: Optional[str] = None
    """The transaction amount in the merchant's local currency before conversion."""

    memo: Optional[str] = None
    """A user-provided note attached to the transaction."""

    merchant_category: Optional[str] = None
    """The enriched or raw category label for the merchant."""

    merchant_category_code: Optional[str] = None
    """The four-digit ISO 18245 merchant category code (MCC)."""

    merchant_icon_url: Optional[str] = None
    """A URL to the enriched merchant logo image."""

    merchant_name: Optional[str] = None
    """The enriched or raw name of the merchant."""

    posted_at: Optional[str] = None
    """ISO 8601 timestamp of when the transaction was settled by the card network."""

    usd_amount: Optional[str] = None
    """The transaction amount in USD."""
