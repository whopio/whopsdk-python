# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AudienceUpdateParams"]


class AudienceUpdateParams(TypedDict, total=False):
    filters: object
    """Replaces the People filters that define membership.

    The whole definition is replaced rather than merged, so send every filter you
    want to keep — a filter you leave out stops applying. Keys and values are the
    ones `GET /people` accepts, such as an `os` of `iOS` or a `country` of `US`, and
    at least one filter is required. Date filters must be rolling windows —
    `first_seen_within_days` or `last_seen_within_days` — so the audience re-anchors
    every time it rebuilds; fixed dates such as `first_seen_after` are rejected, as
    is `audience_id`. An array value holds at most 500 items, and each value at most
    10 KB. Only an audience with a `source_type` of `people_filter` and
    `auto_refresh` of `true` accepts filters: an uploaded list has no filters to
    replace, and with auto refresh off the audience keeps the people it matched when
    it was built, so create a new audience instead.
    """

    name: str
    """New audience display name.

    A blank value is ignored rather than clearing the name.
    """
