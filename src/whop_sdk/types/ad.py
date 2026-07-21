# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Ad",
    "AdCampaign",
    "AdGroup",
    "Creative",
    "CreativeCrop",
    "Issue",
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


class AdCampaign(BaseModel):
    """The ad campaign this ad belongs to."""

    id: str
    """The referenced entity's id."""


class AdGroup(BaseModel):
    """The ad group this ad belongs to."""

    id: str
    """The referenced entity's id."""


class CreativeCrop(BaseModel):
    """The saved crop window for this creative, in source image pixels.

    Null for the original asset or a format that has not been cropped.
    """

    height: float
    """Height of the crop window in source pixels."""

    width: float
    """Width of the crop window in source pixels."""

    x: float
    """Left edge of the crop window in source pixels."""

    y: float
    """Top edge of the crop window in source pixels."""


class Creative(BaseModel):
    """The creative assets used by this ad.

    The original asset has a null format; square, vertical, and horizontal entries are placement-specific variants. A carousel ad returns one format-null entry per attachment, in order.
    """

    id: str
    """The creative attachment's file id."""

    crop: Optional[CreativeCrop] = None
    """The saved crop window for this creative, in source image pixels.

    Null for the original asset or a format that has not been cropped.
    """

    format: Optional[Literal["square", "vertical", "horizontal"]] = None
    """The placement variant this asset covers, or null for the original asset."""

    media_type: Optional[str] = None
    """The kind of asset, image or video."""

    url: Optional[str] = None
    """CDN url of the asset."""


class Issue(BaseModel):
    """Open issues affecting this ad. Empty when there are none."""

    id: str
    """Unique identifier for the issue."""

    message: str
    """A description of what the issue is and how it can be resolved."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class LeadFormCompletion(BaseModel):
    """Screen shown after the form is submitted.

    `null` when the form uses the default.
    """

    button_text: Optional[str] = None
    """Text of the follow-up button."""

    description: Optional[str] = None
    """Body text under the headline."""

    headline: Optional[str] = None
    """Headline of the completion screen."""

    url: Optional[str] = None
    """Website the follow-up button opens. `null` when the screen has no button."""


class LeadFormDisclaimerCheckbox(BaseModel):
    """Consent checkboxes the person can tick. Empty when the disclaimer is text-only."""

    checked_by_default: Optional[bool] = None
    """Whether the checkbox starts ticked."""

    key: Optional[str] = None
    """Stable identifier consent responses are stored under."""

    required: Optional[bool] = None
    """Whether the checkbox must be ticked to submit the form."""

    text: str
    """Consent text next to the checkbox."""


class LeadFormDisclaimer(BaseModel):
    """Custom consent disclaimer shown before submission.

    `null` when the form has none.
    """

    body: Optional[str] = None
    """Disclaimer text."""

    checkboxes: List[LeadFormDisclaimerCheckbox]

    title: Optional[str] = None
    """Disclaimer title."""


class LeadFormIntro(BaseModel):
    """Intro screen shown before the questions. `null` when the form has none."""

    description: Optional[str] = None
    """Body text under the headline."""

    headline: Optional[str] = None
    """Headline of the intro screen."""


class LeadFormPrivacyPolicy(BaseModel):
    """Your privacy policy, linked from the form. `null` when unset."""

    link_text: Optional[str] = None
    """Link text shown for the policy. `null` uses the platform default."""

    url: str
    """URL of your privacy policy."""


class LeadFormQuestionOptionLogic(BaseModel):
    """Where the form goes when this choice is selected.

    Absent when the form just continues to the next question.
    """

    action: Literal["go_to_question", "submit_form", "close_form"]
    """What happens when the choice is selected."""

    target_end_page_index: Optional[float] = None
    """Zero-based index of the ending screen to jump to."""

    target_question_index: Optional[float] = None
    """Zero-based index of the question to jump to, for `go_to_question`."""


class LeadFormQuestionOption(BaseModel):
    """Choices for `multiple_choice` questions. Absent for other formats."""

    value: str
    """Choice text shown to the person."""

    key: Optional[str] = None
    """Stable identifier the choice's answers are stored under.

    Absent for simple choices.
    """

    logic: Optional[LeadFormQuestionOptionLogic] = None
    """Where the form goes when this choice is selected.

    Absent when the form just continues to the next question.
    """


class LeadFormQuestion(BaseModel):
    """Questions on the form, in order."""

    type: str
    """
    Question type: a standard prefill type such as `email`, `phone`, or `full_name`,
    or `custom` for your own question.
    """

    format: Optional[str] = None
    """
    Answer format for `custom` questions: `short_answer`, `multiple_choice`, or
    `appointment`. Absent otherwise.
    """

    label: Optional[str] = None
    """Question text for `custom` questions. Absent for standard prefill questions."""

    options: Optional[List[LeadFormQuestionOption]] = None


class LeadForm(BaseModel):
    """The instant lead form shown when someone taps this ad.

    `null` when the ad group's conversion_location is not an instant-form destination.
    """

    completion: Optional[LeadFormCompletion] = None
    """Screen shown after the form is submitted.

    `null` when the form uses the default.
    """

    disclaimer: Optional[LeadFormDisclaimer] = None
    """Custom consent disclaimer shown before submission.

    `null` when the form has none.
    """

    form_type: Literal["more_volume", "higher_intent"]
    """
    `more_volume` is quickest to submit; `higher_intent` adds a confirmation step
    before submission.
    """

    intro: Optional[LeadFormIntro] = None
    """Intro screen shown before the questions. `null` when the form has none."""

    name: Optional[str] = None
    """Internal name of the form."""

    phone_verification: bool
    """Whether the phone number must be verified by SMS before submitting."""

    privacy_policy: Optional[LeadFormPrivacyPolicy] = None
    """Your privacy policy, linked from the form. `null` when unset."""

    questions: List[LeadFormQuestion]


class MessagingConfig(BaseModel):
    """Welcome message for click-to-message ads, shown when the conversation opens.

    `null` when the ad has none.
    """

    keyword: Optional[str] = None
    """Suggested reply the person can tap to start the conversation."""

    message: Optional[str] = None
    """Greeting shown when the conversation opens."""


class SocialAccount(BaseModel):
    """
    The social accounts the ad runs under — its Facebook page and Instagram profile — each referenced by ID, prefixed `sacc_`.
    """

    id: str
    """The referenced entity's id."""


