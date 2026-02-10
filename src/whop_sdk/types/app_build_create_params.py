# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .shared.app_view_type import AppViewType
from .shared.app_build_platforms import AppBuildPlatforms

__all__ = ["AppBuildCreateParams", "Attachment"]


class AppBuildCreateParams(TypedDict, total=False):
    attachment: Required[Attachment]
    """The build file to upload.

    For iOS and Android, this should be a .zip archive containing a
    main_js_bundle.hbc file and an optional assets folder. For web, this should be a
    JavaScript file.
    """

    checksum: Required[str]
    """
    A client-generated checksum of the build file, used to verify file integrity
    when unpacked on a device.
    """

    platform: Required[AppBuildPlatforms]
    """The target platform for the build. Accepted values: ios, android, web."""

    ai_prompt_id: Optional[str]
    """The identifier of the AI prompt that generated this build, if applicable."""

    app_id: Optional[str]
    """The unique identifier of the app to create the build for.

    Defaults to the app associated with the current API key.
    """

    supported_app_view_types: Optional[List[AppViewType]]
    """The view types this build supports.

    A build can support multiple view types but should only list the ones its code
    implements.
    """


class Attachment(TypedDict, total=False):
    """The build file to upload.

    For iOS and Android, this should be a .zip archive containing a main_js_bundle.hbc file and an optional assets folder. For web, this should be a JavaScript file.
    """

    id: Required[str]
    """The ID of an existing file object."""
