# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["NotificationCreateParams"]


class NotificationCreateParams(TypedDict, total=False):
    content: Required[str]
    """Main body text of the notification."""

    title: Required[str]
    """Headline text of the notification."""

    account_id: str
    """Account whose team members receive the notification (`biz_` tag).

    Exactly one of `experience_id` or `account_id` is required.
    """

    experience_id: str
    """Experience whose users receive the notification (`exp_` tag).

    Exactly one of `experience_id` or `account_id` is required.
    """

    icon_user_id: Optional[str]
    """User whose profile picture is used as the notification icon.

    Defaults to the experience or account avatar.
    """

    rest_path: Optional[str]
    """
    Path segment appended to the generated deep link that opens your app, for
    example `/settings/billing`.
    """

    subtitle: Optional[str]
    """Optional secondary line displayed below the title."""

    user_ids: SequenceNotStr[str]
    """Optional `user_` tags narrowing the audience.

    When provided, only these users are notified (as a mention), provided they are
    in the targeted experience or account.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
