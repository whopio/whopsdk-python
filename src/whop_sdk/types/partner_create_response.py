# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["PartnerCreateResponse"]


class PartnerCreateResponse(BaseModel):
    referral_link: str
    """
    The caller's referral link — businesses that sign up through it are attributed
    to the caller.
    """

    whop_partner_enabled_at: datetime
    """When the caller became a Whop partner."""
