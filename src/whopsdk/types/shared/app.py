# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .app_statuses import AppStatuses

__all__ = ["App", "APIKey", "Company", "Creator", "RequestedPermission", "RequestedPermissionPermissionAction", "Stats"]


class APIKey(BaseModel):
    id: str
    """The ID of this API key"""

    token: str
    """This is the API key used to authenticate requests"""

    created_at: int
    """When this API key was created at"""


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    title: str
    """The title of the company."""


class Creator(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class RequestedPermissionPermissionAction(BaseModel):
    action: str
    """The identifier of the action."""

    name: str
    """The human readable name of the action."""


class RequestedPermission(BaseModel):
    is_required: bool
    """Whether the action is required for the app to function."""

    justification: str
    """The reason for requesting the action."""

    permission_action: RequestedPermissionPermissionAction
    """The action that the app will request off of users when a user installs the app."""


class Stats(BaseModel):
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
    id: str
    """The ID of the app"""

    api_key: Optional[APIKey] = None
    """The API key for the app"""

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

    name: str
    """The name of the app"""

    requested_permissions: List[RequestedPermission]
    """
    The set of permissions that an app requests to be granted when a user installs
    the app.
    """

    stats: Optional[Stats] = None
    """A collection of stats for the app."""

    status: Optional[AppStatuses] = None
    """The status of an experience interface"""

    verified: bool
    """Whether this app has been verified by Whop.

    Verified apps are endorsed by whop and are shown in the 'featured apps' section
    of the app store.
    """
