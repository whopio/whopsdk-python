# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ShipmentCreateParams"]


class ShipmentCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """
    The unique identifier of the company to create the shipment for, starting with
    'biz\\__'.
    """

    payment_id: Required[str]
    """The unique identifier of the payment to associate the shipment with."""

    tracking_code: Required[str]
    """
    The carrier tracking code for the shipment, such as a USPS, UPS, or FedEx
    tracking number.
    """
