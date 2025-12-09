# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .app_type import AppType
from .shared.app_statuses import AppStatuses

__all__ = ["AppUpdateParams", "Icon", "IconAttachmentInputWithDirectUploadID", "IconAttachmentInputWithID"]


class AppUpdateParams(TypedDict, total=False):
    app_store_description: Optional[str]
    """The description of the app for the app store in-depth app view."""

    app_type: Optional[AppType]
    """The type of end-user an app is built for"""

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


class IconAttachmentInputWithDirectUploadID(TypedDict, total=False):
    """Input for an attachment"""

    direct_upload_id: Required[str]
    """This ID should be used the first time you upload an attachment.

    It is the ID of the direct upload that was created when uploading the file to S3
    via the mediaDirectUpload mutation.
    """


class IconAttachmentInputWithID(TypedDict, total=False):
    """Input for an attachment"""

    id: Required[str]
    """The ID of an existing attachment object.

    Use this when updating a resource and keeping a subset of the attachments. Don't
    use this unless you know what you're doing.
    """


Icon: TypeAlias = Union[IconAttachmentInputWithDirectUploadID, IconAttachmentInputWithID]
