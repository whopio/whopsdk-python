# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AdGroupEstimateReachParams",
    "Audiences",
    "Demographics",
    "DetailedTargeting",
    "DetailedTargetingBehavior",
    "DetailedTargetingDemographic",
    "DetailedTargetingInterest",
    "Devices",
    "DevicesOperatingSystem",
    "Regions",
    "RegionsExclude",
    "RegionsExcludeCity",
    "RegionsExcludeCustomLocation",
    "RegionsExcludeZip",
    "RegionsExcludeZipKey",
    "RegionsInclude",
    "RegionsIncludeCity",
    "RegionsIncludeCustomLocation",
    "RegionsIncludeZip",
    "RegionsIncludeZipKey",
]


class AdGroupEstimateReachParams(TypedDict, total=False):
    platform: Required[Literal["meta"]]
    """The ad network the estimate runs on."""

    account_id: str
    """Account to estimate on behalf of. Defaults to the authenticated account."""

    audiences: Audiences
    """Saved audiences to deliver to or exclude.

    Can't be combined with demographics.automatic.
    """

    demographics: Demographics
    """Age, gender, and automatic-audience targeting."""

    detailed_targeting: DetailedTargeting
    """
    Interest, behavior, and demographic targeting, using categories from the ad
    platform's targeting taxonomy. At most 100 entries per section.
    """

    devices: Devices
    """Device platforms and operating systems to target."""

    languages: SequenceNotStr[str]
    """Languages to target, as ISO 639 codes such as `en` or `es`.

    Empty or omitted targets all languages.
    """

    regions: Regions
    """Locations to target and exclude."""


class Audiences(TypedDict, total=False):
    """Saved audiences to deliver to or exclude.

    Can't be combined with demographics.automatic.
    """

    exclude: SequenceNotStr[str]
    """IDs of saved audiences to exclude from delivery, prefixed `adaud_`."""

    include: SequenceNotStr[str]
    """IDs of saved audiences to deliver to, prefixed `adaud_`."""


class Demographics(TypedDict, total=False):
    """Age, gender, and automatic-audience targeting."""

    automatic: bool
    """
    Turn on automatic audience targeting (Advantage+ on Meta): the platform can
    deliver beyond the ages, genders, and detailed targeting you set, treating them
    as suggestions.
    """

    gender: Literal["all", "male", "female"]
    """Gender to target."""

    maximum_age: int
    """Oldest age to target."""

    minimum_age: int
    """Youngest age to target."""


class DetailedTargetingBehavior(TypedDict, total=False):
    id: Required[str]
    """The ad platform's ID for the category in its targeting taxonomy."""

    name: str
    """Category name, such as `Movies`."""


class DetailedTargetingDemographic(TypedDict, total=False):
    id: Required[str]
    """The ad platform's ID for the category in its targeting taxonomy."""

    type: Required[
        Literal[
            "life_events",
            "industries",
            "income",
            "family_statuses",
            "work_employers",
            "work_positions",
            "education_schools",
            "education_majors",
        ]
    ]
    """Kind of demographic the category belongs to."""

    name: str
    """Category name, such as `Recently moved`."""


class DetailedTargetingInterest(TypedDict, total=False):
    id: Required[str]
    """The ad platform's ID for the category in its targeting taxonomy."""

    name: str
    """Category name, such as `Movies`."""


class DetailedTargeting(TypedDict, total=False):
    """
    Interest, behavior, and demographic targeting, using categories from the ad platform's targeting taxonomy. At most 100 entries per section.
    """

    behaviors: Iterable[DetailedTargetingBehavior]
    """Behavior categories to target, such as frequent travelers."""

    demographics: Iterable[DetailedTargetingDemographic]
    """
    Demographic categories to target, such as life events, industries, work
    employers, job titles, schools, or majors.
    """

    interests: Iterable[DetailedTargetingInterest]
    """Interest categories to target, such as an interest in movies."""


class DevicesOperatingSystem(TypedDict, total=False):
    os: Required[Literal["ios", "android"]]
    """Operating system to target."""

    minimum_version: str
    """Lowest OS version to target, such as `18.0`. Omit to target any version."""


