# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AudienceCreateParams", "ColumnMapping"]


class AudienceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    audience_type: Literal["custom", "lookalike"]
    """What to create. Defaults to `custom` (CSV upload)."""

    auto_refresh: bool
    """Filter audiences only, and set only at creation.

    `true` (the default) rebuilds membership from the filters twice a day. `false`
    keeps whoever matched at creation and never rebuilds.
    """

    column_mapping: ColumnMapping
    """Custom audiences only.

    Maps supported identity fields to CSV column headers. Map at least one of
    `email` or `phone`.
    """

    count: int
    """Lookalikes only. Number of lookalike audiences to create (1–6)."""

    file_id: str
    """Custom audiences only.

    The uploaded customer CSV — a file id (`file_...`) returned by `POST /files`.
    """

    filters: object
    """Filter audiences only.

    The People filters that define membership, keyed exactly as `GET /people`
    accepts them — for example `{"os": "iOS", "country": "US"}`. Date filters must
    be rolling windows — `first_seen_within_days` or `last_seen_within_days` — so
    the audience re-anchors on every refresh; fixed dates such as `first_seen_after`
    are rejected. Source values are canonical source paths
    (`whop:<campaign>:<group>:<ad>`, `ext:<platform>:...`, `referrer:<domain>`,
    `direct`), exact or with a trailing `:*` wildcard.
    """

    name: str
    """Audience display name.

    Required for custom audiences; lookalike names are generated from the source
    audience.
    """

    percentage: int
    """Lookalikes only.

    Total similarity reach as a whole percent (1–20), sliced evenly across `count` —
    must be divisible by `count`.
    """

    source_audience_id: str
    """Lookalikes only.

    The ready custom audience (`adaud_`) to build from; it needs at least 100
    matched people.
    """


class ColumnMapping(TypedDict, total=False):
    """Custom audiences only.

    Maps supported identity fields to CSV column headers. Map at least one of `email` or `phone`.
    """

    country: str
    """CSV header for ISO 3166-1 alpha-2 country codes, such as `US`."""

    email: str
    """CSV header for email addresses."""

    first_name: str
    """CSV header for first names."""

    last_name: str
    """CSV header for last names."""

    ltv: str
    """
    CSV header for each customer's lifetime value — a non-negative number, currency
    symbols allowed. When mapped, Meta creates the audience as value-based, so
    lookalikes built from it favor people similar to the highest-value customers.
    """

    phone: str
    """CSV header for phone numbers."""
