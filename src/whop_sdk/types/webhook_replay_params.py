# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookReplayParams"]


class WebhookReplayParams(TypedDict, total=False):
    sent_after: Required[str]
    """Start of the delivery window to replay, as an ISO 8601 timestamp.

    Clamped to the 30-day delivery retention.
    """

    events: SequenceNotStr[str]
    """Only replay these event types, in dot form (for example `payment.succeeded`).

    Omit to include every event.
    """

    failed_only: bool
    """Only replay messages whose most recent delivery attempt in the window failed.

    Defaults to false. Best-effort: a message whose attempts span processing batches
    can still be re-sent — replays keep the original `webhook-id` by default, so
    consumers that deduplicate are unaffected.
    """

    regenerate_ids: bool
    """
    Re-send each replayed message under a freshly generated `webhook-id` (in both
    the envelope and the signed headers) instead of its original one. Defaults to
    false. Use this when your endpoint deduplicates on `webhook-id` and you want it
    to process the replays as new messages.
    """

    sent_before: str
    """End of the delivery window to replay, as an ISO 8601 timestamp.

    Defaults to now.
    """
