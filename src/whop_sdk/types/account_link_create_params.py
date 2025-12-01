# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountLinkCreateParams"]


class AccountLinkCreateParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID of the Company to generate the url for.

    The company must be a sub-merchant of the API key's company.
    """

    refresh_url: Required[str]
    """
    The URL to redirect to if the session expires and needs to be re-authenticated
    due to the token expiring.
    """

    return_url: Required[str]
    """The URL to redirect to when the customer wants to return to your site."""

    use_case: Required[Literal["account_onboarding", "payouts_portal"]]
    """The use case for which the link will be used."""
