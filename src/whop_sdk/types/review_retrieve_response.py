# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .review_status import ReviewStatus

__all__ = ["ReviewRetrieveResponse", "Attachment", "Company", "Product", "User"]


class Attachment(BaseModel):
    """Represents an image attachment"""

    id: str
    """The unique identifier of the attachment."""

    content_type: Optional[str] = None
    """The MIME type of the uploaded file (e.g., image/jpeg, video/mp4, audio/mpeg)."""

    filename: Optional[str] = None
    """The original filename of the uploaded attachment, including its file extension."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class Company(BaseModel):
    """The company the review is for."""

    id: str
    """The unique identifier for the company."""

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    title: str
    """The display name of the company shown to customers."""


class Product(BaseModel):
    """The product the review is for."""

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class User(BaseModel):
    """The user account that performed the action."""

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class ReviewRetrieveResponse(BaseModel):
    """An object representing a user review of a company."""

    id: str
    """The unique identifier for the review."""

    attachments: List[Attachment]
    """The attachments attached to the review."""

    company: Company
    """The company the review is for."""

    created_at: datetime
    """The datetime the review was created."""

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
    """The datetime the review was last updated."""

    user: User
    """The user account that performed the action."""
