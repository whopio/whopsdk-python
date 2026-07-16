# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonRetrieveParams"]


class PersonRetrieveParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start of the time range as an ISO 8601 timestamp."""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time range as an ISO 8601 timestamp. Defaults to now."""
