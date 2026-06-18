# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SwapCreateQuoteParams"]


class SwapCreateQuoteParams(TypedDict, total=False):
    amount: Required[str]
    """Input token amount."""

    from_token: Required[str]
    """Source token, by contract address or ticker symbol (e.g. "USDT")."""

    to_token: Required[str]
    """Destination token, by contract address or ticker symbol (e.g. "XAUT")."""

    from_address: Optional[str]

    from_chain: Union[str, int, None]

    metadata: Dict[str, object]

    slippage_bps: Optional[int]

    to_address: Optional[str]

    to_chain: Union[str, int, None]
