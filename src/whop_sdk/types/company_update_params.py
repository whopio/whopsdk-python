# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .social_link_websites import SocialLinkWebsites

__all__ = ["CompanyUpdateParams", "BannerImage", "Logo", "SocialLink", "SocialLinkImage"]


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

    social_links: Optional[Iterable[SocialLink]]
    """The social media links to display on the company's store page.

    Pass the full list of desired social links — any existing links not included
    will be removed.
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


class SocialLinkImage(TypedDict, total=False):
    """The custom image for the social link"""

    id: Required[str]
    """The ID of an existing file object."""


class SocialLink(TypedDict, total=False):
    """Input for creating a social link for a company"""

    url: Required[str]
    """The URL of the social link"""

    website: Required[SocialLinkWebsites]
    """The website this link is for"""

    image: Optional[SocialLinkImage]
    """The custom image for the social link"""

    order: Optional[str]
    """The order of the social link"""

    title: Optional[str]
    """The title of the social link"""

    website_order: Optional[str]
    """The order of the website social link"""
