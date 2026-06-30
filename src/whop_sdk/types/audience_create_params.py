# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AudienceCreateParams"]


class AudienceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that will own the audience."""

    column_mapping: Required[Dict[str, str]]
    """
    Map of identity field (email, phone, first_name, last_name, country) to the CSV
    column header that holds it. Map at least an email or phone column.
    """

    file_id: Required[str]
    """A direct upload ID returned by the standard media upload endpoint."""

    name: Required[str]
    """A display name for the audience."""
