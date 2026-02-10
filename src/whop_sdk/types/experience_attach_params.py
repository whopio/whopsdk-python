# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExperienceAttachParams"]


class ExperienceAttachParams(TypedDict, total=False):
    product_id: Required[str]
    """The unique identifier of the product to attach the experience to."""
