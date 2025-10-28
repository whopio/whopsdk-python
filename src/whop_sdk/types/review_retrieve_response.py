# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .review_status import ReviewStatus

__all__ = ["ReviewRetrieveResponse", "Attachment", "Company", "Product", "User"]


class Attachment(BaseModel):
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


class Company(BaseModel):
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""


class Product(BaseModel):
    id: str
    """The internal ID of the public product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class User(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class ReviewRetrieveResponse(BaseModel):
    id: str
    """The internal ID of the review."""

    attachments: List[Attachment]
    """The attachments attached to the review."""

    company: Company
    """The company the review is for."""

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

    product: Product
    """The product the review is for."""

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
