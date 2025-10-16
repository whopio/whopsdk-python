# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared.custom_cta import CustomCta
from .shared.visibility import Visibility
from .shared.business_types import BusinessTypes
from .shared.industry_types import IndustryTypes
from .shared.global_affiliate_status import GlobalAffiliateStatus

__all__ = ["ProductUpdateParams", "BannerImage"]


class ProductUpdateParams(TypedDict, total=False):
    banner_image: Optional[BannerImage]
    """A banner image for the product in png, jpeg format"""

    business_type: Optional[BusinessTypes]
    """The different business types a company can be."""

    collect_shipping_address: Optional[bool]
    """Whether or not to collect shipping information at checkout from the customer."""

    custom_cta: Optional[CustomCta]
    """The different types of custom CTAs that can be selected."""

    custom_cta_url: Optional[str]
    """The custom call to action URL for the product."""

    custom_statement_descriptor: Optional[str]
    """The custom statement descriptor for the product i.e.

    WHOP\\**SPORTS, must be between 5 and 22 characters, contain at least one letter,
    and not contain any of the following characters: <, >, \\,, ', "
    """

    description: Optional[str]
    """A written description of the product."""

    global_affiliate_percentage: Optional[float]
    """The percentage of the revenue that goes to the global affiliate program."""

    global_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for an access pass."""

    headline: Optional[str]
    """The headline of the product."""

    industry_type: Optional[IndustryTypes]
    """The different industry types a company can be in."""

    member_affiliate_percentage: Optional[float]
    """The percentage of the revenue that goes to the member affiliate program."""

    member_affiliate_status: Optional[GlobalAffiliateStatus]
    """The different statuses of the global affiliate program for an access pass."""

    product_tax_code_id: Optional[str]
    """The ID of the product tax code to apply to this product."""

    redirect_purchase_url: Optional[str]
    """The URL to redirect the customer to after a purchase."""

    route: Optional[str]
    """The route of the product."""

    title: Optional[str]
    """The title of the product."""

    visibility: Optional[Visibility]
    """Visibility of a resource"""


class BannerImage(TypedDict, total=False):
    id: Optional[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """

    direct_upload_id: Optional[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """
