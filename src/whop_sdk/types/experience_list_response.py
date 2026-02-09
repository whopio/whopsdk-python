# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ExperienceListResponse", "App", "AppIcon", "Company", "Image"]


class AppIcon(BaseModel):
    """The icon for the app.

    This icon is shown on discovery, on the product page, on checkout, and as a default icon for the experiences.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class App(BaseModel):
    """The experience interface for this experience."""

    id: str
    """The unique identifier for the app."""

    icon: Optional[AppIcon] = None
    """The icon for the app.

    This icon is shown on discovery, on the product page, on checkout, and as a
    default icon for the experiences.
    """

    name: str
    """The name of the app"""


class Company(BaseModel):
    """The company that owns this experience."""

    id: str
    """The unique identifier for the company."""

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    title: str
    """The display name of the company shown to customers."""


class Image(BaseModel):
    """The logo for the experience."""

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class ExperienceListResponse(BaseModel):
    """
    An experience is a feature or content module within a product, such as a chat, course, or app.
    """

    id: str
    """The unique identifier for the experience."""

    app: App
    """The experience interface for this experience."""

    company: Company
    """The company that owns this experience."""

    created_at: datetime
    """The datetime the experience was created."""

    image: Optional[Image] = None
    """The logo for the experience."""

    is_public: bool
    """Whether the experience is visible to the public"""

    name: str
    """The written name of the description."""

    order: Optional[str] = None
    """The order of the experience in the section"""
