# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AdRetrieveParams"]


class AdRetrieveParams(TypedDict, total=False):
    attribution_model: Literal["last_touch", "first_touch"]
    """Attribution model the conversion stats count under (defaults to last_touch).

    Under both models a journey with any whop ad touch attributes to whop; the model
    picks which whop touch credits the entity and which non-whop source wins
    otherwise.
    """

    stats_from: str
    """Start of the stats window."""

    stats_to: str
    """End of the stats window."""

    time_zone: str
    """IANA timezone the stats window is interpreted in. Defaults to UTC."""
