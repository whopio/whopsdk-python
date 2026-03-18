# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AffiliateCreateParams"]


class AffiliateCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the affiliate for."""

    user_identifier: Required[str]
    """The user identifier (username, email, user ID, or Discord ID)."""
