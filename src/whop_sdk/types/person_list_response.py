# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PersonListResponse",
    "Device",
    "FirstSource",
    "FirstSourceAd",
    "FirstSourceAdGroup",
    "FirstSourceCampaign",
    "LastSource",
    "LastSourceAd",
    "LastSourceAdGroup",
    "LastSourceCampaign",
    "Location",
    "Member",
    "User",
]


class Device(BaseModel):
    browser: Optional[str] = None

    device: Optional[str] = None

    os: Optional[str] = None


class FirstSourceAd(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class FirstSourceAdGroup(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class FirstSourceCampaign(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class FirstSource(BaseModel):
    """
    Where a visit came from: a whop ad click, a lead form, an external ad, or a referring site.
    """

    type: Literal["ad_click", "lead_form", "external_ad_click", "referrer", "utm"]

    ad: Optional[FirstSourceAd] = None

    ad_group: Optional[FirstSourceAdGroup] = None

    campaign: Optional[FirstSourceCampaign] = None

    domain: Optional[str] = None

    occurred_at: Optional[datetime] = None

    platform: Optional[str] = None

    utm_source: Optional[str] = None


class LastSourceAd(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class LastSourceAdGroup(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class LastSourceCampaign(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class LastSource(BaseModel):
    """
    Where a visit came from: a whop ad click, a lead form, an external ad, or a referring site.
    """

    type: Literal["ad_click", "lead_form", "external_ad_click", "referrer", "utm"]

    ad: Optional[LastSourceAd] = None

    ad_group: Optional[LastSourceAdGroup] = None

    campaign: Optional[LastSourceCampaign] = None

    domain: Optional[str] = None

    occurred_at: Optional[datetime] = None

    platform: Optional[str] = None

    utm_source: Optional[str] = None


class Location(BaseModel):
    city: Optional[str] = None

    continent: Optional[str] = None

    country: Optional[str] = None


class Member(BaseModel):
    """The user's member record at this account, when they are a member of it."""

    id: str

    joined_at: Optional[datetime] = None

    status: Optional[str] = None

    usd_total_spend: Optional[float] = None


class User(BaseModel):
    """The person's primary whop user, when one of their identities is a whop account."""

    id: str

    username: str

    name: Optional[str] = None

    profile_pic_url: Optional[str] = None


class PersonListResponse(BaseModel):
    id: str

    account_id: str

    event_count: int

    first_seen_at: datetime

    last_seen_at: datetime

    purchase_count: int

    aov: Optional[float] = None

    device: Optional[Device] = None

    email: Optional[str] = None
    """The email from the person's most recent event that carried one."""

    first_purchase_at: Optional[datetime] = None

    first_source: Optional[FirstSource] = None
    """
    Where a visit came from: a whop ad click, a lead form, an external ad, or a
    referring site.
    """

    last_ip: Optional[str] = None

    last_purchase_at: Optional[datetime] = None

    last_source: Optional[LastSource] = None
    """
    Where a visit came from: a whop ad click, a lead form, an external ad, or a
    referring site.
    """

    location: Optional[Location] = None

    ltv: Optional[float] = None

    member: Optional[Member] = None
    """The user's member record at this account, when they are a member of it."""

    name: Optional[str] = None
    """The name from the person's most recent event that carried one."""

    phone: Optional[str] = None
    """The phone from the person's most recent event that carried one."""

    timezone: Optional[str] = None

    user: Optional[User] = None
    """The person's primary whop user, when one of their identities is a whop account."""
