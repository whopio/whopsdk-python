# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PreferenceUpdateResponse", "AdsPaymentMethods", "AdsPaymentMethodsBackup", "AdsPaymentMethodsPrimary"]


class AdsPaymentMethodsBackup(BaseModel):
    id: str
    """
    The funding source ID: a Whop balance (`ldgr_`) for `platform_balance`, or a
    payment method (`payt_`) for `card`.
    """

    type: Literal["platform_balance", "card"]
    """The funding source kind: a Whop balance or a saved card."""


class AdsPaymentMethodsPrimary(BaseModel):
    id: str
    """
    The funding source ID: a Whop balance (`ldgr_`) for `platform_balance`, or a
    payment method (`payt_`) for `card`.
    """

    type: Literal["platform_balance", "card"]
    """The funding source kind: a Whop balance or a saved card."""


class AdsPaymentMethods(BaseModel):
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails. `null` until ads billing has been configured.
    """

    backup: Optional[AdsPaymentMethodsBackup] = None

    primary: Optional[AdsPaymentMethodsPrimary] = None


class PreferenceUpdateResponse(BaseModel):
    ads_payment_methods: Optional[AdsPaymentMethods] = None
    """How the account pays for Whop Ads spend.

    `primary` is charged first; `backup` covers the charge when the primary fails.
    `null` until ads billing has been configured.
    """
