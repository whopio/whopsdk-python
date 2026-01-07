# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["LeadUpdateParams"]


class LeadUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, object]]
    """Custom metadata for the lead."""

    referrer: Optional[str]
    """The url referrer of the lead."""
