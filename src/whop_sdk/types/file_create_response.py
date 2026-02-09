# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .upload_status import UploadStatus

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    """A file that has been uploaded or is pending upload."""

    id: str
    """The unique identifier for the file."""

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded file, including its file extension."""

    size: Optional[str] = None
    """The file size in bytes. Null if the file has not finished uploading."""

    upload_headers: Optional[Dict[str, object]] = None
    """Headers to include in the upload request.

    Only present in the response from the create mutation.
    """

    upload_status: UploadStatus
    """The current upload status of the file (e.g., pending, ready)."""

    upload_url: Optional[str] = None
    """The presigned URL to upload the file contents to.

    Only present in the response from the create mutation.
    """

    url: Optional[str] = None
    """The CDN URL for accessing the file.

    Null if the file has not finished uploading.
    """
