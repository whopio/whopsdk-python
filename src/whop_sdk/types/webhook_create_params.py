# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to send the webhook to."""

    api_version: Literal["v1", "v2", "v5"]
    """The API version for this webhook. Defaults to `v2`."""

    child_resource_events: bool
    """Whether to send events for child resources.

    For example, if the webhook is created for an account, enabling this sends
    events only from its connected accounts.
    """

    enabled: bool
    """Whether or not the webhook is enabled. Defaults to `true`."""

    events: SequenceNotStr[str]
    """
    The events to send the webhook for, in dot form (for example
    `payment.succeeded`).
    """

    resource_id: Optional[str]
    """The account or app to create the webhook for. Defaults to the current account."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
