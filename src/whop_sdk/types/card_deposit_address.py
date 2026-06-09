# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardDepositAddress"]


class CardDepositAddress(BaseModel):
    address: str
    """The on-chain deposit address used to fund the card account."""

    object: Literal["card_deposit_address"]
