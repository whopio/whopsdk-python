# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["MethodCreateParams"]


class MethodCreateParams(TypedDict, total=False):
    supported_payout_method_id: Required[str]
    """
    The supported payout method to save (a podst\\__ identifier from a previous
    listing).
    """

    account_id: str
    """The account to add the payout method for, prefixed `biz_`.

    Provide this or `user_id`.
    """

    destination_currency: str
    """Currency the supported payout method delivers payouts in."""

    fields: Dict[str, str]
    """
    The supported payout method's required field values, keyed by field id — list
    them with `GET /payouts/supported_methods?supported_payout_method_id=...`. A
    Basis Theory token id may be passed in place of a raw value. For a U.S. bank
    routing-number field, a raw nine-digit value must also pass the ABA checksum. A
    validation failure returns the method's full required_fields schema alongside
    the error. Required whenever the account details are supplied directly.
    """

    is_default: bool
    """Whether to make this the account's default payout method."""

    nickname: str
    """A label for the payout method, unique per destination."""

    user_id: str
    """The user to add the payout method for, prefixed `user_`.

    Provide this or `account_id`.
    """
