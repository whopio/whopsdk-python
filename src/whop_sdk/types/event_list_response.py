# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EventListResponse", "Context", "Question", "User"]


class Context(BaseModel):
    ad_campaign_id: Optional[str] = None

    ad_id: Optional[str] = None

    ad_set_id: Optional[str] = None

    utm_campaign: Optional[str] = None

    utm_content: Optional[str] = None

    utm_medium: Optional[str] = None

    utm_source: Optional[str] = None

    utm_term: Optional[str] = None


class Question(BaseModel):
    id: Optional[str] = None

    answer: Optional[str] = None

    key: Optional[str] = None

    options: Optional[List[str]] = None

    question: Optional[str] = None

    type: Optional[str] = None


class User(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    state: Optional[str] = None


class EventListResponse(BaseModel):
    id: str

    event_id: str

    event_name: str

    event_time: int

    context: Optional[Context] = None

    currency: Optional[str] = None

    custom_name: Optional[str] = None

    path: Optional[str] = None

    questions: Optional[List[Question]] = None

    referrer_url: Optional[str] = None

    total_usd_amount: Optional[float] = None

    url: Optional[str] = None

    user: Optional[User] = None

    value: Optional[float] = None
