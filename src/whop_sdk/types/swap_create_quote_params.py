# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SwapCreateQuoteParams"]


class SwapCreateQuoteParams(TypedDict, total=False):
    amount: Required[str]
    """Source token amount."""

    from_token: Required[str]
    """Source token contract address or ticker symbol, such as "USDT"."""

    to_token: Required[str]
    """Destination token contract address or ticker symbol, such as "XAUT"."""

    from_address: Optional[str]
    """Source wallet address used for the quote."""

    from_chain: Union[str, int, None]
    """Source chain name or chain ID.

    Defaults to the source token's chain when omitted.
    """

    metadata: Dict[str, object]
    """Metadata to include with the quote response."""

    slippage_bps: Optional[int]
    """Maximum slippage tolerance in basis points."""

    to_address: Optional[str]
    """Destination wallet address used for the quote."""

    to_chain: Union[str, int, None]
    """Destination chain name or chain ID.

    Defaults to the destination token's chain when omitted.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
