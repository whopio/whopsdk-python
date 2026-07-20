# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "AdCreateParams",
    "Creative",
    "CreativeCrop",
    "LeadForm",
    "LeadFormCompletion",
    "LeadFormDisclaimer",
    "LeadFormDisclaimerCheckbox",
    "LeadFormIntro",
    "LeadFormPrivacyPolicy",
    "LeadFormQuestion",
    "LeadFormQuestionOption",
    "LeadFormQuestionOptionLogic",
    "MessagingConfig",
    "SocialAccount",
]


class AdCreateParams(TypedDict, total=False):
    ad_group: object
    """
    An inline ad group to create (same shape as POST /ad_groups, including
    ad_campaign_id). Creates the ad group and the ad together. Provide this OR
    ad_group_id.
    """

    ad_group_id: str
    """The existing ad group to create the ad in. Provide this OR ad_group, not both."""

    call_to_action: Literal[
        "apply_now",
        "book_now",
        "call_now",
        "contact_us",
        "download",
        "get_directions",
        "get_offer",
        "get_quote",
        "learn_more",
        "listen_now",
        "message_page",
        "no_button",
        "open_link",
        "order_now",
        "request_time",
        "see_details",
        "see_menu",
        "send_updates",
        "shop_now",
        "sign_up",
        "subscribe",
        "watch_more",
    ]
    """The call-to-action button shown on the ad."""

    creatives: Iterable[Creative]
    """The ad's creative assets.

    Each entry is an uploaded file id with an optional format; omit format for the
    original asset.
    """

    descriptions: SequenceNotStr[str]
    """The description variants shown on the ad."""

    headlines: SequenceNotStr[str]
    """The headline variants shown on the ad."""

    lead_form: LeadForm
    """Instant lead form for the ad.

    Only allowed when the ad group's conversion_location is an instant-form
    destination (instant_forms, instant_forms_and_messenger,
    website_and_instant_forms). Mutually exclusive with lead_form_id.
    """

    lead_form_id: str
    """
    Use an existing instant form instead of creating one — the form's platform ID,
    from a form already on the ad's Facebook page. Only allowed when the ad group's
    conversion_location is an instant-form destination. Mutually exclusive with
    lead_form.
    """

    messaging_config: MessagingConfig
    """
    Click-to-message welcome copy: the greeting (message) and the ice-breaker prompt
    (keyword).
    """

    multi_advertiser_ads: bool
    """Whether the ad can appear alongside other advertisers' ads in the same unit.

    Defaults to true.
    """

    post_id: str
    """
    Promote an existing post instead of uploading creatives — a Facebook post or
    Instagram media id. Mutually exclusive with creatives. Pair with post_source.
    """

    post_source: Literal["facebook", "instagram"]
    """
    Which network post_id refers to — facebook (a page post) or instagram (a media
    id). Authoritative; when omitted the source is inferred from the id shape.
    """

    primary_texts: SequenceNotStr[str]
    """The primary text variants shown in the ad body."""

    social_accounts: Iterable[SocialAccount]
    """
    The social accounts the ad runs under — a connected Facebook page and,
    optionally, an Instagram profile.
    """

    title: str
    """The display name of the ad."""

    url: str
    """The URL the ad links to."""

    url_parameters: object
    """Query parameters appended to the destination URL, keyed by parameter name."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class CreativeCrop(TypedDict, total=False):
    """The saved crop window for this creative, in source image pixels.

    Omit it for the original asset or for a format that has not been cropped.
    """

    height: float

    width: float

    x: float

    y: float


class Creative(TypedDict, total=False):
    id: str
    """Uploaded file ID, prefixed `file_`."""

    crop: CreativeCrop
    """The saved crop window for this creative, in source image pixels.

    Omit it for the original asset or for a format that has not been cropped.
    """

    format: Literal["square", "vertical", "horizontal"]


class LeadFormCompletion(TypedDict, total=False):
    """
    Optional completion screen shown after submission; url sets the follow-up website button.
    """

    button_text: str

    description: str

    headline: str

    url: str


class LeadFormDisclaimerCheckbox(TypedDict, total=False):
    checked_by_default: bool

    key: str

    required: bool

    text: str


class LeadFormDisclaimer(TypedDict, total=False):
    """Optional custom consent disclaimer with checkboxes."""

    body: str

    checkboxes: Iterable[LeadFormDisclaimerCheckbox]

    title: str


class LeadFormIntro(TypedDict, total=False):
    """Optional intro screen shown before the questions."""

    description: str

    headline: str


class LeadFormPrivacyPolicy(TypedDict, total=False):
    """Your privacy policy. url is required by the ad platform."""

    link_text: str

    url: str


class LeadFormQuestionOptionLogic(TypedDict, total=False):
    action: Literal["go_to_question", "submit_form", "close_form"]

    target_end_page_index: int

    target_question_index: int


class LeadFormQuestionOption(TypedDict, total=False):
    key: str

    logic: LeadFormQuestionOptionLogic

    value: str


class LeadFormQuestion(TypedDict, total=False):
    format: Literal["short_answer", "multiple_choice", "appointment"]

    label: str

    options: Iterable[LeadFormQuestionOption]

    type: Literal[
        "email",
        "phone",
        "full_name",
        "first_name",
        "last_name",
        "city",
        "state",
        "zip",
        "country",
        "street_address",
        "job_title",
        "company_name",
        "work_email",
        "work_phone_number",
        "dob",
        "gender",
        "marital_status",
        "relationship_status",
        "military_status",
        "date_time",
        "custom",
    ]


class LeadForm(TypedDict, total=False):
    """Instant lead form for the ad.

    Only allowed when the ad group's conversion_location is an instant-form destination (instant_forms, instant_forms_and_messenger, website_and_instant_forms). Mutually exclusive with lead_form_id.
    """

    completion: LeadFormCompletion
    """
    Optional completion screen shown after submission; url sets the follow-up
    website button.
    """

    disclaimer: LeadFormDisclaimer
    """Optional custom consent disclaimer with checkboxes."""

    form_type: Literal["more_volume", "higher_intent"]
    """
    more_volume (default) is quickest to submit; higher_intent adds a confirmation
    step.
    """

    intro: LeadFormIntro
    """Optional intro screen shown before the questions."""

    name: str
    """Internal name for the form. Auto-generated if omitted."""

    phone_verification: bool
    """Require SMS verification of the phone number (higher_intent forms)."""

    privacy_policy: LeadFormPrivacyPolicy
    """Your privacy policy. url is required by the ad platform."""

    questions: Iterable[LeadFormQuestion]
    """The questions on the form.

    Standard prefill types need only a type; a custom question needs a label and a
    format (plus options for multiple_choice). Options carry an optional key and
    answer-routing logic.
    """


class MessagingConfig(TypedDict, total=False):
    """
    Click-to-message welcome copy: the greeting (message) and the ice-breaker prompt (keyword).
    """

    keyword: str

    message: str


class SocialAccount(TypedDict, total=False):
    id: str
    """Social account ID, prefixed `sacc_`."""
