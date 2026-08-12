# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookDeleteResponse"]


class WebhookDeleteResponse(BaseModel):
    id: str
    """The ID of the deleted resource."""

    deleted: bool
    """Always `true`: the resource was deleted."""
