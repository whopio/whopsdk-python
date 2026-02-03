# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CancelOptions"]

CancelOptions: TypeAlias = Literal[
    "too_expensive", "switching", "missing_features", "technical_issues", "bad_experience", "other", "testing"
]
