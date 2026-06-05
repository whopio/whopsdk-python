# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdRetrieveParams"]


class AdRetrieveParams(TypedDict, total=False):
    stats_from: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Inclusive start of the window for the ad's metric fields (spend, impressions,
    …).

    Omit both statsFrom and statsTo for all-time stats.
    """

    stats_to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Inclusive end of the window for the ad's metric fields.

    Omit both statsFrom and statsTo for all-time stats.
    """
