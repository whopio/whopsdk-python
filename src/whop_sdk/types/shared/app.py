# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "App",
    "Account",
    "APIKey",
    "Creator",
    "DefaultAPIKey",
    "Icon",
    "ProductionAndroidBuild",
    "ProductionIosBuild",
    "ProductionWebBuild",
    "RequestedPermission",
    "RequestedPermissionPermissionAction",
]


class Account(BaseModel):
    """The account that owns the app."""

    id: str
    """Account ID, prefixed `biz_`."""

    logo_url: Optional[str] = None
    """Account logo image URL."""

    route: str
    """Account public route identifier."""

    title: str
    """Account display name."""


class APIKey(BaseModel):
    """Legacy app API key used to authenticate requests on the app's behalf.

    `null` when no key exists or the caller lacks the `developer:manage_api_key` permission.
    """

    token: str
    """
    The key's secret token, sent as a bearer token to authenticate requests on the
    app's behalf.
    """

    created_at: str
    """When the key was created, as an ISO 8601 timestamp."""


class Creator(BaseModel):
    """The user who owns the publishing account."""

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    username: str
    """Public username."""


class DefaultAPIKey(BaseModel):
    """The app's default API key.

    `null` when the app has no default key or the caller lacks the `developer:manage_api_key` permission; `secret_key` is additionally `null` unless the caller could have created the key themselves.
    """

    id: str
    """API key ID, prefixed `apik_`."""

    name: Optional[str] = None
    """Human-readable name identifying the API key, or `null` when none was set."""

    obfuscated_secret_key: str
    """
    Masked version of the secret key, so the key can be recognized without revealing
    the full secret.
    """

    secret_key: Optional[str] = None
    """The full secret used to authenticate requests.

    `null` unless the caller could have created the key themselves.
    """


class Icon(BaseModel):
    """The app's icon. Falls back to the default app icon when none is uploaded."""

    url: str
    """Icon image URL. Always present — the default app icon when none is uploaded."""


class ProductionAndroidBuild(BaseModel):
    """
    The approved build currently served on Android, or `null` when none is deployed.
    """

    id: str
    """App build ID, prefixed `abld_`."""

    checksum: Optional[str] = None
    """Client-generated checksum of the build file, used to verify file integrity."""

    file_url: Optional[str] = None
    """URL to download the uploaded build artifact."""

    source_url: Optional[str] = None
    """
    URL to download the compressed source code archive that produced this build, or
    `null` when the build was uploaded without a source archive.
    """

    status: Literal["draft", "pending", "approved", "rejected"]
    """The build's review status."""


class ProductionIosBuild(BaseModel):
    """The approved build currently served on iOS, or `null` when none is deployed."""

    id: str
    """App build ID, prefixed `abld_`."""

    checksum: Optional[str] = None
    """Client-generated checksum of the build file, used to verify file integrity."""

    file_url: Optional[str] = None
    """URL to download the uploaded build artifact."""

    source_url: Optional[str] = None
    """
    URL to download the compressed source code archive that produced this build, or
    `null` when the build was uploaded without a source archive.
    """

    status: Literal["draft", "pending", "approved", "rejected"]
    """The build's review status."""


class ProductionWebBuild(BaseModel):
    """The approved build currently served on web, or `null` when none is deployed."""

    id: str
    """App build ID, prefixed `abld_`."""

    checksum: Optional[str] = None
    """Client-generated checksum of the build file, used to verify file integrity."""

    file_url: Optional[str] = None
    """URL to download the uploaded build artifact."""

    source_url: Optional[str] = None
    """
    URL to download the compressed source code archive that produced this build, or
    `null` when the build was uploaded without a source archive.
    """

    status: Literal["draft", "pending", "approved", "rejected"]
    """The build's review status."""


class RequestedPermissionPermissionAction(BaseModel):
    """The permission action the app requests."""

    action: str
    """The permission action's identifier, for example `company:basic:read`."""

    name: str
    """Human-readable name of the action."""


