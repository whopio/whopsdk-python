# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AppDeployParams"]


class AppDeployParams(TypedDict, total=False):
    draft: bool
    """Upload the build without making it live.

    Defaults to `false`, which deploys and promotes in one step.
    """
