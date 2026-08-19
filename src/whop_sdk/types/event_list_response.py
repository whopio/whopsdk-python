# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "EventListResponse",
    "Context",
    "Question",
    "Related",
    "RelatedAccount",
    "RelatedAd",
    "RelatedAdCampaign",
    "RelatedAdGroup",
    "RelatedApp",
    "RelatedAudience",
    "RelatedPayment",
    "RelatedPlan",
    "RelatedProduct",
    "RelatedUser",
    "User",
]


class Context(BaseModel):
    ad_campaign_id: Optional[str] = None

    ad_click_id: Optional[str] = None
    """Stable identity for the ad click this event belongs to.

    Every event from one click carries the same value, so events group into clicks
    without re-deriving them.
    """

    ad_click_type: Optional[str] = None
    """
    How the ad click was identified: the network's click-id param (`fbclid`,
    `ttclid`, `gclid`, `gbraid`, `wbraid`, `twclid`) or `synthetic` when the click
    carried none.
    """

    ad_id: Optional[str] = None

    ad_set_id: Optional[str] = None

    source_type: Optional[Literal["ad_click", "lead_form", "external_ad_click", "referrer"]] = None
    """
    How this event counts as an acquisition touch, using the same rule attribution
    credits a conversion with. `ad_click` and `lead_form` resolved to a Whop ad;
    `external_ad_click` is a paid click on a campaign run outside Whop; `referrer`
    is organic. Null when the event is not a touch.
    """

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


class RelatedAd(BaseModel):
    """The Whop ad this event's click resolved to."""

    id: Optional[str] = None

    thumbnail_url: Optional[str] = None

    title: Optional[str] = None


class RelatedAdCampaign(BaseModel):
    """
    The Whop ad campaign this event's click resolved to, read from the ad entity tree rather than the click's url params.
    """

    id: Optional[str] = None

    platform: Optional[str] = None

    title: Optional[str] = None


class RelatedAdGroup(BaseModel):
    """The Whop ad group this event's click resolved to."""

    id: Optional[str] = None

    title: Optional[str] = None


class RelatedApp(BaseModel):
    id: Optional[str] = None

    domain_id: Optional[str] = None

    icon_url: Optional[str] = None

    title: Optional[str] = None


class RelatedAudience(BaseModel):
    """The saved audience this event came from.

    Present on the identify events an audience ingest writes for each of its members.
    """

    id: Optional[str] = None

    audience_type: Optional[Literal["custom", "lookalike"]] = None

    file_name: Optional[str] = None

    source_type: Optional[Literal["csv_upload", "people_filter"]] = None

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

    ad: Optional[RelatedAd] = None
    """The Whop ad this event's click resolved to."""

    ad_campaign: Optional[RelatedAdCampaign] = None
    """
    The Whop ad campaign this event's click resolved to, read from the ad entity
    tree rather than the click's url params.
    """

    ad_group: Optional[RelatedAdGroup] = None
    """The Whop ad group this event's click resolved to."""

    app: Optional[RelatedApp] = None

    audience: Optional[RelatedAudience] = None
    """The saved audience this event came from.

    Present on the identify events an audience ingest writes for each of its
    members.
    """

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

    recommended_action_chain_id: Optional[str] = None

    recommended_action_shown_position: Optional[int] = None

    referrer_url: Optional[str] = None

    related: Optional[Related] = None
    """Hydrated details for the records this event references.

    Only present keys resolved.
    """

    total_usd_amount: Optional[float] = None

    url: Optional[str] = None

    user: Optional[User] = None

    value: Optional[float] = None
