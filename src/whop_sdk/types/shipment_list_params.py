# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ShipmentListParams"]


class ShipmentListParams(TypedDict, total=False):
    account_id: str
    """The account to list shipments for. Defaults to the acting account."""

    after: str
    """A cursor; returns shipments after this position."""

    before: str
    """A cursor; returns shipments before this position."""

    created_after: str
    """Return shipments created after this ISO 8601 timestamp."""

    created_before: str
    """Return shipments created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction."""

    first: int
    """The number of shipments to return."""

    last: int
    """The number of shipments to return from the end of the range."""

    order: Literal["created_at"]
    """The field to sort by."""

    payment_id: SequenceNotStr[str]
    """Only shipments fulfilling these payments, each prefixed `pay_`.

    Repeat the parameter to pass several, up to 100 per request — one paginated list
    covers all of them.
    """

    status: Literal[
        "unknown",
        "pre_transit",
        "in_transit",
        "out_for_delivery",
        "delivered",
        "available_for_pickup",
        "return_to_sender",
        "failure",
        "cancelled",
        "error",
    ]
    """Filter to shipments with this delivery status."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
