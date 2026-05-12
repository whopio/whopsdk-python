# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PaymentRefundParams"]


class PaymentRefundParams(TypedDict, total=False):
    partial_amount: Optional[float]
    """The amount to refund.

    For multi-currency payments, this is in the charge currency (what the buyer
    paid). For single-currency, this is in the payment currency. If omitted, the
    full payment amount is refunded.
    """
