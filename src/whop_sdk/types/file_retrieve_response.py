# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileRetrieveResponse", "MultipartUploadURL"]


class MultipartUploadURL(BaseModel):
    """The presigned URL for each part.

    Present only on create, and only for multipart uploads.
    """

    part_number: int
    """The 1-based index of this part within the multipart upload."""

    url: str
    """The presigned URL to PUT this part's bytes to."""


class FileRetrieveResponse(BaseModel):
    id: str
    """The file's ID, prefixed `file_`."""

    content_type: Optional[str] = None
    """The file's MIME type, e.g. `application/pdf`."""

    created_at: str
    """When the file was created, as an ISO 8601 timestamp."""

    filename: Optional[str] = None
    """The original filename, including its extension."""

    object: str
    """The type of this object, always `file`."""

    size: Optional[int] = None
    """The file size in bytes. `null` until the upload has finished."""

    upload_status: Literal["pending", "processing", "ready", "failed"]
    """Where the file is in its upload lifecycle."""

    url: Optional[str] = None
    """
    A URL to download the file: a permanent CDN URL for public files, a signed
    expiring URL for private ones. `null` until the upload has finished.
    """

    visibility: Literal["public", "private"]
    """
    `public` files are served via an unsigned CDN URL; `private` files via a signed,
    expiring URL.
    """

    multipart_chunk_size: Optional[int] = None
    """The byte size each part (except the last) must be.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_id: Optional[str] = None
    """The ID of the multipart upload, passed back to `complete`.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_urls: Optional[List[MultipartUploadURL]] = None

    upload_headers: Optional[builtins.object] = None
    """Headers to send with the upload PUT. Present only on create."""

    upload_url: Optional[str] = None
    """Presigned URL to PUT the file's bytes to.

    Present only on create, and only for single-part uploads.
    """
