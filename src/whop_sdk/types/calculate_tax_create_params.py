# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CalculateTaxCreateParams", "CustomerDetails", "CustomerDetailsAddress", "CustomerDetailsTaxID", "LineItem"]


class CalculateTaxCreateParams(TypedDict, total=False):
    checkout_configuration_id: Required[str]
    """The ID of the checkout configuration (ch\\__\\**)."""

    customer_details: Required[CustomerDetails]
    """Buyer location.

    ip_address is required; address provides more precise tax calculation.
    """

    line_items: Required[Iterable[LineItem]]
    """Items to calculate tax for. Currently supports exactly one item."""


class CustomerDetailsAddress(TypedDict, total=False):
    city: Optional[str]
    """City name."""

    country: str
    """ISO 3166-1 alpha-2 country code."""

    line1: Optional[str]
    """Street address line 1."""

    line2: Optional[str]
    """Street address line 2."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code."""


class CustomerDetailsTaxID(TypedDict, total=False):
    type: str
    """Tax ID type (e.g. eu_vat)."""

    value: str
    """Tax ID value."""


class CustomerDetails(TypedDict, total=False):
    """Buyer location.

    ip_address is required; address provides more precise tax calculation.
    """

    address: Optional[CustomerDetailsAddress]

    ip_address: str
    """Buyer's IP address for tax resolution."""

    tax_ids: Optional[Iterable[CustomerDetailsTaxID]]
    """Tax identification numbers for B2B exemptions."""


class LineItem(TypedDict, total=False):
    amount: Required[int]
    """Amount in smallest currency unit (e.g. cents)."""

    reference: Optional[str]
    """Caller-provided identifier echoed back in the response."""
