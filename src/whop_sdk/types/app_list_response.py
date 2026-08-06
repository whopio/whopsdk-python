# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AppListResponse", "Account", "Creator", "Icon"]


class Account(BaseModel):
    """The account that owns the app."""

    id: str
    """Account ID, prefixed `biz_`."""

    title: str
    """Account display name."""


class Creator(BaseModel):
    """The user who owns the publishing account."""

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    username: str
    """Public username."""


class Icon(BaseModel):
    """The app's icon. Falls back to the default app icon when none is uploaded."""

    url: str
    """Icon image URL. Always present — the default app icon when none is uploaded."""


class AppListResponse(BaseModel):
    id: str
    """App ID, prefixed `app_`."""

    account: Account
    """The account that owns the app."""

    app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"]
    """The type of end-user the app is built for."""

    base_url: Optional[str] = None
    """Production base URL where the app is hosted, or `null` if none is configured."""

    creator: Creator
    """The user who owns the publishing account."""

    dashboard_path: Optional[str] = None
    """URL path for the account dashboard view, or `null` when not configured."""

    description: Optional[str] = None
    """
    Short description shown in listings and search results, or `null` if none has
    been set.
    """

    discover_path: Optional[str] = None
    """URL path for the discover view, or `null` when not configured."""

    domain_id: str
    """
    Subdomain identifier for the app's proxied URL, forming
    https://{domain_id}.apps.whop.com.
    """

    experience_path: Optional[str] = None
    """URL path for the member-facing hub view, or `null` when not configured."""

    hosted_url: Optional[str] = None
    """
    Full URL where the app's hosted web build is served, or `null` if no route is
    claimed.
    """

    icon: Icon
    """The app's icon. Falls back to the default app icon when none is uploaded."""

    name: str
    """Display name shown on the app store and in experience navigation."""

    openapi_path: Optional[str] = None
    """URL path to the app's OpenAPI spec file, or `null` when not configured."""

    origin: Optional[str] = None
    """
    Full origin URL of the app's proxied domain, for example
    https://ab1c2d3e4f.apps.whop.com.
    """

    route: Optional[str] = None
    """
    Claimed subdomain route where hosted web builds are served (`myapp` for
    myapp.whop.app), or `null` if no route is claimed.
    """

    skills_path: Optional[str] = None
    """URL path to the app's skills directory, or `null` when not configured."""

    status: Literal["live", "unlisted", "hidden"]
    """
    Visibility on the Whop app store: `live` is publicly discoverable, `unlisted` is
    accessible only via direct link, `hidden` is not visible anywhere.
    """

    verified: bool
    """
    Whether the app has been verified by Whop and is eligible for the featured apps
    section.
    """
