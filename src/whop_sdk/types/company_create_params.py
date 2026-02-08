# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes

__all__ = ["CompanyCreateParams", "Logo"]


class CompanyCreateParams(TypedDict, total=False):
    title: Required[str]
    """The name of the company being created."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    description: Optional[str]
    """A description of what the company offers or does."""

    email: Optional[str]
    """The email of the user who the sub-company will belong to.

    Required when parent_company_id is provided.
    """

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    logo: Optional[Logo]
    """The logo for the company in png, jpeg, or gif format"""

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the company"""

    parent_company_id: Optional[str]
    """The company ID of the platform creating this sub-company.

    If omitted, the company is created for the current user.
    """

    send_customer_emails: Optional[bool]
    """Whether Whop sends transactional emails to customers on behalf of this company.

    Only used when parent_company_id is provided.
    """


class Logo(TypedDict, total=False):
    """The logo for the company in png, jpeg, or gif format"""

    id: Required[str]
    """The ID of an existing file object."""
