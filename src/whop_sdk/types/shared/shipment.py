# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .shipment_status import ShipmentStatus
from .shipment_carrier import ShipmentCarrier
from .shipment_substatus import ShipmentSubstatus

__all__ = ["Shipment", "Payment"]


class Payment(BaseModel):
    """The payment of the shipment"""

    id: str
    """The payment ID"""


class Shipment(BaseModel):
    """A shipment"""

    id: str
    """The ID of the shipment"""

    carrier: ShipmentCarrier
    """The carrier of the shipment"""

    created_at: datetime
    """The date and time the shipment was created"""

    delivery_estimate: Optional[datetime] = None
    """The delivery estimate of the shipment"""

    payment: Optional[Payment] = None
    """The payment of the shipment"""

    service: Optional[str] = None
    """The service of the shipment"""

    status: ShipmentStatus
    """The status of the shipment"""

    substatus: Optional[ShipmentSubstatus] = None
    """The substatus of a shipment"""

    tracking_code: str
    """The tracking code of the shipment"""

    updated_at: datetime
    """The date and time the shipment was last updated"""
