# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AuthorizedUserRoles"]

AuthorizedUserRoles: TypeAlias = Literal[
    "owner", "admin", "sales_manager", "moderator", "app_manager", "support", "manager"
]
