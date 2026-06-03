# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import TypedDict

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

    description: Optional[str]
    """A promotional description for the account."""

    featured_affiliate_product_id: Optional[str]
    """The ID of the product to feature for affiliates. Pass null to clear."""

    industry_group: Optional[str]
    """The industry group the account belongs to."""

    industry_type: Optional[str]
    """The specific industry vertical the account operates in."""

    logo: Optional[Dict[str, object]]
    """Attachment input for the account logo."""

    metadata: Dict[str, object]
    """Arbitrary key/value metadata to store on the account."""

    route: Optional[str]
    """The unique URL slug for the account."""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account."""

    social_links: Iterable[Dict[str, object]]
    """The full list of social links to display for the account."""

    target_audience: Optional[str]
    """The target audience for this account."""

    title: Optional[str]
    """The display name of the account."""
