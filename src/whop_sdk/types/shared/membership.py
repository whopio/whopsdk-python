# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Membership", "Account", "Member"]


class Account(BaseModel):
    """The account (seller) this membership belongs to."""

    id: str
    """Account ID, prefixed `biz_`."""

    logo_url: Optional[str] = None
    """Account logo image URL. `null` when the account has not set one."""

    route: str
    """Account public route identifier — the `whop.com/{route}` storefront path."""

    title: str
    """Account display name."""


class Member(BaseModel):
    """The caller's member row on the account.

    Present only when the membership belongs to the caller; `null` on seller-side reads.
    """

    access_level: Literal["no_access", "admin", "customer"]
    """
    What the member can reach on the account: `customer` for paying members, `admin`
    for team members, `no_access` once every grant has lapsed.
    """

    last_accessed_at: Optional[str] = None
    """When the member last opened the account's content, as an ISO 8601 timestamp.

    `null` if they never have.
    """

    position: Optional[float] = None
    """The member's sort position in the buyer's own account list.

    `null` until they arrange it.
    """


class Membership(BaseModel):
    id: str
    """Membership ID, prefixed `mem_`."""

    account: Account
    """The account (seller) this membership belongs to."""

    cancel_at_period_end: bool
    """Whether the membership is set to cancel when the current billing period ends.

    Only meaningful for recurring plans.
    """

    created_at: str
    """When the membership was created, as an ISO 8601 timestamp."""

    current_period_end: Optional[str] = None
    """
    When the current billing period renews, or when a non-renewing membership
    expires, as an ISO 8601 timestamp. `null` for one-time purchases with no
    expiration.
    """

    license_key: Optional[str] = None
    """The software license key for this membership.

    Only present when the product includes a software licensing experience.
    """

    member: Optional[Member] = None
    """The caller's member row on the account.

    Present only when the membership belongs to the caller; `null` on seller-side
    reads.
    """

    metadata: object
    """
    Custom key-value pairs stored on the membership, commonly used for software
    licensing.
    """

    phone_number: Optional[str] = None
    """The buyer's phone number recorded for this membership, or `null`.

    The number collected (or verified) at checkout when the seller's phone
    collection is on; falls back to the buyer's account number when they have shared
    one with this seller.
    """

    plan_id: str
    """The plan the buyer purchased, prefixed `plan_`."""

    product_id: str
    """The product this membership grants access to, prefixed `prod_`."""

    status: Literal["trialing", "active", "past_due", "completed", "canceled", "expired", "unresolved"]
    """Billing state of the membership.

    `active`/`trialing` memberships grant access; `past_due` is the grace period
    after a failed payment; `completed` one-time purchases keep access;
    `canceled`/`expired` do not.
    """

    user_id: Optional[str] = None
    """The buyer, prefixed `user_`.

    `null` when the buyer is another business or the membership is unclaimed.
    """
