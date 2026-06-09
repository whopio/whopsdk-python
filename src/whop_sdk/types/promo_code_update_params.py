# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromoCodeUpdateParams"]


class PromoCodeUpdateParams(TypedDict, total=False):
    status: Required[Literal["active", "inactive"]]
    """The status to apply to the promo code."""
