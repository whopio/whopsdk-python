# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["DisputeSummaryResponse", "Groups", "GroupsStatus"]


class GroupsStatus(BaseModel):
    """How many of the matching disputes are in each status.

    Every status is present, including those with a count of zero.
    """

    closed: int

    lost: int

    needs_response: int

    under_review: int

    won: int


class Groups(BaseModel):
    """One entry per requested breakdown, keyed by the field it groups on.

    A field you did not ask for is absent.
    """

    currency: Optional[Dict[str, int]] = None
    """
    How many of the matching disputes are in each currency, keyed by three-letter
    ISO code. Only currencies with at least one dispute are present.
    """

    status: Optional[GroupsStatus] = None
    """How many of the matching disputes are in each status.

    Every status is present, including those with a count of zero.
    """


class DisputeSummaryResponse(BaseModel):
    groups: Groups
    """One entry per requested breakdown, keyed by the field it groups on.

    A field you did not ask for is absent.
    """

    total: int
    """How many disputes match the filters."""
