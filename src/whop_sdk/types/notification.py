# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Notification", "Account", "Experience", "ExperienceApp", "Sender", "Topic"]


class Account(BaseModel):
    """Account the notification belongs to.

    `null` when the notification is not associated with an account.
    """

    id: str
    """Account ID, prefixed `biz_`."""

    logo_url: Optional[str] = None
    """Account logo image URL. `null` when the account has not uploaded one."""

    route: Optional[str] = None
    """URL slug of the account's store page on whop.com."""

    title: str
    """Account display name."""


class ExperienceApp(BaseModel):
    """App the experience belongs to."""

    id: str
    """App ID, prefixed `app_`."""

    icon_url: str
    """Icon image URL. Always present — the default app icon when none is uploaded."""


class Experience(BaseModel):
    """Experience the notification is related to.

    `null` when not tied to a specific experience.
    """

    id: str
    """Experience ID, prefixed `exp_`."""

    app: Optional[ExperienceApp] = None
    """App the experience belongs to."""

    name: Optional[str] = None
    """Display name of the experience."""


class Sender(BaseModel):
    """User who triggered the notification. `null` when it was system-generated."""

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    username: str
    """Public username."""


class Topic(BaseModel):
    """
    Topic category the notification belongs to, used for grouping and preference management. `null` when uncategorized.
    """

    id: str
    """Notification topic ID, prefixed `topic_`."""

    default_preference_value: bool
    """
    Whether notifications for this topic are enabled by default when the user has
    not set a preference.
    """

    is_mention: bool
    """Whether this topic exclusively handles mention-based notifications."""

    topic_type: Literal["account", "user", "account_team"]
    """
    Scope of the topic: whether it applies to an account, a user, or an account's
    team.
    """


class Notification(BaseModel):
    id: str
    """Notification ID.

    Feed rows carry a composite id that doubles as the list cursor.
    """

    account: Optional[Account] = None
    """Account the notification belongs to.

    `null` when the notification is not associated with an account.
    """

    attachment_url: str
    """
    Image displayed alongside the notification — the sender's avatar, or the default
    notification image.
    """

    content: str
    """The body text of the notification displayed to the user."""

    created_at: str
    """When the notification was created, as an ISO 8601 timestamp."""

    experience: Optional[Experience] = None
    """Experience the notification is related to.

    `null` when not tied to a specific experience.
    """

    iframe_link: Optional[str] = None
    """
    The same destination on the app's own domain, which the Whop web and mobile
    clients embed instead of navigating to it. Only relevant if you render Whop apps
    yourself. `null` when the notification carries its own `link`.
    """

    link: Optional[str] = None
    """The whop.com page the notification opens, as a normal top-level navigation.

    This is the link to use unless you host Whop apps yourself. `null` when the
    notification has no click-through destination.
    """

    mentions_me: bool
    """Whether the authenticated user was directly mentioned in this notification."""

    rest_path: Optional[str] = None
    """Additional path information appended to the notification's deep link, if any."""

    sender: Optional[Sender] = None
    """User who triggered the notification. `null` when it was system-generated."""

    subject: str
    """The title line of the notification displayed to the user."""

    topic: Optional[Topic] = None
    """
    Topic category the notification belongs to, used for grouping and preference
    management. `null` when uncategorized.
    """
