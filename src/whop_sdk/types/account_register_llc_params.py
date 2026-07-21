# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountRegisterLlcParams", "BusinessInfo", "BusinessInfoAddress", "Founder", "FounderAddress"]


class AccountRegisterLlcParams(TypedDict, total=False):
    business_info: Required[BusinessInfo]
    """The company to form."""

    founders: Required[Iterable[Founder]]
    """The company's founders.

    Exactly one must be marked `is_primary` — the responsible party for the filing.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class BusinessInfoAddress(TypedDict, total=False):
    """Company mailing address. Required unless `use_registered_agent` is `true`."""

    city: Required[str]

    country: Required[str]
    """Two-letter ISO 3166-1 country code, for example `US`."""

    line1: Required[str]
    """First line of the street address."""

    postal_code: Required[str]
    """Postal or ZIP code."""

    state: Required[str]
    """State or region code, for example `CA`."""

    line2: str
    """Second line of the street address."""


class BusinessInfo(TypedDict, total=False):
    """The company to form."""

    business_type: Required[str]
    """High-level business category, from the Whop business taxonomy.

    Valid values are listed on
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary).
    """

    formation_state: Required[
        Literal[
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "DC",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY",
        ]
    ]
    """Two-letter code of the US state (or `DC`) to form the LLC in."""

    industry_group: Required[str]
    """Industry group, from the Whop business taxonomy.

    Valid values are listed on
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary).
    """

    industry_type: Required[str]
    """Specific industry vertical, from the Whop business taxonomy.

    Valid values are listed on
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary).
    """

    legal_name: Required[str]
    """Legal name for the new company."""

    address: BusinessInfoAddress
    """Company mailing address. Required unless `use_registered_agent` is `true`."""

    entity_suffix: Literal["LLC", "L.L.C", "L.L.C.", "Limited Liability Company"]
    """Legal entity ending appended to `legal_name`.

    Defaults to `LLC`; unrecognized values fall back to `LLC`.
    """

    expedite_ein: bool
    """Request expedited EIN processing for an additional fee.

    Available only when no founder supplies an SSN.
    """

    phone: str
    """Business phone number in E.164 format, for example `+12125550100`.

    Required unless `use_registered_agent` is `true`.
    """

    use_registered_agent: bool
    """Use the registered agent's address as the company address instead of `address`."""

    website: str
    """Company website URL."""


class FounderAddress(TypedDict, total=False):
    """Founder's personal address."""

    city: Required[str]

    country: Required[str]
    """Two-letter ISO 3166-1 country code, for example `US`."""

    line1: Required[str]
    """First line of the street address."""

    postal_code: Required[str]
    """Postal or ZIP code."""

    state: Required[str]
    """State or region code, for example `CA`."""

    line2: str
    """Second line of the street address."""


class Founder(TypedDict, total=False):
    address: Required[FounderAddress]
    """Founder's personal address."""

    email: Required[str]

    first_name: Required[str]

    is_primary: Required[bool]
    """Marks the responsible party for the filing.

    Exactly one founder must be primary.
    """

    last_name: Required[str]

    ownership_percentage: Required[float]
    """The founder's ownership share: greater than `0`, at most `100`.

    Shares across founders must total `100`.
    """

    phone: Required[str]
    """Phone number in E.164 format, for example `+12125550100`."""

    date_of_birth: str
    """Formatted as `YYYY-MM-DD`."""

    ssn: str
    """The founder's US Social Security Number.

    Leave empty if the founder is not a US resident. Non-US founders can request
    expedited EIN processing via the `expedite_ein` option in `business_info`.
    """
