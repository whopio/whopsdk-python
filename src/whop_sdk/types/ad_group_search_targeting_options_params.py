# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AdGroupSearchTargetingOptionsParams"]


class AdGroupSearchTargetingOptionsParams(TypedDict, total=False):
    platform: Required[Literal["meta"]]
    """The ad network whose targeting taxonomy to search."""

    account_id: str
    """Account to search on behalf of. Defaults to the authenticated account."""

    country: str
    """Narrow location results to one country, as an ISO 3166-1 code such as `US`.

    Only applies when `types` includes `locations`.
    """

    limit: int
    """Maximum number of results per requested type."""

    location_types: List[Literal["country", "region", "city", "zip"]]
    """Narrow location results to these kinds of places.

    Only applies when `types` includes `locations`.
    """

    query: str
    """The search term.

    Blank browses the fixed lists; interests and locations return nothing without
    one.
    """

    types: List[
        Literal[
            "interests", "behaviors", "life_events", "industries", "income", "family_statuses", "languages", "locations"
        ]
    ]
    """Kinds of targeting options to search. Defaults to all of them."""
