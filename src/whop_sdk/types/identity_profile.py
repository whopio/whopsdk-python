# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = ["IdentityProfile", "BusinessAddress", "LinkedCompany", "PersonalAddress", "Verification"]


class BusinessAddress(BaseModel):
    """Registered business address reported by the identity provider.

    Present on `business` profiles.
    """

    city: Optional[str] = None
    """The city of the address."""

    country: Optional[str] = None
    """The country of the address."""

    line1: Optional[str] = None
    """The line 1 of the address."""

    line2: Optional[str] = None
    """The line 2 of the address."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    state: Optional[str] = None
    """The state of the address."""


class LinkedCompany(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class PersonalAddress(BaseModel):
    """Residential address reported by the identity provider.

    Present on `individual` profiles.
    """

    city: Optional[str] = None
    """The city of the address."""

    country: Optional[str] = None
    """The country of the address."""

    line1: Optional[str] = None
    """The line 1 of the address."""

    line2: Optional[str] = None
    """The line 2 of the address."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    state: Optional[str] = None
    """The state of the address."""


class Verification(BaseModel):
    """
    An identity verification session used to confirm a person or entity's identity for payout account eligibility.
    """

    id: str
    """The numeric id of the verification record."""

    created_at: datetime
    """When the verification record was created."""

    last_error_code: Optional[VerificationErrorCode] = None
    """An error code for a verification attempt."""

    last_error_reason: Optional[str] = None
    """A human-readable explanation of the most recent verification error.

    Null if no error has occurred.
    """

    session_url: Optional[str] = None
    """A URL the user can visit to complete the verification process.

    Null if the session does not require user interaction.
    """

    status: VerificationStatus
    """The current status of this verification session."""


class IdentityProfile(BaseModel):
    """
    A consolidated identity or business profile synced from verification provider data.
    """

    id: str
    """The tag of the identity profile (idpf_xxx)."""

    business_address: Optional[BusinessAddress] = None
    """Registered business address reported by the identity provider.

    Present on `business` profiles.
    """

    business_name: Optional[str] = None
    """Business entity name. Present on `business` profiles."""

    business_structure: Optional[str] = None
    """Reported legal structure of a business profile (e.g.

    `corp`, `llc`). Provider-specific values; present on `business` profiles.
    """

    country: Optional[str] = None
    """ISO 3166-1 alpha-3 country code (e.g.

    `USA`, `GBR`). For individuals this is the country of citizenship or residence
    reported by the identity provider; for businesses this is the country of
    incorporation.
    """

    created_at: datetime
    """When the identity profile was first created."""

    date_of_birth: Optional[str] = None
    """ISO date (`YYYY-MM-DD`) reported by the identity provider.

    Present on `individual` profiles.
    """

    email: Optional[str] = None
    """Email address reported by the identity provider.

    Typically present on `individual` profiles.
    """

    first_name: Optional[str] = None
    """Individual's first name."""

    last_name: Optional[str] = None
    """Individual's last name."""

    linked_companies: List[LinkedCompany]
    """The companies this identity profile is currently linked to.

    Only populated for direct Whop user sessions; always empty when authenticated
    via API key, app, or OAuth scope (a single identity can be linked to companies
    the calling platform is not entitled to see).
    """

    personal_address: Optional[PersonalAddress] = None
    """Residential address reported by the identity provider.

    Present on `individual` profiles.
    """

    phone: Optional[str] = None
    """Phone number reported by the identity provider.

    Typically present on `individual` profiles.
    """

    profile_type: str
    """Whether this is an 'individual' or 'business' profile."""

    status: Literal["not_started", "pending", "approved", "rejected"]
    """Derived verification status across all linked verifications."""

    updated_at: datetime
    """When the identity profile was last synced from a verification."""

    verifications: List[Verification]
    """
    All verification attempts attached to this identity profile, ordered most-recent
    first.
    """
