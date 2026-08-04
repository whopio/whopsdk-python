# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdGroupDuplicateParams"]


class AdGroupDuplicateParams(TypedDict, total=False):
    count: int
    """Number of copies to create (1-10). Defaults to 1."""

    preserve_engagement: bool
    """
    Whether the copied ads keep the original posts' engagement (likes, comments,
    shares). Defaults to false.
    """

    target_ad_campaign_id: str
    """Campaign to duplicate into. Defaults to the ad group's own campaign."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
