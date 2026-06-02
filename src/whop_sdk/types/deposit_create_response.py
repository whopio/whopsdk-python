# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DepositCreateResponse", "DepositAddress", "Destination"]


class DepositAddress(BaseModel):
    evm: str

    solana: str


class Destination(BaseModel):
    address: str

    currency: str

    network: str

    account_id: Optional[str] = None


class DepositCreateResponse(BaseModel):
    amount: str

    deposit_address: DepositAddress

    destination: Destination

    hosted_url: Optional[str] = None

    metadata: Dict[str, object]

    object: Literal["deposit"]
