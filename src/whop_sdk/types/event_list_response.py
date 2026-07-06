# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EventListResponse", "Data", "DataContext", "DataUser"]


class DataContext(BaseModel):
    ad_campaign_id: Optional[str] = None

    ad_id: Optional[str] = None

    ad_set_id: Optional[str] = None

    utm_campaign: Optional[str] = None

    utm_content: Optional[str] = None

    utm_medium: Optional[str] = None

    utm_source: Optional[str] = None

    utm_term: Optional[str] = None


class DataUser(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    state: Optional[str] = None


class Data(BaseModel):
    id: str

    event_id: str

    event_name: str

    event_time: int

    context: Optional[DataContext] = None

    currency: Optional[str] = None

    custom_name: Optional[str] = None

    path: Optional[str] = None

    referrer_url: Optional[str] = None

    total_usd_amount: Optional[float] = None

    url: Optional[str] = None

    user: Optional[DataUser] = None

    value: Optional[float] = None


class EventListResponse(BaseModel):
    data: List[Data]
