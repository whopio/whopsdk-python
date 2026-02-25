# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompanyUpdateParams", "BannerImage", "Logo"]


class CompanyUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """The company's banner image. Accepts PNG or JPEG format."""

    description: Optional[str]
    """
    A promotional pitch displayed to potential customers on the company's store
    page.
    """

    logo: Optional[Logo]
    """The company's logo image. Accepts PNG, JPEG, or GIF format."""

    route: Optional[str]
    """The unique URL slug for the company's store page.

    Must be lowercase and can include hyphens (e.g., 'my-company'). If not provided,
    the route will remain unchanged.
    """

    send_customer_emails: Optional[bool]
    """
    Whether Whop sends transactional emails (receipts, renewals, cancelations) to
    customers on behalf of this company.
    """

    target_audience: Optional[str]
    """
    The target audience for this company (e.g., 'beginner day traders aged 18-25
    looking to learn options').
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
