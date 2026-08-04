# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdDuplicateParams"]


class AdDuplicateParams(TypedDict, total=False):
    count: int
    """Number of copies to create (1-10). Defaults to 1."""

    preserve_engagement: bool
    """Whether the copies keep the original post's engagement (likes, comments,
    shares).

    Defaults to false.
    """

    target_ad_group_id: str
    """Ad group to duplicate into. Defaults to the ad's own ad group."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
