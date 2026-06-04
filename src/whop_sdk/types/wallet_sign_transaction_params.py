# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WalletSignTransactionParams"]


class WalletSignTransactionParams(TypedDict, total=False):
    chain_id: Required[int]
    """EIP-155 chain ID to broadcast on (e.g. 9745 for Plasma)."""

    to: Required[str]
    """Target contract or recipient address (0x...)."""

    data: str
    """Hex-encoded calldata. Defaults to 0x (plain transfer)."""

    idempotency_key: str
    """Optional retry-safety key (max 256 chars).

    Retried requests with the same key within 24 hours return the original
    transaction instead of broadcasting a second one.
    """

    value: str
    """Hex-encoded wei value. Defaults to 0x0."""
