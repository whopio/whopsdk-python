# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SocialAccountLeadFormsResponse", "Data"]


class Data(BaseModel):
    id: str
    """The ad platform's identifier for the form.

    Use it as lead_gen_form_id on an ad to reuse the form.
    """

    created_at: Optional[str] = None
    """When the form was created, as an ISO 8601 timestamp."""

    locale: Optional[str] = None
    """Language the form is shown in, such as en_US."""

    name: Optional[str] = None
    """Advertiser-facing form name."""

    privacy_policy_url: Optional[str] = None
    """Privacy policy URL configured on the form."""

    question_labels: List[str]


class SocialAccountLeadFormsResponse(BaseModel):
    data: List[Data]
