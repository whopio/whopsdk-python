# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique identifier of the account to list webhooks for."""

    after: str
    """A cursor; returns webhooks after this position."""

    app_id: str
    """Only return webhooks attached to this app.

    Omit to list the account's own webhooks.
    """

    before: str
    """A cursor; returns webhooks before this position."""

    first: int
    """The number of webhooks to return (default 20, max 100)."""

    last: int
    """The number of webhooks to return from the end of the range."""
