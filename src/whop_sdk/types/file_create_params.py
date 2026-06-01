# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .file_visibility import FileVisibility

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    filename: Required[str]
    """
    The name of the file including its extension (e.g., "photo.png" or
    "document.pdf").
    """

    visibility: Optional[FileVisibility]
    """
    Controls whether an uploaded file is publicly accessible or requires
    authentication to access.
    """
