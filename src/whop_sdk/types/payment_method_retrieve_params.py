# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaymentMethodRetrieveParams"]


class PaymentMethodRetrieveParams(TypedDict, total=False):
    account_id: str
    """The unique identifier of the company.

    Provide either this or member_id, not both. Omit both to address your own saved
    payment methods.
    """

    member_id: str
    """The unique identifier of the member.

    Provide either this or account_id, not both. Omit both to address your own saved
    payment methods.
    """
