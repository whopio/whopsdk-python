# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ShipmentCreateParams"]


class ShipmentCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the shipment for"""

    payment_id: Required[str]
    """The ID of the payment to create the shipment for"""

    tracking_code: Required[str]
    """The tracking code for the shipment"""
