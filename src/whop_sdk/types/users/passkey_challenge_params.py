# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PasskeyChallengeParams"]


class PasskeyChallengeParams(TypedDict, total=False):
    challenge_type: Required[Literal["registration", "deletion"]]
    """The ceremony this challenge is for."""

    passkey_id: str
    """The passkey the ceremony targets, prefixed `wcred_`.

    Required when `challenge_type` is `deletion`, ignored otherwise.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
