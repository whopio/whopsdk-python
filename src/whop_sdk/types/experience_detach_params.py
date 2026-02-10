# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExperienceDetachParams"]


class ExperienceDetachParams(TypedDict, total=False):
    product_id: Required[str]
    """The unique identifier of the product to detach the experience from."""
