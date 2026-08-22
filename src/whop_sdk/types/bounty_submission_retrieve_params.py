# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BountySubmissionRetrieveParams"]


class BountySubmissionRetrieveParams(TypedDict, total=False):
    account_id: str
    """
    Read the submission as this account (`biz_` tag), scoping the lookup to its
    bounties rather than the caller's own work. Requires read access to the account.
    Without it the lookup covers only what the credential owns — the submissions the
    caller authored plus those on bounties they posted.
    """
