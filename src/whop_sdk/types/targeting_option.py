# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["TargetingOption", "DetailedTargetingOption", "LanguageTargetingOption", "LocationTargetingOption"]


class DetailedTargetingOption(BaseModel):
    id: str
    """The ad platform's ID for the option in its targeting taxonomy.

    Use it as the `id` of a `detailed_targeting` entry.
    """

    audience_size_lower_bound: Optional[float] = None
    """Low end of the ad platform's estimate of how many people this option can reach.

    Null when the platform doesn't publish one.
    """

    audience_size_upper_bound: Optional[float] = None
    """High end of the ad platform's estimate of how many people this option can reach.

    Null when the platform doesn't publish one.
    """

    behavior_type: Optional[Literal["video", "creator", "hashtag"]] = None
    """What a behavior category is measured on, on ad platforms that scope them.

    Send it back on the `detailed_targeting.behaviors` entry alongside the id. Null
    for options that aren't scoped.
    """

    description: Optional[str] = None
    """The ad platform's description of who the option covers, when it publishes one."""

    name: str
    """Display name, such as `Movies`."""

    type: Literal[
        "interests",
        "behaviors",
        "life_events",
        "industries",
        "income",
        "family_statuses",
        "work_employers",
        "work_positions",
        "education_schools",
        "education_majors",
    ]
    """
    Which detailed-targeting field the option belongs in: `interests` and
    `behaviors` go in the matching `detailed_targeting` field; demographic
    categories (`life_events`, `industries`, `income`, `family_statuses`,
    `work_employers`, `work_positions`, `education_schools`, `education_majors`) go
    in `detailed_targeting.demographics` with this value as the entry's `type`.
    """


class LanguageTargetingOption(BaseModel):
    code: str
    """ISO 639 code the ad-group `languages` field takes, such as `en`."""

    name: str
    """Display name, such as `English`."""

    type: Literal["languages"]
    """Always `languages`. The option goes in the ad-group `languages` field."""


class LocationTargetingOption(BaseModel):
    code: Optional[str] = None
    """
    The standardized code the ad-group `regions` field takes: an ISO 3166-1 code for
    countries (`US`) or an ISO 3166-2 code for states and provinces (`US-CA`,
    `CA-ON`). Null for a location that has no standard code, such as a city or a
    metro area — target those by `key` in the `regions` cities list instead.
    """

    country_code: Optional[str] = None
    """ISO 3166-1 code of the country the location sits in."""

    country_name: Optional[str] = None
    """Name of the country the location sits in."""

    key: str
    """The ad platform's key for the location in its location taxonomy.

    Use it as the `key` of a `regions` city or zip entry.
    """

    location_type: Literal[
        "country", "region", "city", "zip", "neighborhood", "subcity", "medium_geo_area", "district", "dma"
    ]
    """Granularity of the location.

    Which of these an ad platform reports depends on how finely it divides its
    location taxonomy.
    """

    name: str
    """Display name, such as `California`."""

    region: Optional[str] = None
    """Name of the state or province a city sits in. Null for everything but cities."""

    type: Literal["locations"]
    """Always `locations`. The option goes in the ad-group `regions` field."""


TargetingOption: TypeAlias = Union[DetailedTargetingOption, LanguageTargetingOption, LocationTargetingOption]
