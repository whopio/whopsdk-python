# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .app_type import AppType
from .shared.app_statuses import AppStatuses

__all__ = ["AppListResponse", "Company", "Creator", "Icon"]


class Company(BaseModel):
    """The company that owns and publishes this app."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The display name of the company shown to customers."""


class Creator(BaseModel):
    """The user who created and owns the company that published this app."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class Icon(BaseModel):
    """
    The icon image for this app, displayed on the app store, product pages, checkout, and as the default icon for experiences using this app.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class AppListResponse(BaseModel):
    """An app is an integration built on Whop.

    Apps can serve consumers as experiences within products, or serve companies as business tools.
    """

    id: str
    """The unique identifier for the app."""

    app_type: AppType
    """
    The target audience classification for this app (e.g., 'b2b_app', 'b2c_app',
    'company_app', 'component').
    """

    base_url: Optional[str] = None
    """The production base URL where the app is hosted.

    Null if no base URL is configured.
    """

    company: Company
    """The company that owns and publishes this app."""

    creator: Creator
    """The user who created and owns the company that published this app."""

    dashboard_path: Optional[str] = None
    """
    The URL path template for a specific view of this app, appended to the base
    domain (e.g., '/experiences/[experienceId]'). Null if the specified view type is
    not configured.
    """

    description: Optional[str] = None
    """
    A written description of what this app does, displayed on the app store listing
    page. Null if no description has been set.
    """

    discover_path: Optional[str] = None
    """
    The URL path template for a specific view of this app, appended to the base
    domain (e.g., '/experiences/[experienceId]'). Null if the specified view type is
    not configured.
    """

    domain_id: str
    """The unique subdomain identifier for this app's proxied URL on the Whop platform.

    Forms the URL pattern https://{domain_id}.apps.whop.com.
    """

    experience_path: Optional[str] = None
    """
    The URL path template for a specific view of this app, appended to the base
    domain (e.g., '/experiences/[experienceId]'). Null if the specified view type is
    not configured.
    """

    icon: Optional[Icon] = None
    """
    The icon image for this app, displayed on the app store, product pages,
    checkout, and as the default icon for experiences using this app.
    """

    name: str
    """The display name of this app shown on the app store and in experience
    navigation.

    Maximum 30 characters.
    """

    status: AppStatuses
    """The current visibility status of this app on the Whop app store.

    'live' means publicly discoverable, 'unlisted' means accessible only via direct
    link, and 'hidden' means not visible anywhere.
    """

    verified: bool
    """Whether this app has been verified by Whop.

    Verified apps are endorsed by Whop and displayed in the featured apps section of
    the app store.
    """
