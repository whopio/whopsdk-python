# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PreferenceRetrieveResponse"]


class PreferenceRetrieveResponse(BaseModel):
    bounty_worker_onboarding_dismissed: bool
    """Whether the user has dismissed the first-time bounty worker onboarding.

    Set to `false` to show it again.
    """

    investigation_enabled: bool
    """Whether investigation mode is enabled for the user.

    Only meaningful for staff users with investigation access.
    """

    terms_accepted: bool
    """Whether the user has accepted Whop's terms and policies.

    `false` until recorded via `PATCH` with `terms_accepted: true`.
    """

    terms_accepted_at: Optional[str] = None
    """
    When the user most recently accepted Whop's terms and policies, as an ISO 8601
    timestamp. `null` until accepted.
    """
