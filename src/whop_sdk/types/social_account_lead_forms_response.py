# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SocialAccountLeadFormsResponse",
    "Data",
    "DataCompletion",
    "DataDisclaimer",
    "DataDisclaimerCheckbox",
    "DataIntro",
    "DataQuestion",
    "DataQuestionOption",
    "DataQuestionOptionLogic",
]


class DataCompletion(BaseModel):
    """Screen shown after the form is submitted. `null` when the form has none."""

    button_text: Optional[str] = None
    """Text of the follow-up button."""

    description: Optional[str] = None
    """Body text under the headline."""

    headline: Optional[str] = None
    """Headline of the completion screen."""

    url: Optional[str] = None
    """Website the follow-up button opens. `null` when the screen has no button."""


class DataDisclaimerCheckbox(BaseModel):
    """Consent checkboxes the person can tick. Empty when the disclaimer is text-only."""

    checked_by_default: Optional[bool] = None
    """Whether the checkbox starts ticked."""

    key: Optional[str] = None
    """Stable identifier consent responses are stored under."""

    required: Optional[bool] = None
    """Whether the checkbox must be ticked to submit the form."""

    text: str
    """Consent text next to the checkbox."""


class DataDisclaimer(BaseModel):
    """Custom consent disclaimer shown before submission.

    `null` when the form has none.
    """

    body: Optional[str] = None
    """Disclaimer text."""

    checkboxes: List[DataDisclaimerCheckbox]

    title: Optional[str] = None
    """Disclaimer title."""


class DataIntro(BaseModel):
    """Intro screen shown before the questions. `null` when the form has none."""

    description: Optional[str] = None
    """Body text under the headline."""

    headline: Optional[str] = None
    """Headline of the intro screen."""


class DataQuestionOptionLogic(BaseModel):
    """Where the form goes when this choice is selected.

    Absent when the form just continues to the next question.
    """

    action: Literal["go_to_question", "submit_form", "close_form"]
    """What happens when the choice is selected."""

    target_end_page_index: Optional[float] = None
    """Zero-based index of the ending screen to jump to."""

    target_question_index: Optional[float] = None
    """Zero-based index of the question to jump to, for `go_to_question`."""


class DataQuestionOption(BaseModel):
    """Choices for `multiple_choice` questions. Absent for other formats."""

    value: str
    """Choice text shown to the person."""

    key: Optional[str] = None
    """Stable identifier the choice's answers are stored under.

    Absent for simple choices.
    """

    logic: Optional[DataQuestionOptionLogic] = None
    """Where the form goes when this choice is selected.

    Absent when the form just continues to the next question.
    """


class DataQuestion(BaseModel):
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

    options: Optional[List[DataQuestionOption]] = None


class Data(BaseModel):
    id: str
    """The ad platform's identifier for the form.

    Use it as lead_gen_form_id on an ad to reuse the form.
    """

    completion: Optional[DataCompletion] = None
    """Screen shown after the form is submitted. `null` when the form has none."""

    created_at: Optional[str] = None
    """When the form was created, as an ISO 8601 timestamp."""

    disclaimer: Optional[DataDisclaimer] = None
    """Custom consent disclaimer shown before submission.

    `null` when the form has none.
    """

    form_type: Literal["more_volume", "higher_intent"]
    """
    `more_volume` is quickest to submit; `higher_intent` adds a confirmation step
    before submission.
    """

    intro: Optional[DataIntro] = None
    """Intro screen shown before the questions. `null` when the form has none."""

    locale: Optional[str] = None
    """Language the form is shown in, such as en_US."""

    name: Optional[str] = None
    """Advertiser-facing form name."""

    privacy_policy_link_text: Optional[str] = None
    """Custom link text for the privacy policy. `null` when the default is used."""

    privacy_policy_url: Optional[str] = None
    """Privacy policy URL configured on the form."""

    question_labels: List[str]

    questions: List[DataQuestion]


class SocialAccountLeadFormsResponse(BaseModel):
    data: List[Data]
