# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SwapCreateParams"]


class SwapCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID whose wallet should execute the swap."""

    amount: Required[str]
    """Input token amount."""

    from_token: Required[str]
    """Source token contract address."""

    to_token: Required[str]
    """Destination token contract address."""

    from_chain: Union[str, int, None]

    slippage_bps: Optional[int]

    to_chain: Union[str, int, None]
