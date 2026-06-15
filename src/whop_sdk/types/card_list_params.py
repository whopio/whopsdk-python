# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    card_id: str
    """An icrd\\__ identifier. When provided, only that card is returned."""

    reveal_secrets: bool
    """
    When true, each active card includes a secrets object with the full card number
    (pan), cvc, and cardholder name.
    """

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
