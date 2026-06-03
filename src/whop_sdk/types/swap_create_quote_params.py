# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SwapCreateQuoteParams"]


class SwapCreateQuoteParams(TypedDict, total=False):
    amount: Required[str]
    """Input token amount."""

    from_token: Required[str]
    """Source token contract address."""

    to_token: Required[str]
    """Destination token contract address."""

    account_id: Optional[str]
    """Caller-owned account whose wallet address should be used."""

    from_address: Optional[str]

    from_chain: Union[str, int, None]

    metadata: Dict[str, object]

    slippage_bps: Optional[int]

    to_address: Optional[str]

    to_chain: Union[str, int, None]
