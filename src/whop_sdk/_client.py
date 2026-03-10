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
        files,
        leads,
        plans,
        users,
        forums,
        topups,
        courses,
        entries,
        members,
        refunds,
        reviews,
        ai_chats,
        disputes,
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
        dm_members,
        dm_channels,
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
        verifications,
        course_lessons,
        dispute_alerts,
        payout_methods,
        course_chapters,
        course_students,
        ledger_accounts,
        payment_methods,
        authorized_users,
        support_channels,
        checkout_configurations,
        company_token_transactions,
        course_lesson_interactions,
    )
    from .resources.apps import AppsResource, AsyncAppsResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.leads import LeadsResource, AsyncLeadsResource
    from .resources.plans import PlansResource, AsyncPlansResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.forums import ForumsResource, AsyncForumsResource
    from .resources.topups import TopupsResource, AsyncTopupsResource
    from .resources.courses import CoursesResource, AsyncCoursesResource
    from .resources.entries import EntriesResource, AsyncEntriesResource
    from .resources.members import MembersResource, AsyncMembersResource
    from .resources.refunds import RefundsResource, AsyncRefundsResource
    from .resources.reviews import ReviewsResource, AsyncReviewsResource
    from .resources.ai_chats import AIChatsResource, AsyncAIChatsResource
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
    from .resources.dm_members import DmMembersResource, AsyncDmMembersResource
    from .resources.dm_channels import DmChannelsResource, AsyncDmChannelsResource
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
    from .resources.verifications import VerificationsResource, AsyncVerificationsResource
    from .resources.course_lessons import CourseLessonsResource, AsyncCourseLessonsResource
    from .resources.dispute_alerts import DisputeAlertsResource, AsyncDisputeAlertsResource
    from .resources.payout_methods import PayoutMethodsResource, AsyncPayoutMethodsResource
    from .resources.course_chapters import CourseChaptersResource, AsyncCourseChaptersResource
    from .resources.course_students import CourseStudentsResource, AsyncCourseStudentsResource
    from .resources.ledger_accounts import LedgerAccountsResource, AsyncLedgerAccountsResource
    from .resources.payment_methods import PaymentMethodsResource, AsyncPaymentMethodsResource
    from .resources.authorized_users import AuthorizedUsersResource, AsyncAuthorizedUsersResource
    from .resources.support_channels import SupportChannelsResource, AsyncSupportChannelsResource
    from .resources.checkout_configurations import CheckoutConfigurationsResource, AsyncCheckoutConfigurationsResource
    from .resources.company_token_transactions import (
        CompanyTokenTransactionsResource,
        AsyncCompanyTokenTransactionsResource,
    )
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
        """Apps"""
        from .resources.apps import AppsResource

        return AppsResource(self)

    @cached_property
    def invoices(self) -> InvoicesResource:
        """Invoices"""
        from .resources.invoices import InvoicesResource

        return InvoicesResource(self)

    @cached_property
    def course_lesson_interactions(self) -> CourseLessonInteractionsResource:
        """Course lesson interactions"""
        from .resources.course_lesson_interactions import CourseLessonInteractionsResource

        return CourseLessonInteractionsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        """Products"""
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def companies(self) -> CompaniesResource:
        """Companies"""
        from .resources.companies import CompaniesResource

        return CompaniesResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhooks"""
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def plans(self) -> PlansResource:
        """Plans"""
        from .resources.plans import PlansResource

        return PlansResource(self)

    @cached_property
    def entries(self) -> EntriesResource:
        """Entries"""
        from .resources.entries import EntriesResource

        return EntriesResource(self)

    @cached_property
    def forum_posts(self) -> ForumPostsResource:
        """Forum posts"""
        from .resources.forum_posts import ForumPostsResource

        return ForumPostsResource(self)

    @cached_property
    def transfers(self) -> TransfersResource:
        """Transfers"""
        from .resources.transfers import TransfersResource

        return TransfersResource(self)

    @cached_property
    def ledger_accounts(self) -> LedgerAccountsResource:
        """Ledger accounts"""
        from .resources.ledger_accounts import LedgerAccountsResource

        return LedgerAccountsResource(self)

    @cached_property
    def memberships(self) -> MembershipsResource:
        """Memberships"""
        from .resources.memberships import MembershipsResource

        return MembershipsResource(self)

    @cached_property
    def authorized_users(self) -> AuthorizedUsersResource:
        """Authorized users"""
        from .resources.authorized_users import AuthorizedUsersResource

        return AuthorizedUsersResource(self)

    @cached_property
    def app_builds(self) -> AppBuildsResource:
        """App builds"""
        from .resources.app_builds import AppBuildsResource

        return AppBuildsResource(self)

    @cached_property
    def shipments(self) -> ShipmentsResource:
        """Shipments"""
        from .resources.shipments import ShipmentsResource

        return ShipmentsResource(self)

    @cached_property
    def checkout_configurations(self) -> CheckoutConfigurationsResource:
        """Checkout configurations"""
        from .resources.checkout_configurations import CheckoutConfigurationsResource

        return CheckoutConfigurationsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """Messages"""
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def chat_channels(self) -> ChatChannelsResource:
        """Chat channels"""
        from .resources.chat_channels import ChatChannelsResource

        return ChatChannelsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """Users"""
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        """Payments"""
        from .resources.payments import PaymentsResource

        return PaymentsResource(self)

    @cached_property
    def support_channels(self) -> SupportChannelsResource:
        """Support channels"""
        from .resources.support_channels import SupportChannelsResource

        return SupportChannelsResource(self)

    @cached_property
    def experiences(self) -> ExperiencesResource:
        """Experiences"""
        from .resources.experiences import ExperiencesResource

        return ExperiencesResource(self)

    @cached_property
    def reactions(self) -> ReactionsResource:
        """Reactions"""
        from .resources.reactions import ReactionsResource

        return ReactionsResource(self)

    @cached_property
    def members(self) -> MembersResource:
        """Members"""
        from .resources.members import MembersResource

        return MembersResource(self)

    @cached_property
    def forums(self) -> ForumsResource:
        """Forums"""
        from .resources.forums import ForumsResource

        return ForumsResource(self)

    @cached_property
    def promo_codes(self) -> PromoCodesResource:
        """Promo codes"""
        from .resources.promo_codes import PromoCodesResource

        return PromoCodesResource(self)

    @cached_property
    def courses(self) -> CoursesResource:
        """Courses"""
        from .resources.courses import CoursesResource

        return CoursesResource(self)

    @cached_property
    def course_chapters(self) -> CourseChaptersResource:
        """Course chapters"""
        from .resources.course_chapters import CourseChaptersResource

        return CourseChaptersResource(self)

    @cached_property
    def course_lessons(self) -> CourseLessonsResource:
        """Course lessons"""
        from .resources.course_lessons import CourseLessonsResource

        return CourseLessonsResource(self)

    @cached_property
    def reviews(self) -> ReviewsResource:
        """Reviews"""
        from .resources.reviews import ReviewsResource

        return ReviewsResource(self)

    @cached_property
    def course_students(self) -> CourseStudentsResource:
        """Course students"""
        from .resources.course_students import CourseStudentsResource

        return CourseStudentsResource(self)

    @cached_property
    def access_tokens(self) -> AccessTokensResource:
        """Access tokens"""
        from .resources.access_tokens import AccessTokensResource

        return AccessTokensResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        """Notifications"""
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def disputes(self) -> DisputesResource:
        """Disputes"""
        from .resources.disputes import DisputesResource

        return DisputesResource(self)

    @cached_property
    def refunds(self) -> RefundsResource:
        """Refunds"""
        from .resources.refunds import RefundsResource

        return RefundsResource(self)

    @cached_property
    def withdrawals(self) -> WithdrawalsResource:
        """Withdrawals"""
        from .resources.withdrawals import WithdrawalsResource

        return WithdrawalsResource(self)

    @cached_property
    def account_links(self) -> AccountLinksResource:
        """Account links"""
        from .resources.account_links import AccountLinksResource

        return AccountLinksResource(self)

    @cached_property
    def setup_intents(self) -> SetupIntentsResource:
        """Setup intents"""
        from .resources.setup_intents import SetupIntentsResource

        return SetupIntentsResource(self)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        """Payment methods"""
        from .resources.payment_methods import PaymentMethodsResource

        return PaymentMethodsResource(self)

    @cached_property
    def fee_markups(self) -> FeeMarkupsResource:
        """Fee markups"""
        from .resources.fee_markups import FeeMarkupsResource

        return FeeMarkupsResource(self)

    @cached_property
    def payout_methods(self) -> PayoutMethodsResource:
        """Payout methods"""
        from .resources.payout_methods import PayoutMethodsResource

        return PayoutMethodsResource(self)

    @cached_property
    def verifications(self) -> VerificationsResource:
        """Verifications"""
        from .resources.verifications import VerificationsResource

        return VerificationsResource(self)

    @cached_property
    def leads(self) -> LeadsResource:
        """Leads"""
        from .resources.leads import LeadsResource

        return LeadsResource(self)

    @cached_property
    def topups(self) -> TopupsResource:
        """Topups"""
        from .resources.topups import TopupsResource

        return TopupsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        """Files"""
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def company_token_transactions(self) -> CompanyTokenTransactionsResource:
        """Company token transactions"""
        from .resources.company_token_transactions import CompanyTokenTransactionsResource

        return CompanyTokenTransactionsResource(self)

    @cached_property
    def dm_members(self) -> DmMembersResource:
        """Dm members"""
        from .resources.dm_members import DmMembersResource

        return DmMembersResource(self)

    @cached_property
    def ai_chats(self) -> AIChatsResource:
        """Ai chats"""
        from .resources.ai_chats import AIChatsResource

        return AIChatsResource(self)

    @cached_property
    def dm_channels(self) -> DmChannelsResource:
        """Dm channels"""
        from .resources.dm_channels import DmChannelsResource

        return DmChannelsResource(self)

    @cached_property
    def dispute_alerts(self) -> DisputeAlertsResource:
        """Dispute alerts"""
        from .resources.dispute_alerts import DisputeAlertsResource

        return DisputeAlertsResource(self)

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
        """Apps"""
        from .resources.apps import AsyncAppsResource

        return AsyncAppsResource(self)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        """Invoices"""
        from .resources.invoices import AsyncInvoicesResource

        return AsyncInvoicesResource(self)

    @cached_property
    def course_lesson_interactions(self) -> AsyncCourseLessonInteractionsResource:
        """Course lesson interactions"""
        from .resources.course_lesson_interactions import AsyncCourseLessonInteractionsResource

        return AsyncCourseLessonInteractionsResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        """Products"""
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        """Companies"""
        from .resources.companies import AsyncCompaniesResource

        return AsyncCompaniesResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhooks"""
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        """Plans"""
        from .resources.plans import AsyncPlansResource

        return AsyncPlansResource(self)

    @cached_property
    def entries(self) -> AsyncEntriesResource:
        """Entries"""
        from .resources.entries import AsyncEntriesResource

        return AsyncEntriesResource(self)

    @cached_property
    def forum_posts(self) -> AsyncForumPostsResource:
        """Forum posts"""
        from .resources.forum_posts import AsyncForumPostsResource

        return AsyncForumPostsResource(self)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        """Transfers"""
        from .resources.transfers import AsyncTransfersResource

        return AsyncTransfersResource(self)

    @cached_property
    def ledger_accounts(self) -> AsyncLedgerAccountsResource:
        """Ledger accounts"""
        from .resources.ledger_accounts import AsyncLedgerAccountsResource

        return AsyncLedgerAccountsResource(self)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        """Memberships"""
        from .resources.memberships import AsyncMembershipsResource

        return AsyncMembershipsResource(self)

    @cached_property
    def authorized_users(self) -> AsyncAuthorizedUsersResource:
        """Authorized users"""
        from .resources.authorized_users import AsyncAuthorizedUsersResource

        return AsyncAuthorizedUsersResource(self)

    @cached_property
    def app_builds(self) -> AsyncAppBuildsResource:
        """App builds"""
        from .resources.app_builds import AsyncAppBuildsResource

        return AsyncAppBuildsResource(self)

    @cached_property
    def shipments(self) -> AsyncShipmentsResource:
        """Shipments"""
        from .resources.shipments import AsyncShipmentsResource

        return AsyncShipmentsResource(self)

    @cached_property
    def checkout_configurations(self) -> AsyncCheckoutConfigurationsResource:
        """Checkout configurations"""
        from .resources.checkout_configurations import AsyncCheckoutConfigurationsResource

        return AsyncCheckoutConfigurationsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Messages"""
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def chat_channels(self) -> AsyncChatChannelsResource:
        """Chat channels"""
        from .resources.chat_channels import AsyncChatChannelsResource

        return AsyncChatChannelsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Users"""
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        """Payments"""
        from .resources.payments import AsyncPaymentsResource

        return AsyncPaymentsResource(self)

    @cached_property
    def support_channels(self) -> AsyncSupportChannelsResource:
        """Support channels"""
        from .resources.support_channels import AsyncSupportChannelsResource

        return AsyncSupportChannelsResource(self)

    @cached_property
    def experiences(self) -> AsyncExperiencesResource:
        """Experiences"""
        from .resources.experiences import AsyncExperiencesResource

        return AsyncExperiencesResource(self)

    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        """Reactions"""
        from .resources.reactions import AsyncReactionsResource

        return AsyncReactionsResource(self)

    @cached_property
    def members(self) -> AsyncMembersResource:
        """Members"""
        from .resources.members import AsyncMembersResource

        return AsyncMembersResource(self)

    @cached_property
    def forums(self) -> AsyncForumsResource:
        """Forums"""
        from .resources.forums import AsyncForumsResource

        return AsyncForumsResource(self)

    @cached_property
    def promo_codes(self) -> AsyncPromoCodesResource:
        """Promo codes"""
        from .resources.promo_codes import AsyncPromoCodesResource

        return AsyncPromoCodesResource(self)

    @cached_property
    def courses(self) -> AsyncCoursesResource:
        """Courses"""
        from .resources.courses import AsyncCoursesResource

        return AsyncCoursesResource(self)

    @cached_property
    def course_chapters(self) -> AsyncCourseChaptersResource:
        """Course chapters"""
        from .resources.course_chapters import AsyncCourseChaptersResource

        return AsyncCourseChaptersResource(self)

    @cached_property
    def course_lessons(self) -> AsyncCourseLessonsResource:
        """Course lessons"""
        from .resources.course_lessons import AsyncCourseLessonsResource

        return AsyncCourseLessonsResource(self)

    @cached_property
    def reviews(self) -> AsyncReviewsResource:
        """Reviews"""
        from .resources.reviews import AsyncReviewsResource

        return AsyncReviewsResource(self)

    @cached_property
    def course_students(self) -> AsyncCourseStudentsResource:
        """Course students"""
        from .resources.course_students import AsyncCourseStudentsResource

        return AsyncCourseStudentsResource(self)

    @cached_property
    def access_tokens(self) -> AsyncAccessTokensResource:
        """Access tokens"""
        from .resources.access_tokens import AsyncAccessTokensResource

        return AsyncAccessTokensResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        """Notifications"""
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def disputes(self) -> AsyncDisputesResource:
        """Disputes"""
        from .resources.disputes import AsyncDisputesResource

        return AsyncDisputesResource(self)

    @cached_property
    def refunds(self) -> AsyncRefundsResource:
        """Refunds"""
        from .resources.refunds import AsyncRefundsResource

        return AsyncRefundsResource(self)

    @cached_property
    def withdrawals(self) -> AsyncWithdrawalsResource:
        """Withdrawals"""
        from .resources.withdrawals import AsyncWithdrawalsResource

        return AsyncWithdrawalsResource(self)

    @cached_property
    def account_links(self) -> AsyncAccountLinksResource:
        """Account links"""
        from .resources.account_links import AsyncAccountLinksResource

        return AsyncAccountLinksResource(self)

    @cached_property
    def setup_intents(self) -> AsyncSetupIntentsResource:
        """Setup intents"""
        from .resources.setup_intents import AsyncSetupIntentsResource

        return AsyncSetupIntentsResource(self)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        """Payment methods"""
        from .resources.payment_methods import AsyncPaymentMethodsResource

        return AsyncPaymentMethodsResource(self)

    @cached_property
    def fee_markups(self) -> AsyncFeeMarkupsResource:
        """Fee markups"""
        from .resources.fee_markups import AsyncFeeMarkupsResource

        return AsyncFeeMarkupsResource(self)

    @cached_property
    def payout_methods(self) -> AsyncPayoutMethodsResource:
        """Payout methods"""
        from .resources.payout_methods import AsyncPayoutMethodsResource

        return AsyncPayoutMethodsResource(self)

    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """Verifications"""
        from .resources.verifications import AsyncVerificationsResource

        return AsyncVerificationsResource(self)

    @cached_property
    def leads(self) -> AsyncLeadsResource:
        """Leads"""
        from .resources.leads import AsyncLeadsResource

        return AsyncLeadsResource(self)

    @cached_property
    def topups(self) -> AsyncTopupsResource:
        """Topups"""
        from .resources.topups import AsyncTopupsResource

        return AsyncTopupsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        """Files"""
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def company_token_transactions(self) -> AsyncCompanyTokenTransactionsResource:
        """Company token transactions"""
        from .resources.company_token_transactions import AsyncCompanyTokenTransactionsResource

        return AsyncCompanyTokenTransactionsResource(self)

    @cached_property
    def dm_members(self) -> AsyncDmMembersResource:
        """Dm members"""
        from .resources.dm_members import AsyncDmMembersResource

        return AsyncDmMembersResource(self)

    @cached_property
    def ai_chats(self) -> AsyncAIChatsResource:
        """Ai chats"""
        from .resources.ai_chats import AsyncAIChatsResource

        return AsyncAIChatsResource(self)

    @cached_property
    def dm_channels(self) -> AsyncDmChannelsResource:
        """Dm channels"""
        from .resources.dm_channels import AsyncDmChannelsResource

        return AsyncDmChannelsResource(self)

    @cached_property
    def dispute_alerts(self) -> AsyncDisputeAlertsResource:
        """Dispute alerts"""
        from .resources.dispute_alerts import AsyncDisputeAlertsResource

        return AsyncDisputeAlertsResource(self)

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
        """Apps"""
        from .resources.apps import AppsResourceWithRawResponse

        return AppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithRawResponse:
        """Invoices"""
        from .resources.invoices import InvoicesResourceWithRawResponse

        return InvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(self) -> course_lesson_interactions.CourseLessonInteractionsResourceWithRawResponse:
        """Course lesson interactions"""
        from .resources.course_lesson_interactions import CourseLessonInteractionsResourceWithRawResponse

        return CourseLessonInteractionsResourceWithRawResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        """Products"""
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithRawResponse:
        """Companies"""
        from .resources.companies import CompaniesResourceWithRawResponse

        return CompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Webhooks"""
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.PlansResourceWithRawResponse:
        """Plans"""
        from .resources.plans import PlansResourceWithRawResponse

        return PlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.EntriesResourceWithRawResponse:
        """Entries"""
        from .resources.entries import EntriesResourceWithRawResponse

        return EntriesResourceWithRawResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.ForumPostsResourceWithRawResponse:
        """Forum posts"""
        from .resources.forum_posts import ForumPostsResourceWithRawResponse

        return ForumPostsResourceWithRawResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.TransfersResourceWithRawResponse:
        """Transfers"""
        from .resources.transfers import TransfersResourceWithRawResponse

        return TransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsResourceWithRawResponse:
        """Ledger accounts"""
        from .resources.ledger_accounts import LedgerAccountsResourceWithRawResponse

        return LedgerAccountsResourceWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithRawResponse:
        """Memberships"""
        from .resources.memberships import MembershipsResourceWithRawResponse

        return MembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AuthorizedUsersResourceWithRawResponse:
        """Authorized users"""
        from .resources.authorized_users import AuthorizedUsersResourceWithRawResponse

        return AuthorizedUsersResourceWithRawResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AppBuildsResourceWithRawResponse:
        """App builds"""
        from .resources.app_builds import AppBuildsResourceWithRawResponse

        return AppBuildsResourceWithRawResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.ShipmentsResourceWithRawResponse:
        """Shipments"""
        from .resources.shipments import ShipmentsResourceWithRawResponse

        return ShipmentsResourceWithRawResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.CheckoutConfigurationsResourceWithRawResponse:
        """Checkout configurations"""
        from .resources.checkout_configurations import CheckoutConfigurationsResourceWithRawResponse

        return CheckoutConfigurationsResourceWithRawResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """Messages"""
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.ChatChannelsResourceWithRawResponse:
        """Chat channels"""
        from .resources.chat_channels import ChatChannelsResourceWithRawResponse

        return ChatChannelsResourceWithRawResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """Users"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        """Payments"""
        from .resources.payments import PaymentsResourceWithRawResponse

        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.SupportChannelsResourceWithRawResponse:
        """Support channels"""
        from .resources.support_channels import SupportChannelsResourceWithRawResponse

        return SupportChannelsResourceWithRawResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.ExperiencesResourceWithRawResponse:
        """Experiences"""
        from .resources.experiences import ExperiencesResourceWithRawResponse

        return ExperiencesResourceWithRawResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.ReactionsResourceWithRawResponse:
        """Reactions"""
        from .resources.reactions import ReactionsResourceWithRawResponse

        return ReactionsResourceWithRawResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.MembersResourceWithRawResponse:
        """Members"""
        from .resources.members import MembersResourceWithRawResponse

        return MembersResourceWithRawResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.ForumsResourceWithRawResponse:
        """Forums"""
        from .resources.forums import ForumsResourceWithRawResponse

        return ForumsResourceWithRawResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.PromoCodesResourceWithRawResponse:
        """Promo codes"""
        from .resources.promo_codes import PromoCodesResourceWithRawResponse

        return PromoCodesResourceWithRawResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.CoursesResourceWithRawResponse:
        """Courses"""
        from .resources.courses import CoursesResourceWithRawResponse

        return CoursesResourceWithRawResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.CourseChaptersResourceWithRawResponse:
        """Course chapters"""
        from .resources.course_chapters import CourseChaptersResourceWithRawResponse

        return CourseChaptersResourceWithRawResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.CourseLessonsResourceWithRawResponse:
        """Course lessons"""
        from .resources.course_lessons import CourseLessonsResourceWithRawResponse

        return CourseLessonsResourceWithRawResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.ReviewsResourceWithRawResponse:
        """Reviews"""
        from .resources.reviews import ReviewsResourceWithRawResponse

        return ReviewsResourceWithRawResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.CourseStudentsResourceWithRawResponse:
        """Course students"""
        from .resources.course_students import CourseStudentsResourceWithRawResponse

        return CourseStudentsResourceWithRawResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensResourceWithRawResponse:
        """Access tokens"""
        from .resources.access_tokens import AccessTokensResourceWithRawResponse

        return AccessTokensResourceWithRawResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        """Notifications"""
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithRawResponse:
        """Disputes"""
        from .resources.disputes import DisputesResourceWithRawResponse

        return DisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithRawResponse:
        """Refunds"""
        from .resources.refunds import RefundsResourceWithRawResponse

        return RefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.WithdrawalsResourceWithRawResponse:
        """Withdrawals"""
        from .resources.withdrawals import WithdrawalsResourceWithRawResponse

        return WithdrawalsResourceWithRawResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AccountLinksResourceWithRawResponse:
        """Account links"""
        from .resources.account_links import AccountLinksResourceWithRawResponse

        return AccountLinksResourceWithRawResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.SetupIntentsResourceWithRawResponse:
        """Setup intents"""
        from .resources.setup_intents import SetupIntentsResourceWithRawResponse

        return SetupIntentsResourceWithRawResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.PaymentMethodsResourceWithRawResponse:
        """Payment methods"""
        from .resources.payment_methods import PaymentMethodsResourceWithRawResponse

        return PaymentMethodsResourceWithRawResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.FeeMarkupsResourceWithRawResponse:
        """Fee markups"""
        from .resources.fee_markups import FeeMarkupsResourceWithRawResponse

        return FeeMarkupsResourceWithRawResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.PayoutMethodsResourceWithRawResponse:
        """Payout methods"""
        from .resources.payout_methods import PayoutMethodsResourceWithRawResponse

        return PayoutMethodsResourceWithRawResponse(self._client.payout_methods)

    @cached_property
    def verifications(self) -> verifications.VerificationsResourceWithRawResponse:
        """Verifications"""
        from .resources.verifications import VerificationsResourceWithRawResponse

        return VerificationsResourceWithRawResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.LeadsResourceWithRawResponse:
        """Leads"""
        from .resources.leads import LeadsResourceWithRawResponse

        return LeadsResourceWithRawResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.TopupsResourceWithRawResponse:
        """Topups"""
        from .resources.topups import TopupsResourceWithRawResponse

        return TopupsResourceWithRawResponse(self._client.topups)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        """Files"""
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def company_token_transactions(self) -> company_token_transactions.CompanyTokenTransactionsResourceWithRawResponse:
        """Company token transactions"""
        from .resources.company_token_transactions import CompanyTokenTransactionsResourceWithRawResponse

        return CompanyTokenTransactionsResourceWithRawResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.DmMembersResourceWithRawResponse:
        """Dm members"""
        from .resources.dm_members import DmMembersResourceWithRawResponse

        return DmMembersResourceWithRawResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AIChatsResourceWithRawResponse:
        """Ai chats"""
        from .resources.ai_chats import AIChatsResourceWithRawResponse

        return AIChatsResourceWithRawResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.DmChannelsResourceWithRawResponse:
        """Dm channels"""
        from .resources.dm_channels import DmChannelsResourceWithRawResponse

        return DmChannelsResourceWithRawResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.DisputeAlertsResourceWithRawResponse:
        """Dispute alerts"""
        from .resources.dispute_alerts import DisputeAlertsResourceWithRawResponse

        return DisputeAlertsResourceWithRawResponse(self._client.dispute_alerts)


class AsyncWhopWithRawResponse:
    _client: AsyncWhop

    def __init__(self, client: AsyncWhop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithRawResponse:
        """Apps"""
        from .resources.apps import AsyncAppsResourceWithRawResponse

        return AsyncAppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithRawResponse:
        """Invoices"""
        from .resources.invoices import AsyncInvoicesResourceWithRawResponse

        return AsyncInvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(
        self,
    ) -> course_lesson_interactions.AsyncCourseLessonInteractionsResourceWithRawResponse:
        """Course lesson interactions"""
        from .resources.course_lesson_interactions import AsyncCourseLessonInteractionsResourceWithRawResponse

        return AsyncCourseLessonInteractionsResourceWithRawResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        """Products"""
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithRawResponse:
        """Companies"""
        from .resources.companies import AsyncCompaniesResourceWithRawResponse

        return AsyncCompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Webhooks"""
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithRawResponse:
        """Plans"""
        from .resources.plans import AsyncPlansResourceWithRawResponse

        return AsyncPlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.AsyncEntriesResourceWithRawResponse:
        """Entries"""
        from .resources.entries import AsyncEntriesResourceWithRawResponse

        return AsyncEntriesResourceWithRawResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.AsyncForumPostsResourceWithRawResponse:
        """Forum posts"""
        from .resources.forum_posts import AsyncForumPostsResourceWithRawResponse

        return AsyncForumPostsResourceWithRawResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.AsyncTransfersResourceWithRawResponse:
        """Transfers"""
        from .resources.transfers import AsyncTransfersResourceWithRawResponse

        return AsyncTransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsResourceWithRawResponse:
        """Ledger accounts"""
        from .resources.ledger_accounts import AsyncLedgerAccountsResourceWithRawResponse

        return AsyncLedgerAccountsResourceWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithRawResponse:
        """Memberships"""
        from .resources.memberships import AsyncMembershipsResourceWithRawResponse

        return AsyncMembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AsyncAuthorizedUsersResourceWithRawResponse:
        """Authorized users"""
        from .resources.authorized_users import AsyncAuthorizedUsersResourceWithRawResponse

        return AsyncAuthorizedUsersResourceWithRawResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AsyncAppBuildsResourceWithRawResponse:
        """App builds"""
        from .resources.app_builds import AsyncAppBuildsResourceWithRawResponse

        return AsyncAppBuildsResourceWithRawResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.AsyncShipmentsResourceWithRawResponse:
        """Shipments"""
        from .resources.shipments import AsyncShipmentsResourceWithRawResponse

        return AsyncShipmentsResourceWithRawResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.AsyncCheckoutConfigurationsResourceWithRawResponse:
        """Checkout configurations"""
        from .resources.checkout_configurations import AsyncCheckoutConfigurationsResourceWithRawResponse

        return AsyncCheckoutConfigurationsResourceWithRawResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """Messages"""
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.AsyncChatChannelsResourceWithRawResponse:
        """Chat channels"""
        from .resources.chat_channels import AsyncChatChannelsResourceWithRawResponse

        return AsyncChatChannelsResourceWithRawResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """Users"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        """Payments"""
        from .resources.payments import AsyncPaymentsResourceWithRawResponse

        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.AsyncSupportChannelsResourceWithRawResponse:
        """Support channels"""
        from .resources.support_channels import AsyncSupportChannelsResourceWithRawResponse

        return AsyncSupportChannelsResourceWithRawResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.AsyncExperiencesResourceWithRawResponse:
        """Experiences"""
        from .resources.experiences import AsyncExperiencesResourceWithRawResponse

        return AsyncExperiencesResourceWithRawResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.AsyncReactionsResourceWithRawResponse:
        """Reactions"""
        from .resources.reactions import AsyncReactionsResourceWithRawResponse

        return AsyncReactionsResourceWithRawResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithRawResponse:
        """Members"""
        from .resources.members import AsyncMembersResourceWithRawResponse

        return AsyncMembersResourceWithRawResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.AsyncForumsResourceWithRawResponse:
        """Forums"""
        from .resources.forums import AsyncForumsResourceWithRawResponse

        return AsyncForumsResourceWithRawResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.AsyncPromoCodesResourceWithRawResponse:
        """Promo codes"""
        from .resources.promo_codes import AsyncPromoCodesResourceWithRawResponse

        return AsyncPromoCodesResourceWithRawResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.AsyncCoursesResourceWithRawResponse:
        """Courses"""
        from .resources.courses import AsyncCoursesResourceWithRawResponse

        return AsyncCoursesResourceWithRawResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.AsyncCourseChaptersResourceWithRawResponse:
        """Course chapters"""
        from .resources.course_chapters import AsyncCourseChaptersResourceWithRawResponse

        return AsyncCourseChaptersResourceWithRawResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.AsyncCourseLessonsResourceWithRawResponse:
        """Course lessons"""
        from .resources.course_lessons import AsyncCourseLessonsResourceWithRawResponse

        return AsyncCourseLessonsResourceWithRawResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.AsyncReviewsResourceWithRawResponse:
        """Reviews"""
        from .resources.reviews import AsyncReviewsResourceWithRawResponse

        return AsyncReviewsResourceWithRawResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.AsyncCourseStudentsResourceWithRawResponse:
        """Course students"""
        from .resources.course_students import AsyncCourseStudentsResourceWithRawResponse

        return AsyncCourseStudentsResourceWithRawResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensResourceWithRawResponse:
        """Access tokens"""
        from .resources.access_tokens import AsyncAccessTokensResourceWithRawResponse

        return AsyncAccessTokensResourceWithRawResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        """Notifications"""
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithRawResponse:
        """Disputes"""
        from .resources.disputes import AsyncDisputesResourceWithRawResponse

        return AsyncDisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithRawResponse:
        """Refunds"""
        from .resources.refunds import AsyncRefundsResourceWithRawResponse

        return AsyncRefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.AsyncWithdrawalsResourceWithRawResponse:
        """Withdrawals"""
        from .resources.withdrawals import AsyncWithdrawalsResourceWithRawResponse

        return AsyncWithdrawalsResourceWithRawResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AsyncAccountLinksResourceWithRawResponse:
        """Account links"""
        from .resources.account_links import AsyncAccountLinksResourceWithRawResponse

        return AsyncAccountLinksResourceWithRawResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.AsyncSetupIntentsResourceWithRawResponse:
        """Setup intents"""
        from .resources.setup_intents import AsyncSetupIntentsResourceWithRawResponse

        return AsyncSetupIntentsResourceWithRawResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.AsyncPaymentMethodsResourceWithRawResponse:
        """Payment methods"""
        from .resources.payment_methods import AsyncPaymentMethodsResourceWithRawResponse

        return AsyncPaymentMethodsResourceWithRawResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.AsyncFeeMarkupsResourceWithRawResponse:
        """Fee markups"""
        from .resources.fee_markups import AsyncFeeMarkupsResourceWithRawResponse

        return AsyncFeeMarkupsResourceWithRawResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.AsyncPayoutMethodsResourceWithRawResponse:
        """Payout methods"""
        from .resources.payout_methods import AsyncPayoutMethodsResourceWithRawResponse

        return AsyncPayoutMethodsResourceWithRawResponse(self._client.payout_methods)

    @cached_property
    def verifications(self) -> verifications.AsyncVerificationsResourceWithRawResponse:
        """Verifications"""
        from .resources.verifications import AsyncVerificationsResourceWithRawResponse

        return AsyncVerificationsResourceWithRawResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.AsyncLeadsResourceWithRawResponse:
        """Leads"""
        from .resources.leads import AsyncLeadsResourceWithRawResponse

        return AsyncLeadsResourceWithRawResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.AsyncTopupsResourceWithRawResponse:
        """Topups"""
        from .resources.topups import AsyncTopupsResourceWithRawResponse

        return AsyncTopupsResourceWithRawResponse(self._client.topups)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        """Files"""
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def company_token_transactions(
        self,
    ) -> company_token_transactions.AsyncCompanyTokenTransactionsResourceWithRawResponse:
        """Company token transactions"""
        from .resources.company_token_transactions import AsyncCompanyTokenTransactionsResourceWithRawResponse

        return AsyncCompanyTokenTransactionsResourceWithRawResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.AsyncDmMembersResourceWithRawResponse:
        """Dm members"""
        from .resources.dm_members import AsyncDmMembersResourceWithRawResponse

        return AsyncDmMembersResourceWithRawResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AsyncAIChatsResourceWithRawResponse:
        """Ai chats"""
        from .resources.ai_chats import AsyncAIChatsResourceWithRawResponse

        return AsyncAIChatsResourceWithRawResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.AsyncDmChannelsResourceWithRawResponse:
        """Dm channels"""
        from .resources.dm_channels import AsyncDmChannelsResourceWithRawResponse

        return AsyncDmChannelsResourceWithRawResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.AsyncDisputeAlertsResourceWithRawResponse:
        """Dispute alerts"""
        from .resources.dispute_alerts import AsyncDisputeAlertsResourceWithRawResponse

        return AsyncDisputeAlertsResourceWithRawResponse(self._client.dispute_alerts)


class WhopWithStreamedResponse:
    _client: Whop

    def __init__(self, client: Whop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AppsResourceWithStreamingResponse:
        """Apps"""
        from .resources.apps import AppsResourceWithStreamingResponse

        return AppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithStreamingResponse:
        """Invoices"""
        from .resources.invoices import InvoicesResourceWithStreamingResponse

        return InvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(
        self,
    ) -> course_lesson_interactions.CourseLessonInteractionsResourceWithStreamingResponse:
        """Course lesson interactions"""
        from .resources.course_lesson_interactions import CourseLessonInteractionsResourceWithStreamingResponse

        return CourseLessonInteractionsResourceWithStreamingResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        """Products"""
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithStreamingResponse:
        """Companies"""
        from .resources.companies import CompaniesResourceWithStreamingResponse

        return CompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Webhooks"""
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.PlansResourceWithStreamingResponse:
        """Plans"""
        from .resources.plans import PlansResourceWithStreamingResponse

        return PlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.EntriesResourceWithStreamingResponse:
        """Entries"""
        from .resources.entries import EntriesResourceWithStreamingResponse

        return EntriesResourceWithStreamingResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.ForumPostsResourceWithStreamingResponse:
        """Forum posts"""
        from .resources.forum_posts import ForumPostsResourceWithStreamingResponse

        return ForumPostsResourceWithStreamingResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.TransfersResourceWithStreamingResponse:
        """Transfers"""
        from .resources.transfers import TransfersResourceWithStreamingResponse

        return TransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsResourceWithStreamingResponse:
        """Ledger accounts"""
        from .resources.ledger_accounts import LedgerAccountsResourceWithStreamingResponse

        return LedgerAccountsResourceWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithStreamingResponse:
        """Memberships"""
        from .resources.memberships import MembershipsResourceWithStreamingResponse

        return MembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AuthorizedUsersResourceWithStreamingResponse:
        """Authorized users"""
        from .resources.authorized_users import AuthorizedUsersResourceWithStreamingResponse

        return AuthorizedUsersResourceWithStreamingResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AppBuildsResourceWithStreamingResponse:
        """App builds"""
        from .resources.app_builds import AppBuildsResourceWithStreamingResponse

        return AppBuildsResourceWithStreamingResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.ShipmentsResourceWithStreamingResponse:
        """Shipments"""
        from .resources.shipments import ShipmentsResourceWithStreamingResponse

        return ShipmentsResourceWithStreamingResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.CheckoutConfigurationsResourceWithStreamingResponse:
        """Checkout configurations"""
        from .resources.checkout_configurations import CheckoutConfigurationsResourceWithStreamingResponse

        return CheckoutConfigurationsResourceWithStreamingResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """Messages"""
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.ChatChannelsResourceWithStreamingResponse:
        """Chat channels"""
        from .resources.chat_channels import ChatChannelsResourceWithStreamingResponse

        return ChatChannelsResourceWithStreamingResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """Users"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        """Payments"""
        from .resources.payments import PaymentsResourceWithStreamingResponse

        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.SupportChannelsResourceWithStreamingResponse:
        """Support channels"""
        from .resources.support_channels import SupportChannelsResourceWithStreamingResponse

        return SupportChannelsResourceWithStreamingResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.ExperiencesResourceWithStreamingResponse:
        """Experiences"""
        from .resources.experiences import ExperiencesResourceWithStreamingResponse

        return ExperiencesResourceWithStreamingResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.ReactionsResourceWithStreamingResponse:
        """Reactions"""
        from .resources.reactions import ReactionsResourceWithStreamingResponse

        return ReactionsResourceWithStreamingResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.MembersResourceWithStreamingResponse:
        """Members"""
        from .resources.members import MembersResourceWithStreamingResponse

        return MembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.ForumsResourceWithStreamingResponse:
        """Forums"""
        from .resources.forums import ForumsResourceWithStreamingResponse

        return ForumsResourceWithStreamingResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.PromoCodesResourceWithStreamingResponse:
        """Promo codes"""
        from .resources.promo_codes import PromoCodesResourceWithStreamingResponse

        return PromoCodesResourceWithStreamingResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.CoursesResourceWithStreamingResponse:
        """Courses"""
        from .resources.courses import CoursesResourceWithStreamingResponse

        return CoursesResourceWithStreamingResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.CourseChaptersResourceWithStreamingResponse:
        """Course chapters"""
        from .resources.course_chapters import CourseChaptersResourceWithStreamingResponse

        return CourseChaptersResourceWithStreamingResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.CourseLessonsResourceWithStreamingResponse:
        """Course lessons"""
        from .resources.course_lessons import CourseLessonsResourceWithStreamingResponse

        return CourseLessonsResourceWithStreamingResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.ReviewsResourceWithStreamingResponse:
        """Reviews"""
        from .resources.reviews import ReviewsResourceWithStreamingResponse

        return ReviewsResourceWithStreamingResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.CourseStudentsResourceWithStreamingResponse:
        """Course students"""
        from .resources.course_students import CourseStudentsResourceWithStreamingResponse

        return CourseStudentsResourceWithStreamingResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensResourceWithStreamingResponse:
        """Access tokens"""
        from .resources.access_tokens import AccessTokensResourceWithStreamingResponse

        return AccessTokensResourceWithStreamingResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        """Notifications"""
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithStreamingResponse:
        """Disputes"""
        from .resources.disputes import DisputesResourceWithStreamingResponse

        return DisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithStreamingResponse:
        """Refunds"""
        from .resources.refunds import RefundsResourceWithStreamingResponse

        return RefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.WithdrawalsResourceWithStreamingResponse:
        """Withdrawals"""
        from .resources.withdrawals import WithdrawalsResourceWithStreamingResponse

        return WithdrawalsResourceWithStreamingResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AccountLinksResourceWithStreamingResponse:
        """Account links"""
        from .resources.account_links import AccountLinksResourceWithStreamingResponse

        return AccountLinksResourceWithStreamingResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.SetupIntentsResourceWithStreamingResponse:
        """Setup intents"""
        from .resources.setup_intents import SetupIntentsResourceWithStreamingResponse

        return SetupIntentsResourceWithStreamingResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.PaymentMethodsResourceWithStreamingResponse:
        """Payment methods"""
        from .resources.payment_methods import PaymentMethodsResourceWithStreamingResponse

        return PaymentMethodsResourceWithStreamingResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.FeeMarkupsResourceWithStreamingResponse:
        """Fee markups"""
        from .resources.fee_markups import FeeMarkupsResourceWithStreamingResponse

        return FeeMarkupsResourceWithStreamingResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.PayoutMethodsResourceWithStreamingResponse:
        """Payout methods"""
        from .resources.payout_methods import PayoutMethodsResourceWithStreamingResponse

        return PayoutMethodsResourceWithStreamingResponse(self._client.payout_methods)

    @cached_property
    def verifications(self) -> verifications.VerificationsResourceWithStreamingResponse:
        """Verifications"""
        from .resources.verifications import VerificationsResourceWithStreamingResponse

        return VerificationsResourceWithStreamingResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.LeadsResourceWithStreamingResponse:
        """Leads"""
        from .resources.leads import LeadsResourceWithStreamingResponse

        return LeadsResourceWithStreamingResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.TopupsResourceWithStreamingResponse:
        """Topups"""
        from .resources.topups import TopupsResourceWithStreamingResponse

        return TopupsResourceWithStreamingResponse(self._client.topups)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        """Files"""
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def company_token_transactions(
        self,
    ) -> company_token_transactions.CompanyTokenTransactionsResourceWithStreamingResponse:
        """Company token transactions"""
        from .resources.company_token_transactions import CompanyTokenTransactionsResourceWithStreamingResponse

        return CompanyTokenTransactionsResourceWithStreamingResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.DmMembersResourceWithStreamingResponse:
        """Dm members"""
        from .resources.dm_members import DmMembersResourceWithStreamingResponse

        return DmMembersResourceWithStreamingResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AIChatsResourceWithStreamingResponse:
        """Ai chats"""
        from .resources.ai_chats import AIChatsResourceWithStreamingResponse

        return AIChatsResourceWithStreamingResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.DmChannelsResourceWithStreamingResponse:
        """Dm channels"""
        from .resources.dm_channels import DmChannelsResourceWithStreamingResponse

        return DmChannelsResourceWithStreamingResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.DisputeAlertsResourceWithStreamingResponse:
        """Dispute alerts"""
        from .resources.dispute_alerts import DisputeAlertsResourceWithStreamingResponse

        return DisputeAlertsResourceWithStreamingResponse(self._client.dispute_alerts)


class AsyncWhopWithStreamedResponse:
    _client: AsyncWhop

    def __init__(self, client: AsyncWhop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithStreamingResponse:
        """Apps"""
        from .resources.apps import AsyncAppsResourceWithStreamingResponse

        return AsyncAppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithStreamingResponse:
        """Invoices"""
        from .resources.invoices import AsyncInvoicesResourceWithStreamingResponse

        return AsyncInvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def course_lesson_interactions(
        self,
    ) -> course_lesson_interactions.AsyncCourseLessonInteractionsResourceWithStreamingResponse:
        """Course lesson interactions"""
        from .resources.course_lesson_interactions import AsyncCourseLessonInteractionsResourceWithStreamingResponse

        return AsyncCourseLessonInteractionsResourceWithStreamingResponse(self._client.course_lesson_interactions)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        """Products"""
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithStreamingResponse:
        """Companies"""
        from .resources.companies import AsyncCompaniesResourceWithStreamingResponse

        return AsyncCompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Webhooks"""
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithStreamingResponse:
        """Plans"""
        from .resources.plans import AsyncPlansResourceWithStreamingResponse

        return AsyncPlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def entries(self) -> entries.AsyncEntriesResourceWithStreamingResponse:
        """Entries"""
        from .resources.entries import AsyncEntriesResourceWithStreamingResponse

        return AsyncEntriesResourceWithStreamingResponse(self._client.entries)

    @cached_property
    def forum_posts(self) -> forum_posts.AsyncForumPostsResourceWithStreamingResponse:
        """Forum posts"""
        from .resources.forum_posts import AsyncForumPostsResourceWithStreamingResponse

        return AsyncForumPostsResourceWithStreamingResponse(self._client.forum_posts)

    @cached_property
    def transfers(self) -> transfers.AsyncTransfersResourceWithStreamingResponse:
        """Transfers"""
        from .resources.transfers import AsyncTransfersResourceWithStreamingResponse

        return AsyncTransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsResourceWithStreamingResponse:
        """Ledger accounts"""
        from .resources.ledger_accounts import AsyncLedgerAccountsResourceWithStreamingResponse

        return AsyncLedgerAccountsResourceWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithStreamingResponse:
        """Memberships"""
        from .resources.memberships import AsyncMembershipsResourceWithStreamingResponse

        return AsyncMembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AsyncAuthorizedUsersResourceWithStreamingResponse:
        """Authorized users"""
        from .resources.authorized_users import AsyncAuthorizedUsersResourceWithStreamingResponse

        return AsyncAuthorizedUsersResourceWithStreamingResponse(self._client.authorized_users)

    @cached_property
    def app_builds(self) -> app_builds.AsyncAppBuildsResourceWithStreamingResponse:
        """App builds"""
        from .resources.app_builds import AsyncAppBuildsResourceWithStreamingResponse

        return AsyncAppBuildsResourceWithStreamingResponse(self._client.app_builds)

    @cached_property
    def shipments(self) -> shipments.AsyncShipmentsResourceWithStreamingResponse:
        """Shipments"""
        from .resources.shipments import AsyncShipmentsResourceWithStreamingResponse

        return AsyncShipmentsResourceWithStreamingResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(
        self,
    ) -> checkout_configurations.AsyncCheckoutConfigurationsResourceWithStreamingResponse:
        """Checkout configurations"""
        from .resources.checkout_configurations import AsyncCheckoutConfigurationsResourceWithStreamingResponse

        return AsyncCheckoutConfigurationsResourceWithStreamingResponse(self._client.checkout_configurations)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """Messages"""
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def chat_channels(self) -> chat_channels.AsyncChatChannelsResourceWithStreamingResponse:
        """Chat channels"""
        from .resources.chat_channels import AsyncChatChannelsResourceWithStreamingResponse

        return AsyncChatChannelsResourceWithStreamingResponse(self._client.chat_channels)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """Users"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        """Payments"""
        from .resources.payments import AsyncPaymentsResourceWithStreamingResponse

        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def support_channels(self) -> support_channels.AsyncSupportChannelsResourceWithStreamingResponse:
        """Support channels"""
        from .resources.support_channels import AsyncSupportChannelsResourceWithStreamingResponse

        return AsyncSupportChannelsResourceWithStreamingResponse(self._client.support_channels)

    @cached_property
    def experiences(self) -> experiences.AsyncExperiencesResourceWithStreamingResponse:
        """Experiences"""
        from .resources.experiences import AsyncExperiencesResourceWithStreamingResponse

        return AsyncExperiencesResourceWithStreamingResponse(self._client.experiences)

    @cached_property
    def reactions(self) -> reactions.AsyncReactionsResourceWithStreamingResponse:
        """Reactions"""
        from .resources.reactions import AsyncReactionsResourceWithStreamingResponse

        return AsyncReactionsResourceWithStreamingResponse(self._client.reactions)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithStreamingResponse:
        """Members"""
        from .resources.members import AsyncMembersResourceWithStreamingResponse

        return AsyncMembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def forums(self) -> forums.AsyncForumsResourceWithStreamingResponse:
        """Forums"""
        from .resources.forums import AsyncForumsResourceWithStreamingResponse

        return AsyncForumsResourceWithStreamingResponse(self._client.forums)

    @cached_property
    def promo_codes(self) -> promo_codes.AsyncPromoCodesResourceWithStreamingResponse:
        """Promo codes"""
        from .resources.promo_codes import AsyncPromoCodesResourceWithStreamingResponse

        return AsyncPromoCodesResourceWithStreamingResponse(self._client.promo_codes)

    @cached_property
    def courses(self) -> courses.AsyncCoursesResourceWithStreamingResponse:
        """Courses"""
        from .resources.courses import AsyncCoursesResourceWithStreamingResponse

        return AsyncCoursesResourceWithStreamingResponse(self._client.courses)

    @cached_property
    def course_chapters(self) -> course_chapters.AsyncCourseChaptersResourceWithStreamingResponse:
        """Course chapters"""
        from .resources.course_chapters import AsyncCourseChaptersResourceWithStreamingResponse

        return AsyncCourseChaptersResourceWithStreamingResponse(self._client.course_chapters)

    @cached_property
    def course_lessons(self) -> course_lessons.AsyncCourseLessonsResourceWithStreamingResponse:
        """Course lessons"""
        from .resources.course_lessons import AsyncCourseLessonsResourceWithStreamingResponse

        return AsyncCourseLessonsResourceWithStreamingResponse(self._client.course_lessons)

    @cached_property
    def reviews(self) -> reviews.AsyncReviewsResourceWithStreamingResponse:
        """Reviews"""
        from .resources.reviews import AsyncReviewsResourceWithStreamingResponse

        return AsyncReviewsResourceWithStreamingResponse(self._client.reviews)

    @cached_property
    def course_students(self) -> course_students.AsyncCourseStudentsResourceWithStreamingResponse:
        """Course students"""
        from .resources.course_students import AsyncCourseStudentsResourceWithStreamingResponse

        return AsyncCourseStudentsResourceWithStreamingResponse(self._client.course_students)

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensResourceWithStreamingResponse:
        """Access tokens"""
        from .resources.access_tokens import AsyncAccessTokensResourceWithStreamingResponse

        return AsyncAccessTokensResourceWithStreamingResponse(self._client.access_tokens)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        """Notifications"""
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithStreamingResponse:
        """Disputes"""
        from .resources.disputes import AsyncDisputesResourceWithStreamingResponse

        return AsyncDisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithStreamingResponse:
        """Refunds"""
        from .resources.refunds import AsyncRefundsResourceWithStreamingResponse

        return AsyncRefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def withdrawals(self) -> withdrawals.AsyncWithdrawalsResourceWithStreamingResponse:
        """Withdrawals"""
        from .resources.withdrawals import AsyncWithdrawalsResourceWithStreamingResponse

        return AsyncWithdrawalsResourceWithStreamingResponse(self._client.withdrawals)

    @cached_property
    def account_links(self) -> account_links.AsyncAccountLinksResourceWithStreamingResponse:
        """Account links"""
        from .resources.account_links import AsyncAccountLinksResourceWithStreamingResponse

        return AsyncAccountLinksResourceWithStreamingResponse(self._client.account_links)

    @cached_property
    def setup_intents(self) -> setup_intents.AsyncSetupIntentsResourceWithStreamingResponse:
        """Setup intents"""
        from .resources.setup_intents import AsyncSetupIntentsResourceWithStreamingResponse

        return AsyncSetupIntentsResourceWithStreamingResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.AsyncPaymentMethodsResourceWithStreamingResponse:
        """Payment methods"""
        from .resources.payment_methods import AsyncPaymentMethodsResourceWithStreamingResponse

        return AsyncPaymentMethodsResourceWithStreamingResponse(self._client.payment_methods)

    @cached_property
    def fee_markups(self) -> fee_markups.AsyncFeeMarkupsResourceWithStreamingResponse:
        """Fee markups"""
        from .resources.fee_markups import AsyncFeeMarkupsResourceWithStreamingResponse

        return AsyncFeeMarkupsResourceWithStreamingResponse(self._client.fee_markups)

    @cached_property
    def payout_methods(self) -> payout_methods.AsyncPayoutMethodsResourceWithStreamingResponse:
        """Payout methods"""
        from .resources.payout_methods import AsyncPayoutMethodsResourceWithStreamingResponse

        return AsyncPayoutMethodsResourceWithStreamingResponse(self._client.payout_methods)

    @cached_property
    def verifications(self) -> verifications.AsyncVerificationsResourceWithStreamingResponse:
        """Verifications"""
        from .resources.verifications import AsyncVerificationsResourceWithStreamingResponse

        return AsyncVerificationsResourceWithStreamingResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.AsyncLeadsResourceWithStreamingResponse:
        """Leads"""
        from .resources.leads import AsyncLeadsResourceWithStreamingResponse

        return AsyncLeadsResourceWithStreamingResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.AsyncTopupsResourceWithStreamingResponse:
        """Topups"""
        from .resources.topups import AsyncTopupsResourceWithStreamingResponse

        return AsyncTopupsResourceWithStreamingResponse(self._client.topups)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        """Files"""
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def company_token_transactions(
        self,
    ) -> company_token_transactions.AsyncCompanyTokenTransactionsResourceWithStreamingResponse:
        """Company token transactions"""
        from .resources.company_token_transactions import AsyncCompanyTokenTransactionsResourceWithStreamingResponse

        return AsyncCompanyTokenTransactionsResourceWithStreamingResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.AsyncDmMembersResourceWithStreamingResponse:
        """Dm members"""
        from .resources.dm_members import AsyncDmMembersResourceWithStreamingResponse

        return AsyncDmMembersResourceWithStreamingResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AsyncAIChatsResourceWithStreamingResponse:
        """Ai chats"""
        from .resources.ai_chats import AsyncAIChatsResourceWithStreamingResponse

        return AsyncAIChatsResourceWithStreamingResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.AsyncDmChannelsResourceWithStreamingResponse:
        """Dm channels"""
        from .resources.dm_channels import AsyncDmChannelsResourceWithStreamingResponse

        return AsyncDmChannelsResourceWithStreamingResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.AsyncDisputeAlertsResourceWithStreamingResponse:
        """Dispute alerts"""
        from .resources.dispute_alerts import AsyncDisputeAlertsResourceWithStreamingResponse

        return AsyncDisputeAlertsResourceWithStreamingResponse(self._client.dispute_alerts)


Client = Whop

AsyncClient = AsyncWhop
