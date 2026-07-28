# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["TopicListResponse", "Scope"]


class Scope(BaseModel):
    """What the preference applies to.

    Echo it back to `PATCH /users/me/preferences/notifications` to change this preference.
    """

    account_id: Optional[str] = None
    """Account the preference is scoped to (member notifications), prefixed `biz_`."""

    channel: Optional[Literal["in_app", "mobile"]] = None
    """Delivery channel the preference applies to. `null` applies to every channel."""

    experience_id: Optional[str] = None
    """Experience the preference is scoped to, prefixed `exp_`."""

    team_account_id: Optional[str] = None
    """Account whose team notifications the preference is scoped to, prefixed `biz_`."""

    topic_id: Optional[str] = None
    """Notification topic the preference is scoped to, prefixed `topic_`."""


class TopicListResponse(BaseModel):
    id: str
    """Notification preference ID, prefixed `unpf_`."""

    created_at: str
    """When the preference was created, as an ISO 8601 timestamp."""

    level: Literal["all", "nothing"]
    """What the user is notified about in this scope: `all` or `nothing`."""

    object: Literal["notification_preference"]
    """The type of object. Always `notification_preference`."""

    scope: Scope
    """What the preference applies to.

    Echo it back to `PATCH /users/me/preferences/notifications` to change this
    preference.
    """

    updated_at: str
    """When the preference was last changed, as an ISO 8601 timestamp."""
