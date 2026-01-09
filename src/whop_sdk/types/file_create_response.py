# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    """A file that has been uploaded or is pending upload"""

    id: str
    """The ID of the file"""

    content_type: Optional[str] = None
    """The MIME type of the file (e.g., image/jpeg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    size: Optional[str] = None
    """The size of the file in bytes"""

    upload_headers: Optional[Dict[str, object]] = None
    """Headers to include in the upload request (only on create)"""

    upload_status: Literal["pending", "processing", "ready", "failed"]
    """The upload status of the file"""

    upload_url: Optional[str] = None
    """The presigned URL to upload the file to (only on create)"""

    url: Optional[str] = None
    """The URL to access the file"""
