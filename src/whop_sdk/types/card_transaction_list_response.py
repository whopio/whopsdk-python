# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardTransactionListResponse"]


class CardTransactionListResponse(BaseModel):
    """A card transaction record."""

    id: str
    """The unique identifier for the card transaction."""

    authorization_method: Optional[str] = None
    """How the card was presented or authenticated for the purchase."""

    card_id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    cashback_usd_amount: Optional[float] = None
    """The cashback reward amount earned on this transaction, in USD."""

    created_at: datetime
    """The datetime the card transaction was created."""

    currency: Optional[str] = None
    """The ISO 4217 currency code for the transaction amount."""

    declined_reason: Optional[str] = None
    """The issuer-provided reason the transaction was declined."""

    international: bool
    """
    Whether the transaction was made with a merchant outside the card's home
    country.
    """

    local_amount: Optional[float] = None
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
    """The enriched or raw name of the merchant where the purchase was made."""

    posted_at: Optional[datetime] = None
    """When the transaction was settled by the card network."""

    status: Literal["pending", "completed", "reversed", "declined"]
    """The current lifecycle status of the transaction."""

    transaction_type: str
    """The type of transaction."""

    usd_amount: Optional[float] = None
    """The transaction amount in USD."""
