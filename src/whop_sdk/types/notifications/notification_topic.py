# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NotificationTopic"]


class NotificationTopic(BaseModel):
    id: str
    """Notification topic ID, prefixed `topic_`.

    This is the value the notification preference endpoints take as `topic_id`.
    """

    default_preference_value: bool
    """
    Whether notifications for this topic are enabled by default when the user has
    not set a preference.
    """

    description: Optional[str] = None
    """Human-readable explanation of what notifications in this topic are about.

    `null` when no description has been set.
    """

    identifier: str
    """Stable, human-readable name for the category, such as `new-follower`.

    Unlike `id`, it is the same in every environment, which makes it the value to
    match on in code and to read in logs. Treat it as an opaque string: the set is
    open and the casing is historical rather than normalized.
    """

    is_mention: bool
    """Whether this topic exclusively handles mention-based notifications."""

    name: str
    """Display name shown in notification preference settings."""

    topic_type: Literal["account", "user", "account_team"]
    """
    Scope of the topic: whether it applies to an account, a user, or an account's
    team.
    """
