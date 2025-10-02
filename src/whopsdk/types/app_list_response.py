# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.app_statuses import AppStatuses

__all__ = ["AppListResponse"]


class AppListResponse(BaseModel):
    id: str
    """The ID of the app"""

    base_url: Optional[str] = None
    """The base url of the app"""

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

    status: Optional[AppStatuses] = None
    """The status of an experience interface"""

    verified: bool
    """Whether this app has been verified by Whop.

    Verified apps are endorsed by whop and are shown in the 'featured apps' section
    of the app store.
    """
