# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Shipment", "Checkpoint"]


class Checkpoint(BaseModel):
    """Carrier scan history for this shipment, oldest scan first.

    Empty until the carrier reports its first scan.
    """

    location: Optional[str] = None
    """Where the carrier recorded the scan, such as `PHILADELPHIA, PA`.

    Null when the carrier sent none.
    """

    message: Optional[str] = None
    """Carrier's description of the scan, such as `Departed USPS Regional Facility`.

    Null when the carrier sent none.
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
    """Delivery status this carrier scan maps to."""

    timestamp: Optional[str] = None
    """When the carrier recorded the scan, as an ISO 8601 timestamp.

    Null when the carrier sent no scan time.
    """


class Shipment(BaseModel):
    id: str
    """Shipment ID, prefixed `ship_`."""

    account_id: str
    """The account that owns this shipment, prefixed `biz_`."""

    carrier: Optional[str] = None
    """The shipping carrier detected for this shipment.

    Null until a tracking update identifies it.
    """

    checkpoints: List[Checkpoint]

    created_at: str
    """The datetime the shipment was created (ISO 8601)."""

    payment_id: str
    """The payment this shipment fulfills, prefixed `pay_`."""

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
    """The current delivery status of this shipment."""

    tracking_number: str
    """The carrier-assigned tracking number used to look up shipment progress."""

    tracking_url: str
    """A customer-facing URL to track this shipment's progress."""

    updated_at: str
    """The datetime the shipment was last updated (ISO 8601)."""
