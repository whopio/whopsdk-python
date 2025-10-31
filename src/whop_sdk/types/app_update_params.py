# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .shared.app_statuses import AppStatuses

__all__ = ["AppUpdateParams", "Icon"]


class AppUpdateParams(TypedDict, total=False):
    app_store_description: Optional[str]
    """The description of the app for the app store in-depth app view."""

    base_url: Optional[str]
    """The base production url of the app"""

    dashboard_path: Optional[str]
    """The path for the dashboard view of the app"""

    description: Optional[str]
    """The description of the app"""

    discover_path: Optional[str]
    """The path for the discover view of the app"""

    experience_path: Optional[str]
    """The path for the hub view of the app"""

    icon: Optional[Icon]
    """The icon for the app"""

    name: Optional[str]
    """The name of the app"""

    required_scopes: Optional[List[Literal["read_user"]]]
    """The scopes that the app will request off of users when a user installs the app."""

    status: Optional[AppStatuses]
    """The status of an experience interface"""


class Icon(TypedDict, total=False):
    id: Optional[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """

    direct_upload_id: Optional[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """
