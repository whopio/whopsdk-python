# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WalletDepositAddressParams"]


class WalletDepositAddressParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID whose deposit address should be returned."""

    asset: str
    """Optional asset symbol the caller intends to deposit (e.g.

    USDT). Unsupported assets are rejected with a 400 rather than silently ignored.
    """

    network: Literal["plasma", "base", "ethereum"]
    """Optional network the caller intends to deposit on (e.g.

    plasma). Unsupported networks are rejected with a 400 rather than silently
    ignored.
    """
