# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardTransaction"]


class CardTransaction(BaseModel):
    id: str
    """Card transaction ID, prefixed `citx_`."""

    card_id: str
    """The card this transaction was charged to, prefixed `icrd_`."""

    cardholder_id: Optional[str] = None
    """The user the card is assigned to, prefixed `user_`.

    Null when the card has no assigned cardholder.
    """

    cashback_usd_amount: Optional[float] = None
    """Cashback earned on this transaction as a USD amount.

    Zero for declined or ineligible transactions, and null when cashback has not
    been computed yet.
    """

    created_at: str
    """When the transaction was authorized, as an ISO 8601 timestamp."""

    currency: Optional[str] = None
    """ISO 4217 currency code the merchant charged in."""

    declined_reason: Optional[str] = None
    """Why the transaction was declined. Null unless `status` is `declined`."""

    international: bool
    """True when the merchant is outside the card's home country."""

    local_amount: Optional[float] = None
    """Amount the merchant charged in their own currency. Pair with `currency`."""

    merchant_category: Optional[str] = None
    """
    Merchant category label, enriched where available and otherwise as the card
    network reported it.
    """

    merchant_category_code: Optional[str] = None
    """Four-digit ISO 18245 merchant category code (MCC)."""

    merchant_icon_url: Optional[str] = None
    """URL of the enriched merchant logo. Null when no logo was matched."""

    merchant_name: Optional[str] = None
    """
    Merchant name, enriched where available and otherwise as the card network
    reported it.
    """

    posted_at: Optional[str] = None
    """When the card network settled the transaction, as an ISO 8601 timestamp.

    Null until it settles.
    """

    status: Literal["pending", "completed", "reversed", "declined"]
    """Current status of the transaction."""

    transaction_type: Literal["spend"]
    """The kind of card transaction. Always `spend` today."""

    usd_amount: Optional[float] = None
    """Amount charged in USD. Negative when the merchant refunded the card."""
