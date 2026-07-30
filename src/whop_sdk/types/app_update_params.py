# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AppUpdateParams", "Icon"]


class AppUpdateParams(TypedDict, total=False):
    app_store_description: str
    """The detailed description shown on the app store's in-depth app view page."""

    app_type: Literal["b2b_app", "b2c_app", "company_app", "component"]
    """The type of end-user the app is built for."""

    base_url: str
    """The base production URL where the app is hosted."""

    dashboard_path: Optional[str]
    """The URL path for the account dashboard view."""

    description: str
    """A short description of the app shown in listings and search results."""

    discover_path: Optional[str]
    """The URL path for the discover view."""

    experience_path: Optional[str]
    """
    The URL path for the member-facing hub view, such as
    `/experiences/[experienceId]`.
    """

    icon: Icon
    """
    The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded
    file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new
    direct upload.
    """

    name: str
    """
    The display name for the app, shown to users on the app store and product pages.
    """

    oauth_client_type: Literal["public", "confidential"]
    """How the app authenticates at the OAuth token endpoint."""

    openapi_path: Optional[str]
    """The URL path to the app's OpenAPI spec file (requires the ai_chat capability)."""

    production_android_build_id: Optional[str]
    """
    The app build (`abld_` tag) to serve as the Android production build, or `null`
    to unassign it. Same rules as `production_web_build_id`.
    """

    production_ios_build_id: Optional[str]
    """
    The app build (`abld_` tag) to serve as the iOS production build, or `null` to
    unassign it. Same rules as `production_web_build_id`.
    """

    production_web_build_id: Optional[str]
    """
    The app build (`abld_` tag) to serve as the web production build, or `null` to
    unassign it. The build must belong to this app, target web, and be in the draft
    or approved status; a draft build is queued for approval and takes over once
    approved. Requires the `developer:manage_builds` scope.
    """

    redirect_uris: SequenceNotStr[str]
    """
    The whitelisted OAuth callback URLs users are redirected to after authorizing
    the app.
    """

    required_scopes: SequenceNotStr[str]
    """The OAuth scopes the app requests from users when they install it."""

    route: str
    """The subdomain route where the app's hosted web builds are served."""

    secrets: object
    """Secrets to add or overwrite on the app, as an object of string values.

    Keys not included are left untouched; pass null or an empty string as the value
    to delete a secret. Encrypted at rest and injected into the app's hosted server
    runtime.
    """

    skills_path: Optional[str]
    """The URL path to the app's skills directory (requires the ai_chat capability)."""

    status: Literal["live", "unlisted", "hidden"]
    """Controls the app's visibility.

    `live` publishes on Whop discovery (requires name, icon, and description);
    `unlisted` hides it from discovery while keeping direct-link access.
    """


class Icon(TypedDict, total=False):
    """
    The icon image for the app in PNG, JPEG, or GIF format, referencing an uploaded file: `{ id }` for an existing attachment or `{ direct_upload_id }` for a new direct upload.
    """

    id: str
    """The tag of an already-uploaded attachment."""

    direct_upload_id: str
    """The signed id of a completed direct upload."""
