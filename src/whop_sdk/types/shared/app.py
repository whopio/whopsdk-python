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
    """The API key for the app"""

    id: str
    """The ID of this API key"""

    token: str
    """This is the API key used to authenticate requests"""

    created_at: datetime
    """When this API key was created at"""


class Company(BaseModel):
    """The company that owns the app"""

    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class Creator(BaseModel):
    """The creator of the app"""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Icon(BaseModel):
    """The icon for the app.

    This icon is shown on discovery, on the product page, on checkout, and as a default icon for the experiences.
    """

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
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
    """A collection of stats for the app."""

    dau: int
    """
    This is the number of users that have spent time in this app in the last 24
    hours.
    """

    mau: int
    """
    This is the number of users that have spent time in this app in the last 28
    days.
    """

    time_spent_last24_hours: int
    """
    This how much time, in seconds, users have spent in this app in the last 24
    hours.
    """

    wau: int
    """
    This is the number of users that have spent time in this app in the last 7 days.
    """


class App(BaseModel):
    """An object representing an app"""

    id: str
    """The ID of the app"""

    api_key: Optional[APIKey] = None
    """The API key for the app"""

    app_type: AppType
    """The type of end-user an app is built for"""

    base_url: Optional[str] = None
    """The base url of the app"""

    company: Company
    """The company that owns the app"""

    creator: Creator
    """The creator of the app"""

    dashboard_path: Optional[str] = None
    """The path part for a specific view of the app.

    This is the template part of the url after the base domain. Eg:
    /experiences/[experienceId]
    """

    description: Optional[str] = None
    """The description of the app"""

    discover_path: Optional[str] = None
    """The path part for a specific view of the app.

    This is the template part of the url after the base domain. Eg:
    /experiences/[experienceId]
    """

    domain_id: str
    """The unique part of the proxied domain for this app.

    Used to generate the base url used to display the app inside the whop platform.
    Refers to the id part in the final url: https://{domain_id}.apps.whop.com
    """

    experience_path: Optional[str] = None
    """The path part for a specific view of the app.

    This is the template part of the url after the base domain. Eg:
    /experiences/[experienceId]
    """

    icon: Optional[Icon] = None
    """The icon for the app.

    This icon is shown on discovery, on the product page, on checkout, and as a
    default icon for the experiences.
    """

    name: str
    """The name of the app"""

    requested_permissions: List[RequestedPermission]
    """
    The set of permissions that an app requests to be granted when a user installs
    the app.
    """

    stats: Optional[Stats] = None
    """A collection of stats for the app."""

    status: AppStatuses
    """If the status is live, the app is visible on Whop discovery.

    In order to be live, you need to set the name, icon, and description. Being
    unlisted or hidden means it's not visible on Whop but you can still install the
    app via direct link. To remove the app from whop discovery, you should set the
    status to unlisted.
    """

    verified: bool
    """Whether this app has been verified by Whop.

    Verified apps are endorsed by whop and are shown in the 'featured apps' section
    of the app store.
    """
