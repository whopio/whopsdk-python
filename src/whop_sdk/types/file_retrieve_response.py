# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .upload_status import UploadStatus
from .file_visibility import FileVisibility

__all__ = ["FileRetrieveResponse"]


class FileRetrieveResponse(BaseModel):
    """A file that has been uploaded or is pending upload."""

    id: str
    """The unique identifier for the file."""

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded file, including its file extension."""

    size: Optional[str] = None
    """The file size in bytes. Null if the file has not finished uploading."""

    upload_status: UploadStatus
    """The current upload status of the file (e.g., pending, ready)."""

    url: Optional[str] = None
    """The URL for accessing the file.

    For public files, this is a permanent CDN URL. For private files, this is a
    signed URL that expires. Null if the file has not finished uploading.
    """

    visibility: FileVisibility
    """Whether the file is publicly accessible or requires authentication."""
