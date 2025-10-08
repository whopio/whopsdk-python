# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ShipmentSubstatus"]

ShipmentSubstatus: TypeAlias = Literal[
    "address_correction",
    "arrived_at_destination",
    "arrived_at_facility",
    "arrived_at_pickup_location",
    "awaiting_information",
    "substatus_cancelled",
    "damaged",
    "delayed",
    "delivery_exception",
    "departed_facility",
    "departed_origin_facility",
    "expired",
    "substatus_failure",
    "held",
    "substatus_in_transit",
    "label_created",
    "lost",
    "missorted",
    "substatus_out_for_delivery",
    "received_at_destination_facility",
    "received_at_origin_facility",
    "refused",
    "return",
    "status_update",
    "transferred_to_destination_carrier",
    "transit_exception",
    "substatus_unknown",
    "weather_delay",
]
