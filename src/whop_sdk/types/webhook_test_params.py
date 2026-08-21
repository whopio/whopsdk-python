# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookTestParams"]


class WebhookTestParams(TypedDict, total=False):
    event: Required[str]
    """
    The event to test the webhook for, in dot form (for example
    `payment.succeeded`).
    """
