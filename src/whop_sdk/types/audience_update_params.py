# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AudienceUpdateParams"]


class AudienceUpdateParams(TypedDict, total=False):
    filters: object
    """Only for an audience that keeps itself up to date.

    Replaces the People filters that define membership, keyed as `GET /people`
    accepts them. With auto refresh off the audience keeps the people it matched
    when it was built, so its filters can't be replaced — create a new audience
    instead.
    """

    name: str
    """New audience display name."""
