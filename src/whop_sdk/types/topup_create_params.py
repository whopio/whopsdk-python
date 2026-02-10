# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared.currency import Currency

__all__ = ["TopupCreateParams"]


class TopupCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to add to the balance in the specified currency.

    For example, 50.00 for $50.00 USD.
    """

    company_id: Required[str]
    """The unique identifier of the company to add funds to, starting with 'biz\\__'."""

    currency: Required[Currency]
    """The currency for the top-up amount, such as 'usd'."""

    payment_method_id: Required[str]
    """The unique identifier of the stored payment method to charge for the top-up."""
