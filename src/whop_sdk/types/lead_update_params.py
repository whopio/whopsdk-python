# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["LeadUpdateParams"]


class LeadUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, object]]
    """
    A JSON object of custom metadata to set on the lead, replacing any existing
    metadata.
    """

    referrer: Optional[str]
    """The updated referral URL for the lead, such as 'https://example.com/landing'."""
