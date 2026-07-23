# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookListDeliveriesParams"]


class WebhookListDeliveriesParams(TypedDict, total=False):
    after: str
    """A cursor; returns deliveries after this position."""

    first: int
    """The number of deliveries to return (default 50, max 100)."""
