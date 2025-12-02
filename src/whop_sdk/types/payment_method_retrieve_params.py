# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentMethodRetrieveParams"]


class PaymentMethodRetrieveParams(TypedDict, total=False):
    member_id: Required[str]
    """The ID of the Member associated with the PaymentMethod"""
