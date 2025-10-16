# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PaymentRefundParams"]


class PaymentRefundParams(TypedDict, total=False):
    partial_amount: Optional[float]
    """An amount if the refund is supposed to be partial."""
