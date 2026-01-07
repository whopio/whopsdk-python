# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LeadCreateParams"]


class LeadCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create a lead for."""

    metadata: Optional[Dict[str, object]]
    """Custom metadata for the lead."""

    product_id: Optional[str]
    """The ID of the product the lead is interested in."""

    referrer: Optional[str]
    """The url referrer of the lead, if any."""

    user_id: Optional[str]
    """The ID of the user to create a lead for.

    If the request is made by a user, that user will be used.
    """
