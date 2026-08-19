# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .granularities import Granularities

__all__ = ["AdReportRetrieveParams"]


class AdReportRetrieveParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Inclusive start of the reporting window."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive end of the reporting window."""

    ad_campaign_ids: SequenceNotStr[str]
    """Scope the report to these ad campaigns (max 100); stats are summed across them.

    Mutually exclusive with `companyId`, `adGroupIds`, and `adIds`.
    """

    ad_group_ids: SequenceNotStr[str]
    """Scope the report to these ad groups (max 100); stats are summed across them.

    Mutually exclusive with `companyId`, `adCampaignIds`, and `adIds`.
    """

    ad_ids: SequenceNotStr[str]
    """Scope the report to these ads (max 100); stats are summed across them.

    Mutually exclusive with `companyId`, `adCampaignIds`, and `adGroupIds`.
    """

    breakdown: Literal["campaign", "ad_group", "ad"]
    """Entity level to break down the report by.

    When set, `breakdown` on the response contains one row per entity at the
    requested level inside the requested scope. `ad` returns one row per ad,
    `ad_group` per ad group, `campaign` per ad campaign. The breakdown level must be
    at or below the scope (e.g. `adId` cannot be broken down by `campaign`). The
    `summary` totals are unaffected.
    """

    company_id: str
    """The unique identifier of a company.

    Mutually exclusive with `adCampaignIds`, `adGroupIds`, and `adIds`. Use with
    `breakdown` to fan out across every campaign, ad group, or ad in the company
    without paging.
    """

    currency: str
    """ISO 4217 currency code to report `spend` in.

    Defaults to the company's ads reporting currency.
    """

    granularity: Granularities
    """Bucket grain for the per-bucket `granularity` time series.

    Omit (`null`) for summary-only. `hourly`/`daily` max 90 days, `weekly` max 366
    days, `monthly` max 4 years. The `summary` totals are unaffected. With
    `breakdown`, each row gets its own series at the same grain.
    """
