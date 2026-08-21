# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookReplayDeliveryParams"]


class WebhookReplayDeliveryParams(TypedDict, total=False):
    id: Required[str]

    regenerate_id: bool
    """
    Re-send the delivery under a freshly generated `webhook-id` (in both the
    envelope and the signed headers) instead of the original one. Defaults to false.
    Use this when your endpoint deduplicates on `webhook-id` and you want it to
    process the replay as a new message.
    """
