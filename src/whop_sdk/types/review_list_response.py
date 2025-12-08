# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .review_status import ReviewStatus

__all__ = ["ReviewListResponse", "Attachment", "User"]


class Attachment(BaseModel):
    """Represents an image attachment"""

    id: str
    """The ID of the attachment"""

    content_type: Optional[str] = None
    """The attachment's content type (e.g., image/jpg, video/mp4)"""

    filename: Optional[str] = None
    """The name of the file"""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class User(BaseModel):
    """The user account that performed the action."""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class ReviewListResponse(BaseModel):
    """An object representing a user review of a company."""

    id: str
    """The internal ID of the review."""

    attachments: List[Attachment]
    """The attachments attached to the review."""

    created_at: datetime
    """The timestamp of when the review was created."""

    description: Optional[str] = None
    """The description of the review."""

    joined_at: Optional[datetime] = None
    """The timestamp of when the user joined the product."""

    paid_for_product: Optional[bool] = None
    """Whether or not the user paid for the product.

    If null, the payment status is unknown.
    """

    published_at: Optional[datetime] = None
    """The timestamp of when the review was published."""

    stars: int
    """The number of stars the user gave the product."""

    status: ReviewStatus
    """The status of the review."""

    title: Optional[str] = None
    """The title of the review."""

    updated_at: datetime
    """The timestamp of when the review was last updated."""

    user: User
    """The user account that performed the action."""
