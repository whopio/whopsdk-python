# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MembershipInviteResponse"]


class MembershipInviteResponse(BaseModel):
    invitation_sent: bool