class Ad(BaseModel):
    id: str
    """Unique identifier for the ad, prefixed `ad_`."""

    ad_campaign: AdCampaign
    """The ad campaign this ad belongs to."""

    ad_group: AdGroup
    """The ad group this ad belongs to."""

    added_to_cart_value: float
    """USD value attributed to add-to-cart events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    added_to_carts: float
    """Whop pixel-attributed add-to-cart events, last-click."""

    call_to_action: Optional[
        Literal[
            "learn_more",
            "shop_now",
            "sign_up",
            "subscribe",
            "get_started",
            "book_now",
            "apply_now",
            "contact_us",
            "download",
            "order_now",
            "buy_now",
            "get_quote",
            "message_page",
            "whatsapp_message",
            "instagram_message",
            "call_now",
            "get_directions",
            "send_updates",
            "get_offer",
            "watch_more",
            "listen_now",
            "play_game",
            "open_link",
            "no_button",
            "get_offer_view",
            "get_event_tickets",
            "see_menu",
            "request_time",
            "event_rsvp",
            "see_details",
            "view_instagram_profile",
        ]
    ] = None
    """The call-to-action button shown on the ad."""

    click_through_rate: float
    """Clicks divided by impressions, between 0 and 1."""

    clicks: float
    """The number of clicks."""

    completed_registration_value: float
    """USD value attributed to complete-registration events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    completed_registrations: float
    """Whop pixel-attributed complete-registration events, last-click."""

    contact_value: float
    """USD value attributed to contact events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    contacts: float
    """Whop pixel-attributed contact events, last-click."""

    cost_per_added_to_cart: Optional[float] = None
    """
    Spend divided by attributed add-to-cart events; null when they are not the goal
    and none are attributed.
    """

    cost_per_click: float
    """Spend divided by clicks; 0 when there are no clicks."""

    cost_per_completed_registration: Optional[float] = None
    """
    Spend divided by attributed complete-registration events; null when they are not
    the goal and none are attributed.
    """

    cost_per_contact: Optional[float] = None
    """
    Spend divided by attributed contact events; null when contacts are not the goal
    and none are attributed.
    """

    cost_per_lead: Optional[float] = None
    """
    Spend divided by attributed leads; null when leads are not a goal and none are
    attributed.
    """

    cost_per_mille: float
    """Spend per 1,000 impressions; 0 when there are no impressions."""

    cost_per_purchase: Optional[float] = None
    """
    Spend divided by attributed purchases; null when purchases are not a goal and
    none are attributed.
    """

    cost_per_result: Optional[float] = None
    """
    Spend divided by Whop pixel-attributed results; null when nothing
    Whop-attributable is being optimized for.
    """

    cost_per_schedule: Optional[float] = None
    """
    Spend divided by attributed schedule events; null when schedules are not the
    goal and none are attributed.
    """

    cost_per_submitted_application: Optional[float] = None
    """
    Spend divided by attributed submit-application events; null when they are not
    the goal and none are attributed.
    """

    cost_per_unique_click: Optional[float] = None
    """Spend divided by unique clicks; null when there are no unique clicks."""

    cost_per_viewed_content: Optional[float] = None
    """
    Spend divided by attributed view-content events; null when they are not the goal
    and none are attributed.
    """

    created_at: str
    """When the ad was created, as an ISO 8601 timestamp."""

    creatives: List[Creative]

    custom_conversions: float
    """
    Whop pixel-attributed custom (merchant-defined) conversion events, last-click,
    across all custom event names.
    """

    custom_event_counts: object
    """
    Whop pixel-attributed custom conversions, keyed by your event name with its
    last-click count as the value. Empty when no named custom events are attributed.
    Custom events fired without a name are counted in custom_conversions but omitted
    here, so these values sum to at most custom_conversions.
    """

    custom_event_values: object
    """
    Conversion value attributed to each custom event, keyed by event name like
    custom_event_counts. Sums the value passed to whop.track, normalized to USD;
    events fired without a value contribute 0.
    """

    delivery_status: Literal[
        "rejected",
        "in_review",
        "draft",
        "campaign_paused",
        "ad_group_paused",
        "paused",
        "processing",
        "issues",
        "learning_limited",
        "learning",
        "active",
    ]
    """Whether the ad is delivering right now, and if not, why.

    When several states apply at once, the highest-precedence one is returned.
    """

    descriptions: List[str]

    frequency: Optional[float] = None
    """Platform-reported impressions divided by reach."""

    headlines: List[str]

    impressions: float
    """The number of impressions."""

    issues: List[Issue]

    lead_form: Optional[LeadForm] = None
    """The instant lead form shown when someone taps this ad.

    `null` when the ad group's conversion_location is not an instant-form
    destination.
    """

    lead_form_id: Optional[str] = None
    """The ad platform's ID for the instant form the ad uses.

    Set when the ad references an existing form via `lead_form_id`, or once a form
    built from `lead_form` has been created on the platform.
    """

    lead_value: float
    """USD value attributed to lead events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    leads: float
    """Whop pixel-attributed leads, last-click."""

    messaging_config: Optional[MessagingConfig] = None
    """Welcome message for click-to-message ads, shown when the conversation opens.

    `null` when the ad has none.
    """

    multi_advertiser_ads: bool
    """Whether the ad can appear alongside other advertisers' ads in the same unit.

    Defaults to true.
    """

    post_id: Optional[str] = None
    """The existing post this ad promotes — a Facebook post or Instagram media ID.

    `null` when the ad uses uploaded creatives.
    """

    post_source: Optional[Literal["facebook", "instagram"]] = None
    """
    Which network `post_id` refers to: `facebook` (a page post) or `instagram` (a
    media ID). `null` when the ad uses uploaded creatives.
    """

    post_thumbnail_url: Optional[str] = None
    """Preview image of the existing post this ad promotes.

    `null` for ads that use uploaded creatives, or until the post's media has been
    fetched from the network.
    """

    primary_texts: List[str]

    purchase_value: float
    """USD value of pixel-attributed purchases."""

    purchases: float
    """Whop pixel-attributed purchases, last-click."""

    reach: float
    """The number of unique people who saw this."""

    result_event: Optional[
        Literal[
            "purchase",
            "lead",
            "schedule",
            "submit_application",
            "contact",
            "complete_registration",
            "view_content",
            "add_to_cart",
            "custom",
        ]
    ] = None
    """
    The Whop pixel conversion event whose attributed count represents results — the
    optimization goal, or the highest-volume attributed event for campaigns that
    budget per ad group. Null when the goal isn't a Whop-attributed event.
    """

    result_event_name: Optional[str] = None
    """
    The merchant-defined event name when result_event is custom; null for the
    standard events.
    """

    results: Optional[float] = None
    """The Whop pixel-attributed count behind result_event.

    When a campaign's ad groups optimize different goals there is no single
    result_event (it is null), and this is instead the sum of each ad group's own
    attributed results. Null when nothing Whop-attributable is being optimized for.
    """

    return_on_ad_spend: float
    """
    Purchase value divided by spend, both in USD (a currency-neutral ratio); 0 when
    there is no spend.
    """

    schedule_value: float
    """USD value attributed to schedule events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    schedules: float
    """Whop pixel-attributed schedule events, last-click."""

    social_accounts: List[SocialAccount]

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    status: Literal["active", "paused", "in_review", "rejected"]
    """Whether the ad is enabled.

    `active` and `paused` are set by you; `in_review` and `rejected` come from ad
    review.
    """

    submitted_application_value: float
    """USD value attributed to submit-application events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    submitted_applications: float
    """Whop pixel-attributed submit-application events, last-click."""

    title: Optional[str] = None
    """Display title of the ad."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """People who clicked, reported by the Whop pixel, counted once per person."""

    updated_at: str
    """When the ad was last updated, as an ISO 8601 timestamp."""

    url: Optional[str] = None
    """The URL the ad links to."""

    url_parameters: object
    """Query parameters appended to the URL, keyed by parameter name."""

    viewed_content_value: float
    """USD value attributed to view-content events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    viewed_contents: float
    """Whop pixel-attributed view-content events, last-click."""
