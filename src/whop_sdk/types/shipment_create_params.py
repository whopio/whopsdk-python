# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ShipmentCreateParams"]


class ShipmentCreateParams(TypedDict, total=False):
    payment_id: Required[str]
    """The payment to attach the shipment to, prefixed `pay_`."""

    tracking_number: Required[str]
    """The carrier-assigned tracking number."""

    account_id: str
    """The unique identifier of the account, prefixed `biz_`."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
