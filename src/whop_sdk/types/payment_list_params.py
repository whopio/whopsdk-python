# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    account_id: str
    """Only payments charged by this account, prefixed `biz_`."""

    after: str
    """A cursor; returns payments after this position."""

    before: str
    """A cursor; returns payments before this position."""

    billing_reason: Literal[
        "subscription_create", "subscription_cycle", "subscription_update", "one_time", "manual", "subscription"
    ]
    """Only payments charged for this reason."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only payments created after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only payments created before this ISO 8601 timestamp."""

    currency: str
    """Only payments presented in this three-letter currency, such as `usd`."""

    direction: Literal["asc", "desc"]
    """The sort direction."""

    first: int
    """The number of payments to return."""

    last: int
    """The number of payments to return from the end of the range."""

    member_id: str
    """Only payments made by this member, prefixed `mber_`."""

    membership_id: str
    """Only payments billed under this membership, prefixed `mem_`."""

    order: Literal["created_at", "paid_at"]
    """The field to sort by."""

    plan_id: str
    """Only payments priced by this plan, prefixed `plan_`."""

    product_id: str
    """Only payments for this product, prefixed `prod_`."""

    query: str
    """Search payments by user ID, membership ID, user email, name, or username.

    Email filtering requires the member:email:read permission.
    """

    status: Literal["open", "authorized", "paid", "pending", "uncollectible", "unresolved", "void"]
    """Only payments in this lifecycle state."""

    user_id: str
    """Only payments made by this buyer, prefixed `user_`."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
