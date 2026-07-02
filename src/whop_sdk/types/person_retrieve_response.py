# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PersonRetrieveResponse", "Data", "DataAdSet", "DataAd", "DataCampaign"]


class DataAdSet(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class DataAd(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class DataCampaign(BaseModel):
    id: str

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None


class Data(BaseModel):
    id: str

    first_seen_at: int

    last_seen_at: int

    person_id: str

    purchase_count: int

    ad_sets: Optional[List[DataAdSet]] = None

    ads: Optional[List[DataAd]] = None

    aov: Optional[float] = None

    campaigns: Optional[List[DataCampaign]] = None

    email: Optional[str] = None

    has_failed_payment: Optional[bool] = None

    ltv: Optional[float] = None

    name: Optional[str] = None

    phone: Optional[str] = None


class PersonRetrieveResponse(BaseModel):
    data: Data
