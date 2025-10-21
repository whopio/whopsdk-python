# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Experience", "App", "AppIcon", "Company", "Image", "Product"]


class AppIcon(BaseModel):
    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class App(BaseModel):
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
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""


class Image(BaseModel):
    url: Optional[str] = None
    """This is the URL you use to render optimized attachments on the client.

    This should be used for apps.
    """


class Product(BaseModel):
    id: str
    """The internal ID of the public product."""

    route: str
    """The route of the product."""

    title: str
    """The title of the product. Use for Whop 4.0."""


class Experience(BaseModel):
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

    name: str
    """The written name of the description."""

    order: Optional[str] = None
    """The order of the experience in the section"""

    products: List[Product]
    """The access passes that are associated with this experience.

    This should not be used unless you are trying to list all access passes the
    experience has, for some reason. You probably don't want to use this though and
    should be using accessPass.
    """
