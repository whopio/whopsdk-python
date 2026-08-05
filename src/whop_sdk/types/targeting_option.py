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

    description: Optional[str] = None
    """The ad platform's description of who the option covers, when it publishes one."""

    name: str
    """Display name, such as `Movies`."""

    type: Literal["interests", "behaviors", "life_events", "industries", "income", "family_statuses"]
    """
    Which detailed-targeting field the option belongs in: `interests`/`behaviors` go
    in `detailed_targeting.interests`/`.behaviors`; the demographic categories go in
    `detailed_targeting.demographics` with this value as the entry's `type`.
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
    The standardized code the ad-group targeting fields take: an ISO 3166-1 code for
    countries (`US`) or an ISO 3166-2 code for US states and DC (`US-CA`). Null for
    locations without one, such as cities — target those by `key` instead.
    """

    country_code: Optional[str] = None
    """ISO 3166-1 code of the country the location sits in."""

    country_name: Optional[str] = None
    """Name of the country the location sits in."""

    key: str
    """The ad platform's key for the location in its location taxonomy.

    Use it as the `key` of a `regions` city or zip entry.
    """

    location_type: Literal["country", "region", "city", "zip"]
    """Kind of location: `country`, `region`, `city`, or `zip`."""

    name: str
    """Display name, such as `California`."""

    region: Optional[str] = None
    """Name of the state or province a city sits in. Null for everything but cities."""

    type: Literal["locations"]
    """Always `locations`. The option goes in the ad-group `regions` field."""


TargetingOption: TypeAlias = Union[DetailedTargetingOption, LanguageTargetingOption, LocationTargetingOption]
