# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Experience", "App", "AppIcon", "Company", "Image", "Product"]


class AppIcon(BaseModel):
    """
    The icon image for this app, displayed on the app store, product pages, checkout, and as the default icon for experiences using this app.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class App(BaseModel):
    """The app that powers this experience, defining its interface and behavior."""

    id: str
    """The unique identifier for the app."""

    icon: Optional[AppIcon] = None
    """
    The icon image for this app, displayed on the app store, product pages,
    checkout, and as the default icon for experiences using this app.
    """

    name: str
    """The display name of this app shown on the app store and in experience
    navigation.

    Maximum 30 characters.
    """


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
    """The custom logo image for this experience.

    Null if no custom logo has been uploaded.
    """

    url: Optional[str] = None
    """A pre-optimized URL for rendering this attachment on the client.

    This should be used for displaying attachments in apps.
    """


class Product(BaseModel):
    """A product is a digital good or service sold on Whop.

    Products contain plans for pricing and experiences for content delivery.
    """

    id: str
    """The unique identifier for the product."""

    route: str
    """
    The URL slug used in the product's public link (e.g., 'my-product' in
    whop.com/company/my-product).
    """

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class Experience(BaseModel):
    """
    An experience is a feature or content module within a product, such as a chat, course, or app.
    """

    id: str
    """The unique identifier for the experience."""

    app: App
    """The app that powers this experience, defining its interface and behavior."""

    company: Company
    """The company that owns this experience."""

    created_at: datetime
    """The datetime the experience was created."""

    image: Optional[Image] = None
    """The custom logo image for this experience.

    Null if no custom logo has been uploaded.
    """

    is_public: bool
    """
    Whether this experience is publicly visible to all users, including those
    without a membership.
    """

    name: str
    """The display name of this experience shown to users in the product navigation.

    Maximum 255 characters.
    """

    order: Optional[str] = None
    """The sort position of this experience within its section.

    Lower values appear first. Null if no position has been set.
    """

    products: List[Product]
    """
    The list of products this experience is attached to, which determines which
    customers have access. Empty if the experience is only visible to authorized
    company team members.
    """
