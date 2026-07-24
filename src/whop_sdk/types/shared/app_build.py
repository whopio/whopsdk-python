# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AppBuild"]


class AppBuild(BaseModel):
    id: str
    """App build ID, prefixed `abld_`."""

    checksum: str
    """Client-generated checksum of the build file, used to verify file integrity."""

    created_at: str
    """When the build was uploaded, as an ISO 8601 timestamp."""

    file_url: Optional[str] = None
    """URL to download the uploaded build artifact."""

    is_production: bool
    """Whether this build is the currently active production build for its platform."""

    platform: Literal["ios", "android", "web"]
    """The target platform for this build."""

    review_message: Optional[str] = None
    """
    Feedback from the reviewer explaining a rejection, or `null` if the build has
    not been reviewed or was approved.
    """

    source_url: Optional[str] = None
    """
    URL to download the compressed source code archive that produced this build, or
    `null` when the build was uploaded without a source archive.
    """

    status: Literal["draft", "pending", "approved", "rejected"]
    """The build's review status."""

    supported_app_view_types: List[str]
