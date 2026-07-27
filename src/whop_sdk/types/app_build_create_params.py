# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppBuildCreateParams", "Attachment", "SourceAttachment"]


class AppBuildCreateParams(TypedDict, total=False):
    attachment: Required[Attachment]
    """
    The uploaded build file: `{ id }` for an existing file or `{ direct_upload_id }`
    for a completed direct upload.
    """

    checksum: Required[str]
    """
    A client-generated checksum of the build file, used to verify file integrity
    when unpacked.
    """

    platform: Required[Literal["ios", "android", "web"]]
    """The target platform for the build."""

    ai_prompt_id: str
    """The AI prompt that generated this build, if applicable."""

    app_id: str
    """The app to create the build for, prefixed `app_`.

    Defaults to the app behind the presented credential.
    """

    source_attachment: SourceAttachment
    """
    An optional compressed archive (.zip or .gz) of the source code that produced
    this build, stored alongside the build so it can be downloaded later. Referenced
    like `attachment`, and must be a different file.
    """

    supported_app_view_types: List[Literal["hub", "discover", "dash", "dashboard", "analytics", "skills", "openapi"]]
    """The view types this build supports. Only list the ones its code implements."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Attachment(TypedDict, total=False):
    """
    The uploaded build file: `{ id }` for an existing file or `{ direct_upload_id }` for a completed direct upload.
    """

    id: str
    """The tag of an already-uploaded file."""

    direct_upload_id: str
    """The signed id of a completed direct upload."""


class SourceAttachment(TypedDict, total=False):
    """
    An optional compressed archive (.zip or .gz) of the source code that produced this build, stored alongside the build so it can be downloaded later. Referenced like `attachment`, and must be a different file.
    """

    id: str
    """The tag of an already-uploaded file."""

    direct_upload_id: str
    """The signed id of a completed direct upload."""
