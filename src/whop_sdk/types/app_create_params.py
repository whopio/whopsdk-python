# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AppCreateParams", "Icon"]


class AppCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the company to create the app for"""

    name: Required[str]
    """The name of the app to be created"""

    base_url: Optional[str]
    """The base URL of the app to be created"""

    icon: Optional[Icon]
    """The icon for the app in png, jpeg, or gif format"""


class Icon(TypedDict, total=False):
    """The icon for the app in png, jpeg, or gif format"""

    id: Required[str]
    """The ID of an existing file object."""
