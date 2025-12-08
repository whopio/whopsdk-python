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
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class App(BaseModel):
    """The experience interface for this experience."""

    id: str
    """The ID of the app"""

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
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""


class Image(BaseModel):
    """The logo for the experience."""

    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class ExperienceListResponse(BaseModel):
    """An object representing an experience belonging to a company."""

    id: str
    """The unique ID representing this experience"""

    app: App
    """The experience interface for this experience."""

    company: Company
    """The company that owns this experience."""

    created_at: datetime
    """The timestamp of when this experience was created."""

    image: Optional[Image] = None
    """The logo for the experience."""

    is_public: bool
    """Whether the experience is visible to the public"""

    name: str
    """The written name of the description."""

    order: Optional[str] = None
    """The order of the experience in the section"""
