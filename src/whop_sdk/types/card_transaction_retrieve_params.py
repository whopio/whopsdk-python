# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardTransactionRetrieveParams"]


class CardTransactionRetrieveParams(TypedDict, total=False):
    account_id: str
    """The account that owns the transaction, prefixed `biz_`.

    Defaults to the credential's account.
    """
