# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PersonRetrieveParams"]


class PersonRetrieveParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """
