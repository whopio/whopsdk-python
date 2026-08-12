# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PreferenceUpdateResponse"]


class PreferenceUpdateResponse(BaseModel):
    bounty_worker_onboarding_dismissed: bool
    """Whether the user has dismissed the first-time bounty worker onboarding.

    Set to `false` to show it again.
    """

    investigation_enabled: bool
    """Whether investigation mode is enabled for the user.

    Only meaningful for staff users with investigation access.
    """
