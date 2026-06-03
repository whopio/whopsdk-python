# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountWallet"]


class AccountWallet(BaseModel):
    id: str
    """The ID of the wallet, which will look like wallet\\__******\\********"""

    address: str
    """The on-chain address of the wallet"""

    network: Literal["solana", "ethereum", "bitcoin"]
    """The blockchain network the wallet lives on"""
