# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NotificationMarkReadParams"]


class NotificationMarkReadParams(TypedDict, total=False):
    all: bool
    """Pass `true` to mark every notification read.

    Exactly one of `experience_id` or `all` is required.
    """

    experience_id: str
    """Experience to mark read (`exp_` tag).

    Exactly one of `experience_id` or `all` is required.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
