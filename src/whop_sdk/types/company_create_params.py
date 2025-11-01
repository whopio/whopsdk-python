# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompanyCreateParams"]


class CompanyCreateParams(TypedDict, total=False):
    email: Required[str]
    """The email of the user who the company will belong to."""

    parent_company_id: Required[str]
    """The company ID of the platform creating this company."""

    title: Required[str]
    """The name of the company being created."""

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the account"""
