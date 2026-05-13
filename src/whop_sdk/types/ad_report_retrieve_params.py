# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .granularities import Granularities

__all__ = ["AdReportRetrieveParams"]


class AdReportRetrieveParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Inclusive start of the reporting window."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive end of the reporting window."""

    ad_campaign_id: Optional[str]
    """The unique identifier of an ad campaign.

    Mutually exclusive with `adGroupId` and `adId`.
    """

    ad_group_id: Optional[str]
    """The unique identifier of an ad group.

    Mutually exclusive with `adCampaignId` and `adId`.
    """

    ad_id: Optional[str]
    """The unique identifier of an ad.

    Mutually exclusive with `adCampaignId` and `adGroupId`.
    """

    breakdown: Optional[Granularities]
    """Bucket size for external ad stat rows."""

    currency: Optional[str]
    """ISO 4217 currency code to report `spend` in.

    Defaults to the company's ads reporting currency.
    """
