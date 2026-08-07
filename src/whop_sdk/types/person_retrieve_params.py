# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PersonRetrieveParams"]


class PersonRetrieveParams(TypedDict, total=False):
    account_id: str
    """Account ID, prefixed `biz_`.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """
