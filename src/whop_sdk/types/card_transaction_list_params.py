# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["CardTransactionListParams"]


class CardTransactionListParams(TypedDict, total=False):
    account_id: str
    """The account whose card transactions to list, prefixed `biz_`.

    Defaults to the credential's account.
    """

    after: str
    """A cursor; returns card transactions after this position."""

    before: str
    """A cursor; returns card transactions before this position."""

    card_id: SequenceNotStr[str]
    """Return only transactions charged to these cards, each prefixed `icrd_`."""

    cardholder_id: SequenceNotStr[str]
    """
    Return only transactions on cards assigned to these users, each prefixed
    `user_`.
    """

    created_after: str
    """Return only transactions authorized at or after this ISO 8601 timestamp."""

    created_before: str
    """Return only transactions authorized at or before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction. Defaults to `desc`."""

    first: int
    """The number of card transactions to return."""

    last: int
    """The number of card transactions to return, counting back from the end."""

    order: Literal["created_at"]
    """The field to sort by. Defaults to `created_at`."""

    status: Literal["pending", "completed", "reversed", "declined"]
    """Return only transactions with this status."""

    transaction_ids: SequenceNotStr[str]
    """Return only these card transactions, each prefixed `citx_`.

    Repeat the parameter, or pass one comma-separated value.
    """
