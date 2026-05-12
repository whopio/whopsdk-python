# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AdCampaignUpdateParams"]


class AdCampaignUpdateParams(TypedDict, total=False):
    budget: Optional[float]
    """The campaign budget in dollars.

    The interpretation (daily or lifetime) follows the campaign's existing budget
    type.
    """
