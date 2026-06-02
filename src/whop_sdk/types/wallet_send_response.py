# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletSendResponse", "Destination", "Source"]


class Destination(BaseModel):
    account_id: str

    address: str


class Source(BaseModel):
    account_id: str

    address: str


class WalletSendResponse(BaseModel):
    amount: str

    currency: str

    destination: Destination

    object: Literal["send"]

    source: Source

    tx_hash: str
