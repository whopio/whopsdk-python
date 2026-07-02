# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AdRetrieveParams"]


class AdRetrieveParams(TypedDict, total=False):
    stats_from: str
    """Start of the stats window."""

    stats_to: str
    """End of the stats window."""
