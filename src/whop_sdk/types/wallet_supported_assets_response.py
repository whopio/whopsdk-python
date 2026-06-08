# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletSupportedAssetsResponse", "Asset"]


class Asset(BaseModel):
    chain_id: int

    decimals: int

    name: str

    network: str

    symbol: str

    token_address: str

    tradable: bool


class WalletSupportedAssetsResponse(BaseModel):
    assets: List[Asset]

    object: Literal["supported_assets"]
