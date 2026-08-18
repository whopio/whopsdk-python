# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list webhooks for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    app_id: str
    """Only return webhooks attached to this app.

    Omit to list the company's own webhooks.
    """

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""
