# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..app_type import AppType
from .app_statuses import AppStatuses

__all__ = [
    "App",
    "APIKey",
    "Company",
    "Creator",
    "Icon",
    "RequestedPermission",
    "RequestedPermissionPermissionAction",
    "Stats",
]


class APIKey(BaseModel):
    """The API key used to authenticate requests on behalf of this app.

    Null if no API key has been generated. Requires the 'developer:manage_api_key' permission.
    """

    id: str
    """The unique identifier for the private api key."""

    token: str
    """This is the API key used to authenticate requests"""

    created_at: datetime
    """The datetime the private api key was created."""


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


class RequestedPermissionPermissionAction(BaseModel):
    """The action that the app will request off of users when a user installs the app."""

    action: str
    """The identifier of the action."""

    name: str
    """The human readable name of the action."""


class RequestedPermission(BaseModel):
    """
    A permission that the app requests from the admin of a company during the oauth flow.
    """

    is_required: bool
    """Whether the action is required for the app to function."""

    justification: str
    """The reason for requesting the action."""

    permission_action: RequestedPermissionPermissionAction
    """The action that the app will request off of users when a user installs the app."""


class Stats(BaseModel):
    """
    Aggregate usage statistics for this app, including daily, weekly, and monthly active user counts.
    """

    dau: int
    """The number of unique users who have spent time in this app in the last 24 hours.

    Returns 0 if no usage data is available.
    """

    mau: int
    """The number of unique users who have spent time in this app in the last 28 days.

    Returns 0 if no usage data is available.
    """

    time_spent_last24_hours: int
    """
    The total time, in seconds, that all users have spent in this app over the last
    24 hours. Returns 0 if no usage data is available.
    """

    wau: int
    """The number of unique users who have spent time in this app in the last 7 days.

    Returns 0 if no usage data is available.
    """


class App(BaseModel):
    """An app is an integration built on Whop.

    Apps can serve consumers as experiences within products, or serve companies as business tools.
    """

    id: str
    """The unique identifier for the app."""

    api_key: Optional[APIKey] = None
    """The API key used to authenticate requests on behalf of this app.

    Null if no API key has been generated. Requires the 'developer:manage_api_key'
    permission.
    """

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

    redirect_uris: List[str]
    """
    The whitelisted OAuth callback URLs that users are redirected to after
    authorizing the app.
    """

    requested_permissions: List[RequestedPermission]
    """
    The list of permissions this app requests when installed, including both
    required and optional permissions with justifications.
    """

    stats: Optional[Stats] = None
    """
    Aggregate usage statistics for this app, including daily, weekly, and monthly
    active user counts.
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
