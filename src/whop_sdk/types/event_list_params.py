# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    after: str
    """A cursor for fetching events after a previous page."""

    attribution_model: Literal["last_touch", "first_touch"]
    """Attribution model for the source filter (defaults to last_touch)."""

    before: str
    """A cursor for fetching events before a later page."""

    browser: str
    """Browser families to filter by, comma-separated (e.g. Chrome, Mobile Safari)."""

    city: str
    """Cities to filter by, comma-separated."""

    country: str
    """Country codes to filter by, comma-separated."""

    device: str
    """Device families to filter by, comma-separated (e.g. iPhone, Mac)."""

    event: str
    """
    Full event names to filter by, comma-separated (payment.completed, pixel.lead,
    pixel.page, pixel.custom:<name>) — the same vocabulary the events / people
    metrics use.
    """

    first: int
    """The number of events to return."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start of the time range as an ISO 8601 timestamp.

    Required when identifier is omitted.
    """

    hostname: str
    """Page hostnames to filter by, comma-separated."""

    identifier: str
    """
    Any hard identifier of the person: a person ID (prsn\\__\\**), user ID, email, phone
    number, or a tracking cookie value (wuid, anonymous ID, fbp/fbc/ttp/ga). Omit to
    list recent events for the account.
    """

    os: str
    """Operating system families to filter by, comma-separated (e.g. iOS, Windows)."""

    page: str
    """Page paths to filter by, comma-separated."""

    source: str
    """
    Canonical source path, exact or with a trailing :_ prefix (whop:<campaign>:_,
    ext:meta:\\**, referrer:<domain>, direct). Restricts the list to conversion
    targets attributed to that source — the debuggability twin of a metric cell's
    source parameter.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time range as an ISO 8601 timestamp.

    Required when identifier is omitted; otherwise defaults to now.
    """

    utm_source: str
    """utm_source values to filter by, comma-separated."""
