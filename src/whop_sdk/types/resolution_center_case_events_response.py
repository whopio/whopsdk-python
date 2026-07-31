# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResolutionCenterCaseEventsResponse", "Data", "DataAttachment", "PageInfo"]


class DataAttachment(BaseModel):
    """Files attached to this event, such as screenshots or documents."""

    id: str
    """Unique identifier for the attachment, prefixed `att_`."""

    content_type: Optional[str] = None
    """The file's MIME type."""

    filename: Optional[str] = None
    """The original file name."""

    url: Optional[str] = None
    """A URL to view or download the file."""


class Data(BaseModel):
    id: str
    """Unique identifier for the event, prefixed `revt_`."""

    action: Literal[
        "created",
        "responded",
        "accepted",
        "denied",
        "appealed",
        "withdrew",
        "requested_more_info",
        "escalated",
        "dispute_opened",
        "dispute_customer_won",
        "dispute_merchant_won",
    ]
    """The action recorded in this event."""

    attachments: List[DataAttachment]

    created_at: str
    """When the event occurred, as an ISO 8601 timestamp."""

    details: Optional[str] = None
    """The message body or additional context provided with the event."""

    reporter_type: Literal["merchant", "customer", "platform", "system"]
    """The party that performed the action."""

    viewable_by_customer: bool
    """Whether the customer can see this event in the timeline."""

    viewable_by_merchant: bool
    """Whether the merchant can see this event in the timeline."""


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class ResolutionCenterCaseEventsResponse(BaseModel):
    data: List[Data]

    page_info: PageInfo
