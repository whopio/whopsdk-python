# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventValidatePixelParams"]


class EventValidatePixelParams(TypedDict, total=False):
    account_id: str
    """Account to check. Defaults to the authenticated account."""

    url: str
    """A page to read for the pixel, e.g.

    an ad destination. Omit it to check the account from its events alone.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
