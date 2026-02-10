# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LeadCreateParams"]


class LeadCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """
    The unique identifier of the company to create the lead for, starting with
    'biz\\__'.
    """

    metadata: Optional[Dict[str, object]]
    """A JSON object of custom metadata to attach to the lead for tracking purposes."""

    product_id: Optional[str]
    """
    The unique identifier of the product the lead is interested in, starting with
    'prod\\__'.
    """

    referrer: Optional[str]
    """
    The referral URL that brought the lead to the company, such as
    'https://example.com/landing'.
    """

    user_id: Optional[str]
    """The unique identifier of the user to record as the lead.

    If authenticated as a user, that user is used automatically.
    """