class RequestedPermission(BaseModel):
    """Permissions the app requests on install."""

    is_required: bool
    """
    Whether the app requires the permission to be granted on install, as opposed to
    requesting it optionally.
    """

    justification: Optional[str] = None
    """
    The developer's explanation of why the app needs the permission, or `null` when
    none was provided.
    """

    permission_action: RequestedPermissionPermissionAction
    """The permission action the app requests."""


class App(BaseModel):
    id: str
    """App ID, prefixed `app_`."""

    account: Account
    """The account that owns the app."""

    api_key: Optional[APIKey] = None
    """Legacy app API key used to authenticate requests on the app's behalf.

    `null` when no key exists or the caller lacks the `developer:manage_api_key`
    permission.
    """

    app_store_description: Optional[str] = None
    """
    Detailed description shown on the app store's in-depth app page, or `null` when
    none has been set.
    """

    app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"]
    """The type of end-user the app is built for."""

    base_url: Optional[str] = None
    """The production base URL where the app is hosted.

    `null` if no base URL is configured, if the caller lacks the
    `developer:basic:read` permission on the app's account, or on list responses,
    which never expose it.
    """

    creator: Creator
    """The user who owns the publishing account."""

    dashboard_path: Optional[str] = None
    """URL path for the account dashboard view, or `null` when not configured."""

    default_api_key: Optional[DefaultAPIKey] = None
    """The app's default API key.

    `null` when the app has no default key or the caller lacks the
    `developer:manage_api_key` permission; `secret_key` is additionally `null`
    unless the caller could have created the key themselves.
    """

    description: Optional[str] = None
    """
    Short description shown in listings and search results, or `null` if none has
    been set.
    """

    discover_path: Optional[str] = None
    """URL path for the discover view, or `null` when not configured."""

    domain_id: str
    """
    Subdomain identifier for the app's proxied URL, forming
    https://{domain_id}.apps.whop.com.
    """

    experience_path: Optional[str] = None
    """URL path for the member-facing hub view, or `null` when not configured."""

    hosted_url: Optional[str] = None
    """
    Full URL where the app's hosted web build is served, or `null` if no route is
    claimed.
    """

    icon: Icon
    """The app's icon. Falls back to the default app icon when none is uploaded."""

    marketplace_status: Optional[Literal["not_available", "pending_review", "live_marketplace"]] = None
    """
    Approval status of the app's product listing on the Whop app store, or `null`
    when the app has no associated product.
    """

    name: str
    """Display name shown on the app store and in experience navigation."""

    oauth_client_type: Literal["public", "confidential"]
    """How the app authenticates at the OAuth token endpoint."""

    openapi_path: Optional[str] = None
    """URL path to the app's OpenAPI spec file, or `null` when not configured."""

    origin: Optional[str] = None
    """
    Full origin URL of the app's proxied domain, for example
    https://ab1c2d3e4f.apps.whop.com.
    """

    product_id: Optional[str] = None
    """
    ID of the app's product listing on the Whop app store, or `null` when the app
    has no associated product.
    """

    production_android_build: Optional[ProductionAndroidBuild] = None
    """
    The approved build currently served on Android, or `null` when none is deployed.
    """

    production_ios_build: Optional[ProductionIosBuild] = None
    """The approved build currently served on iOS, or `null` when none is deployed."""

    production_web_build: Optional[ProductionWebBuild] = None
    """The approved build currently served on web, or `null` when none is deployed."""

    redirect_uris: List[str]

    requested_permissions: List[RequestedPermission]

    required_scopes: List[Literal["read_user"]]

    route: Optional[str] = None
    """
    Claimed subdomain route where hosted web builds are served (`myapp` for
    myapp.whop.app), or `null` if no route is claimed.
    """

    secrets: Optional[object] = None
    """
    The app's production secrets as an object of string values, injected into the
    hosted server runtime. `null` when the caller lacks the `developer:update_app`
    permission.
    """

    skills_path: Optional[str] = None
    """URL path to the app's skills directory, or `null` when not configured."""

    status: Literal["live", "unlisted", "hidden"]
    """
    Visibility on the Whop app store: `live` is publicly discoverable, `unlisted` is
    accessible only via direct link, `hidden` is not visible anywhere.
    """

    verified: bool
    """
    Whether the app has been verified by Whop and is eligible for the featured apps
    section.
    """
