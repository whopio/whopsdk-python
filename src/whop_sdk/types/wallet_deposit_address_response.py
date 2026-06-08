# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletDepositAddressResponse", "SupportedNetwork"]


class SupportedNetwork(BaseModel):
    address_kind: Literal["evm", "solana"]

    chain_id: Optional[int] = None

    network: str

    onramp_supported: bool


class WalletDepositAddressResponse(BaseModel):
    evm_address: Optional[str] = None

    hosted_url: Optional[str] = None

    object: Literal["deposit_address"]

    solana_address: Optional[str] = None

    status: Literal["ready", "provisioning"]

    supported_networks: List[SupportedNetwork]

    asset: Optional[str] = None
    """Echo of the validated asset filter, present when the caller passed ?asset=."""

    network: Optional[str] = None
    """Echo of the validated network filter, present when the caller passed ?network=."""
