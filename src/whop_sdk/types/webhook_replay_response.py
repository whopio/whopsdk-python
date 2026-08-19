# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookReplayResponse"]


class WebhookReplayResponse(BaseModel):
    queued: bool
    """Whether the replay was accepted.

    Watch the webhook's delivery log for the re-sends.
    """
