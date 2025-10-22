# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    apps,
    plans,
    users,
    forums,
    entries,
    members,
    invoices,
    messages,
    payments,
    products,
    webhooks,
    companies,
    reactions,
    shipments,
    transfers,
    app_builds,
    experiences,
    forum_posts,
    memberships,
    chat_channels,
    ledger_accounts,
    authorized_users,
    support_channels,
    checkout_configurations,
    course_lesson_interactions,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import WhopError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Whop", "AsyncWhop", "Client", "AsyncClient"]


class Whop(SyncAPIClient):
    apps: apps.AppsResource
    invoices: invoices.InvoicesResource
    course_lesson_interactions: course_lesson_interactions.CourseLessonInteractionsResource
    products: products.ProductsResource
    companies: companies.CompaniesResource
    webhooks: webhooks.WebhooksResource
    plans: plans.PlansResource
    entries: entries.EntriesResource
    forum_posts: forum_posts.ForumPostsResource
    transfers: transfers.TransfersResource
    ledger_accounts: ledger_accounts.LedgerAccountsResource
    memberships: memberships.MembershipsResource
    authorized_users: authorized_users.AuthorizedUsersResource
    app_builds: app_builds.AppBuildsResource
    shipments: shipments.ShipmentsResource
    checkout_configurations: checkout_configurations.CheckoutConfigurationsResource
    messages: messages.MessagesResource
    chat_channels: chat_channels.ChatChannelsResource
    users: users.UsersResource
    payments: payments.PaymentsResource
    support_channels: support_channels.SupportChannelsResource
    experiences: experiences.ExperiencesResource
    reactions: reactions.ReactionsResource
    members: members.MembersResource
    forums: forums.ForumsResource
    with_raw_response: WhopWithRawResponse
    with_streaming_response: WhopWithStreamedResponse

    # client options
    api_key: str
    webhook_key: str | None
    app_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Whop client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `WHOP_API_KEY`
        - `webhook_key` from `WHOP_WEBHOOK_SECRET`
        - `app_id` from `WHOP_APP_ID`
        """
        if api_key is None:
            api_key = os.environ.get("WHOP_API_KEY")
        if api_key is None:
            raise WhopError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WHOP_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("WHOP_WEBHOOK_SECRET")
        self.webhook_key = webhook_key

        if app_id is None:
            app_id = os.environ.get("WHOP_APP_ID")
        if app_id is None:
            raise WhopError(
                "The app_id client option must be set either by passing app_id to the client or by setting the WHOP_APP_ID environment variable"
            )
        self.app_id = app_id

        if base_url is None:
            base_url = os.environ.get("WHOP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.whop.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.apps = apps.AppsResource(self)
        self.invoices = invoices.InvoicesResource(self)
        self.course_lesson_interactions = course_lesson_interactions.CourseLessonInteractionsResource(self)
        self.products = products.ProductsResource(self)
        self.companies = companies.CompaniesResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.plans = plans.PlansResource(self)
        self.entries = entries.EntriesResource(self)
        self.forum_posts = forum_posts.ForumPostsResource(self)
        self.transfers = transfers.TransfersResource(self)
        self.ledger_accounts = ledger_accounts.LedgerAccountsResource(self)
        self.memberships = memberships.MembershipsResource(self)
        self.authorized_users = authorized_users.AuthorizedUsersResource(self)
        self.app_builds = app_builds.AppBuildsResource(self)
        self.shipments = shipments.ShipmentsResource(self)
        self.checkout_configurations = checkout_configurations.CheckoutConfigurationsResource(self)
        self.messages = messages.MessagesResource(self)
        self.chat_channels = chat_channels.ChatChannelsResource(self)
        self.users = users.UsersResource(self)
        self.payments = payments.PaymentsResource(self)
        self.support_channels = support_channels.SupportChannelsResource(self)
        self.experiences = experiences.ExperiencesResource(self)
        self.reactions = reactions.ReactionsResource(self)
        self.members = members.MembersResource(self)
        self.forums = forums.ForumsResource(self)
        self.with_raw_response = WhopWithRawResponse(self)
        self.with_streaming_response = WhopWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Whop-App-Id": self.app_id,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_key=webhook_key or self.webhook_key,
            app_id=app_id or self.app_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncWhop(AsyncAPIClient):
    apps: apps.AsyncAppsResource
    invoices: invoices.AsyncInvoicesResource
    course_lesson_interactions: course_lesson_interactions.AsyncCourseLessonInteractionsResource
    products: products.AsyncProductsResource
    companies: companies.AsyncCompaniesResource
    webhooks: webhooks.AsyncWebhooksResource
    plans: plans.AsyncPlansResource
    entries: entries.AsyncEntriesResource
    forum_posts: forum_posts.AsyncForumPostsResource
    transfers: transfers.AsyncTransfersResource
    ledger_accounts: ledger_accounts.AsyncLedgerAccountsResource
    memberships: memberships.AsyncMembershipsResource
    authorized_users: authorized_users.AsyncAuthorizedUsersResource
    app_builds: app_builds.AsyncAppBuildsResource
    shipments: shipments.AsyncShipmentsResource
    checkout_configurations: checkout_configurations.AsyncCheckoutConfigurationsResource
    messages: messages.AsyncMessagesResource
    chat_channels: chat_channels.AsyncChatChannelsResource
    users: users.AsyncUsersResource
    payments: payments.AsyncPaymentsResource
    support_channels: support_channels.AsyncSupportChannelsResource
    experiences: experiences.AsyncExperiencesResource
    reactions: reactions.AsyncReactionsResource
    members: members.AsyncMembersResource
    forums: forums.AsyncForumsResource
    with_raw_response: AsyncWhopWithRawResponse
    with_streaming_response: AsyncWhopWithStreamedResponse

    # client options
    api_key: str
    webhook_key: str | None
    app_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncWhop client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `WHOP_API_KEY`
        - `webhook_key` from `WHOP_WEBHOOK_SECRET`
        - `app_id` from `WHOP_APP_ID`
        """
        if api_key is None:
            api_key = os.environ.get("WHOP_API_KEY")
        if api_key is None:
            raise WhopError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WHOP_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("WHOP_WEBHOOK_SECRET")
        self.webhook_key = webhook_key

        if app_id is None:
            app_id = os.environ.get("WHOP_APP_ID")
        if app_id is None:
            raise WhopError(
                "The app_id client option must be set either by passing app_id to the client or by setting the WHOP_APP_ID environment variable"
            )
        self.app_id = app_id

        if base_url is None:
            base_url = os.environ.get("WHOP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.whop.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.apps = apps.AsyncAppsResource(self)
        self.invoices = invoices.AsyncInvoicesResource(self)
        self.course_lesson_interactions = course_lesson_interactions.AsyncCourseLessonInteractionsResource(self)
        self.products = products.AsyncProductsResource(self)
        self.companies = companies.AsyncCompaniesResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.plans = plans.AsyncPlansResource(self)
        self.entries = entries.AsyncEntriesResource(self)
        self.forum_posts = forum_posts.AsyncForumPostsResource(self)
        self.transfers = transfers.AsyncTransfersResource(self)
        self.ledger_accounts = ledger_accounts.AsyncLedgerAccountsResource(self)
        self.memberships = memberships.AsyncMembershipsResource(self)
        self.authorized_users = authorized_users.AsyncAuthorizedUsersResource(self)
        self.app_builds = app_builds.AsyncAppBuildsResource(self)
        self.shipments = shipments.AsyncShipmentsResource(self)
        self.checkout_configurations = checkout_configurations.AsyncCheckoutConfigurationsResource(self)
        self.messages = messages.AsyncMessagesResource(self)
        self.chat_channels = chat_channels.AsyncChatChannelsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.payments = payments.AsyncPaymentsResource(self)
        self.support_channels = support_channels.AsyncSupportChannelsResource(self)
        self.experiences = experiences.AsyncExperiencesResource(self)
        self.reactions = reactions.AsyncReactionsResource(self)
        self.members = members.AsyncMembersResource(self)
        self.forums = forums.AsyncForumsResource(self)
        self.with_raw_response = AsyncWhopWithRawResponse(self)
        self.with_streaming_response = AsyncWhopWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Whop-App-Id": self.app_id,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_key=webhook_key or self.webhook_key,
            app_id=app_id or self.app_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class WhopWithRawResponse:
    def __init__(self, client: Whop) -> None:
        self.apps = apps.AppsResourceWithRawResponse(client.apps)
        self.invoices = invoices.InvoicesResourceWithRawResponse(client.invoices)
        self.course_lesson_interactions = course_lesson_interactions.CourseLessonInteractionsResourceWithRawResponse(
            client.course_lesson_interactions
        )
        self.products = products.ProductsResourceWithRawResponse(client.products)
        self.companies = companies.CompaniesResourceWithRawResponse(client.companies)
        self.plans = plans.PlansResourceWithRawResponse(client.plans)
        self.entries = entries.EntriesResourceWithRawResponse(client.entries)
        self.forum_posts = forum_posts.ForumPostsResourceWithRawResponse(client.forum_posts)
        self.transfers = transfers.TransfersResourceWithRawResponse(client.transfers)
        self.ledger_accounts = ledger_accounts.LedgerAccountsResourceWithRawResponse(client.ledger_accounts)
        self.memberships = memberships.MembershipsResourceWithRawResponse(client.memberships)
        self.authorized_users = authorized_users.AuthorizedUsersResourceWithRawResponse(client.authorized_users)
        self.app_builds = app_builds.AppBuildsResourceWithRawResponse(client.app_builds)
        self.shipments = shipments.ShipmentsResourceWithRawResponse(client.shipments)
        self.checkout_configurations = checkout_configurations.CheckoutConfigurationsResourceWithRawResponse(
            client.checkout_configurations
        )
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.chat_channels = chat_channels.ChatChannelsResourceWithRawResponse(client.chat_channels)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.payments = payments.PaymentsResourceWithRawResponse(client.payments)
        self.support_channels = support_channels.SupportChannelsResourceWithRawResponse(client.support_channels)
        self.experiences = experiences.ExperiencesResourceWithRawResponse(client.experiences)
        self.reactions = reactions.ReactionsResourceWithRawResponse(client.reactions)
        self.members = members.MembersResourceWithRawResponse(client.members)
        self.forums = forums.ForumsResourceWithRawResponse(client.forums)


class AsyncWhopWithRawResponse:
    def __init__(self, client: AsyncWhop) -> None:
        self.apps = apps.AsyncAppsResourceWithRawResponse(client.apps)
        self.invoices = invoices.AsyncInvoicesResourceWithRawResponse(client.invoices)
        self.course_lesson_interactions = (
            course_lesson_interactions.AsyncCourseLessonInteractionsResourceWithRawResponse(
                client.course_lesson_interactions
            )
        )
        self.products = products.AsyncProductsResourceWithRawResponse(client.products)
        self.companies = companies.AsyncCompaniesResourceWithRawResponse(client.companies)
        self.plans = plans.AsyncPlansResourceWithRawResponse(client.plans)
        self.entries = entries.AsyncEntriesResourceWithRawResponse(client.entries)
        self.forum_posts = forum_posts.AsyncForumPostsResourceWithRawResponse(client.forum_posts)
        self.transfers = transfers.AsyncTransfersResourceWithRawResponse(client.transfers)
        self.ledger_accounts = ledger_accounts.AsyncLedgerAccountsResourceWithRawResponse(client.ledger_accounts)
        self.memberships = memberships.AsyncMembershipsResourceWithRawResponse(client.memberships)
        self.authorized_users = authorized_users.AsyncAuthorizedUsersResourceWithRawResponse(client.authorized_users)
        self.app_builds = app_builds.AsyncAppBuildsResourceWithRawResponse(client.app_builds)
        self.shipments = shipments.AsyncShipmentsResourceWithRawResponse(client.shipments)
        self.checkout_configurations = checkout_configurations.AsyncCheckoutConfigurationsResourceWithRawResponse(
            client.checkout_configurations
        )
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.chat_channels = chat_channels.AsyncChatChannelsResourceWithRawResponse(client.chat_channels)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.payments = payments.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.support_channels = support_channels.AsyncSupportChannelsResourceWithRawResponse(client.support_channels)
        self.experiences = experiences.AsyncExperiencesResourceWithRawResponse(client.experiences)
        self.reactions = reactions.AsyncReactionsResourceWithRawResponse(client.reactions)
        self.members = members.AsyncMembersResourceWithRawResponse(client.members)
        self.forums = forums.AsyncForumsResourceWithRawResponse(client.forums)


class WhopWithStreamedResponse:
    def __init__(self, client: Whop) -> None:
        self.apps = apps.AppsResourceWithStreamingResponse(client.apps)
        self.invoices = invoices.InvoicesResourceWithStreamingResponse(client.invoices)
        self.course_lesson_interactions = (
            course_lesson_interactions.CourseLessonInteractionsResourceWithStreamingResponse(
                client.course_lesson_interactions
            )
        )
        self.products = products.ProductsResourceWithStreamingResponse(client.products)
        self.companies = companies.CompaniesResourceWithStreamingResponse(client.companies)
        self.plans = plans.PlansResourceWithStreamingResponse(client.plans)
        self.entries = entries.EntriesResourceWithStreamingResponse(client.entries)
        self.forum_posts = forum_posts.ForumPostsResourceWithStreamingResponse(client.forum_posts)
        self.transfers = transfers.TransfersResourceWithStreamingResponse(client.transfers)
        self.ledger_accounts = ledger_accounts.LedgerAccountsResourceWithStreamingResponse(client.ledger_accounts)
        self.memberships = memberships.MembershipsResourceWithStreamingResponse(client.memberships)
        self.authorized_users = authorized_users.AuthorizedUsersResourceWithStreamingResponse(client.authorized_users)
        self.app_builds = app_builds.AppBuildsResourceWithStreamingResponse(client.app_builds)
        self.shipments = shipments.ShipmentsResourceWithStreamingResponse(client.shipments)
        self.checkout_configurations = checkout_configurations.CheckoutConfigurationsResourceWithStreamingResponse(
            client.checkout_configurations
        )
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.chat_channels = chat_channels.ChatChannelsResourceWithStreamingResponse(client.chat_channels)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.payments = payments.PaymentsResourceWithStreamingResponse(client.payments)
        self.support_channels = support_channels.SupportChannelsResourceWithStreamingResponse(client.support_channels)
        self.experiences = experiences.ExperiencesResourceWithStreamingResponse(client.experiences)
        self.reactions = reactions.ReactionsResourceWithStreamingResponse(client.reactions)
        self.members = members.MembersResourceWithStreamingResponse(client.members)
        self.forums = forums.ForumsResourceWithStreamingResponse(client.forums)


class AsyncWhopWithStreamedResponse:
    def __init__(self, client: AsyncWhop) -> None:
        self.apps = apps.AsyncAppsResourceWithStreamingResponse(client.apps)
        self.invoices = invoices.AsyncInvoicesResourceWithStreamingResponse(client.invoices)
        self.course_lesson_interactions = (
            course_lesson_interactions.AsyncCourseLessonInteractionsResourceWithStreamingResponse(
                client.course_lesson_interactions
            )
        )
        self.products = products.AsyncProductsResourceWithStreamingResponse(client.products)
        self.companies = companies.AsyncCompaniesResourceWithStreamingResponse(client.companies)
        self.plans = plans.AsyncPlansResourceWithStreamingResponse(client.plans)
        self.entries = entries.AsyncEntriesResourceWithStreamingResponse(client.entries)
        self.forum_posts = forum_posts.AsyncForumPostsResourceWithStreamingResponse(client.forum_posts)
        self.transfers = transfers.AsyncTransfersResourceWithStreamingResponse(client.transfers)
        self.ledger_accounts = ledger_accounts.AsyncLedgerAccountsResourceWithStreamingResponse(client.ledger_accounts)
        self.memberships = memberships.AsyncMembershipsResourceWithStreamingResponse(client.memberships)
        self.authorized_users = authorized_users.AsyncAuthorizedUsersResourceWithStreamingResponse(
            client.authorized_users
        )
        self.app_builds = app_builds.AsyncAppBuildsResourceWithStreamingResponse(client.app_builds)
        self.shipments = shipments.AsyncShipmentsResourceWithStreamingResponse(client.shipments)
        self.checkout_configurations = checkout_configurations.AsyncCheckoutConfigurationsResourceWithStreamingResponse(
            client.checkout_configurations
        )
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.chat_channels = chat_channels.AsyncChatChannelsResourceWithStreamingResponse(client.chat_channels)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.payments = payments.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.support_channels = support_channels.AsyncSupportChannelsResourceWithStreamingResponse(
            client.support_channels
        )
        self.experiences = experiences.AsyncExperiencesResourceWithStreamingResponse(client.experiences)
        self.reactions = reactions.AsyncReactionsResourceWithStreamingResponse(client.reactions)
        self.members = members.AsyncMembersResourceWithStreamingResponse(client.members)
        self.forums = forums.AsyncForumsResourceWithStreamingResponse(client.forums)


Client = Whop

AsyncClient = AsyncWhop
