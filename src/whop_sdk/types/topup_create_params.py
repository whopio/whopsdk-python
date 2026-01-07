# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared.currency import Currency

__all__ = ["TopupCreateParams"]


class TopupCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to add to the balance."""

    company_id: Required[str]
    """The ID of the company to add funds to."""

    currency: Required[Currency]
    """The currency of the top-up."""

    payment_method_id: Required[str]
    """The ID of the payment method to charge for the top-up."""
