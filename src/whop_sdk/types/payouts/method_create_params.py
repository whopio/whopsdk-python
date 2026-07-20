# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MethodCreateParams"]


class MethodCreateParams(TypedDict, total=False):
    destination_id: Required[str]
    """The payout destination to add (a pd\\__ identifier from a previous listing)."""

    fields: Required[Dict[str, str]]
    """The destination's required field values, keyed by field id."""

    nickname: Required[str]
    """A label for the payout method, unique per destination."""

    account_id: str
    """The account to add the payout method for (a biz\\__ identifier).

    Provide this or user_id.
    """

    destination_currency: str
    """Currency the destination delivers payouts in."""

    is_default: bool
    """Whether to make this the account's default payout method."""

    user_id: str
    """The user to add the payout method for (a user\\__ identifier).

    Provide this or account_id.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
