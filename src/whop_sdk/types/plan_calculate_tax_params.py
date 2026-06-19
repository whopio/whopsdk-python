# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PlanCalculateTaxParams", "Address", "TaxID"]


class PlanCalculateTaxParams(TypedDict, total=False):
    address: Optional[Address]
    """The buyer's billing address. Provide this or ip_address."""

    ip_address: str
    """
    The buyer's IP address, used to resolve their location when no address is
    provided.
    """

    tax_ids: Optional[Iterable[TaxID]]
    """
    The buyer's tax IDs, such as a VAT number, used to apply B2B reverse-charge
    exemptions.
    """


class Address(TypedDict, total=False):
    """The buyer's billing address. Provide this or ip_address."""

    country: Required[str]
    """The two-letter ISO 3166-1 country code, for example US, DE, or GB."""

    city: Optional[str]
    """The city name."""

    line1: Optional[str]
    """The first line of the street address."""

    line2: Optional[str]
    """The second line of the street address."""

    postal_code: Optional[str]
    """The postal or ZIP code."""

    state: Optional[str]
    """The state, province, or region code, for example CA."""


class TaxID(TypedDict, total=False):
    type: str
    """The tax ID type, for example eu_vat."""

    value: str
    """The tax ID number, for example DE123456789."""
