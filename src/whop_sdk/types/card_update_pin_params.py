# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardUpdatePinParams"]


class CardUpdatePinParams(TypedDict, total=False):
    pin: Required[str]
    """The new 4-digit PIN."""
