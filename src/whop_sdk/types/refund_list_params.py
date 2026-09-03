# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RefundListParams"]


class RefundListParams(TypedDict, total=False):
    account_id: str
    """Only refunds issued by this account, prefixed `biz_`."""

    after: str
    """A cursor; returns refunds after this position."""

    before: str
    """A cursor; returns refunds before this position."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only refunds requested after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only refunds requested before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction."""

    first: int
    """The number of refunds to return."""

    last: int
    """The number of refunds to return from the end of the range."""

    order: Literal["created_at"]
    """The field to sort by."""

    payment_id: str
    """Only refunds of this payment, prefixed `pay_`."""

    user_id: str
    """Only refunds to this buyer, prefixed `user_`."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
