# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PayoutRetrieveParams"]


class PayoutRetrieveParams(TypedDict, total=False):
    account_id: str
    """Owning account ID, prefixed `biz_`.

    Provide exactly one of `account_id` or `user_id`.
    """

    user_id: str
    """Owning user ID, prefixed `user_`.

    Provide exactly one of `account_id` or `user_id`.
    """
