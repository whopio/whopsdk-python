# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PersonListResponse", "AdSet", "Ad", "Campaign"]


class AdSet(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class Ad(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class Campaign(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class PersonListResponse(BaseModel):
    id: str

    account_id: str

    first_seen_at: int

    last_seen_at: int

    person_id: str

    purchase_count: int

    ad_sets: Optional[List[AdSet]] = None

    ads: Optional[List[Ad]] = None

    aov: Optional[float] = None

    campaigns: Optional[List[Campaign]] = None

    email: Optional[str] = None

    has_failed_payment: Optional[bool] = None

    ltv: Optional[float] = None

    name: Optional[str] = None

    phone: Optional[str] = None
