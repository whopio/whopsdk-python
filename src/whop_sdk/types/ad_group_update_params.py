# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["AdGroupUpdateParams"]


class AdGroupUpdateParams(TypedDict, total=False):
    audience: object
    """Demographic targeting: { automatic, minimum_age, maximum_age, gender }."""

    bid_type: Literal["minimum_cost", "average_target", "maximum_target"]
    """Bid strategy."""

    budget_amount: float
    """Ad-set budget in dollars (ABO only; omit under CBO)."""

    budget_type: Literal["daily", "lifetime"]
    """Whether the budget is daily or lifetime."""

    conversion_event: Union[
        Literal[
            "purchase",
            "add_to_cart",
            "initiated_checkout",
            "add_payment_info",
            "complete_registration",
            "lead",
            "content_view",
            "search",
            "contact",
            "customize_product",
            "donate",
            "find_location",
            "schedule",
            "start_trial",
            "submit_application",
            "subscribe",
        ],
        str,
        None,
    ]
    """The pixel event optimized for.

    A standard event, or any custom pixel event name.
    """

    conversion_location: Literal["website"]
    """Where conversions happen."""

    desired_cost_per_result: float
    """Target/cap cost for average_target / maximum_target."""

    devices: object
    """Device targeting: { platforms, operating_systems: [{ os, minimum_version }] }."""

    ends_at: str
    """Schedule end, ISO 8601."""

    frequency_cap: object
    """{ maximum_impressions, per_days } — only valid for reach optimization."""

    minimum_daily_spend: float
    """Daily spend floor within the budget."""

    optimization_goal: str
    """What the ad group optimizes for (e.g. conversions, link_clicks, reach)."""

    placements: object
    """'automatic' (Advantage+) or a list of { platform, positions }."""

    regions: object
    """Geo targeting: { include / exclude: { countries, cities, zips } }."""

    starts_at: str
    """Schedule start, ISO 8601."""

    status: Literal["active", "paused"]
    """Initial status (default: active)."""

    title: str
    """The display name of the ad group."""
