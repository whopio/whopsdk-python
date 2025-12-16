# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import WhopError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        apps,
        plans,
        users,
        forums,
        courses,
        entries,
        members,
        refunds,
        reviews,
        disputes,
        invoices,
        messages,
        payments,
        products,
        companies,
        reactions,
        shipments,
        transfers,
        app_builds,
        experiences,
        fee_markups,
        forum_posts,
        memberships,
        promo_codes,
        withdrawals,
        access_tokens,
        account_links,
        chat_channels,
        notifications,
        setup_intents,
        course_lessons,
        payout_methods,
        course_chapters,
        course_students,
        ledger_accounts,
        payment_methods,
        authorized_users,
        support_channels,
        checkout_configurations,
        course_lesson_interactions,
    )
    from .resources.apps import AppsResource, AsyncAppsResource
    from .resources.plans import PlansResource, AsyncPlansResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.forums import ForumsResource, AsyncForumsResource
    from .resources.courses import CoursesResource, AsyncCoursesResource
    from .resources.entries import EntriesResource, AsyncEntriesResource
    from .resources.members import MembersResource, AsyncMembersResource
    from .resources.refunds import RefundsResource, AsyncRefundsResource
    from .resources.reviews import ReviewsResource, AsyncReviewsResource
    from .resources.disputes import DisputesResource, AsyncDisputesResource
    from .resources.invoices import InvoicesResource, AsyncInvoicesResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.products import ProductsResource, AsyncProductsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.companies import CompaniesResource, AsyncCompaniesResource
    from .resources.reactions import ReactionsResource, AsyncReactionsResource
    from .resources.shipments import ShipmentsResource, AsyncShipmentsResource
    from .resources.transfers import TransfersResource, AsyncTransfersResource
    from .resources.app_builds import AppBuildsResource, AsyncAppBuildsResource
    from .resources.experiences import ExperiencesResource, AsyncExperiencesResource
    from .resources.fee_markups import FeeMarkupsResource, AsyncFeeMarkupsResource
    from .resources.forum_posts import ForumPostsResource, AsyncForumPostsResource
    from .resources.memberships import MembershipsResource, AsyncMembershipsResource
    from .resources.promo_codes import PromoCodesResource, AsyncPromoCodesResource
    from .resources.withdrawals import WithdrawalsResource, AsyncWithdrawalsResource
    from .resources.access_tokens import AccessTokensResource, AsyncAccessTokensResource
    from .resources.account_links import AccountLinksResource, AsyncAccountLinksResource
    from .resources.chat_channels import ChatChannelsResource, AsyncChatChannelsResource
    from .resources.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.setup_intents import SetupIntentsResource, AsyncSetupIntentsResource
    from .resources.course_lessons import CourseLessonsResource, AsyncCourseLessonsResource
    from .resources.payout_methods import PayoutMethodsResource, AsyncPayoutMethodsResource
    from .resources.course_chapters import CourseChaptersResource, AsyncCourseChaptersResource
    from .resources.course_students import CourseStudentsResource, AsyncCourseStudentsResource
    from .resources.ledger_accounts import LedgerAccountsResource, AsyncLedgerAccountsResource
    from .resources.payment_methods import PaymentMethodsResource, AsyncPaymentMethodsResource
    from .resources.authorized_users import AuthorizedUsersResource, AsyncAuthorizedUsersResource
    from .resources.support_channels import SupportChannelsResource, AsyncSupportChannelsResource
    from .resources.checkout_configurations import CheckoutConfigurationsResource, AsyncCheckoutConfigurationsResource
    from .resources.course_lesson_interactions import (
        CourseLessonInteractionsResource,
        AsyncCourseLessonInteractionsResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Whop", "AsyncWhop", "Client", "AsyncClient"]


class Whop(SyncAPIClient):
    # client options
    api_key: str
    webhook_key: str | None
    app_id: str | None

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

    @cached_property
    def apps(self) -> AppsResource:
        from .resources.apps import AppsResource

        return AppsResource(self)

    @cached_property
    def invoices(self) -> InvoicesResource:
        from .resources.invoices import InvoicesResource

        return InvoicesResource(self)

    @cached_property
    def course_lesson_interactions(self) -> CourseLessonInteractionsResource:
        from .resources.course_lesson_interactions import CourseLessonInteractionsResource

        return CourseLessonInteractionsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def companies(self) -> CompaniesResource:
        from .resources.companies import CompaniesResource

        return CompaniesResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def plans(self) -> PlansResource:
        from .resources.plans import PlansResource

        return PlansResource(self)

    @cached_property
    def entries(self) -> EntriesResource:
        from .resources.entries import EntriesResource

        return EntriesResource(self)

    @cached_property
    def forum_posts(self) -> ForumPostsResource:
        from .resources.forum_posts import ForumPostsResource

        return ForumPostsResource(self)

    @cached_property
    def transfers(self) -> TransfersResource:
        from .resources.transfers import TransfersResource

        return TransfersResource(self)

    @cached_property
    def ledger_accounts(self) -> LedgerAccountsResource:
        from .resources.ledger_accounts import LedgerAccountsResource

        return LedgerAccountsResource(self)

    @cached_property
    def memberships(self) -> MembershipsResource:
        from .resources.memberships import MembershipsResource

        return MembershipsResource(self)

    @cached_property
    def authorized_users(self) -> AuthorizedUsersResource:
        from .resources.authorized_users import AuthorizedUsersResource

        return AuthorizedUsersResource(self)

    @cached_property
    def app_builds(self) -> AppBuildsResource:
        from .resources.app_builds import AppBuildsResource

        return AppBuildsResource(self)

    @cached_property
    def shipments(self) -> ShipmentsResource:
        from .resources.shipments import ShipmentsResource

        return ShipmentsResource(self)

    @cached_property
    def checkout_configurations(self) -> CheckoutConfigurationsResource:
        from .resources.checkout_configurations import CheckoutConfigurationsResource

        return CheckoutConfigurationsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def chat_channels(self) -> ChatChannelsResource:
        from .resources.chat_channels import ChatChannelsResource

        return ChatChannelsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        from .resources.payments import PaymentsResource

        return PaymentsResource(self)

    @cached_property
    def support_channels(self) -> SupportChannelsResource:
        from .resources.support_channels import SupportChannelsResource

        return SupportChannelsResource(self)

    @cached_property
    def experiences(self) -> ExperiencesResource:
        from .resources.experiences import ExperiencesResource

        return ExperiencesResource(self)

    @cached_property
    def reactions(self) -> ReactionsResource:
        from .resources.reactions import ReactionsResource

        return ReactionsResource(self)

    @cached_property
    def members(self) -> MembersResource:
        from .resources.members import MembersResource

        return MembersResource(self)

    @cached_property
    def forums(self) -> ForumsResource:
        from .resources.forums import ForumsResource

        return ForumsResource(self)

    @cached_property
    def promo_codes(self) -> PromoCodesResource:
        from .resources.promo_codes import PromoCodesResource

        return PromoCodesResource(self)

    @cached_property
    def courses(self) -> CoursesResource:
        from .resources.courses import CoursesResource

        return CoursesResource(self)

    @cached_property
    def course_chapters(self) -> CourseChaptersResource:
        from .resources.course_chapters import CourseChaptersResource

        return CourseChaptersResource(self)

    @cached_property
    def course_lessons(self) -> CourseLessonsResource:
        from .resources.course_lessons import CourseLessonsResource

        return CourseLessonsResource(self)

    @cached_property
    def reviews(self) -> ReviewsResource:
        from .resources.reviews import ReviewsResource

        return ReviewsResource(self)

    @cached_property
    def course_students(self) -> CourseStudentsResource:
        from .resources.course_students import CourseStudentsResource

        return CourseStudentsResource(self)

    @cached_property
    def access_tokens(self) -> AccessTokensResource:
        from .resources.access_tokens import AccessTokensResource

        return AccessTokensResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def disputes(self) -> DisputesResource:
        from .resources.disputes import DisputesResource

        return DisputesResource(self)

    @cached_property
    def refunds(self) -> RefundsResource:
        from .resources.refunds import RefundsResource

        return RefundsResource(self)

    @cached_property
    def withdrawals(self) -> WithdrawalsResource:
        from .resources.withdrawals import WithdrawalsResource

        return WithdrawalsResource(self)

    @cached_property
    def account_links(self) -> AccountLinksResource:
        from .resources.account_links import AccountLinksResource

        return AccountLinksResource(self)

    @cached_property
    def setup_intents(self) -> SetupIntentsResource:
        from .resources.setup_intents import SetupIntentsResource

        return SetupIntentsResource(self)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        from .resources.payment_methods import PaymentMethodsResource

        return PaymentMethodsResource(self)

    @cached_property
    def fee_markups(self) -> FeeMarkupsResource:
        from .resources.fee_markups import FeeMarkupsResource

        return FeeMarkupsResource(self)

    @cached_property
    def payout_methods(self) -> PayoutMethodsResource:
        from .resources.payout_methods import PayoutMethodsResource

        return PayoutMethodsResource(self)

    @cached_property
    def with_raw_response(self) -> WhopWithRawResponse:
        return WhopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhopWithStreamedResponse:
        return WhopWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

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
            "X-Whop-App-Id": self.app_id if self.app_id is not None else Omit(),
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
    # client options
    api_key: str
    webhook_key: str | None
    app_id: str | None

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

    @cached_property
    def apps(self) -> AsyncAppsResource:
        from .resources.apps import AsyncAppsResource

        return AsyncAppsResource(self)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        from .resources.invoices import AsyncInvoicesResource

        return AsyncInvoicesResource(self)

    @cached_property
    def course_lesson_interactions(self) -> AsyncCourseLessonInteractionsResource:
        from .resources.course_lesson_interactions import AsyncCourseLessonInteractionsResource

        return AsyncCourseLessonInteractionsResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        from .resources.companies import AsyncCompaniesResource

        return AsyncCompaniesResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        from .resources.plans import AsyncPlansResource

        return AsyncPlansResource(self)

    @cached_property
    def entries(self) -> AsyncEntriesResource:
        from .resources.entries import AsyncEntriesResource

        return AsyncEntriesResource(self)

    @cached_property
    def forum_posts(self) -> AsyncForumPostsResource:
        from .resources.forum_posts import AsyncForumPostsResource

        return AsyncForumPostsResource(self)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        from .resources.transfers import AsyncTransfersResource

        return AsyncTransfersResource(self)

    @cached_property
    def ledger_accounts(self) -> AsyncLedgerAccountsResource:
        from .resources.ledger_accounts import AsyncLedgerAccountsResource

        return AsyncLedgerAccountsResource(self)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        from .resources.memberships import AsyncMembershipsResource

        return AsyncMembershipsResource(self)

    @cached_property
    def authorized_users(self) -> AsyncAuthorizedUsersResource:
        from .resources.authorized_users import AsyncAuthorizedUsersResource

        return AsyncAuthorizedUsersResource(self)

    @cached_property
    def app_builds(self) -> AsyncAppBuildsResource:
        from .resources.app_builds import AsyncAppBuildsResource

        return AsyncAppBuildsResource(self)

    @cached_property
    def shipments(self) -> AsyncShipmentsResource:
        from .resources.shipments import AsyncShipmentsResource

        return AsyncShipmentsResource(self)

    @cached_property
    def checkout_configurations(self) -> AsyncCheckoutConfigurationsResource:
        from .resources.checkout_configurations import AsyncCheckoutConfigurationsResource

        return AsyncCheckoutConfigurationsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def chat_channels(self) -> AsyncChatChannelsResource:
        from .resources.chat_channels import AsyncChatChannelsResource

        return AsyncChatChannelsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        from .resources.payments import AsyncPaymentsResource

        return AsyncPaymentsResource(self)

    @cached_property
    def support_channels(self) -> AsyncSupportChannelsResource:
        from .resources.support_channels import AsyncSupportChannelsResource

        return AsyncSupportChannelsResource(self)

    @cached_property
    def experiences(self) -> AsyncExperiencesResource:
        from .resources.experiences import AsyncExperiencesResource

        return AsyncExperiencesResource(self)

    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        from .resources.reactions import AsyncReactionsResource

        return AsyncReactionsResource(self)

    @cached_property
    def members(self) -> AsyncMembersResource:
        from .resources.members import AsyncMembersResource

        return AsyncMembersResource(self)

    @cached_property
    def forums(self) -> AsyncForumsResource:
        from .resources.forums import AsyncForumsResource

        return AsyncForumsResource(self)

    @cached_property
    def promo_codes(self) -> AsyncPromoCodesResource:
        from .resources.promo_codes import AsyncPromoCodesResource

        return AsyncPromoCodesResource(self)

    @cached_property
    def courses(self) -> AsyncCoursesResource:
        from .resources.courses import AsyncCoursesResource

        return AsyncCoursesResource(self)

    @cached_property
    def course_chapters(self) -> AsyncCourseChaptersResource:
        from .resources.course_chapters import AsyncCourseChaptersResource

        return AsyncCourseChaptersResource(self)

    @cached_property
    def course_lessons(self) -> AsyncCourseLessonsResource:
        from .resources.course_lessons import AsyncCourseLessonsResource

        return AsyncCourseLessonsResource(self)

    @cached_property
    def reviews(self) -> AsyncReviewsResource:
        from .resources.reviews import AsyncReviewsResource

        return AsyncReviewsResource(self)

    @cached_property
    def course_students(self) -> AsyncCourseStudentsResource:
        from .resources.course_students import AsyncCourseStudentsResource

        return AsyncCourseStudentsResource(self)

    @cached_property
    def access_tokens(self) -> AsyncAccessTokensResource:
        from .resources.access_tokens import AsyncAccessTokensResource

        return AsyncAccessTokensResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def disputes(self) -> AsyncDisputesResource:
        from .resources.disputes import AsyncDisputesResource

        return AsyncDisputesResource(self)

    @cached_property
    def refunds(self) -> AsyncRefundsResource:
        from .resources.refunds import AsyncRefundsResource

        return AsyncRefundsResource(self)

    @cached_property
    def withdrawals(self) -> AsyncWithdrawalsResource:
        from .resources.withdrawals import AsyncWithdrawalsResource

        return AsyncWithdrawalsResource(self)

    @cached_property
    def account_links(self) -> AsyncAccountLinksResource:
        from .resources.account_links import AsyncAccountLinksResource

        return AsyncAccountLinksResource(self)

    @cached_property
    def setup_intents(self) -> AsyncSetupIntentsResource:
        from .resources.setup_intents import AsyncSetupIntentsResource

        return AsyncSetupIntentsResource(self)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        from .resources.payment_methods import AsyncPaymentMethodsResource

        return AsyncPaymentMethodsResource(self)

    @cached_property
    def fee_markups(self) -> AsyncFeeMarkupsResource:
        from .resources.fee_markups import AsyncFeeMarkupsResource

        return AsyncFeeMarkupsResource(self)

    @cached_property
    def payout_methods(self) -> AsyncPayoutMethodsResource:
        from .resources.payout_methods import AsyncPayoutMethodsResource

        return AsyncPayoutMethodsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncWhopWithRawResponse:
        return AsyncWhopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhopWithStreamedResponse:
        return AsyncWhopWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

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
            "X-Whop-App-Id": self.app_id if self.app_id is not None else Omit(),
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
    _client: Whop

    def __init__(self, client: Whop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AppsResourceWithRawResponse:
        from .resources.apps import AppsResourceWithRawResponse

        return AppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithRawResponse:
        from .resources.invoices import InvoicesResourceWithRawResponse

        return InvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(self) -> course_lesson_interactions.CourseLessonInteractionsResourceWithRawResponse:
        from .resources.course_lesson_interactions import CourseLessonInteractionsResourceWithRawResponse

        return CourseLessonInteractionsResourceWithRawResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithRawResponse:
        from .resources.companies import CompaniesResourceWithRawResponse

        return CompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def plans(self) -> plans.PlansResourceWithRawResponse:
        from .resources.plans import PlansResourceWithRawResponse

        return PlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.EntriesResourceWithRawResponse:
        from .resources.entries import EntriesResourceWithRawResponse

        return EntriesResourceWithRawResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.ForumPostsResourceWithRawResponse:
        from .resources.forum_posts import ForumPostsResourceWithRawResponse

        return ForumPostsResourceWithRawResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.TransfersResourceWithRawResponse:
        from .resources.transfers import TransfersResourceWithRawResponse

        return TransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsResourceWithRawResponse:
        from .resources.ledger_accounts import LedgerAccountsResourceWithRawResponse

        return LedgerAccountsResourceWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithRawResponse:
        from .resources.memberships import MembershipsResourceWithRawResponse

        return MembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AuthorizedUsersResourceWithRawResponse:
        from .resources.authorized_users import AuthorizedUsersResourceWithRawResponse

        return AuthorizedUsersResourceWithRawResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AppBuildsResourceWithRawResponse:
        from .resources.app_builds import AppBuildsResourceWithRawResponse

        return AppBuildsResourceWithRawResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.ShipmentsResourceWithRawResponse:
        from .resources.shipments import ShipmentsResourceWithRawResponse

        return ShipmentsResourceWithRawResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.CheckoutConfigurationsResourceWithRawResponse:
        from .resources.checkout_configurations import CheckoutConfigurationsResourceWithRawResponse

        return CheckoutConfigurationsResourceWithRawResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.ChatChannelsResourceWithRawResponse:
        from .resources.chat_channels import ChatChannelsResourceWithRawResponse

        return ChatChannelsResourceWithRawResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        from .resources.payments import PaymentsResourceWithRawResponse

        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.SupportChannelsResourceWithRawResponse:
        from .resources.support_channels import SupportChannelsResourceWithRawResponse

        return SupportChannelsResourceWithRawResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.ExperiencesResourceWithRawResponse:
        from .resources.experiences import ExperiencesResourceWithRawResponse

        return ExperiencesResourceWithRawResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.ReactionsResourceWithRawResponse:
        from .resources.reactions import ReactionsResourceWithRawResponse

        return ReactionsResourceWithRawResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.MembersResourceWithRawResponse:
        from .resources.members import MembersResourceWithRawResponse

        return MembersResourceWithRawResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.ForumsResourceWithRawResponse:
        from .resources.forums import ForumsResourceWithRawResponse

        return ForumsResourceWithRawResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.PromoCodesResourceWithRawResponse:
        from .resources.promo_codes import PromoCodesResourceWithRawResponse

        return PromoCodesResourceWithRawResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.CoursesResourceWithRawResponse:
        from .resources.courses import CoursesResourceWithRawResponse

        return CoursesResourceWithRawResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.CourseChaptersResourceWithRawResponse:
        from .resources.course_chapters import CourseChaptersResourceWithRawResponse

        return CourseChaptersResourceWithRawResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.CourseLessonsResourceWithRawResponse:
        from .resources.course_lessons import CourseLessonsResourceWithRawResponse

        return CourseLessonsResourceWithRawResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.ReviewsResourceWithRawResponse:
        from .resources.reviews import ReviewsResourceWithRawResponse

        return ReviewsResourceWithRawResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.CourseStudentsResourceWithRawResponse:
        from .resources.course_students import CourseStudentsResourceWithRawResponse

        return CourseStudentsResourceWithRawResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensResourceWithRawResponse:
        from .resources.access_tokens import AccessTokensResourceWithRawResponse

        return AccessTokensResourceWithRawResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithRawResponse:
        from .resources.disputes import DisputesResourceWithRawResponse

        return DisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithRawResponse:
        from .resources.refunds import RefundsResourceWithRawResponse

        return RefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.WithdrawalsResourceWithRawResponse:
        from .resources.withdrawals import WithdrawalsResourceWithRawResponse

        return WithdrawalsResourceWithRawResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AccountLinksResourceWithRawResponse:
        from .resources.account_links import AccountLinksResourceWithRawResponse

        return AccountLinksResourceWithRawResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.SetupIntentsResourceWithRawResponse:
        from .resources.setup_intents import SetupIntentsResourceWithRawResponse

        return SetupIntentsResourceWithRawResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.PaymentMethodsResourceWithRawResponse:
        from .resources.payment_methods import PaymentMethodsResourceWithRawResponse

        return PaymentMethodsResourceWithRawResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.FeeMarkupsResourceWithRawResponse:
        from .resources.fee_markups import FeeMarkupsResourceWithRawResponse

        return FeeMarkupsResourceWithRawResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.PayoutMethodsResourceWithRawResponse:
        from .resources.payout_methods import PayoutMethodsResourceWithRawResponse

        return PayoutMethodsResourceWithRawResponse(self._client.payout_methods)


class AsyncWhopWithRawResponse:
    _client: AsyncWhop

    def __init__(self, client: AsyncWhop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithRawResponse:
        from .resources.apps import AsyncAppsResourceWithRawResponse

        return AsyncAppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithRawResponse:
        from .resources.invoices import AsyncInvoicesResourceWithRawResponse

        return AsyncInvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(
        self,
    ) -> course_lesson_interactions.AsyncCourseLessonInteractionsResourceWithRawResponse:
        from .resources.course_lesson_interactions import AsyncCourseLessonInteractionsResourceWithRawResponse

        return AsyncCourseLessonInteractionsResourceWithRawResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithRawResponse:
        from .resources.companies import AsyncCompaniesResourceWithRawResponse

        return AsyncCompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithRawResponse:
        from .resources.plans import AsyncPlansResourceWithRawResponse

        return AsyncPlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.AsyncEntriesResourceWithRawResponse:
        from .resources.entries import AsyncEntriesResourceWithRawResponse

        return AsyncEntriesResourceWithRawResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.AsyncForumPostsResourceWithRawResponse:
        from .resources.forum_posts import AsyncForumPostsResourceWithRawResponse

        return AsyncForumPostsResourceWithRawResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.AsyncTransfersResourceWithRawResponse:
        from .resources.transfers import AsyncTransfersResourceWithRawResponse

        return AsyncTransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsResourceWithRawResponse:
        from .resources.ledger_accounts import AsyncLedgerAccountsResourceWithRawResponse

        return AsyncLedgerAccountsResourceWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithRawResponse:
        from .resources.memberships import AsyncMembershipsResourceWithRawResponse

        return AsyncMembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AsyncAuthorizedUsersResourceWithRawResponse:
        from .resources.authorized_users import AsyncAuthorizedUsersResourceWithRawResponse

        return AsyncAuthorizedUsersResourceWithRawResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AsyncAppBuildsResourceWithRawResponse:
        from .resources.app_builds import AsyncAppBuildsResourceWithRawResponse

        return AsyncAppBuildsResourceWithRawResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.AsyncShipmentsResourceWithRawResponse:
        from .resources.shipments import AsyncShipmentsResourceWithRawResponse

        return AsyncShipmentsResourceWithRawResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.AsyncCheckoutConfigurationsResourceWithRawResponse:
        from .resources.checkout_configurations import AsyncCheckoutConfigurationsResourceWithRawResponse

        return AsyncCheckoutConfigurationsResourceWithRawResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.AsyncChatChannelsResourceWithRawResponse:
        from .resources.chat_channels import AsyncChatChannelsResourceWithRawResponse

        return AsyncChatChannelsResourceWithRawResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        from .resources.payments import AsyncPaymentsResourceWithRawResponse

        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.AsyncSupportChannelsResourceWithRawResponse:
        from .resources.support_channels import AsyncSupportChannelsResourceWithRawResponse

        return AsyncSupportChannelsResourceWithRawResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.AsyncExperiencesResourceWithRawResponse:
        from .resources.experiences import AsyncExperiencesResourceWithRawResponse

        return AsyncExperiencesResourceWithRawResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.AsyncReactionsResourceWithRawResponse:
        from .resources.reactions import AsyncReactionsResourceWithRawResponse

        return AsyncReactionsResourceWithRawResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithRawResponse:
        from .resources.members import AsyncMembersResourceWithRawResponse

        return AsyncMembersResourceWithRawResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.AsyncForumsResourceWithRawResponse:
        from .resources.forums import AsyncForumsResourceWithRawResponse

        return AsyncForumsResourceWithRawResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.AsyncPromoCodesResourceWithRawResponse:
        from .resources.promo_codes import AsyncPromoCodesResourceWithRawResponse

        return AsyncPromoCodesResourceWithRawResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.AsyncCoursesResourceWithRawResponse:
        from .resources.courses import AsyncCoursesResourceWithRawResponse

        return AsyncCoursesResourceWithRawResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.AsyncCourseChaptersResourceWithRawResponse:
        from .resources.course_chapters import AsyncCourseChaptersResourceWithRawResponse

        return AsyncCourseChaptersResourceWithRawResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.AsyncCourseLessonsResourceWithRawResponse:
        from .resources.course_lessons import AsyncCourseLessonsResourceWithRawResponse

        return AsyncCourseLessonsResourceWithRawResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.AsyncReviewsResourceWithRawResponse:
        from .resources.reviews import AsyncReviewsResourceWithRawResponse

        return AsyncReviewsResourceWithRawResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.AsyncCourseStudentsResourceWithRawResponse:
        from .resources.course_students import AsyncCourseStudentsResourceWithRawResponse

        return AsyncCourseStudentsResourceWithRawResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensResourceWithRawResponse:
        from .resources.access_tokens import AsyncAccessTokensResourceWithRawResponse

        return AsyncAccessTokensResourceWithRawResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithRawResponse:
        from .resources.disputes import AsyncDisputesResourceWithRawResponse

        return AsyncDisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithRawResponse:
        from .resources.refunds import AsyncRefundsResourceWithRawResponse

        return AsyncRefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.AsyncWithdrawalsResourceWithRawResponse:
        from .resources.withdrawals import AsyncWithdrawalsResourceWithRawResponse

        return AsyncWithdrawalsResourceWithRawResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AsyncAccountLinksResourceWithRawResponse:
        from .resources.account_links import AsyncAccountLinksResourceWithRawResponse

        return AsyncAccountLinksResourceWithRawResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.AsyncSetupIntentsResourceWithRawResponse:
        from .resources.setup_intents import AsyncSetupIntentsResourceWithRawResponse

        return AsyncSetupIntentsResourceWithRawResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.AsyncPaymentMethodsResourceWithRawResponse:
        from .resources.payment_methods import AsyncPaymentMethodsResourceWithRawResponse

        return AsyncPaymentMethodsResourceWithRawResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.AsyncFeeMarkupsResourceWithRawResponse:
        from .resources.fee_markups import AsyncFeeMarkupsResourceWithRawResponse

        return AsyncFeeMarkupsResourceWithRawResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.AsyncPayoutMethodsResourceWithRawResponse:
        from .resources.payout_methods import AsyncPayoutMethodsResourceWithRawResponse

        return AsyncPayoutMethodsResourceWithRawResponse(self._client.payout_methods)


class WhopWithStreamedResponse:
    _client: Whop

    def __init__(self, client: Whop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AppsResourceWithStreamingResponse:
        from .resources.apps import AppsResourceWithStreamingResponse

        return AppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithStreamingResponse:
        from .resources.invoices import InvoicesResourceWithStreamingResponse

        return InvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(
        self,
    ) -> course_lesson_interactions.CourseLessonInteractionsResourceWithStreamingResponse:
        from .resources.course_lesson_interactions import CourseLessonInteractionsResourceWithStreamingResponse

        return CourseLessonInteractionsResourceWithStreamingResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithStreamingResponse:
        from .resources.companies import CompaniesResourceWithStreamingResponse

        return CompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def plans(self) -> plans.PlansResourceWithStreamingResponse:
        from .resources.plans import PlansResourceWithStreamingResponse

        return PlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.EntriesResourceWithStreamingResponse:
        from .resources.entries import EntriesResourceWithStreamingResponse

        return EntriesResourceWithStreamingResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.ForumPostsResourceWithStreamingResponse:
        from .resources.forum_posts import ForumPostsResourceWithStreamingResponse

        return ForumPostsResourceWithStreamingResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.TransfersResourceWithStreamingResponse:
        from .resources.transfers import TransfersResourceWithStreamingResponse

        return TransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsResourceWithStreamingResponse:
        from .resources.ledger_accounts import LedgerAccountsResourceWithStreamingResponse

        return LedgerAccountsResourceWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithStreamingResponse:
        from .resources.memberships import MembershipsResourceWithStreamingResponse

        return MembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AuthorizedUsersResourceWithStreamingResponse:
        from .resources.authorized_users import AuthorizedUsersResourceWithStreamingResponse

        return AuthorizedUsersResourceWithStreamingResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AppBuildsResourceWithStreamingResponse:
        from .resources.app_builds import AppBuildsResourceWithStreamingResponse

        return AppBuildsResourceWithStreamingResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.ShipmentsResourceWithStreamingResponse:
        from .resources.shipments import ShipmentsResourceWithStreamingResponse

        return ShipmentsResourceWithStreamingResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.CheckoutConfigurationsResourceWithStreamingResponse:
        from .resources.checkout_configurations import CheckoutConfigurationsResourceWithStreamingResponse

        return CheckoutConfigurationsResourceWithStreamingResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.ChatChannelsResourceWithStreamingResponse:
        from .resources.chat_channels import ChatChannelsResourceWithStreamingResponse

        return ChatChannelsResourceWithStreamingResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        from .resources.payments import PaymentsResourceWithStreamingResponse

        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.SupportChannelsResourceWithStreamingResponse:
        from .resources.support_channels import SupportChannelsResourceWithStreamingResponse

        return SupportChannelsResourceWithStreamingResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.ExperiencesResourceWithStreamingResponse:
        from .resources.experiences import ExperiencesResourceWithStreamingResponse

        return ExperiencesResourceWithStreamingResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.ReactionsResourceWithStreamingResponse:
        from .resources.reactions import ReactionsResourceWithStreamingResponse

        return ReactionsResourceWithStreamingResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.MembersResourceWithStreamingResponse:
        from .resources.members import MembersResourceWithStreamingResponse

        return MembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.ForumsResourceWithStreamingResponse:
        from .resources.forums import ForumsResourceWithStreamingResponse

        return ForumsResourceWithStreamingResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.PromoCodesResourceWithStreamingResponse:
        from .resources.promo_codes import PromoCodesResourceWithStreamingResponse

        return PromoCodesResourceWithStreamingResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.CoursesResourceWithStreamingResponse:
        from .resources.courses import CoursesResourceWithStreamingResponse

        return CoursesResourceWithStreamingResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.CourseChaptersResourceWithStreamingResponse:
        from .resources.course_chapters import CourseChaptersResourceWithStreamingResponse

        return CourseChaptersResourceWithStreamingResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.CourseLessonsResourceWithStreamingResponse:
        from .resources.course_lessons import CourseLessonsResourceWithStreamingResponse

        return CourseLessonsResourceWithStreamingResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.ReviewsResourceWithStreamingResponse:
        from .resources.reviews import ReviewsResourceWithStreamingResponse

        return ReviewsResourceWithStreamingResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.CourseStudentsResourceWithStreamingResponse:
        from .resources.course_students import CourseStudentsResourceWithStreamingResponse

        return CourseStudentsResourceWithStreamingResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensResourceWithStreamingResponse:
        from .resources.access_tokens import AccessTokensResourceWithStreamingResponse

        return AccessTokensResourceWithStreamingResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithStreamingResponse:
        from .resources.disputes import DisputesResourceWithStreamingResponse

        return DisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithStreamingResponse:
        from .resources.refunds import RefundsResourceWithStreamingResponse

        return RefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.WithdrawalsResourceWithStreamingResponse:
        from .resources.withdrawals import WithdrawalsResourceWithStreamingResponse

        return WithdrawalsResourceWithStreamingResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AccountLinksResourceWithStreamingResponse:
        from .resources.account_links import AccountLinksResourceWithStreamingResponse

        return AccountLinksResourceWithStreamingResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.SetupIntentsResourceWithStreamingResponse:
        from .resources.setup_intents import SetupIntentsResourceWithStreamingResponse

        return SetupIntentsResourceWithStreamingResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.PaymentMethodsResourceWithStreamingResponse:
        from .resources.payment_methods import PaymentMethodsResourceWithStreamingResponse

        return PaymentMethodsResourceWithStreamingResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.FeeMarkupsResourceWithStreamingResponse:
        from .resources.fee_markups import FeeMarkupsResourceWithStreamingResponse

        return FeeMarkupsResourceWithStreamingResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.PayoutMethodsResourceWithStreamingResponse:
        from .resources.payout_methods import PayoutMethodsResourceWithStreamingResponse

        return PayoutMethodsResourceWithStreamingResponse(self._client.payout_methods)


class AsyncWhopWithStreamedResponse:
    _client: AsyncWhop

    def __init__(self, client: AsyncWhop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithStreamingResponse:
        from .resources.apps import AsyncAppsResourceWithStreamingResponse

        return AsyncAppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithStreamingResponse:
        from .resources.invoices import AsyncInvoicesResourceWithStreamingResponse

        return AsyncInvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(
        self,
    ) -> course_lesson_interactions.AsyncCourseLessonInteractionsResourceWithStreamingResponse:
        from .resources.course_lesson_interactions import AsyncCourseLessonInteractionsResourceWithStreamingResponse

        return AsyncCourseLessonInteractionsResourceWithStreamingResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithStreamingResponse:
        from .resources.companies import AsyncCompaniesResourceWithStreamingResponse

        return AsyncCompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithStreamingResponse:
        from .resources.plans import AsyncPlansResourceWithStreamingResponse

        return AsyncPlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.AsyncEntriesResourceWithStreamingResponse:
        from .resources.entries import AsyncEntriesResourceWithStreamingResponse

        return AsyncEntriesResourceWithStreamingResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.AsyncForumPostsResourceWithStreamingResponse:
        from .resources.forum_posts import AsyncForumPostsResourceWithStreamingResponse

        return AsyncForumPostsResourceWithStreamingResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.AsyncTransfersResourceWithStreamingResponse:
        from .resources.transfers import AsyncTransfersResourceWithStreamingResponse

        return AsyncTransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsResourceWithStreamingResponse:
        from .resources.ledger_accounts import AsyncLedgerAccountsResourceWithStreamingResponse

        return AsyncLedgerAccountsResourceWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithStreamingResponse:
        from .resources.memberships import AsyncMembershipsResourceWithStreamingResponse

        return AsyncMembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AsyncAuthorizedUsersResourceWithStreamingResponse:
        from .resources.authorized_users import AsyncAuthorizedUsersResourceWithStreamingResponse

        return AsyncAuthorizedUsersResourceWithStreamingResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AsyncAppBuildsResourceWithStreamingResponse:
        from .resources.app_builds import AsyncAppBuildsResourceWithStreamingResponse

        return AsyncAppBuildsResourceWithStreamingResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.AsyncShipmentsResourceWithStreamingResponse:
        from .resources.shipments import AsyncShipmentsResourceWithStreamingResponse

        return AsyncShipmentsResourceWithStreamingResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(
        self,
    ) -> checkout_configurations.AsyncCheckoutConfigurationsResourceWithStreamingResponse:
        from .resources.checkout_configurations import AsyncCheckoutConfigurationsResourceWithStreamingResponse

        return AsyncCheckoutConfigurationsResourceWithStreamingResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.AsyncChatChannelsResourceWithStreamingResponse:
        from .resources.chat_channels import AsyncChatChannelsResourceWithStreamingResponse

        return AsyncChatChannelsResourceWithStreamingResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        from .resources.payments import AsyncPaymentsResourceWithStreamingResponse

        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.AsyncSupportChannelsResourceWithStreamingResponse:
        from .resources.support_channels import AsyncSupportChannelsResourceWithStreamingResponse

        return AsyncSupportChannelsResourceWithStreamingResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.AsyncExperiencesResourceWithStreamingResponse:
        from .resources.experiences import AsyncExperiencesResourceWithStreamingResponse

        return AsyncExperiencesResourceWithStreamingResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.AsyncReactionsResourceWithStreamingResponse:
        from .resources.reactions import AsyncReactionsResourceWithStreamingResponse

        return AsyncReactionsResourceWithStreamingResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithStreamingResponse:
        from .resources.members import AsyncMembersResourceWithStreamingResponse

        return AsyncMembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.AsyncForumsResourceWithStreamingResponse:
        from .resources.forums import AsyncForumsResourceWithStreamingResponse

        return AsyncForumsResourceWithStreamingResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.AsyncPromoCodesResourceWithStreamingResponse:
        from .resources.promo_codes import AsyncPromoCodesResourceWithStreamingResponse

        return AsyncPromoCodesResourceWithStreamingResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.AsyncCoursesResourceWithStreamingResponse:
        from .resources.courses import AsyncCoursesResourceWithStreamingResponse

        return AsyncCoursesResourceWithStreamingResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.AsyncCourseChaptersResourceWithStreamingResponse:
        from .resources.course_chapters import AsyncCourseChaptersResourceWithStreamingResponse

        return AsyncCourseChaptersResourceWithStreamingResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.AsyncCourseLessonsResourceWithStreamingResponse:
        from .resources.course_lessons import AsyncCourseLessonsResourceWithStreamingResponse

        return AsyncCourseLessonsResourceWithStreamingResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.AsyncReviewsResourceWithStreamingResponse:
        from .resources.reviews import AsyncReviewsResourceWithStreamingResponse

        return AsyncReviewsResourceWithStreamingResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.AsyncCourseStudentsResourceWithStreamingResponse:
        from .resources.course_students import AsyncCourseStudentsResourceWithStreamingResponse

        return AsyncCourseStudentsResourceWithStreamingResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensResourceWithStreamingResponse:
        from .resources.access_tokens import AsyncAccessTokensResourceWithStreamingResponse

        return AsyncAccessTokensResourceWithStreamingResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithStreamingResponse:
        from .resources.disputes import AsyncDisputesResourceWithStreamingResponse

        return AsyncDisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithStreamingResponse:
        from .resources.refunds import AsyncRefundsResourceWithStreamingResponse

        return AsyncRefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.AsyncWithdrawalsResourceWithStreamingResponse:
        from .resources.withdrawals import AsyncWithdrawalsResourceWithStreamingResponse

        return AsyncWithdrawalsResourceWithStreamingResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AsyncAccountLinksResourceWithStreamingResponse:
        from .resources.account_links import AsyncAccountLinksResourceWithStreamingResponse

        return AsyncAccountLinksResourceWithStreamingResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.AsyncSetupIntentsResourceWithStreamingResponse:
        from .resources.setup_intents import AsyncSetupIntentsResourceWithStreamingResponse

        return AsyncSetupIntentsResourceWithStreamingResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.AsyncPaymentMethodsResourceWithStreamingResponse:
        from .resources.payment_methods import AsyncPaymentMethodsResourceWithStreamingResponse

        return AsyncPaymentMethodsResourceWithStreamingResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.AsyncFeeMarkupsResourceWithStreamingResponse:
        from .resources.fee_markups import AsyncFeeMarkupsResourceWithStreamingResponse

        return AsyncFeeMarkupsResourceWithStreamingResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.AsyncPayoutMethodsResourceWithStreamingResponse:
        from .resources.payout_methods import AsyncPayoutMethodsResourceWithStreamingResponse

        return AsyncPayoutMethodsResourceWithStreamingResponse(self._client.payout_methods)


Client = Whop

AsyncClient = AsyncWhop
