# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletSignMessageResponse"]


class WalletSignMessageResponse(BaseModel):
    address: str

    chain_id: int

    object: Literal["signature"]

    signature: str

    type: str
