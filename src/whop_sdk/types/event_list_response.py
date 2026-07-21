# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "EventListResponse",
    "Context",
    "Question",
    "Related",
    "RelatedAccount",
    "RelatedApp",
    "RelatedPayment",
    "RelatedPlan",
    "RelatedProduct",
    "RelatedUser",
    "User",
]


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


class RelatedAccount(BaseModel):
    id: Optional[str] = None

    logo_url: Optional[str] = None

    route: Optional[str] = None

    title: Optional[str] = None


class RelatedApp(BaseModel):
    id: Optional[str] = None

    domain_id: Optional[str] = None

    icon_url: Optional[str] = None

    title: Optional[str] = None


class RelatedPayment(BaseModel):
    id: Optional[str] = None

    card_brand: Optional[str] = None

    card_last4: Optional[str] = None

    provider: Optional[str] = None


class RelatedPlan(BaseModel):
    id: Optional[str] = None

    billing_period: Optional[int] = None

    currency: Optional[str] = None

    initial_price: Optional[float] = None

    renewal_price: Optional[float] = None

    title: Optional[str] = None


class RelatedProduct(BaseModel):
    id: Optional[str] = None

    route: Optional[str] = None

    title: Optional[str] = None


class RelatedUser(BaseModel):
    id: Optional[str] = None

    avatar_url: Optional[str] = None

    name: Optional[str] = None

    username: Optional[str] = None


class Related(BaseModel):
    """Hydrated details for the records this event references.

    Only present keys resolved.
    """

    account: Optional[RelatedAccount] = None

    app: Optional[RelatedApp] = None

    payment: Optional[RelatedPayment] = None

    plan: Optional[RelatedPlan] = None

    product: Optional[RelatedProduct] = None

    user: Optional[RelatedUser] = None


class User(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None


class EventListResponse(BaseModel):
    id: str

    event_id: str

    event_name: str

    event_time: datetime

    person_id: str

    context: Optional[Context] = None

    currency: Optional[str] = None

    custom_name: Optional[str] = None

    path: Optional[str] = None

    questions: Optional[List[Question]] = None

    referrer_url: Optional[str] = None

    related: Optional[Related] = None
    """Hydrated details for the records this event references.

    Only present keys resolved.
    """

    total_usd_amount: Optional[float] = None

    url: Optional[str] = None

    user: Optional[User] = None

    value: Optional[float] = None
