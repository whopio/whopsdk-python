# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletSignTransactionResponse"]


class WalletSignTransactionResponse(BaseModel):
    address: str

    chain_id: int

    object: Literal["transaction"]

    to: str

    tx_hash: str
