# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .upload_status import UploadStatus

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
    """The CDN URL for accessing the file.

    Null if the file has not finished uploading.
    """
