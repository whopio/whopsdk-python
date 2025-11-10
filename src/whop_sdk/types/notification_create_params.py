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
    """The id of the company to target.

    Only team members of this company will receive the notification. When clicked
    will take the user to your dashboard app view.
    """

    content: Required[str]
    """The content of the notification"""

    title: Required[str]
    """The title of the notification"""

    icon_user_id: Optional[str]
    """
    Optional: ID of a Whop user whose profile picture will be used as the
    notification icon. If not provided, defaults to the experience or company
    avatar.
    """

    rest_path: Optional[str]
    """The rest path to append to the generated deep link that opens your app.

    Use [restPath] in your app path in the dashboard to read this parameter.
    """

    subtitle: Optional[str]
    """The subtitle of the notification"""

    user_ids: Optional[SequenceNotStr[str]]
    """
    If provided, this will only send to these users if they are also in the main
    scope (experience or company)
    """


class SendNotificationV2InputWithExperienceID(TypedDict, total=False):
    content: Required[str]
    """The content of the notification"""

    experience_id: Required[str]
    """The id of the experience to target.

    All users with access to this experience (customers and admins) will receive the
    notification. When clicked, open your experience view.
    """

    title: Required[str]
    """The title of the notification"""

    icon_user_id: Optional[str]
    """
    Optional: ID of a Whop user whose profile picture will be used as the
    notification icon. If not provided, defaults to the experience or company
    avatar.
    """

    rest_path: Optional[str]
    """The rest path to append to the generated deep link that opens your app.

    Use [restPath] in your app path in the dashboard to read this parameter.
    """

    subtitle: Optional[str]
    """The subtitle of the notification"""

    user_ids: Optional[SequenceNotStr[str]]
    """
    If provided, this will only send to these users if they are also in the main
    scope (experience or company)
    """


NotificationCreateParams: TypeAlias = Union[
    SendNotificationV2InputWithCompanyID, SendNotificationV2InputWithExperienceID
]
