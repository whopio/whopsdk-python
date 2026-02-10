# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountLinkCreateParams"]


class AccountLinkCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """
    The unique identifier of the company to generate the link for, starting with
    'biz\\__'. Must be a sub-merchant of the API key's company.
    """

    refresh_url: Required[str]
    """
    The URL to redirect the user to if the session expires and needs to be
    re-authenticated, such as 'https://example.com/refresh'.
    """

    return_url: Required[str]
    """
    The URL to redirect the user to when they want to return to your site, such as
    'https://example.com/return'.
    """

    use_case: Required[Literal["account_onboarding", "payouts_portal"]]
    """
    The purpose of the account link, such as hosted payouts portal or hosted KYC
    onboarding.
    """
