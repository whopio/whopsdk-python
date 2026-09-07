# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "AdUpdatedWebhookEvent",
    "Data",
    "DataAdCampaign",
    "DataAdGroup",
    "DataCreative",
    "DataCreativeCrop",
    "DataIssue",
    "DataSocialAccount",
    "DataLeadForm",
    "DataLeadFormCompletion",
    "DataLeadFormDisclaimer",
    "DataLeadFormDisclaimerCheckbox",
    "DataLeadFormIntro",
    "DataLeadFormPrivacyPolicy",
    "DataLeadFormQuestion",
    "DataLeadFormQuestionOption",
    "DataLeadFormQuestionOptionLogic",
    "DataMessagingConfig",
    "DataMusic",
]


class DataAdCampaign(BaseModel):
    """The ad campaign this ad belongs to."""

    id: str
    """The referenced entity's id."""


class DataAdGroup(BaseModel):
    """The ad group this ad belongs to."""

    id: str
    """The referenced entity's id."""


class DataCreativeCrop(BaseModel):
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


class DataCreative(BaseModel):
    """The creative assets used by this ad.

    The original asset has a null format; square, vertical, and horizontal entries are placement-specific variants. A carousel ad returns one format-null entry per attachment, in order.
    """

    id: str
    """The creative attachment's file id."""

    crop: Optional[DataCreativeCrop] = None
    """The saved crop window for this creative, in source image pixels.

    Null for the original asset or a format that has not been cropped.
    """

    format: Optional[Literal["square", "vertical", "horizontal"]] = None
    """The placement variant this asset covers, or null for the original asset."""

    media_type: Optional[str] = None
    """The kind of asset, image or video."""

    url: Optional[str] = None
    """CDN url of the asset."""


class DataIssue(BaseModel):
    """Open issues affecting this ad. Empty when there are none."""

    id: str
    """Unique identifier for the issue."""

    message: str
    """A description of what the issue is and how it can be resolved."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class DataSocialAccount(BaseModel):
    """
    The social accounts the ad runs under — its Facebook page and Instagram profile — each referenced by ID, prefixed `sacc_`.
    """

    id: str
    """The referenced entity's id."""


class DataLeadFormCompletion(BaseModel):
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


class DataLeadFormDisclaimerCheckbox(BaseModel):
    """Consent checkboxes the person can tick. Empty when the disclaimer is text-only."""

    checked_by_default: Optional[bool] = None
    """Whether the checkbox starts ticked."""

    key: Optional[str] = None
    """Stable identifier consent responses are stored under."""

    required: Optional[bool] = None
    """Whether the checkbox must be ticked to submit the form."""

    text: str
    """Consent text next to the checkbox."""


class DataLeadFormDisclaimer(BaseModel):
    """Custom consent disclaimer shown before submission.

    `null` when the form has none.
    """

    body: Optional[str] = None
    """Disclaimer text."""

    checkboxes: List[DataLeadFormDisclaimerCheckbox]

    title: Optional[str] = None
    """Disclaimer title."""


class DataLeadFormIntro(BaseModel):
    """Intro screen shown before the questions. `null` when the form has none."""

    description: Optional[str] = None
    """Body text under the headline."""

    headline: Optional[str] = None
    """Headline of the intro screen."""


class DataLeadFormPrivacyPolicy(BaseModel):
    """Your privacy policy, linked from the form. `null` when unset."""

    link_text: Optional[str] = None
    """Link text shown for the policy. `null` uses the platform default."""

    url: str
    """URL of your privacy policy."""


class DataLeadFormQuestionOptionLogic(BaseModel):
    """Where the form goes when this choice is selected.

    Absent when the form just continues to the next question.
    """

    action: Literal["go_to_question", "submit_form", "close_form"]
    """What happens when the choice is selected."""

    target_end_page_index: Optional[float] = None
    """Zero-based index of the ending screen to jump to."""

    target_question_index: Optional[float] = None
    """Zero-based index of the question to jump to, for `go_to_question`."""


class DataLeadFormQuestionOption(BaseModel):
    """Choices for `multiple_choice` questions. Absent for other formats."""

    value: str
    """Choice text shown to the person."""

    key: Optional[str] = None
    """Stable identifier the choice's answers are stored under.

    Absent for simple choices.
    """

    logic: Optional[DataLeadFormQuestionOptionLogic] = None
    """Where the form goes when this choice is selected.

    Absent when the form just continues to the next question.
    """


class DataLeadFormQuestion(BaseModel):
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

    options: Optional[List[DataLeadFormQuestionOption]] = None


class DataLeadForm(BaseModel):
    """The instant lead form shown when someone taps this ad.

    `null` when the ad group's conversion_location is not an instant-form destination.
    """

    completion: Optional[DataLeadFormCompletion] = None
    """Screen shown after the form is submitted.

    `null` when the form uses the default.
    """

    disclaimer: Optional[DataLeadFormDisclaimer] = None
    """Custom consent disclaimer shown before submission.

    `null` when the form has none.
    """

    form_type: Literal["more_volume", "higher_intent"]
    """
    `more_volume` is quickest to submit; `higher_intent` adds a confirmation step
    before submission.
    """

    intro: Optional[DataLeadFormIntro] = None
    """Intro screen shown before the questions. `null` when the form has none."""

    name: Optional[str] = None
    """Internal name of the form."""

    phone_verification: bool
    """Whether the phone number must be verified by SMS before submitting."""

    privacy_policy: Optional[DataLeadFormPrivacyPolicy] = None
    """Your privacy policy, linked from the form. `null` when unset."""

    questions: List[DataLeadFormQuestion]