class Devices(TypedDict, total=False):
    """Device platforms and operating systems to target."""

    operating_systems: Iterable[DevicesOperatingSystem]
    """Operating systems to target. Empty targets all operating systems."""

    platforms: List[Literal["mobile", "desktop"]]
    """Device types to target. Empty targets all devices."""


class RegionsExcludeCity(TypedDict, total=False):
    key: Required[str]
    """The ad platform's key for the city in its location taxonomy."""

    name: str
    """City name, such as `Austin`."""


class RegionsExcludeCustomLocation(TypedDict, total=False):
    latitude: Required[float]
    """Latitude of the center point."""

    longitude: Required[float]
    """Longitude of the center point."""

    radius: Required[float]
    """Radius around the center point: 1-50 miles or 1-80 kilometers."""

    distance_unit: Literal["mile", "kilometer"]
    """Unit for `radius`. Defaults to `mile`."""

    name: str
    """Label for the location, such as a city or address."""


class RegionsExcludeZipKey(TypedDict, total=False):
    key: Required[str]
    """The ZIP or postal code."""


RegionsExcludeZip: TypeAlias = Union[str, RegionsExcludeZipKey]


class RegionsExclude(TypedDict, total=False):
    """Locations excluded from targeting. Country groups can't be excluded."""

    cities: Iterable[RegionsExcludeCity]
    """Cities, keyed by the ad platform's location taxonomy."""

    countries: SequenceNotStr[str]
    """Countries, as ISO 3166-1 alpha-2 codes such as `US`."""

    country_groups: SequenceNotStr[str]
    """Multi-country groups such as `worldwide` or `europe`.

    Include-only — groups can't be excluded.
    """

    custom_locations: Iterable[RegionsExcludeCustomLocation]
    """Circular areas, each a coordinate plus a radius.

    At most 200 across include and exclude.
    """

    regions: SequenceNotStr[str]
    """US states and DC, as ISO 3166-2 codes such as `US-CA`.

    US territories (`PR`, `GU`, `VI`, `AS`, `MP`) and everywhere outside the US are
    targeted through `countries`.
    """

    zips: SequenceNotStr[RegionsExcludeZip]
    """ZIP and postal codes, as bare strings or objects with a key."""


class RegionsIncludeCity(TypedDict, total=False):
    key: Required[str]
    """The ad platform's key for the city in its location taxonomy."""

    name: str
    """City name, such as `Austin`."""


class RegionsIncludeCustomLocation(TypedDict, total=False):
    latitude: Required[float]
    """Latitude of the center point."""

    longitude: Required[float]
    """Longitude of the center point."""

    radius: Required[float]
    """Radius around the center point: 1-50 miles or 1-80 kilometers."""

    distance_unit: Literal["mile", "kilometer"]
    """Unit for `radius`. Defaults to `mile`."""

    name: str
    """Label for the location, such as a city or address."""


class RegionsIncludeZipKey(TypedDict, total=False):
    key: Required[str]
    """The ZIP or postal code."""


RegionsIncludeZip: TypeAlias = Union[str, RegionsIncludeZipKey]


class RegionsInclude(TypedDict, total=False):
    """Locations the ad group targets."""

    cities: Iterable[RegionsIncludeCity]
    """Cities, keyed by the ad platform's location taxonomy."""

    countries: SequenceNotStr[str]
    """Countries, as ISO 3166-1 alpha-2 codes such as `US`."""

    country_groups: SequenceNotStr[str]
    """Multi-country groups such as `worldwide` or `europe`.

    Include-only — groups can't be excluded.
    """

    custom_locations: Iterable[RegionsIncludeCustomLocation]
    """Circular areas, each a coordinate plus a radius.

    At most 200 across include and exclude.
    """

    regions: SequenceNotStr[str]
    """US states and DC, as ISO 3166-2 codes such as `US-CA`.

    US territories (`PR`, `GU`, `VI`, `AS`, `MP`) and everywhere outside the US are
    targeted through `countries`.
    """

    zips: SequenceNotStr[RegionsIncludeZip]
    """ZIP and postal codes, as bare strings or objects with a key."""


class Regions(TypedDict, total=False):
    """Locations to target and exclude."""

    exclude: RegionsExclude
    """Locations excluded from targeting. Country groups can't be excluded."""

    include: RegionsInclude
    """Locations the ad group targets."""
