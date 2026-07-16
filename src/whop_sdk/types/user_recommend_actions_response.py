# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserRecommendActionsResponse", "Data"]


class Data(BaseModel):
    account_id: Optional[str] = None
    """
    The account (`biz_`) a business recommendation is for, or `null` for personal
    recommendations
    """

    account_name: Optional[str] = None
    """The account's display name, or `null`"""

    action: Literal[
        "create_business",
        "become_affiliate",
        "become_whop_partner",
        "theme_business",
        "create_product",
        "create_plan",
        "verify_identity",
        "connect_affiliate_program",
        "create_promotion",
        "setup_tracking_pixel",
        "migrate_from_stripe",
        "accept_first_payment",
        "launch_first_ad",
        "invite_team_member",
        "enable_tax_collection",
        "create_card",
        "join_whop_university",
        "apply_for_financing",
    ]
    """
    The recommendation; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: str
    """The URL the call-to-action links to"""

    cta_label: str
    """Button label"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """Illustration icon URL, or `null`"""

    impact_score: Optional[int] = None
    """Estimated impact from 0-100, or `null` when not ranked"""

    reasoning: Optional[str] = None
    """Why this action was recommended, or `null`"""

    status: Literal["optional"]
    """Always optional — never blocking"""

    title: str
    """Headline for the recommendation"""


class UserRecommendActionsResponse(BaseModel):
    data: List[Data]
