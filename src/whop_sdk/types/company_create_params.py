# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes

__all__ = ["CompanyCreateParams", "Logo"]


class CompanyCreateParams(TypedDict, total=False):
    title: Required[str]
    """The display name of the company shown to customers."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    description: Optional[str]
    """
    A promotional pitch displayed to potential customers on the company's store
    page.
    """

    email: Optional[str]
    """The email address of the user who will own the connected account.

    Required when parent_company_id is provided.
    """

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    logo: Optional[Logo]
    """The company's logo image. Accepts PNG, JPEG, or GIF format."""

    metadata: Optional[Dict[str, object]]
    """A key-value JSON object of custom metadata to store on the company."""

    parent_company_id: Optional[str]
    """The unique identifier of the parent platform company.

    When provided, creates a connected account under that platform. Omit to create a
    company for the current user.
    """

    send_customer_emails: Optional[bool]
    """Whether Whop sends transactional emails to customers on behalf of this company.

    Only applies when creating a connected account.
    """


class Logo(TypedDict, total=False):
    """The company's logo image. Accepts PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
