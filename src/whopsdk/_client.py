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
    entries,
    invoices,
    products,
    webhooks,
    companies,
    transfers,
    app_builds,
    forum_posts,
    memberships,
    ledger_accounts,
    authorized_users,
    course_lesson_interactions,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import WhopsdkError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Whopsdk", "AsyncWhopsdk", "Client", "AsyncClient"]


class Whopsdk(SyncAPIClient):
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
    with_raw_response: WhopsdkWithRawResponse
    with_streaming_response: WhopsdkWithStreamedResponse

    # client options
    api_key: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
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
        """Construct a new synchronous Whopsdk client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `WHOP_API_KEY`
        - `webhook_key` from `WHOP_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("WHOP_API_KEY")
        if api_key is None:
            raise WhopsdkError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WHOP_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("WHOP_WEBHOOK_SECRET")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("WHOPSDK_BASE_URL")
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
        self.with_raw_response = WhopsdkWithRawResponse(self)
        self.with_streaming_response = WhopsdkWithStreamedResponse(self)

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
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
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


class AsyncWhopsdk(AsyncAPIClient):
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
    with_raw_response: AsyncWhopsdkWithRawResponse
    with_streaming_response: AsyncWhopsdkWithStreamedResponse

    # client options
    api_key: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
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
        """Construct a new async AsyncWhopsdk client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `WHOP_API_KEY`
        - `webhook_key` from `WHOP_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("WHOP_API_KEY")
        if api_key is None:
            raise WhopsdkError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WHOP_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("WHOP_WEBHOOK_SECRET")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("WHOPSDK_BASE_URL")
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
        self.with_raw_response = AsyncWhopsdkWithRawResponse(self)
        self.with_streaming_response = AsyncWhopsdkWithStreamedResponse(self)

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
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
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


class WhopsdkWithRawResponse:
    def __init__(self, client: Whopsdk) -> None:
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


class AsyncWhopsdkWithRawResponse:
    def __init__(self, client: AsyncWhopsdk) -> None:
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


class WhopsdkWithStreamedResponse:
    def __init__(self, client: Whopsdk) -> None:
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


class AsyncWhopsdkWithStreamedResponse:
    def __init__(self, client: AsyncWhopsdk) -> None:
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


Client = Whopsdk

AsyncClient = AsyncWhopsdk
