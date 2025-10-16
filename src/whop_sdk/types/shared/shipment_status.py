# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ShipmentStatus"]

ShipmentStatus: TypeAlias = Literal[
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
