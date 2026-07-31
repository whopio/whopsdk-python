# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SwapCreateParams"]


class SwapCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Business or user account ID (biz*\\** / user*\\**)."""

    from_token: Required[str]
    """Source token contract address or ticker symbol, such as "USDT"."""

    to_token: Required[str]
    """Destination token contract address or ticker symbol, such as "XAUT"."""

    amount: Optional[str]
    """Source token amount.

    Required for crypto swaps. Optional for fiat pairs: the portion of the negative
    to_token balance to repay, which must not exceed the debt; omit to repay the
    full debt.
    """

    from_chain: Union[str, int, None]
    """Source chain name or chain ID.

    Defaults to the source token's chain when omitted.
    """

    slippage_bps: Optional[int]
    """Maximum slippage tolerance in basis points."""

    to_chain: Union[str, int, None]
    """Destination chain name or chain ID.

    Defaults to the destination token's chain when omitted.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
