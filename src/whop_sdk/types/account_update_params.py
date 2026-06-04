# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    affiliate_application_required: bool
    """
    Whether prospective affiliates must submit an application before promoting this
    account.
    """

    affiliate_instructions: Optional[str]
    """Guidelines shown to affiliates promoting this account."""

    banner_image: Optional[Dict[str, object]]
    """Attachment input for the account banner image."""

    business_type: Optional[str]
    """The high-level business category for the account."""

    country: Optional[str]
    """The country the account is located in."""

    description: Optional[str]
    """A promotional description for the account."""

    featured_affiliate_product_id: Optional[str]
    """The ID of the product to feature for affiliates. Pass null to clear."""

    home_preferences: SequenceNotStr[str]
    """Preferences for the public business home page."""

    industry_group: Optional[str]
    """The industry group the account belongs to."""

    industry_type: Optional[str]
    """The specific industry vertical the account operates in."""

    invoice_prefix: Optional[str]
    """The prefix to use for account invoices."""

    logo: Optional[Dict[str, object]]
    """Attachment input for the account logo."""

    metadata: Dict[str, object]
    """Arbitrary key/value metadata to store on the account."""

    onboarding_type: Optional[str]
    """The type of onboarding the account has completed."""

    opengraph_image: Optional[Dict[str, object]]
    """Attachment input for the account Open Graph image."""

    opengraph_image_variant: Optional[str]
    """The account Open Graph image variant."""

    other_business_description: Optional[str]
    """The description of the business type when business_type is other."""

    other_industry_description: Optional[str]
    """The description of the industry type when industry_type is other."""

    require_2fa: bool
    """
    Whether the account requires authorized users to have two-factor authentication
    enabled.
    """

    route: Optional[str]
    """The unique URL slug for the account."""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account."""

    show_joined_whops: bool
    """Whether the account appears in joined whops on other accounts."""

    show_reviews_dtc: bool
    """Whether reviews are displayed on direct-to-consumer product pages."""

    show_user_directory: bool
    """Whether the account shows users in the user directory."""

    social_links: Iterable[Dict[str, object]]
    """The full list of social links to display for the account."""

    store_page_config: Optional[Dict[str, object]]
    """Store page display configuration for the account."""

    target_audience: Optional[str]
    """The target audience for this account."""

    title: Optional[str]
    """The display name of the account."""

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image."""
