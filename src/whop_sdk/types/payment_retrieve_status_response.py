# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentRetrieveStatusResponse", "LastPaymentError", "NextAction", "ProcessingDetails"]


class LastPaymentError(BaseModel):
    """
    Details of the most recent failed attempt, or `null` when the payment has not failed.
    """

    code: Optional[str] = None
    """A machine-readable classification of the failure."""

    decline_code: Optional[str] = None
    """The issuer's or processor's own decline code, when one was returned."""

    message: Optional[str] = None
    """A human-readable explanation of the failure."""


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


class ProcessingDetails(BaseModel):
    """Present while `status` is `processing` on a settlement rail, otherwise `null`."""

    expected_by: Optional[str] = None
    """When the payment is expected to settle, as an ISO 8601 timestamp."""


class PaymentRetrieveStatusResponse(BaseModel):
    id: str
    """The payment this status describes, prefixed `pay_`."""

    last_payment_error: Optional[LastPaymentError] = None
    """
    Details of the most recent failed attempt, or `null` when the payment has not
    failed.
    """

    next_action: Optional[NextAction] = None
    """
    What the buyer must do next while `status` is `requires_action`, otherwise
    `null`.
    """

    object: str
    """Always `payment_status`."""

    processing_details: Optional[ProcessingDetails] = None
    """Present while `status` is `processing` on a settlement rail, otherwise `null`."""

    return_url: Optional[str] = None
    """
    Where to send the buyer once the payment reaches a resting state, or `null` to
    leave them where they are. Editable until they return — see the return_url
    operation.
    """

    status: Literal["requires_confirmation", "requires_action", "confirming", "processing", "succeeded", "canceled"]
    """How far the payment has got.

    `requires_confirmation` — nothing attempted yet, or the last attempt failed and
    can be retried. `requires_action` — the buyer has a step outstanding; see
    `next_action`. `confirming` — the buyer has done their part and the processor is
    deciding. `processing` — the money is moving; see `processing_details`.
    `succeeded` — collected. `canceled` — voided or written off.
    """
