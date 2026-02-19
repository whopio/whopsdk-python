# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.shipment_status import ShipmentStatus
from .shared.shipment_carrier import ShipmentCarrier
from .shared.shipment_substatus import ShipmentSubstatus

__all__ = ["ShipmentListResponse", "Payment"]


class Payment(BaseModel):
    """The payment associated with this shipment.

    Null if the payment has been deleted or is inaccessible.
    """

    id: str
    """The unique identifier for the payment."""


class ShipmentListResponse(BaseModel):
    """
    A physical shipment associated with a payment, including carrier details and tracking information.
    """

    id: str
    """The unique identifier for the shipment."""

    carrier: ShipmentCarrier
    """The shipping carrier responsible for delivering this shipment."""

    created_at: datetime
    """The datetime the shipment was created."""

    delivery_estimate: Optional[datetime] = None
    """The estimated delivery date for this shipment.

    Null if the carrier has not provided an estimate.
    """

    payment: Optional[Payment] = None
    """The payment associated with this shipment.

    Null if the payment has been deleted or is inaccessible.
    """

    service: Optional[str] = None
    """The shipping service level used for this shipment.

    Null if the carrier does not specify a service tier.
    """

    status: ShipmentStatus
    """The current delivery status of this shipment."""

    substatus: Optional[ShipmentSubstatus] = None
    """The substatus of a shipment"""

    tracking_code: str
    """The carrier-assigned tracking number used to look up shipment progress."""

    updated_at: datetime
    """The datetime the shipment was last updated."""
