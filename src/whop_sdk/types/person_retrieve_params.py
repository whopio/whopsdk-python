# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonRetrieveParams"]


class PersonRetrieveParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    from_: Annotated[int, PropertyInfo(alias="from")]
    """Start of the time range as a Unix timestamp."""

    to: int
    """End of the time range as a Unix timestamp. Defaults to now."""
