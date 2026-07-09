# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AudienceCreateParams", "ColumnMapping"]


class AudienceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    column_mapping: Required[ColumnMapping]
    """Maps supported identity fields to CSV column headers.

    Map at least one of `email` or `phone`.
    """

    file_id: Required[str]
    """Direct upload ID from the standard media upload endpoint."""

    name: Required[str]
    """Audience display name."""


class ColumnMapping(TypedDict, total=False):
    """Maps supported identity fields to CSV column headers.

    Map at least one of `email` or `phone`.
    """

    country: str
    """CSV header for ISO 3166-1 alpha-2 country codes, such as `US`."""

    email: str
    """CSV header for email addresses."""

    first_name: str
    """CSV header for first names."""

    last_name: str
    """CSV header for last names."""

    phone: str
    """CSV header for phone numbers."""
