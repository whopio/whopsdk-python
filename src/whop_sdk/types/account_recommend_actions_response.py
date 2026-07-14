# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountRecommendActionsResponse", "Data"]


class Data(BaseModel):
    action: Literal[
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
    """
    Estimated revenue impact from 0-100, comparable across accounts, or `null` when
    not ranked
    """

    reasoning: Optional[str] = None
    """Why this action was recommended for this account, or `null`"""

    status: Literal["optional"]
    """Always optional — never blocking"""

    title: str
    """Headline for the recommendation"""


class AccountRecommendActionsResponse(BaseModel):
    data: List[Data]
