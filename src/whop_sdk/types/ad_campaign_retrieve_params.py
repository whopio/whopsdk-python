# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AdCampaignRetrieveParams"]


class AdCampaignRetrieveParams(TypedDict, total=False):
    stats_from: str
    """Start of the stats window."""

    stats_to: str
    """End of the stats window."""

    time_zone: str
    """IANA timezone the stats window is interpreted in. Defaults to UTC."""
