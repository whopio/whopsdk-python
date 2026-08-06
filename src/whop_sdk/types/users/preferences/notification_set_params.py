# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NotificationSetParams", "Preference", "PreferenceScope"]


class NotificationSetParams(TypedDict, total=False):
    preferences: Required[Iterable[Preference]]
    """The preferences to set, at most 100 per request."""


class PreferenceScope(TypedDict, total=False):
    """What the preference applies to.

    `null` on a dimension means the preference is not narrowed there.
    """

    account_id: Optional[str]
    """Account to scope the preference to (member notifications), `biz_` tag."""

    channel: Optional[Literal["in_app", "mobile"]]
    """Delivery channel the preference applies to.

    Required when setting a topic override.
    """

    experience_id: Optional[str]
    """Experience to scope the preference to (`exp_` tag).

    Requires `account_id` when a `topic_id` is also given.
    """

    team_account_id: Optional[str]
    """Account whose team notifications the preference is scoped to, `biz_` tag."""

    topic_id: Optional[str]
    """Notification topic to scope the preference to, `topic_` tag."""


class Preference(TypedDict, total=False):
    level: Required[Optional[Literal["all", "mentions", "nothing"]]]
    """What the user is notified about in this scope.

    `mentions` is only valid for an experience level. `null` clears the preference.
    """

    scope: Required[PreferenceScope]
    """What the preference applies to.

    `null` on a dimension means the preference is not narrowed there.
    """
