# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletDepositAddressResponse", "SupportedNetwork"]


class SupportedNetwork(BaseModel):
    chain_id: int

    name: str


class WalletDepositAddressResponse(BaseModel):
    address: str

    object: Literal["deposit_address"]

    supported_networks: List[SupportedNetwork]

    asset: Optional[str] = None
    """Echo of the validated asset filter, present when the caller passed ?asset=."""

    network: Optional[str] = None
    """Echo of the validated network filter, present when the caller passed ?network=."""
