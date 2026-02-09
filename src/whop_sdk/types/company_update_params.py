# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes

__all__ = ["CompanyUpdateParams", "BannerImage", "Logo"]


class CompanyUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """The company's banner image. Accepts PNG or JPEG format."""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    description: Optional[str]
    """
    A promotional pitch displayed to potential customers on the company's store
    page.
    """

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    logo: Optional[Logo]
    """The company's logo image. Accepts PNG, JPEG, or GIF format."""

    send_customer_emails: Optional[bool]
    """
    Whether Whop sends transactional emails (receipts, renewals, cancelations) to
    customers on behalf of this company.
    """

    title: Optional[str]
    """The display name of the company shown to customers."""


class BannerImage(TypedDict, total=False):
    """The company's banner image. Accepts PNG or JPEG format."""

    id: Required[str]
    """The ID of an existing file object."""


class Logo(TypedDict, total=False):
    """The company's logo image. Accepts PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