class DataMessagingConfig(BaseModel):
    """Welcome message for click-to-message ads, shown when the conversation opens.

    `null` when the ad has none.
    """

    keyword: Optional[str] = None
    """Suggested reply the person can tap to start the conversation."""

    message: Optional[str] = None
    """Greeting shown when the conversation opens."""


class DataMusic(BaseModel):
    """The advertiser-uploaded MP3 a TikTok carousel ad plays.

    TikTok-only; `null` elsewhere and for non-carousel ads.
    """

    id: str
    """The music attachment's file id."""

    name: Optional[str] = None
    """The uploaded file's name."""

    url: Optional[str] = None
    """CDN url of the MP3."""


class Data(BaseModel):
    id: str
    """Unique identifier for the ad, prefixed `ad_`."""

    ad_campaign: DataAdCampaign
    """The ad campaign this ad belongs to."""

    ad_group: DataAdGroup
    """The ad group this ad belongs to."""

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

    created_at: str
    """When the ad was created, as an ISO 8601 timestamp."""

    creatives: List[DataCreative]

    delivery_status: Literal[
        "rejected",
        "in_review",
        "draft",
        "campaign_paused",
        "ad_group_paused",
        "paused",
        "processing",
        "issues",
        "scheduled",
        "learning_limited",
        "learning",
        "active",
    ]
    """Whether the ad is delivering right now, and if not, why.

    When several states apply at once, the highest-precedence one is returned.
    """

    descriptions: List[str]

    existing_post_id: Optional[str] = None
    """
    The post you pointed this ad at, when it promotes one you already published — a
    Facebook post, Instagram media, or TikTok video ID. `null` when the ad uses
    uploaded creatives.
    """

    headlines: List[str]

    issues: List[DataIssue]

    post_id: Optional[str] = None
    """
    The post the ad network serves for this ad, as `pageID_postID` on Meta — the
    post Meta created for an uploaded creative, or the post being promoted. Use it
    to open the live post, or to promote the same post from another ad. `null` until
    the network has created the post.
    """

    post_source: Optional[Literal["facebook", "instagram"]] = None
    """
    Identifies the network that owns `existing_post_id`; `null` when the ad uses
    uploaded creatives.
    """

    post_thumbnail_url: Optional[str] = None
    """Preview image of the post named by `existing_post_id`.

    `null` for ads that use uploaded creatives, or until the post's media has been
    fetched from the network.
    """

    primary_texts: List[str]

    social_accounts: List[DataSocialAccount]

    status: Literal["active", "paused", "in_review", "rejected"]
    """Whether the ad is enabled.

    `active` and `paused` are set by you; `in_review` and `rejected` come from ad
    review.
    """

    title: Optional[str] = None
    """Display title of the ad."""

    updated_at: str
    """When the ad was last updated, as an ISO 8601 timestamp."""

    url: Optional[str] = None
    """The URL the ad links to, without its query string.

    Parameters belong in `url_parameters`; any you send on `url` are moved there.
    """

    url_parameters: object
    """
    Every query parameter appended to the URL, keyed by parameter name — including
    any you sent on `url` itself. Whop adds its own click-attribution parameters on
    top; those are reserved and rejected if you set them. Which keys are reserved
    depends on the ad's network — Meta: utm_meta_ad_id, utm_meta_adset_id,
    utm_meta_campaign_id, utm_source, utm_placement, utm_medium, utm_content,
    utm_adset, utm_whop, wacid, wasid, waid, tw_source, tw_adid; TikTok: waid,
    wasid, wacid, ad_id, adset_id, campaign_id, utm_source, utm_medium,
    utm_placement, utm_whop, tw_source, tw_adid.
    """

    lead_form: Optional[DataLeadForm] = None
    """The instant lead form shown when someone taps this ad.

    `null` when the ad group's conversion_location is not an instant-form
    destination.
    """

    lead_form_id: Optional[str] = None
    """The ad platform's ID for the instant form the ad uses.

    Set when the ad references an existing form via `lead_form_id`, or once a form
    built from `lead_form` has been created on the platform.
    """

    messaging_config: Optional[DataMessagingConfig] = None
    """Welcome message for click-to-message ads, shown when the conversation opens.

    `null` when the ad has none.
    """

    multi_advertiser_ads: Optional[bool] = None
    """Whether the ad can appear alongside other advertisers' ads in the same unit.

    Defaults to true.
    """

    music: Optional[DataMusic] = None
    """The advertiser-uploaded MP3 a TikTok carousel ad plays.

    TikTok-only; `null` elsewhere and for non-carousel ads.
    """


class AdUpdatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["ad.updated"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
