# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ResolutionCenterCaseSummaryResponse", "Groups", "GroupsOutcome", "GroupsReason", "GroupsStatus"]


class GroupsOutcome(BaseModel):
    """How many of the matching cases ended each way.

    Every outcome is present, including those with a count of zero; open cases are counted in none of them.
    """

    customer_won: int

    merchant_won: int

    withdrawn: int


class GroupsReason(BaseModel):
    """How many of the matching cases were opened for each reason.

    Every reason is present, including those with a count of zero.
    """

    fraudulent: int

    not_as_described: int

    product_not_received: int

    product_unacceptable: int

    subscription_canceled: int


class GroupsStatus(BaseModel):
    """How many of the matching cases are in each status.

    Every status is present, including those with a count of zero.
    """

    awaiting_customer: int

    awaiting_merchant: int

    closed: int

    under_review: int


class Groups(BaseModel):
    """One entry per requested breakdown, keyed by the field it groups on.

    A field you did not ask for is absent.
    """

    outcome: Optional[GroupsOutcome] = None
    """How many of the matching cases ended each way.

    Every outcome is present, including those with a count of zero; open cases are
    counted in none of them.
    """

    reason: Optional[GroupsReason] = None
    """How many of the matching cases were opened for each reason.

    Every reason is present, including those with a count of zero.
    """

    status: Optional[GroupsStatus] = None
    """How many of the matching cases are in each status.

    Every status is present, including those with a count of zero.
    """


class ResolutionCenterCaseSummaryResponse(BaseModel):
    groups: Groups
    """One entry per requested breakdown, keyed by the field it groups on.

    A field you did not ask for is absent.
    """

    total: int
    """How many cases match the filters."""
