# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PersonRetrieveResponse",
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
    "Purchase",
    "Source",
    "SourceAd",
    "SourceAdGroup",
    "SourceCampaign",
    "Usage",
    "UsageBrowser",
    "UsageCity",
    "UsageCountry",
    "UsageDevice",
    "UsageIP",
    "UsageO",
    "UsageReferrer",
    "UsageTimezone",
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


class Purchase(BaseModel):
    event_id: str

    occurred_at: datetime

    usd_value: float


class SourceAd(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class SourceAdGroup(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class SourceCampaign(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class Source(BaseModel):
    """
    Where a visit came from: a whop ad click, a lead form, an external ad, or a referring site.
    """

    type: Literal["ad_click", "lead_form", "external_ad_click", "referrer", "utm"]

    ad: Optional[SourceAd] = None

    ad_group: Optional[SourceAdGroup] = None

    campaign: Optional[SourceCampaign] = None

    domain: Optional[str] = None

    occurred_at: Optional[datetime] = None

    platform: Optional[str] = None

    utm_source: Optional[str] = None


class UsageBrowser(BaseModel):
    events: int

    value: str


class UsageCity(BaseModel):
    events: int

    value: str


class UsageCountry(BaseModel):
    events: int

    value: str


class UsageDevice(BaseModel):
    events: int

    value: str


class UsageIP(BaseModel):
    events: int

    value: str


class UsageO(BaseModel):
    events: int

    value: str


class UsageReferrer(BaseModel):
    events: int

    value: str


class UsageTimezone(BaseModel):
    events: int

    value: str


class Usage(BaseModel):
    """
    Exact usage breakdowns for the person's browser traffic (distinct events per value).
    """

    browser: Optional[List[UsageBrowser]] = None

    city: Optional[List[UsageCity]] = None

    country: Optional[List[UsageCountry]] = None

    device: Optional[List[UsageDevice]] = None

    ip: Optional[List[UsageIP]] = None

    os: Optional[List[UsageO]] = None

    referrer: Optional[List[UsageReferrer]] = None

    timezone: Optional[List[UsageTimezone]] = None


class User(BaseModel):
    """The person's primary whop user, when one of their identities is a whop account."""

    id: str

    username: str

    name: Optional[str] = None

    profile_pic_url: Optional[str] = None


class PersonRetrieveResponse(BaseModel):
    """
    The full profile a retrieve returns: the summary plus every linked identity, purchase rows, all acquisition sources, and exact usage breakdowns.
    """

    id: str

    account_id: str

    event_count: int

    first_seen_at: datetime

    last_seen_at: datetime

    purchase_count: int

    aov: Optional[float] = None

    audience_ids: Optional[List[str]] = None

    custom_event_names: Optional[List[str]] = None

    device: Optional[Device] = None

    email: Optional[str] = None
    """The email from the person's most recent event that carried one."""

    emails: Optional[List[str]] = None
    """Every linked email, primary first."""

    event_names: Optional[List[str]] = None

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

    names: Optional[List[str]] = None
    """Every name the person's linked identities carried, primary first."""

    phone: Optional[str] = None
    """The phone from the person's most recent event that carried one."""

    phones: Optional[List[str]] = None
    """Every linked phone, primary first."""

    purchases: Optional[List[Purchase]] = None

    roles: Optional[List[str]] = None

    sources: Optional[List[Source]] = None
    """
    Every distinct acquisition signal the person ever carried, ad entities hydrated.
    """

    timezone: Optional[str] = None

    usage: Optional[Usage] = None
    """
    Exact usage breakdowns for the person's browser traffic (distinct events per
    value).
    """

    user: Optional[User] = None
    """The person's primary whop user, when one of their identities is a whop account."""

    user_ids: Optional[List[str]] = None
    """Every linked whop account, the most used one first."""
