# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PreferenceUpdateParams"]


class PreferenceUpdateParams(TypedDict, total=False):
    bounty_worker_onboarding_dismissed: bool
    """Whether the user has dismissed the first-time bounty worker onboarding.

    Set to `false` to show it again.
    """

    investigation_enabled: bool
    """Whether investigation mode is enabled for the user.

    Only meaningful for staff users with investigation access.
    """

    terms_accepted: bool
    """Records the user's acceptance of Whop's terms and policies.

    Only `true` is accepted — the server stamps `terms_accepted_at` and acceptance
    cannot be withdrawn here.
    """
