# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.authorized_user_roles import AuthorizedUserRoles

__all__ = ["AuthorizedUserCreateParams", "Elevation"]


class AuthorizedUserCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to add the authorized user to."""

    role: Required[AuthorizedUserRoles]
    """The role to assign to the authorized user within the company.

    Supported roles: 'moderator', 'sales_manager'.
    """

    user_id: Required[str]
    """The ID of the user to add as an authorized user."""

    elevation: Optional[Elevation]
    """Re-authentication proof required to perform this sensitive action."""

    send_emails: Optional[bool]
    """Whether to send notification emails to the user on creation."""


class Elevation(TypedDict, total=False):
    """Re-authentication proof required to perform this sensitive action."""

    authenticator_data: Optional[str]
    """The WebAuthn authenticator data (base64)."""

    client_data_json: Optional[str]
    """The WebAuthn client data JSON (base64)."""

    credential_id: Optional[str]
    """The WebAuthn credential ID (base64)."""

    email_code: Optional[str]
    """The 6-digit code emailed to the user."""

    signature: Optional[str]
    """The WebAuthn signature (base64)."""

    totp_code: Optional[str]
    """The 6-digit code from the authenticator app or SMS."""

    use_finance_session: Optional[bool]
    """Reuse an existing elevated session (for SMS/email 2FA users)."""
