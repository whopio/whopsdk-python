# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AppCreateParams"]


class AppCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the app for"""

    name: Required[str]
    """The name of the app to be created"""

    base_url: Optional[str]
    """The base URL of the app to be created"""
