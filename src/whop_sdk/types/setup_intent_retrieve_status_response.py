# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SetupIntentRetrieveStatusResponse", "NextAction"]


class NextAction(BaseModel):
    """
    What the buyer must do next while `status` is `requires_action`, otherwise `null`.
    """

    data: object
    """
    The payload for this step's type: `url` for `redirect`, `kind` plus that kind's
    details for `display_instructions`, `expires_at` for `await_confirmation`.
    """

    render: List[str]

    type: Literal["redirect", "display_instructions", "await_confirmation"]
    """What kind of step this is.

    `redirect` — send the buyer to `data.url`. `display_instructions` — show them
    `data`, such as a voucher code or bank transfer details. `await_confirmation` —
    nothing to show; they have done their part.
    """


class SetupIntentRetrieveStatusResponse(BaseModel):
    id: str
    """The setup this status describes, prefixed `sint_`."""

    next_action: Optional[NextAction] = None
    """
    What the buyer must do next while `status` is `requires_action`, otherwise
    `null`.
    """

    object: str
    """Always `setup_status`."""

    return_url: Optional[str] = None
    """
    Where to send the buyer once the setup reaches a resting state, or `null` to
    leave them where they are.
    """

    status: Literal["processing", "succeeded", "canceled", "requires_action"]
    """How far the setup has got.

    `requires_action` — the buyer has a step outstanding; see `next_action`.
    `processing` — the buyer has done their part and the processor is deciding.
    `succeeded` — the payment method is saved. `canceled` — abandoned or refused.
    """
