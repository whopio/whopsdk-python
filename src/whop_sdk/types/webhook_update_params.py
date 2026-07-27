# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    api_version: Literal["v1", "v2", "v5"]
    """The API version for this webhook."""

    child_resource_events: bool
    """Whether or not to send events for child resources."""

    enabled: bool
    """Whether or not the webhook is enabled."""

    events: SequenceNotStr[str]
    """
    The events to send the webhook for, in dot form (for example
    `payment.succeeded`).
    """

    url: str
    """The URL to send the webhook to."""
