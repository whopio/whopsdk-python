# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutCreateParams"]


class PayoutCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to pay out in the specified currency."""

    payout_method_id: Required[str]
    """The saved payout method to deliver to (a potk\\__ identifier)."""

    account_id: str
    """Account to pay out from, prefixed `biz_`.

    Provide exactly one of `account_id` or `user_id`.
    """

    acknowledge_bank_warning: bool
    """
    Set to `true` to continue when the destination bank could not confirm the payout
    method account holder's name, or `false` to have the payout refused in that case
    so the account holder can correct the name or link their bank first. Omitting
    the field skips the warning gate — a client that cannot show the warning keeps
    its pre-gate behavior.
    """

    currency: str
    """The currency to pay out.

    Balances are held per currency and the payout draws only from the balance in
    this currency, so match the currency the funds arrived in — for example `cad`
    for an account funded by CAD transfers. Defaults to `usd`.
    """

    api_idempotency_key: Annotated[Optional[str], PropertyInfo(alias="idempotency_key")]
    """A unique key that makes retries safe, at most 255 bytes.

    It claims one durable slot for this account before anything runs, so concurrent
    duplicates can never pay twice: retrying with the same key and body returns the
    original response, a retry while the first request is still running gets a 409,
    and reusing the key with a different body gets a 400. The claim is account-wide:
    reusing the key through a different API key or session of the same account gets
    a 409 — retry through the credential that created the payout. Prefer sending it
    as the `Idempotency-Key` header — the header is the canonical form and this
    field defers to it; if both are sent they must match.
    """

    metadata: Dict[str, str]
    """
    Key-value data to attach to the payout, echoed on every read and in webhook
    payloads. At most 50 keys, key names up to 40 characters, string values up to
    500 characters. Never store secrets or regulated personal data here — webhook
    bodies are retained for delivery inspection.
    """

    notes: Optional[str]
    """Free-form notes to attach to the payout, with a maximum of 255 characters.

    Omit or pass `null` for no notes.
    """

    platform_covers_fees: bool
    """
    Whether the parent platform covers the payout fee instead of the account being
    paid out. Omit to use the platform's configured fee coverage policy; pass
    `false` to opt out of it. `true` is only accepted for accounts that belong to a
    platform, and requires the platform's policy to cover this payout method's
    category or a caller authorized to manage the platform's child account fees.
    """

    speed: Literal["standard", "instant"]
    """How fast the funds should arrive.

    `instant` is only accepted when the account and payout method are eligible;
    otherwise the payout is rejected.
    """

    user_id: str
    """User to pay out from, prefixed `user_`.

    Provide exactly one of `account_id` or `user_id`.
    """
