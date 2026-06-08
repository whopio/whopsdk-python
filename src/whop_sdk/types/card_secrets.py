# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardSecrets"]


class CardSecrets(BaseModel):
    cvc: str
    """The card CVC/CVV."""

    object: Literal["card_secrets"]

    pan: str
    """The full card number (PAN)."""

    name_on_card: Optional[str] = None
    """The cardholder name from the card provider."""
