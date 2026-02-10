# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "NotificationCreateParams",
    "SendNotificationV2InputWithCompanyID",
    "SendNotificationV2InputWithExperienceID",
]


class SendNotificationV2InputWithCompanyID(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to target.

    Only team members of this company will receive the notification. Clicking the
    notification opens your dashboard app view.
    """

    content: Required[str]
    """The main body text of the notification displayed to the user."""

    title: Required[str]
    """The headline text of the notification, displayed prominently to the user."""

    icon_user_id: Optional[str]
    """
    The unique identifier of a user whose profile picture will be used as the
    notification icon. Defaults to the experience or company avatar when not
    provided.
    """

    rest_path: Optional[str]
    """A path segment appended to the generated deep link that opens your app.

    Use [restPath] in your app path configuration to read this parameter. For
    example, '/settings/billing'.
    """

    subtitle: Optional[str]
    """
    An optional secondary line of text displayed below the title in the
    notification.
    """

    user_ids: Optional[SequenceNotStr[str]]
    """An optional list of user IDs to narrow the audience.

    When provided, only these users receive the notification, provided they are in
    the targeted experience or company.
    """


class SendNotificationV2InputWithExperienceID(TypedDict, total=False):
    content: Required[str]
    """The main body text of the notification displayed to the user."""

    experience_id: Required[str]
    """The unique identifier of the experience to target.

    All users with access to this experience will receive the notification. Clicking
    the notification opens the experience view.
    """

    title: Required[str]
    """The headline text of the notification, displayed prominently to the user."""

    icon_user_id: Optional[str]
    """
    The unique identifier of a user whose profile picture will be used as the
    notification icon. Defaults to the experience or company avatar when not
    provided.
    """

    rest_path: Optional[str]
    """A path segment appended to the generated deep link that opens your app.

    Use [restPath] in your app path configuration to read this parameter. For
    example, '/settings/billing'.
    """

    subtitle: Optional[str]
    """
    An optional secondary line of text displayed below the title in the
    notification.
    """

    user_ids: Optional[SequenceNotStr[str]]
    """An optional list of user IDs to narrow the audience.

    When provided, only these users receive the notification, provided they are in
    the targeted experience or company.
    """


NotificationCreateParams: TypeAlias = Union[
    SendNotificationV2InputWithCompanyID, SendNotificationV2InputWithExperienceID
]
