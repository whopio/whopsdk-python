# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID that owns the cards."""
