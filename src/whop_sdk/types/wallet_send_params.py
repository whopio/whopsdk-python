# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WalletSendParams"]


class WalletSendParams(TypedDict, total=False):
    account_id: Required[str]
    """The sending account ID."""

    amount: Required[str]
    """USDT amount to send."""

    to: Required[str]
    """Recipient user ID, business account ID, ledger account ID, or email."""
