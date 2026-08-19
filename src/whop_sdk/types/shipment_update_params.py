# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ShipmentUpdateParams"]


class ShipmentUpdateParams(TypedDict, total=False):
    tracking_number: Required[str]
    """The new carrier-assigned tracking number."""
