# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AppCreateParams", "Icon"]


class AppCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """
    The unique identifier of the company to create the app for, starting with
    'biz\\__'.
    """

    name: Required[str]
    """
    The display name for the app, shown to users on the app store and product pages.
    """

    base_url: Optional[str]
    """
    The base production URL where the app is hosted, such as
    'https://myapp.example.com'.
    """

    icon: Optional[Icon]
    """The icon image for the app in PNG, JPEG, or GIF format."""

    redirect_uris: Optional[SequenceNotStr[str]]
    """
    The whitelisted OAuth callback URLs that users are redirected to after
    authorizing the app.
    """


class Icon(TypedDict, total=False):
    """The icon image for the app in PNG, JPEG, or GIF format."""

    id: Required[str]
    """The ID of an existing file object."""
