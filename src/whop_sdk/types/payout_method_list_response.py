# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayoutMethodListResponse", "Destination"]


class Destination(BaseModel):
    """The payout destination associated with the payout token"""

    category: Literal["crypto", "rtp", "next_day_bank", "bank_wire", "digital_wallet", "unknown"]
    """The category of the payout destination"""

    country_code: str
    """The country code of the payout destination"""

    name: str
    """The name of the payer associated with the payout destination"""


class PayoutMethodListResponse(BaseModel):
    """An object representing an user's setup payout destination."""

    id: str
    """The ID of the payout token"""

    currency: str
    """The currency code of the payout destination.

    This is the currency that payouts will be made in for this token.
    """

    destination: Optional[Destination] = None
    """The payout destination associated with the payout token"""

    nickname: Optional[str] = None
    """An optional nickname for the payout token to help the user identify it.

    This is not used by the provider and is only for the user's reference.
    """
