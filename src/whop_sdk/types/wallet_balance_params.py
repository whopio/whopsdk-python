# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WalletBalanceParams"]


class WalletBalanceParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID whose wallet balance should be returned."""
