# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PaymentMethodRetrieveParams"]


class PaymentMethodRetrieveParams(TypedDict, total=False):
    company_id: Optional[str]
    """The unique identifier of the company.

    Provide either this or member_id, not both.
    """

    member_id: Optional[str]
    """The unique identifier of the member.

    Provide either this or company_id, not both.
    """
