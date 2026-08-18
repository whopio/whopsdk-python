# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ShipmentListParams"]


class ShipmentListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """Filter shipments to only those belonging to this company."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    payment_id: str
    """Filter shipments to only those associated with this specific payment."""

    user_id: str
    """Filter shipments to only those for this specific user."""
