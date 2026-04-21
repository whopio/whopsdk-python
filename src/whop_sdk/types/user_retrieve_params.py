# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserRetrieveParams"]


class UserRetrieveParams(TypedDict, total=False):
    company_id: Optional[str]
    """
    When provided, returns the user's company-specific profile overrides (name,
    profile picture) instead of their global profile.
    """
