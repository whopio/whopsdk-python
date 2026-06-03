# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.currency import Currency

__all__ = ["ConversionCreateParams", "Context", "User"]


class ConversionCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The company to associate with this event."""

    event_name: Required[
        Literal["lead", "submit_application", "contact", "complete_registration", "schedule", "custom"]
    ]
    """The type of event."""

    action_source: Optional[
        Literal[
            "email",
            "website",
            "app",
            "phone_call",
            "chat",
            "physical_store",
            "system_generated",
            "business_messaging",
            "other",
        ]
    ]
    """The channel where an event originated"""

    context: Optional[Context]
    """Tracking and attribution context."""

    currency: Optional[Currency]
    """The available currencies on the platform"""

    custom_name: Optional[str]
    """Custom event name when event_name is 'custom'."""

    event_id: Optional[str]
    """Client-provided identifier for deduplication. Generated if omitted."""

    event_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the event occurred. Defaults to now."""

    plan_id: Optional[str]
    """The plan associated with the event."""

    product_id: Optional[str]
    """The product associated with the event."""

    referrer_url: Optional[str]
    """The referring URL."""

    url: Optional[str]
    """The URL where the event occurred."""

    user: Optional[User]
    """User identity and profile data."""

    value: Optional[float]
    """Monetary value associated with the event."""


class Context(TypedDict, total=False):
    """Tracking and attribution context."""

    ad_campaign_id: Optional[str]
    """Ad campaign ID."""

    ad_id: Optional[str]
    """Ad ID."""

    ad_set_id: Optional[str]
    """Ad set ID."""

    fbc: Optional[str]
    """Facebook click cookie (\\__fbc, format fb.1.{timestamp}.{fbclid})."""

    fbclid: Optional[str]
    """Facebook click ID."""

    fbp: Optional[str]
    """Facebook browser pixel ID."""

    ga: Optional[str]
    """Google Analytics client ID."""

    gclid: Optional[str]
    """Google click ID."""

    ig_sid: Optional[str]
    """Instagram session ID."""

    ip_address: Optional[str]
    """IP address."""

    ttclid: Optional[str]
    """TikTok click ID."""

    ttp: Optional[str]
    """TikTok pixel ID."""

    user_agent: Optional[str]
    """Browser user agent string."""

    utm_campaign: Optional[str]
    """UTM campaign parameter."""

    utm_content: Optional[str]
    """UTM content parameter."""

    utm_id: Optional[str]
    """UTM ID parameter."""

    utm_medium: Optional[str]
    """UTM medium parameter."""

    utm_source: Optional[str]
    """UTM source parameter."""

    utm_term: Optional[str]
    """UTM term parameter."""


class User(TypedDict, total=False):
    """User identity and profile data."""

    anonymous_id: Optional[str]
    """An anonymous identifier for the user."""

    birthdate: Optional[str]
    """Date of birth (YYYY-MM-DD)."""

    city: Optional[str]
    """City."""

    country: Optional[str]
    """Country."""

    email: Optional[str]
    """Email address."""

    external_id: Optional[str]
    """An external identifier for the user."""

    first_name: Optional[str]
    """First name."""

    gender: Optional[Literal["male", "female"]]
    """Gender"""

    last_name: Optional[str]
    """Last name."""

    linked_anonymous_id: Optional[str]
    """A second anonymous identifier to link to this user (e.g.

    captured across an iframe boundary).
    """

    member_id: Optional[str]
    """The Whop member ID."""

    membership_id: Optional[str]
    """The Whop membership ID."""

    name: Optional[str]
    """Full display name."""

    phone: Optional[str]
    """Phone number."""

    postal_code: Optional[str]
    """Postal code."""

    state: Optional[str]
    """State or region."""

    user_id: Optional[str]
    """The Whop user ID."""

    username: Optional[str]
    """Username."""
