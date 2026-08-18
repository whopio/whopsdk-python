# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NotificationSetResponse", "Data", "DataScope"]


class DataScope(BaseModel):
    """The scope that was written, resolved.

    `null` on a dimension means the preference is not narrowed there.
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


class Data(BaseModel):
    level: Optional[Literal["all", "mentions", "nothing"]] = None
    """
    What the user is now notified about in this scope, or `null` if the preference
    was cleared and the scope inherits its default again.
    """

    object: Literal["notification_preference", "experience_notification_preference"]
    """
    Which kind of preference was written: `experience_notification_preference` for
    an experience level, `notification_preference` for a topic override.
    """

    scope: DataScope
    """The scope that was written, resolved.

    `null` on a dimension means the preference is not narrowed there.
    """


class NotificationSetResponse(BaseModel):
    data: List[Data]
