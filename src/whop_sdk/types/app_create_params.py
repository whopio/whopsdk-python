# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AppCreateParams", "Icon"]


class AppCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The display name for the app, shown to users on the app store and product pages.
    """

    account_id: str
    """The account to create the app for (`biz_` tag).

    Defaults to the account behind the presented credential.
    """

    base_url: Optional[str]
    """
    The base production URL where the app is hosted, such as
    `https://myapp.example.com`.
    """

    icon: Icon
    """
    The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded
    file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new
    direct upload.
    """

    redirect_uris: SequenceNotStr[str]
    """
    The whitelisted OAuth callback URLs that users are redirected to after
    authorizing the app.
    """

    route: Optional[str]
    """
    The subdomain route where the app's hosted web builds are served, such as
    `myapp` for myapp.whop.app.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Icon(TypedDict, total=False):
    """
    The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new direct upload.
    """

    id: str
    """The tag of an already-uploaded attachment."""

    direct_upload_id: str
    """The signed id of a completed direct upload."""
