# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AdGroupUpdateParams"]


class AdGroupUpdateParams(TypedDict, total=False):
    budget: Optional[float]
    """Budget amount in dollars.

    The interpretation (daily or lifetime) follows the ad group's existing budget
    type.
    """

    title: Optional[str]
    """Human-readable ad group title."""
