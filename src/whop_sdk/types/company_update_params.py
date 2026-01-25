# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes

__all__ = ["CompanyUpdateParams", "BannerImage", "Logo"]


class CompanyUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """The banner image for the company in png or jpeg format"""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    logo: Optional[Logo]
    """The logo for the company in png, jpeg, or gif format"""

    send_customer_emails: Optional[bool]
    """Whether Whop sends transactional emails to customers on behalf of this company.

    Includes: order confirmations, payment failures, refund notifications, upcoming
    renewals, and membership cancelations/expirations. When disabled, the platform
    is responsible for handling these communications.
    """

    title: Optional[str]
    """The title of the company"""


class BannerImage(TypedDict, total=False):
    """The banner image for the company in png or jpeg format"""

    id: Required[str]
    """The ID of an existing file object."""


class Logo(TypedDict, total=False):
    """The logo for the company in png, jpeg, or gif format"""

    id: Required[str]
    """The ID of an existing file object."""
