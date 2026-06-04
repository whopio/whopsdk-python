# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
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
