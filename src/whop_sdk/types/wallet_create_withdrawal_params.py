# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WalletCreateWithdrawalParams"]


class WalletCreateWithdrawalParams(TypedDict, total=False):
    amount: Required[str]
    """Amount to withdraw, as a decimal string in the given asset (e.g. "100.00")."""

    payout_method_id: Required[str]
    """A payout method already linked to the account."""

    asset: str
    """Currency to withdraw. Defaults to usd."""
