# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .review_status import ReviewStatus

__all__ = ["ReviewRetrieveResponse", "Attachment", "Company", "Product", "User"]


class Attachment(BaseModel):
    """Represents an image attachment"""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class Company(BaseModel):
    """The company that this review was written for."""

    id: str
    """The unique identifier for the company."""

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    title: str
    """The display name of the company shown to customers."""


class Product(BaseModel):
    """The product that this review was written for."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user account of the person who wrote this review."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ReviewRetrieveResponse(BaseModel):
    """
    A user-submitted review of a company, including a star rating and optional text feedback.
    """

    id: str
    """The unique identifier for the review."""

    attachments: List[Attachment]
    """A list of files and media attached to the review."""

    company: Company
    """The company that this review was written for."""

    created_at: datetime
    """The datetime the review was created."""

    description: Optional[str] = None
    """The body text of the review containing the user's detailed feedback.

    Returns an empty string if no description was provided.
    """

    joined_at: Optional[datetime] = None
    """The timestamp of when the reviewer first joined the product. Null if unknown."""

    paid_for_product: Optional[bool] = None
    """Whether the reviewer paid for the product.

    Null if the payment status is unknown.
    """

    product: Product
    """The product that this review was written for."""

    published_at: Optional[datetime] = None
    """The timestamp of when the review was published.

    Null if the review has not been published yet.
    """

    stars: int
    """The star rating given by the reviewer, from 1 to 5."""

    status: ReviewStatus
    """The current moderation status of the review."""

    title: Optional[str] = None
    """A short summary title for the review. Null if the reviewer did not provide one."""

    updated_at: datetime
    """The datetime the review was last updated."""

    user: User
    """The user account of the person who wrote this review."""
