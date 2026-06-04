# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WalletSignMessageParams"]


class WalletSignMessageParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID whose wallet signs."""

    chain_id: Required[int]
    """EIP-155 chain ID the signature is intended for (e.g. 9745 for Plasma)."""

    message: Required[object]
    """
    A UTF-8 string for personal_sign, or an EIP-712 object (domain, types,
    primaryType, message) for typed_data.
    """

    type: Required[Literal["personal_sign", "typed_data"]]
    """Signature scheme."""
