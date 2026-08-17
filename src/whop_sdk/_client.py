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
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
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
        ads,
        apps,
        cards,
        files,
        leads,
        media,
        plans,
        stats,
        swaps,
        users,
        events,
        forums,
        people,
        topups,
        courses,
        entries,
        exports,
        members,
        payouts,
        refunds,
        reviews,
        accounts,
        ai_chats,
        api_keys,
        bounties,
        deposits,
        disputes,
        invoices,
        messages,
        partners,
        payments,
        products,
        webhooks,
        ad_groups,
        audiences,
        companies,
        reactions,
        shipments,
        transfers,
        ad_reports,
        affiliates,
        app_builds,
        dm_members,
        dm_channels,
        experiences,
        fee_markups,
        forum_posts,
        memberships,
        permissions,
        promo_codes,
        withdrawals,
        ad_campaigns,
        team_members,
        access_tokens,
        account_links,
        chat_channels,
        notifications,
        setup_intents,
        verifications,
        course_lessons,
        dispute_alerts,
        app_deployments,
        course_chapters,
        course_students,
        ledger_accounts,
        payment_methods,
        payout_accounts,
        social_accounts,
        authorized_users,
        support_channels,
        card_transactions,
        bounty_submissions,
        financial_activity,
        recommended_actions,
        payment_method_domains,
        checkout_configurations,
        resolution_center_cases,
        company_token_transactions,
        course_lesson_interactions,
    )
    from .resources.ads import AdsResource, AsyncAdsResource
    from .resources.apps import AppsResource, AsyncAppsResource
    from .resources.cards import CardsResource, AsyncCardsResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.leads import LeadsResource, AsyncLeadsResource
    from .resources.media import MediaResource, AsyncMediaResource
    from .resources.plans import PlansResource, AsyncPlansResource
    from .resources.stats import StatsResource, AsyncStatsResource
    from .resources.swaps import SwapsResource, AsyncSwapsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.forums import ForumsResource, AsyncForumsResource
    from .resources.people import PeopleResource, AsyncPeopleResource
    from .resources.topups import TopupsResource, AsyncTopupsResource
    from .resources.courses import CoursesResource, AsyncCoursesResource
    from .resources.entries import EntriesResource, AsyncEntriesResource
    from .resources.exports import ExportsResource, AsyncExportsResource
    from .resources.refunds import RefundsResource, AsyncRefundsResource
    from .resources.reviews import ReviewsResource, AsyncReviewsResource
    from .resources.ai_chats import AIChatsResource, AsyncAIChatsResource
    from .resources.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.deposits import DepositsResource, AsyncDepositsResource
    from .resources.disputes import DisputesResource, AsyncDisputesResource
    from .resources.invoices import InvoicesResource, AsyncInvoicesResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.products import ProductsResource, AsyncProductsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.ad_groups import AdGroupsResource, AsyncAdGroupsResource
    from .resources.audiences import AudiencesResource, AsyncAudiencesResource
    from .resources.companies import CompaniesResource, AsyncCompaniesResource
    from .resources.reactions import ReactionsResource, AsyncReactionsResource
    from .resources.shipments import ShipmentsResource, AsyncShipmentsResource
    from .resources.transfers import TransfersResource, AsyncTransfersResource
    from .resources.ad_reports import AdReportsResource, AsyncAdReportsResource
    from .resources.app_builds import AppBuildsResource, AsyncAppBuildsResource
    from .resources.dm_members import DmMembersResource, AsyncDmMembersResource
    from .resources.dm_channels import DmChannelsResource, AsyncDmChannelsResource
    from .resources.experiences import ExperiencesResource, AsyncExperiencesResource
    from .resources.fee_markups import FeeMarkupsResource, AsyncFeeMarkupsResource
    from .resources.forum_posts import ForumPostsResource, AsyncForumPostsResource
    from .resources.memberships import MembershipsResource, AsyncMembershipsResource
    from .resources.permissions import PermissionsResource, AsyncPermissionsResource
    from .resources.promo_codes import PromoCodesResource, AsyncPromoCodesResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.withdrawals import WithdrawalsResource, AsyncWithdrawalsResource
    from .resources.ad_campaigns import AdCampaignsResource, AsyncAdCampaignsResource
    from .resources.team_members import TeamMembersResource, AsyncTeamMembersResource
    from .resources.access_tokens import AccessTokensResource, AsyncAccessTokensResource
    from .resources.account_links import AccountLinksResource, AsyncAccountLinksResource
    from .resources.chat_channels import ChatChannelsResource, AsyncChatChannelsResource
    from .resources.setup_intents import SetupIntentsResource, AsyncSetupIntentsResource
    from .resources.verifications import VerificationsResource, AsyncVerificationsResource
    from .resources.course_lessons import CourseLessonsResource, AsyncCourseLessonsResource
    from .resources.dispute_alerts import DisputeAlertsResource, AsyncDisputeAlertsResource
    from .resources.app_deployments import AppDeploymentsResource, AsyncAppDeploymentsResource
    from .resources.course_chapters import CourseChaptersResource, AsyncCourseChaptersResource
    from .resources.course_students import CourseStudentsResource, AsyncCourseStudentsResource
    from .resources.ledger_accounts import LedgerAccountsResource, AsyncLedgerAccountsResource
    from .resources.members.members import MembersResource, AsyncMembersResource
    from .resources.payment_methods import PaymentMethodsResource, AsyncPaymentMethodsResource
    from .resources.payout_accounts import PayoutAccountsResource, AsyncPayoutAccountsResource
    from .resources.payouts.payouts import PayoutsResource, AsyncPayoutsResource
    from .resources.social_accounts import SocialAccountsResource, AsyncSocialAccountsResource
    from .resources.authorized_users import AuthorizedUsersResource, AsyncAuthorizedUsersResource
    from .resources.support_channels import SupportChannelsResource, AsyncSupportChannelsResource
    from .resources.accounts.accounts import AccountsResource, AsyncAccountsResource
    from .resources.bounties.bounties import BountiesResource, AsyncBountiesResource
    from .resources.card_transactions import CardTransactionsResource, AsyncCardTransactionsResource
    from .resources.partners.partners import PartnersResource, AsyncPartnersResource
    from .resources.bounty_submissions import BountySubmissionsResource, AsyncBountySubmissionsResource
    from .resources.financial_activity import FinancialActivityResource, AsyncFinancialActivityResource
    from .resources.recommended_actions import RecommendedActionsResource, AsyncRecommendedActionsResource
    from .resources.affiliates.affiliates import AffiliatesResource, AsyncAffiliatesResource
    from .resources.payment_method_domains import PaymentMethodDomainsResource, AsyncPaymentMethodDomainsResource
    from .resources.checkout_configurations import CheckoutConfigurationsResource, AsyncCheckoutConfigurationsResource
    from .resources.resolution_center_cases import ResolutionCenterCasesResource, AsyncResolutionCenterCasesResource
    from .resources.company_token_transactions import (
        CompanyTokenTransactionsResource,
        AsyncCompanyTokenTransactionsResource,
    )
    from .resources.course_lesson_interactions import (
        CourseLessonInteractionsResource,
        AsyncCourseLessonInteractionsResource,
    )
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Whop", "AsyncWhop", "Client", "AsyncClient"]


class Whop(SyncAPIClient):
    # client options
    api_key: str
    webhook_key: str | None
    app_id: str | None
    version: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        version: str | None = None,
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
        - `version` from `WHOP_API_VERSION`
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

        if version is None:
            version = os.environ.get("WHOP_API_VERSION") or "2026-08-13"
        self.version = version

        if base_url is None:
            base_url = os.environ.get("WHOP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.whop.com/api/v1"

        custom_headers_env = os.environ.get("WHOP_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def apps(self) -> AppsResource:
        """An App is software you build on Whop.

        It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

        Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
        """
        from .resources.apps import AppsResource

        return AppsResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        """An API Key is a programmatic credential owned by an account or app.

        Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

        Use the API Keys API to list an account or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
        """
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def permissions(self) -> PermissionsResource:
        """
        A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

        Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
        """
        from .resources.permissions import PermissionsResource

        return PermissionsResource(self)

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
        """A Product is a digital good or service sold on Whop.

        Products may contain plans for pricing and/or experiences for content delivery.

        Use the Products API to create products, list products visible to your credentials, retrieve product details, update product metadata or merchandising fields, and delete products that should no longer be sold.
        """
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def social_accounts(self) -> SocialAccountsResource:
        """
        A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

        Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts or a Facebook page's lead forms.
        """
        from .resources.social_accounts import SocialAccountsResource

        return SocialAccountsResource(self)

    @cached_property
    def audiences(self) -> AudiencesResource:
        """An Audience represents a customer list uploaded to Whop for ad targeting.

        Audiences belong to an account and sync to supported ad platforms as custom audiences.

        Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
        """
        from .resources.audiences import AudiencesResource

        return AudiencesResource(self)

    @cached_property
    def media(self) -> MediaResource:
        """
        A Media Asset is an AI-generated image or video created from a prompt and billed from an account balance. When generation finishes, the asset includes a file that can be attached anywhere Whop accepts files.

        Use the Media API to start a generation job and retrieve the asset while it processes or after it is ready.
        """
        from .resources.media import MediaResource

        return MediaResource(self)

    @cached_property
    def people(self) -> PeopleResource:
        """
        A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

        Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
        """
        from .resources.people import PeopleResource

        return PeopleResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """
        An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

        Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person. The resource also exposes an anonymized read mode — the pulse feed — a platform-wide snapshot of recent purchases that carries nothing identifying. The pulse feed is public; other Events endpoints require authentication and are scoped to an account.

        Events are only as good as the pixel sending them, so [Validate Pixel](/api-reference/beta/events/validate-pixel) answers whether an account's pixel is working: it reads the events the pixel has sent, and when you pass a `url` whose page hasn't sent any lately, it fetches that page and looks for the pixel in its source. Use it before launching an ad to confirm its destination is tracked, or in a setup flow to tell a merchant whether their install is live.
        """
        from .resources.events import EventsResource

        return EventsResource(self)

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
        """A Plan defines how customers buy a product.

        It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

        Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
        """
        from .resources.plans import PlansResource

        return PlansResource(self)

    @cached_property
    def exports(self) -> ExportsResource:
        """
        An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

        Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
        """
        from .resources.exports import ExportsResource

        return ExportsResource(self)

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
        """Transfers move value between identities on Whop.

        They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

        Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
        """
        from .resources.transfers import TransfersResource

        return TransfersResource(self)

    @cached_property
    def ledger_accounts(self) -> LedgerAccountsResource:
        from .resources.ledger_accounts import LedgerAccountsResource

        return LedgerAccountsResource(self)

    @cached_property
    def memberships(self) -> MembershipsResource:
        """
        A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

        Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, invite a recipient to join through a free plan, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, generate a transfer link, and update metadata.
        """
        from .resources.memberships import MembershipsResource

        return MembershipsResource(self)

    @cached_property
    def authorized_users(self) -> AuthorizedUsersResource:
        from .resources.authorized_users import AuthorizedUsersResource

        return AuthorizedUsersResource(self)

    @cached_property
    def team_members(self) -> TeamMembersResource:
        """
        A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

        Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
        """
        from .resources.team_members import TeamMembersResource

        return TeamMembersResource(self)

    @cached_property
    def app_builds(self) -> AppBuildsResource:
        """
        An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

        Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
        """
        from .resources.app_builds import AppBuildsResource

        return AppBuildsResource(self)

    @cached_property
    def app_deployments(self) -> AppDeploymentsResource:
        """A Deployment builds an app's current source and ships it, producing an App Build.

        It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

        Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
        """
        from .resources.app_deployments import AppDeploymentsResource

        return AppDeploymentsResource(self)

    @cached_property
    def shipments(self) -> ShipmentsResource:
        """
        A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

        Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
        """
        from .resources.shipments import ShipmentsResource

        return ShipmentsResource(self)

    @cached_property
    def checkout_configurations(self) -> CheckoutConfigurationsResource:
        """A Checkout Configuration is a reusable checkout link owned by an account.

        In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

        Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
        """
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
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        """A Payment is one charge against a buyer.

        Create it with a payment method already on file, or with a `confirmation_token` describing a method the buyer has just supplied.

        Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
        """
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
        """
        A Member is one buyer's relationship with an account — one record per customer regardless of how many memberships they hold. It carries relationship-level state: whether they have joined or left, their access level (`customer`, `admin`, or `no_access`), when they joined, and when they last opened the account's content.

        Use the Members API to list an account's members with filtering by access level, status, join date, and name or username search, and to retrieve a single member. Member rows are created and maintained by the membership lifecycle; to grant or revoke access, work with memberships instead.
        """
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
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def disputes(self) -> DisputesResource:
        """
        A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

        Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
        """
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
    def accounts(self) -> AccountsResource:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def financial_activity(self) -> FinancialActivityResource:
        """
        A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

        Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
        """
        from .resources.financial_activity import FinancialActivityResource

        return FinancialActivityResource(self)

    @cached_property
    def stats(self) -> StatsResource:
        """Stats represent aggregated activity for an account over time.

        They help you understand revenue, transactions, disputes, members, referrals, and advertising performance across reporting periods like days, weeks, or months.

        Use the Stats API to list available metrics and their filterable properties, then retrieve time-series values for a date range.
        """
        from .resources.stats import StatsResource

        return StatsResource(self)

    @cached_property
    def payouts(self) -> PayoutsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        from .resources.payouts import PayoutsResource

        return PayoutsResource(self)

    @cached_property
    def partners(self) -> PartnersResource:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        from .resources.partners import PartnersResource

        return PartnersResource(self)

    @cached_property
    def cards(self) -> CardsResource:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.cards import CardsResource

        return CardsResource(self)

    @cached_property
    def card_transactions(self) -> CardTransactionsResource:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.card_transactions import CardTransactionsResource

        return CardTransactionsResource(self)

    @cached_property
    def swaps(self) -> SwapsResource:
        """
        Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

        Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
        """
        from .resources.swaps import SwapsResource

        return SwapsResource(self)

    @cached_property
    def deposits(self) -> DepositsResource:
        """
        Deposits describe ways to add funds to an account balance, including hosted deposit pages, bank deposit instructions, and supported crypto wallet addresses.

        Use the Deposits API to create deposit instructions for an account.
        """
        from .resources.deposits import DepositsResource

        return DepositsResource(self)

    @cached_property
    def recommended_actions(self) -> RecommendedActionsResource:
        """
        A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

        Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
        """
        from .resources.recommended_actions import RecommendedActionsResource

        return RecommendedActionsResource(self)

    @cached_property
    def setup_intents(self) -> SetupIntentsResource:
        from .resources.setup_intents import SetupIntentsResource

        return SetupIntentsResource(self)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        from .resources.payment_methods import PaymentMethodsResource

        return PaymentMethodsResource(self)

    @cached_property
    def payment_method_domains(self) -> PaymentMethodDomainsResource:
        """
        A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

        Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
        """
        from .resources.payment_method_domains import PaymentMethodDomainsResource

        return PaymentMethodDomainsResource(self)

    @cached_property
    def fee_markups(self) -> FeeMarkupsResource:
        from .resources.fee_markups import FeeMarkupsResource

        return FeeMarkupsResource(self)

    @cached_property
    def verifications(self) -> VerificationsResource:
        """A Verification represents a legal identity for a person or business.

        Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

        Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
        """
        from .resources.verifications import VerificationsResource

        return VerificationsResource(self)

    @cached_property
    def leads(self) -> LeadsResource:
        from .resources.leads import LeadsResource

        return LeadsResource(self)

    @cached_property
    def topups(self) -> TopupsResource:
        from .resources.topups import TopupsResource

        return TopupsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def company_token_transactions(self) -> CompanyTokenTransactionsResource:
        from .resources.company_token_transactions import CompanyTokenTransactionsResource

        return CompanyTokenTransactionsResource(self)

    @cached_property
    def dm_members(self) -> DmMembersResource:
        from .resources.dm_members import DmMembersResource

        return DmMembersResource(self)

    @cached_property
    def ai_chats(self) -> AIChatsResource:
        from .resources.ai_chats import AIChatsResource

        return AIChatsResource(self)

    @cached_property
    def dm_channels(self) -> DmChannelsResource:
        from .resources.dm_channels import DmChannelsResource

        return DmChannelsResource(self)

    @cached_property
    def dispute_alerts(self) -> DisputeAlertsResource:
        """
        A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

        Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
        """
        from .resources.dispute_alerts import DisputeAlertsResource

        return DisputeAlertsResource(self)

    @cached_property
    def resolution_center_cases(self) -> ResolutionCenterCasesResource:
        """
        A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

        Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
        """
        from .resources.resolution_center_cases import ResolutionCenterCasesResource

        return ResolutionCenterCasesResource(self)

    @cached_property
    def payout_accounts(self) -> PayoutAccountsResource:
        from .resources.payout_accounts import PayoutAccountsResource

        return PayoutAccountsResource(self)

    @cached_property
    def affiliates(self) -> AffiliatesResource:
        from .resources.affiliates import AffiliatesResource

        return AffiliatesResource(self)

    @cached_property
    def bounties(self) -> BountiesResource:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        from .resources.bounties import BountiesResource

        return BountiesResource(self)

    @cached_property
    def bounty_submissions(self) -> BountySubmissionsResource:
        """A Bounty Submission is one worker's attempt on a bounty.

        It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

        Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
        """
        from .resources.bounty_submissions import BountySubmissionsResource

        return BountySubmissionsResource(self)

    @cached_property
    def ad_campaigns(self) -> AdCampaignsResource:
        """An Ad Campaign is the top-level container for paid ads on an ad network.

        It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

        Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
        """
        from .resources.ad_campaigns import AdCampaignsResource

        return AdCampaignsResource(self)

    @cached_property
    def ad_groups(self) -> AdGroupsResource:
        """
        An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

        Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
        """
        from .resources.ad_groups import AdGroupsResource

        return AdGroupsResource(self)

    @cached_property
    def ads(self) -> AdsResource:
        """
        An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

        Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
        """
        from .resources.ads import AdsResource

        return AdsResource(self)

    @cached_property
    def ad_reports(self) -> AdReportsResource:
        from .resources.ad_reports import AdReportsResource

        return AdReportsResource(self)

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
            "Api-Version-Date": self.version if self.version is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        version: str | None = None,
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
            version=version or self.version,
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
    version: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        version: str | None = None,
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
        - `version` from `WHOP_API_VERSION`
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

        if version is None:
            version = os.environ.get("WHOP_API_VERSION") or "2026-08-13"
        self.version = version

        if base_url is None:
            base_url = os.environ.get("WHOP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.whop.com/api/v1"

        custom_headers_env = os.environ.get("WHOP_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def apps(self) -> AsyncAppsResource:
        """An App is software you build on Whop.

        It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

        Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
        """
        from .resources.apps import AsyncAppsResource

        return AsyncAppsResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        """An API Key is a programmatic credential owned by an account or app.

        Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

        Use the API Keys API to list an account or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
        """
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        """
        A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

        Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
        """
        from .resources.permissions import AsyncPermissionsResource

        return AsyncPermissionsResource(self)

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
        """A Product is a digital good or service sold on Whop.

        Products may contain plans for pricing and/or experiences for content delivery.

        Use the Products API to create products, list products visible to your credentials, retrieve product details, update product metadata or merchandising fields, and delete products that should no longer be sold.
        """
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def social_accounts(self) -> AsyncSocialAccountsResource:
        """
        A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

        Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts or a Facebook page's lead forms.
        """
        from .resources.social_accounts import AsyncSocialAccountsResource

        return AsyncSocialAccountsResource(self)

    @cached_property
    def audiences(self) -> AsyncAudiencesResource:
        """An Audience represents a customer list uploaded to Whop for ad targeting.

        Audiences belong to an account and sync to supported ad platforms as custom audiences.

        Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
        """
        from .resources.audiences import AsyncAudiencesResource

        return AsyncAudiencesResource(self)

    @cached_property
    def media(self) -> AsyncMediaResource:
        """
        A Media Asset is an AI-generated image or video created from a prompt and billed from an account balance. When generation finishes, the asset includes a file that can be attached anywhere Whop accepts files.

        Use the Media API to start a generation job and retrieve the asset while it processes or after it is ready.
        """
        from .resources.media import AsyncMediaResource

        return AsyncMediaResource(self)

    @cached_property
    def people(self) -> AsyncPeopleResource:
        """
        A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

        Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
        """
        from .resources.people import AsyncPeopleResource

        return AsyncPeopleResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """
        An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

        Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person. The resource also exposes an anonymized read mode — the pulse feed — a platform-wide snapshot of recent purchases that carries nothing identifying. The pulse feed is public; other Events endpoints require authentication and are scoped to an account.

        Events are only as good as the pixel sending them, so [Validate Pixel](/api-reference/beta/events/validate-pixel) answers whether an account's pixel is working: it reads the events the pixel has sent, and when you pass a `url` whose page hasn't sent any lately, it fetches that page and looks for the pixel in its source. Use it before launching an ad to confirm its destination is tracked, or in a setup flow to tell a merchant whether their install is live.
        """
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

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
        """A Plan defines how customers buy a product.

        It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

        Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
        """
        from .resources.plans import AsyncPlansResource

        return AsyncPlansResource(self)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        """
        An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

        Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
        """
        from .resources.exports import AsyncExportsResource

        return AsyncExportsResource(self)

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
        """Transfers move value between identities on Whop.

        They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

        Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
        """
        from .resources.transfers import AsyncTransfersResource

        return AsyncTransfersResource(self)

    @cached_property
    def ledger_accounts(self) -> AsyncLedgerAccountsResource:
        from .resources.ledger_accounts import AsyncLedgerAccountsResource

        return AsyncLedgerAccountsResource(self)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        """
        A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

        Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, invite a recipient to join through a free plan, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, generate a transfer link, and update metadata.
        """
        from .resources.memberships import AsyncMembershipsResource

        return AsyncMembershipsResource(self)

    @cached_property
    def authorized_users(self) -> AsyncAuthorizedUsersResource:
        from .resources.authorized_users import AsyncAuthorizedUsersResource

        return AsyncAuthorizedUsersResource(self)

    @cached_property
    def team_members(self) -> AsyncTeamMembersResource:
        """
        A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

        Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
        """
        from .resources.team_members import AsyncTeamMembersResource

        return AsyncTeamMembersResource(self)

    @cached_property
    def app_builds(self) -> AsyncAppBuildsResource:
        """
        An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

        Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
        """
        from .resources.app_builds import AsyncAppBuildsResource

        return AsyncAppBuildsResource(self)

    @cached_property
    def app_deployments(self) -> AsyncAppDeploymentsResource:
        """A Deployment builds an app's current source and ships it, producing an App Build.

        It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

        Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
        """
        from .resources.app_deployments import AsyncAppDeploymentsResource

        return AsyncAppDeploymentsResource(self)

    @cached_property
    def shipments(self) -> AsyncShipmentsResource:
        """
        A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

        Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
        """
        from .resources.shipments import AsyncShipmentsResource

        return AsyncShipmentsResource(self)

    @cached_property
    def checkout_configurations(self) -> AsyncCheckoutConfigurationsResource:
        """A Checkout Configuration is a reusable checkout link owned by an account.

        In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

        Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
        """
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
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        """A Payment is one charge against a buyer.

        Create it with a payment method already on file, or with a `confirmation_token` describing a method the buyer has just supplied.

        Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
        """
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
        """
        A Member is one buyer's relationship with an account — one record per customer regardless of how many memberships they hold. It carries relationship-level state: whether they have joined or left, their access level (`customer`, `admin`, or `no_access`), when they joined, and when they last opened the account's content.

        Use the Members API to list an account's members with filtering by access level, status, join date, and name or username search, and to retrieve a single member. Member rows are created and maintained by the membership lifecycle; to grant or revoke access, work with memberships instead.
        """
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
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def disputes(self) -> AsyncDisputesResource:
        """
        A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

        Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
        """
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
    def accounts(self) -> AsyncAccountsResource:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def financial_activity(self) -> AsyncFinancialActivityResource:
        """
        A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

        Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
        """
        from .resources.financial_activity import AsyncFinancialActivityResource

        return AsyncFinancialActivityResource(self)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        """Stats represent aggregated activity for an account over time.

        They help you understand revenue, transactions, disputes, members, referrals, and advertising performance across reporting periods like days, weeks, or months.

        Use the Stats API to list available metrics and their filterable properties, then retrieve time-series values for a date range.
        """
        from .resources.stats import AsyncStatsResource

        return AsyncStatsResource(self)

    @cached_property
    def payouts(self) -> AsyncPayoutsResource:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        from .resources.payouts import AsyncPayoutsResource

        return AsyncPayoutsResource(self)

    @cached_property
    def partners(self) -> AsyncPartnersResource:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        from .resources.partners import AsyncPartnersResource

        return AsyncPartnersResource(self)

    @cached_property
    def cards(self) -> AsyncCardsResource:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.cards import AsyncCardsResource

        return AsyncCardsResource(self)

    @cached_property
    def card_transactions(self) -> AsyncCardTransactionsResource:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.card_transactions import AsyncCardTransactionsResource

        return AsyncCardTransactionsResource(self)

    @cached_property
    def swaps(self) -> AsyncSwapsResource:
        """
        Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

        Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
        """
        from .resources.swaps import AsyncSwapsResource

        return AsyncSwapsResource(self)

    @cached_property
    def deposits(self) -> AsyncDepositsResource:
        """
        Deposits describe ways to add funds to an account balance, including hosted deposit pages, bank deposit instructions, and supported crypto wallet addresses.

        Use the Deposits API to create deposit instructions for an account.
        """
        from .resources.deposits import AsyncDepositsResource

        return AsyncDepositsResource(self)

    @cached_property
    def recommended_actions(self) -> AsyncRecommendedActionsResource:
        """
        A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

        Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
        """
        from .resources.recommended_actions import AsyncRecommendedActionsResource

        return AsyncRecommendedActionsResource(self)

    @cached_property
    def setup_intents(self) -> AsyncSetupIntentsResource:
        from .resources.setup_intents import AsyncSetupIntentsResource

        return AsyncSetupIntentsResource(self)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        from .resources.payment_methods import AsyncPaymentMethodsResource

        return AsyncPaymentMethodsResource(self)

    @cached_property
    def payment_method_domains(self) -> AsyncPaymentMethodDomainsResource:
        """
        A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

        Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
        """
        from .resources.payment_method_domains import AsyncPaymentMethodDomainsResource

        return AsyncPaymentMethodDomainsResource(self)

    @cached_property
    def fee_markups(self) -> AsyncFeeMarkupsResource:
        from .resources.fee_markups import AsyncFeeMarkupsResource

        return AsyncFeeMarkupsResource(self)

    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """A Verification represents a legal identity for a person or business.

        Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

        Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
        """
        from .resources.verifications import AsyncVerificationsResource

        return AsyncVerificationsResource(self)

    @cached_property
    def leads(self) -> AsyncLeadsResource:
        from .resources.leads import AsyncLeadsResource

        return AsyncLeadsResource(self)

    @cached_property
    def topups(self) -> AsyncTopupsResource:
        from .resources.topups import AsyncTopupsResource

        return AsyncTopupsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def company_token_transactions(self) -> AsyncCompanyTokenTransactionsResource:
        from .resources.company_token_transactions import AsyncCompanyTokenTransactionsResource

        return AsyncCompanyTokenTransactionsResource(self)

    @cached_property
    def dm_members(self) -> AsyncDmMembersResource:
        from .resources.dm_members import AsyncDmMembersResource

        return AsyncDmMembersResource(self)

    @cached_property
    def ai_chats(self) -> AsyncAIChatsResource:
        from .resources.ai_chats import AsyncAIChatsResource

        return AsyncAIChatsResource(self)

    @cached_property
    def dm_channels(self) -> AsyncDmChannelsResource:
        from .resources.dm_channels import AsyncDmChannelsResource

        return AsyncDmChannelsResource(self)

    @cached_property
    def dispute_alerts(self) -> AsyncDisputeAlertsResource:
        """
        A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

        Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
        """
        from .resources.dispute_alerts import AsyncDisputeAlertsResource

        return AsyncDisputeAlertsResource(self)

    @cached_property
    def resolution_center_cases(self) -> AsyncResolutionCenterCasesResource:
        """
        A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

        Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
        """
        from .resources.resolution_center_cases import AsyncResolutionCenterCasesResource

        return AsyncResolutionCenterCasesResource(self)

    @cached_property
    def payout_accounts(self) -> AsyncPayoutAccountsResource:
        from .resources.payout_accounts import AsyncPayoutAccountsResource

        return AsyncPayoutAccountsResource(self)

    @cached_property
    def affiliates(self) -> AsyncAffiliatesResource:
        from .resources.affiliates import AsyncAffiliatesResource

        return AsyncAffiliatesResource(self)

    @cached_property
    def bounties(self) -> AsyncBountiesResource:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        from .resources.bounties import AsyncBountiesResource

        return AsyncBountiesResource(self)

    @cached_property
    def bounty_submissions(self) -> AsyncBountySubmissionsResource:
        """A Bounty Submission is one worker's attempt on a bounty.

        It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

        Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
        """
        from .resources.bounty_submissions import AsyncBountySubmissionsResource

        return AsyncBountySubmissionsResource(self)

    @cached_property
    def ad_campaigns(self) -> AsyncAdCampaignsResource:
        """An Ad Campaign is the top-level container for paid ads on an ad network.

        It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

        Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
        """
        from .resources.ad_campaigns import AsyncAdCampaignsResource

        return AsyncAdCampaignsResource(self)

    @cached_property
    def ad_groups(self) -> AsyncAdGroupsResource:
        """
        An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

        Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
        """
        from .resources.ad_groups import AsyncAdGroupsResource

        return AsyncAdGroupsResource(self)

    @cached_property
    def ads(self) -> AsyncAdsResource:
        """
        An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

        Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
        """
        from .resources.ads import AsyncAdsResource

        return AsyncAdsResource(self)

    @cached_property
    def ad_reports(self) -> AsyncAdReportsResource:
        from .resources.ad_reports import AsyncAdReportsResource

        return AsyncAdReportsResource(self)

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
            "Api-Version-Date": self.version if self.version is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        app_id: str | None = None,
        version: str | None = None,
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
            version=version or self.version,
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
        """An App is software you build on Whop.

        It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

        Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
        """
        from .resources.apps import AppsResourceWithRawResponse

        return AppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        """An API Key is a programmatic credential owned by an account or app.

        Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

        Use the API Keys API to list an account or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
        """
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def permissions(self) -> permissions.PermissionsResourceWithRawResponse:
        """
        A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

        Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
        """
        from .resources.permissions import PermissionsResourceWithRawResponse

        return PermissionsResourceWithRawResponse(self._client.permissions)

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
        """A Product is a digital good or service sold on Whop.

        Products may contain plans for pricing and/or experiences for content delivery.

        Use the Products API to create products, list products visible to your credentials, retrieve product details, update product metadata or merchandising fields, and delete products that should no longer be sold.
        """
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def social_accounts(self) -> social_accounts.SocialAccountsResourceWithRawResponse:
        """
        A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

        Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts or a Facebook page's lead forms.
        """
        from .resources.social_accounts import SocialAccountsResourceWithRawResponse

        return SocialAccountsResourceWithRawResponse(self._client.social_accounts)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithRawResponse:
        """An Audience represents a customer list uploaded to Whop for ad targeting.

        Audiences belong to an account and sync to supported ad platforms as custom audiences.

        Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
        """
        from .resources.audiences import AudiencesResourceWithRawResponse

        return AudiencesResourceWithRawResponse(self._client.audiences)

    @cached_property
    def media(self) -> media.MediaResourceWithRawResponse:
        """
        A Media Asset is an AI-generated image or video created from a prompt and billed from an account balance. When generation finishes, the asset includes a file that can be attached anywhere Whop accepts files.

        Use the Media API to start a generation job and retrieve the asset while it processes or after it is ready.
        """
        from .resources.media import MediaResourceWithRawResponse

        return MediaResourceWithRawResponse(self._client.media)

    @cached_property
    def people(self) -> people.PeopleResourceWithRawResponse:
        """
        A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

        Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
        """
        from .resources.people import PeopleResourceWithRawResponse

        return PeopleResourceWithRawResponse(self._client.people)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        """
        An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

        Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person. The resource also exposes an anonymized read mode — the pulse feed — a platform-wide snapshot of recent purchases that carries nothing identifying. The pulse feed is public; other Events endpoints require authentication and are scoped to an account.

        Events are only as good as the pixel sending them, so [Validate Pixel](/api-reference/beta/events/validate-pixel) answers whether an account's pixel is working: it reads the events the pixel has sent, and when you pass a `url` whose page hasn't sent any lately, it fetches that page and looks for the pixel in its source. Use it before launching an ad to confirm its destination is tracked, or in a setup flow to tell a merchant whether their install is live.
        """
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithRawResponse:
        from .resources.companies import CompaniesResourceWithRawResponse

        return CompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.PlansResourceWithRawResponse:
        """A Plan defines how customers buy a product.

        It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

        Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
        """
        from .resources.plans import PlansResourceWithRawResponse

        return PlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def exports(self) -> exports.ExportsResourceWithRawResponse:
        """
        An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

        Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
        """
        from .resources.exports import ExportsResourceWithRawResponse

        return ExportsResourceWithRawResponse(self._client.exports)

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
        """Transfers move value between identities on Whop.

        They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

        Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
        """
        from .resources.transfers import TransfersResourceWithRawResponse

        return TransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsResourceWithRawResponse:
        from .resources.ledger_accounts import LedgerAccountsResourceWithRawResponse

        return LedgerAccountsResourceWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithRawResponse:
        """
        A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

        Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, invite a recipient to join through a free plan, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, generate a transfer link, and update metadata.
        """
        from .resources.memberships import MembershipsResourceWithRawResponse

        return MembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AuthorizedUsersResourceWithRawResponse:
        from .resources.authorized_users import AuthorizedUsersResourceWithRawResponse

        return AuthorizedUsersResourceWithRawResponse(self._client.authorized_users)

    @cached_property
    def team_members(self) -> team_members.TeamMembersResourceWithRawResponse:
        """
        A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

        Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
        """
        from .resources.team_members import TeamMembersResourceWithRawResponse

        return TeamMembersResourceWithRawResponse(self._client.team_members)

    @cached_property
    def app_builds(self) -> app_builds.AppBuildsResourceWithRawResponse:
        """
        An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

        Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
        """
        from .resources.app_builds import AppBuildsResourceWithRawResponse

        return AppBuildsResourceWithRawResponse(self._client.app_builds)

    @cached_property
    def app_deployments(self) -> app_deployments.AppDeploymentsResourceWithRawResponse:
        """A Deployment builds an app's current source and ships it, producing an App Build.

        It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

        Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
        """
        from .resources.app_deployments import AppDeploymentsResourceWithRawResponse

        return AppDeploymentsResourceWithRawResponse(self._client.app_deployments)

    @cached_property
    def shipments(self) -> shipments.ShipmentsResourceWithRawResponse:
        """
        A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

        Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
        """
        from .resources.shipments import ShipmentsResourceWithRawResponse

        return ShipmentsResourceWithRawResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.CheckoutConfigurationsResourceWithRawResponse:
        """A Checkout Configuration is a reusable checkout link owned by an account.

        In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

        Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
        """
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
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        """A Payment is one charge against a buyer.

        Create it with a payment method already on file, or with a `confirmation_token` describing a method the buyer has just supplied.

        Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
        """
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
        """
        A Member is one buyer's relationship with an account — one record per customer regardless of how many memberships they hold. It carries relationship-level state: whether they have joined or left, their access level (`customer`, `admin`, or `no_access`), when they joined, and when they last opened the account's content.

        Use the Members API to list an account's members with filtering by access level, status, join date, and name or username search, and to retrieve a single member. Member rows are created and maintained by the membership lifecycle; to grant or revoke access, work with memberships instead.
        """
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
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithRawResponse:
        """
        A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

        Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
        """
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
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def financial_activity(self) -> financial_activity.FinancialActivityResourceWithRawResponse:
        """
        A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

        Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
        """
        from .resources.financial_activity import FinancialActivityResourceWithRawResponse

        return FinancialActivityResourceWithRawResponse(self._client.financial_activity)

    @cached_property
    def stats(self) -> stats.StatsResourceWithRawResponse:
        """Stats represent aggregated activity for an account over time.

        They help you understand revenue, transactions, disputes, members, referrals, and advertising performance across reporting periods like days, weeks, or months.

        Use the Stats API to list available metrics and their filterable properties, then retrieve time-series values for a date range.
        """
        from .resources.stats import StatsResourceWithRawResponse

        return StatsResourceWithRawResponse(self._client.stats)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        from .resources.payouts import PayoutsResourceWithRawResponse

        return PayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def partners(self) -> partners.PartnersResourceWithRawResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        from .resources.partners import PartnersResourceWithRawResponse

        return PartnersResourceWithRawResponse(self._client.partners)

    @cached_property
    def cards(self) -> cards.CardsResourceWithRawResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.cards import CardsResourceWithRawResponse

        return CardsResourceWithRawResponse(self._client.cards)

    @cached_property
    def card_transactions(self) -> card_transactions.CardTransactionsResourceWithRawResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.card_transactions import CardTransactionsResourceWithRawResponse

        return CardTransactionsResourceWithRawResponse(self._client.card_transactions)

    @cached_property
    def swaps(self) -> swaps.SwapsResourceWithRawResponse:
        """
        Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

        Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
        """
        from .resources.swaps import SwapsResourceWithRawResponse

        return SwapsResourceWithRawResponse(self._client.swaps)

    @cached_property
    def deposits(self) -> deposits.DepositsResourceWithRawResponse:
        """
        Deposits describe ways to add funds to an account balance, including hosted deposit pages, bank deposit instructions, and supported crypto wallet addresses.

        Use the Deposits API to create deposit instructions for an account.
        """
        from .resources.deposits import DepositsResourceWithRawResponse

        return DepositsResourceWithRawResponse(self._client.deposits)

    @cached_property
    def recommended_actions(self) -> recommended_actions.RecommendedActionsResourceWithRawResponse:
        """
        A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

        Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
        """
        from .resources.recommended_actions import RecommendedActionsResourceWithRawResponse

        return RecommendedActionsResourceWithRawResponse(self._client.recommended_actions)

    @cached_property
    def setup_intents(self) -> setup_intents.SetupIntentsResourceWithRawResponse:
        from .resources.setup_intents import SetupIntentsResourceWithRawResponse

        return SetupIntentsResourceWithRawResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.PaymentMethodsResourceWithRawResponse:
        from .resources.payment_methods import PaymentMethodsResourceWithRawResponse

        return PaymentMethodsResourceWithRawResponse(self._client.payment_methods)

    @cached_property
    def payment_method_domains(self) -> payment_method_domains.PaymentMethodDomainsResourceWithRawResponse:
        """
        A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

        Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
        """
        from .resources.payment_method_domains import PaymentMethodDomainsResourceWithRawResponse

        return PaymentMethodDomainsResourceWithRawResponse(self._client.payment_method_domains)

    @cached_property
    def fee_markups(self) -> fee_markups.FeeMarkupsResourceWithRawResponse:
        from .resources.fee_markups import FeeMarkupsResourceWithRawResponse

        return FeeMarkupsResourceWithRawResponse(self._client.fee_markups)

    @cached_property
    def verifications(self) -> verifications.VerificationsResourceWithRawResponse:
        """A Verification represents a legal identity for a person or business.

        Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

        Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
        """
        from .resources.verifications import VerificationsResourceWithRawResponse

        return VerificationsResourceWithRawResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.LeadsResourceWithRawResponse:
        from .resources.leads import LeadsResourceWithRawResponse

        return LeadsResourceWithRawResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.TopupsResourceWithRawResponse:
        from .resources.topups import TopupsResourceWithRawResponse

        return TopupsResourceWithRawResponse(self._client.topups)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def company_token_transactions(self) -> company_token_transactions.CompanyTokenTransactionsResourceWithRawResponse:
        from .resources.company_token_transactions import CompanyTokenTransactionsResourceWithRawResponse

        return CompanyTokenTransactionsResourceWithRawResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.DmMembersResourceWithRawResponse:
        from .resources.dm_members import DmMembersResourceWithRawResponse

        return DmMembersResourceWithRawResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AIChatsResourceWithRawResponse:
        from .resources.ai_chats import AIChatsResourceWithRawResponse

        return AIChatsResourceWithRawResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.DmChannelsResourceWithRawResponse:
        from .resources.dm_channels import DmChannelsResourceWithRawResponse

        return DmChannelsResourceWithRawResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.DisputeAlertsResourceWithRawResponse:
        """
        A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

        Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
        """
        from .resources.dispute_alerts import DisputeAlertsResourceWithRawResponse

        return DisputeAlertsResourceWithRawResponse(self._client.dispute_alerts)

    @cached_property
    def resolution_center_cases(self) -> resolution_center_cases.ResolutionCenterCasesResourceWithRawResponse:
        """
        A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

        Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
        """
        from .resources.resolution_center_cases import ResolutionCenterCasesResourceWithRawResponse

        return ResolutionCenterCasesResourceWithRawResponse(self._client.resolution_center_cases)

    @cached_property
    def payout_accounts(self) -> payout_accounts.PayoutAccountsResourceWithRawResponse:
        from .resources.payout_accounts import PayoutAccountsResourceWithRawResponse

        return PayoutAccountsResourceWithRawResponse(self._client.payout_accounts)

    @cached_property
    def affiliates(self) -> affiliates.AffiliatesResourceWithRawResponse:
        from .resources.affiliates import AffiliatesResourceWithRawResponse

        return AffiliatesResourceWithRawResponse(self._client.affiliates)

    @cached_property
    def bounties(self) -> bounties.BountiesResourceWithRawResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        from .resources.bounties import BountiesResourceWithRawResponse

        return BountiesResourceWithRawResponse(self._client.bounties)

    @cached_property
    def bounty_submissions(self) -> bounty_submissions.BountySubmissionsResourceWithRawResponse:
        """A Bounty Submission is one worker's attempt on a bounty.

        It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

        Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
        """
        from .resources.bounty_submissions import BountySubmissionsResourceWithRawResponse

        return BountySubmissionsResourceWithRawResponse(self._client.bounty_submissions)

    @cached_property
    def ad_campaigns(self) -> ad_campaigns.AdCampaignsResourceWithRawResponse:
        """An Ad Campaign is the top-level container for paid ads on an ad network.

        It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

        Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
        """
        from .resources.ad_campaigns import AdCampaignsResourceWithRawResponse

        return AdCampaignsResourceWithRawResponse(self._client.ad_campaigns)

    @cached_property
    def ad_groups(self) -> ad_groups.AdGroupsResourceWithRawResponse:
        """
        An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

        Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
        """
        from .resources.ad_groups import AdGroupsResourceWithRawResponse

        return AdGroupsResourceWithRawResponse(self._client.ad_groups)

    @cached_property
    def ads(self) -> ads.AdsResourceWithRawResponse:
        """
        An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

        Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
        """
        from .resources.ads import AdsResourceWithRawResponse

        return AdsResourceWithRawResponse(self._client.ads)

    @cached_property
    def ad_reports(self) -> ad_reports.AdReportsResourceWithRawResponse:
        from .resources.ad_reports import AdReportsResourceWithRawResponse

        return AdReportsResourceWithRawResponse(self._client.ad_reports)


class AsyncWhopWithRawResponse:
    _client: AsyncWhop

    def __init__(self, client: AsyncWhop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithRawResponse:
        """An App is software you build on Whop.

        It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

        Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
        """
        from .resources.apps import AsyncAppsResourceWithRawResponse

        return AsyncAppsResourceWithRawResponse(self._client.apps)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        """An API Key is a programmatic credential owned by an account or app.

        Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

        Use the API Keys API to list an account or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
        """
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def permissions(self) -> permissions.AsyncPermissionsResourceWithRawResponse:
        """
        A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

        Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
        """
        from .resources.permissions import AsyncPermissionsResourceWithRawResponse

        return AsyncPermissionsResourceWithRawResponse(self._client.permissions)

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
        """A Product is a digital good or service sold on Whop.

        Products may contain plans for pricing and/or experiences for content delivery.

        Use the Products API to create products, list products visible to your credentials, retrieve product details, update product metadata or merchandising fields, and delete products that should no longer be sold.
        """
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def social_accounts(self) -> social_accounts.AsyncSocialAccountsResourceWithRawResponse:
        """
        A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

        Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts or a Facebook page's lead forms.
        """
        from .resources.social_accounts import AsyncSocialAccountsResourceWithRawResponse

        return AsyncSocialAccountsResourceWithRawResponse(self._client.social_accounts)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithRawResponse:
        """An Audience represents a customer list uploaded to Whop for ad targeting.

        Audiences belong to an account and sync to supported ad platforms as custom audiences.

        Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
        """
        from .resources.audiences import AsyncAudiencesResourceWithRawResponse

        return AsyncAudiencesResourceWithRawResponse(self._client.audiences)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithRawResponse:
        """
        A Media Asset is an AI-generated image or video created from a prompt and billed from an account balance. When generation finishes, the asset includes a file that can be attached anywhere Whop accepts files.

        Use the Media API to start a generation job and retrieve the asset while it processes or after it is ready.
        """
        from .resources.media import AsyncMediaResourceWithRawResponse

        return AsyncMediaResourceWithRawResponse(self._client.media)

    @cached_property
    def people(self) -> people.AsyncPeopleResourceWithRawResponse:
        """
        A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

        Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
        """
        from .resources.people import AsyncPeopleResourceWithRawResponse

        return AsyncPeopleResourceWithRawResponse(self._client.people)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        """
        An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

        Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person. The resource also exposes an anonymized read mode — the pulse feed — a platform-wide snapshot of recent purchases that carries nothing identifying. The pulse feed is public; other Events endpoints require authentication and are scoped to an account.

        Events are only as good as the pixel sending them, so [Validate Pixel](/api-reference/beta/events/validate-pixel) answers whether an account's pixel is working: it reads the events the pixel has sent, and when you pass a `url` whose page hasn't sent any lately, it fetches that page and looks for the pixel in its source. Use it before launching an ad to confirm its destination is tracked, or in a setup flow to tell a merchant whether their install is live.
        """
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithRawResponse:
        from .resources.companies import AsyncCompaniesResourceWithRawResponse

        return AsyncCompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithRawResponse:
        """A Plan defines how customers buy a product.

        It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

        Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
        """
        from .resources.plans import AsyncPlansResourceWithRawResponse

        return AsyncPlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def exports(self) -> exports.AsyncExportsResourceWithRawResponse:
        """
        An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

        Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
        """
        from .resources.exports import AsyncExportsResourceWithRawResponse

        return AsyncExportsResourceWithRawResponse(self._client.exports)

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
        """Transfers move value between identities on Whop.

        They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

        Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
        """
        from .resources.transfers import AsyncTransfersResourceWithRawResponse

        return AsyncTransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsResourceWithRawResponse:
        from .resources.ledger_accounts import AsyncLedgerAccountsResourceWithRawResponse

        return AsyncLedgerAccountsResourceWithRawResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithRawResponse:
        """
        A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

        Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, invite a recipient to join through a free plan, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, generate a transfer link, and update metadata.
        """
        from .resources.memberships import AsyncMembershipsResourceWithRawResponse

        return AsyncMembershipsResourceWithRawResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AsyncAuthorizedUsersResourceWithRawResponse:
        from .resources.authorized_users import AsyncAuthorizedUsersResourceWithRawResponse

        return AsyncAuthorizedUsersResourceWithRawResponse(self._client.authorized_users)

    @cached_property
    def team_members(self) -> team_members.AsyncTeamMembersResourceWithRawResponse:
        """
        A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

        Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
        """
        from .resources.team_members import AsyncTeamMembersResourceWithRawResponse

        return AsyncTeamMembersResourceWithRawResponse(self._client.team_members)

    @cached_property
    def app_builds(self) -> app_builds.AsyncAppBuildsResourceWithRawResponse:
        """
        An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

        Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
        """
        from .resources.app_builds import AsyncAppBuildsResourceWithRawResponse

        return AsyncAppBuildsResourceWithRawResponse(self._client.app_builds)

    @cached_property
    def app_deployments(self) -> app_deployments.AsyncAppDeploymentsResourceWithRawResponse:
        """A Deployment builds an app's current source and ships it, producing an App Build.

        It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

        Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
        """
        from .resources.app_deployments import AsyncAppDeploymentsResourceWithRawResponse

        return AsyncAppDeploymentsResourceWithRawResponse(self._client.app_deployments)

    @cached_property
    def shipments(self) -> shipments.AsyncShipmentsResourceWithRawResponse:
        """
        A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

        Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
        """
        from .resources.shipments import AsyncShipmentsResourceWithRawResponse

        return AsyncShipmentsResourceWithRawResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.AsyncCheckoutConfigurationsResourceWithRawResponse:
        """A Checkout Configuration is a reusable checkout link owned by an account.

        In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

        Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
        """
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
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        """A Payment is one charge against a buyer.

        Create it with a payment method already on file, or with a `confirmation_token` describing a method the buyer has just supplied.

        Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
        """
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
        """
        A Member is one buyer's relationship with an account — one record per customer regardless of how many memberships they hold. It carries relationship-level state: whether they have joined or left, their access level (`customer`, `admin`, or `no_access`), when they joined, and when they last opened the account's content.

        Use the Members API to list an account's members with filtering by access level, status, join date, and name or username search, and to retrieve a single member. Member rows are created and maintained by the membership lifecycle; to grant or revoke access, work with memberships instead.
        """
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
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithRawResponse:
        """
        A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

        Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
        """
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
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def financial_activity(self) -> financial_activity.AsyncFinancialActivityResourceWithRawResponse:
        """
        A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

        Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
        """
        from .resources.financial_activity import AsyncFinancialActivityResourceWithRawResponse

        return AsyncFinancialActivityResourceWithRawResponse(self._client.financial_activity)

    @cached_property
    def stats(self) -> stats.AsyncStatsResourceWithRawResponse:
        """Stats represent aggregated activity for an account over time.

        They help you understand revenue, transactions, disputes, members, referrals, and advertising performance across reporting periods like days, weeks, or months.

        Use the Stats API to list available metrics and their filterable properties, then retrieve time-series values for a date range.
        """
        from .resources.stats import AsyncStatsResourceWithRawResponse

        return AsyncStatsResourceWithRawResponse(self._client.stats)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithRawResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        from .resources.payouts import AsyncPayoutsResourceWithRawResponse

        return AsyncPayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def partners(self) -> partners.AsyncPartnersResourceWithRawResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        from .resources.partners import AsyncPartnersResourceWithRawResponse

        return AsyncPartnersResourceWithRawResponse(self._client.partners)

    @cached_property
    def cards(self) -> cards.AsyncCardsResourceWithRawResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.cards import AsyncCardsResourceWithRawResponse

        return AsyncCardsResourceWithRawResponse(self._client.cards)

    @cached_property
    def card_transactions(self) -> card_transactions.AsyncCardTransactionsResourceWithRawResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.card_transactions import AsyncCardTransactionsResourceWithRawResponse

        return AsyncCardTransactionsResourceWithRawResponse(self._client.card_transactions)

    @cached_property
    def swaps(self) -> swaps.AsyncSwapsResourceWithRawResponse:
        """
        Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

        Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
        """
        from .resources.swaps import AsyncSwapsResourceWithRawResponse

        return AsyncSwapsResourceWithRawResponse(self._client.swaps)

    @cached_property
    def deposits(self) -> deposits.AsyncDepositsResourceWithRawResponse:
        """
        Deposits describe ways to add funds to an account balance, including hosted deposit pages, bank deposit instructions, and supported crypto wallet addresses.

        Use the Deposits API to create deposit instructions for an account.
        """
        from .resources.deposits import AsyncDepositsResourceWithRawResponse

        return AsyncDepositsResourceWithRawResponse(self._client.deposits)

    @cached_property
    def recommended_actions(self) -> recommended_actions.AsyncRecommendedActionsResourceWithRawResponse:
        """
        A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

        Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
        """
        from .resources.recommended_actions import AsyncRecommendedActionsResourceWithRawResponse

        return AsyncRecommendedActionsResourceWithRawResponse(self._client.recommended_actions)

    @cached_property
    def setup_intents(self) -> setup_intents.AsyncSetupIntentsResourceWithRawResponse:
        from .resources.setup_intents import AsyncSetupIntentsResourceWithRawResponse

        return AsyncSetupIntentsResourceWithRawResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.AsyncPaymentMethodsResourceWithRawResponse:
        from .resources.payment_methods import AsyncPaymentMethodsResourceWithRawResponse

        return AsyncPaymentMethodsResourceWithRawResponse(self._client.payment_methods)

    @cached_property
    def payment_method_domains(self) -> payment_method_domains.AsyncPaymentMethodDomainsResourceWithRawResponse:
        """
        A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

        Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
        """
        from .resources.payment_method_domains import AsyncPaymentMethodDomainsResourceWithRawResponse

        return AsyncPaymentMethodDomainsResourceWithRawResponse(self._client.payment_method_domains)

    @cached_property
    def fee_markups(self) -> fee_markups.AsyncFeeMarkupsResourceWithRawResponse:
        from .resources.fee_markups import AsyncFeeMarkupsResourceWithRawResponse

        return AsyncFeeMarkupsResourceWithRawResponse(self._client.fee_markups)

    @cached_property
    def verifications(self) -> verifications.AsyncVerificationsResourceWithRawResponse:
        """A Verification represents a legal identity for a person or business.

        Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

        Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
        """
        from .resources.verifications import AsyncVerificationsResourceWithRawResponse

        return AsyncVerificationsResourceWithRawResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.AsyncLeadsResourceWithRawResponse:
        from .resources.leads import AsyncLeadsResourceWithRawResponse

        return AsyncLeadsResourceWithRawResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.AsyncTopupsResourceWithRawResponse:
        from .resources.topups import AsyncTopupsResourceWithRawResponse

        return AsyncTopupsResourceWithRawResponse(self._client.topups)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def company_token_transactions(
        self,
    ) -> company_token_transactions.AsyncCompanyTokenTransactionsResourceWithRawResponse:
        from .resources.company_token_transactions import AsyncCompanyTokenTransactionsResourceWithRawResponse

        return AsyncCompanyTokenTransactionsResourceWithRawResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.AsyncDmMembersResourceWithRawResponse:
        from .resources.dm_members import AsyncDmMembersResourceWithRawResponse

        return AsyncDmMembersResourceWithRawResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AsyncAIChatsResourceWithRawResponse:
        from .resources.ai_chats import AsyncAIChatsResourceWithRawResponse

        return AsyncAIChatsResourceWithRawResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.AsyncDmChannelsResourceWithRawResponse:
        from .resources.dm_channels import AsyncDmChannelsResourceWithRawResponse

        return AsyncDmChannelsResourceWithRawResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.AsyncDisputeAlertsResourceWithRawResponse:
        """
        A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

        Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
        """
        from .resources.dispute_alerts import AsyncDisputeAlertsResourceWithRawResponse

        return AsyncDisputeAlertsResourceWithRawResponse(self._client.dispute_alerts)

    @cached_property
    def resolution_center_cases(self) -> resolution_center_cases.AsyncResolutionCenterCasesResourceWithRawResponse:
        """
        A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

        Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
        """
        from .resources.resolution_center_cases import AsyncResolutionCenterCasesResourceWithRawResponse

        return AsyncResolutionCenterCasesResourceWithRawResponse(self._client.resolution_center_cases)

    @cached_property
    def payout_accounts(self) -> payout_accounts.AsyncPayoutAccountsResourceWithRawResponse:
        from .resources.payout_accounts import AsyncPayoutAccountsResourceWithRawResponse

        return AsyncPayoutAccountsResourceWithRawResponse(self._client.payout_accounts)

    @cached_property
    def affiliates(self) -> affiliates.AsyncAffiliatesResourceWithRawResponse:
        from .resources.affiliates import AsyncAffiliatesResourceWithRawResponse

        return AsyncAffiliatesResourceWithRawResponse(self._client.affiliates)

    @cached_property
    def bounties(self) -> bounties.AsyncBountiesResourceWithRawResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        from .resources.bounties import AsyncBountiesResourceWithRawResponse

        return AsyncBountiesResourceWithRawResponse(self._client.bounties)

    @cached_property
    def bounty_submissions(self) -> bounty_submissions.AsyncBountySubmissionsResourceWithRawResponse:
        """A Bounty Submission is one worker's attempt on a bounty.

        It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

        Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
        """
        from .resources.bounty_submissions import AsyncBountySubmissionsResourceWithRawResponse

        return AsyncBountySubmissionsResourceWithRawResponse(self._client.bounty_submissions)

    @cached_property
    def ad_campaigns(self) -> ad_campaigns.AsyncAdCampaignsResourceWithRawResponse:
        """An Ad Campaign is the top-level container for paid ads on an ad network.

        It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

        Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
        """
        from .resources.ad_campaigns import AsyncAdCampaignsResourceWithRawResponse

        return AsyncAdCampaignsResourceWithRawResponse(self._client.ad_campaigns)

    @cached_property
    def ad_groups(self) -> ad_groups.AsyncAdGroupsResourceWithRawResponse:
        """
        An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

        Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
        """
        from .resources.ad_groups import AsyncAdGroupsResourceWithRawResponse

        return AsyncAdGroupsResourceWithRawResponse(self._client.ad_groups)

    @cached_property
    def ads(self) -> ads.AsyncAdsResourceWithRawResponse:
        """
        An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

        Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
        """
        from .resources.ads import AsyncAdsResourceWithRawResponse

        return AsyncAdsResourceWithRawResponse(self._client.ads)

    @cached_property
    def ad_reports(self) -> ad_reports.AsyncAdReportsResourceWithRawResponse:
        from .resources.ad_reports import AsyncAdReportsResourceWithRawResponse

        return AsyncAdReportsResourceWithRawResponse(self._client.ad_reports)


class WhopWithStreamedResponse:
    _client: Whop

    def __init__(self, client: Whop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AppsResourceWithStreamingResponse:
        """An App is software you build on Whop.

        It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

        Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
        """
        from .resources.apps import AppsResourceWithStreamingResponse

        return AppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        """An API Key is a programmatic credential owned by an account or app.

        Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

        Use the API Keys API to list an account or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
        """
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def permissions(self) -> permissions.PermissionsResourceWithStreamingResponse:
        """
        A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

        Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
        """
        from .resources.permissions import PermissionsResourceWithStreamingResponse

        return PermissionsResourceWithStreamingResponse(self._client.permissions)

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
        """A Product is a digital good or service sold on Whop.

        Products may contain plans for pricing and/or experiences for content delivery.

        Use the Products API to create products, list products visible to your credentials, retrieve product details, update product metadata or merchandising fields, and delete products that should no longer be sold.
        """
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def social_accounts(self) -> social_accounts.SocialAccountsResourceWithStreamingResponse:
        """
        A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

        Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts or a Facebook page's lead forms.
        """
        from .resources.social_accounts import SocialAccountsResourceWithStreamingResponse

        return SocialAccountsResourceWithStreamingResponse(self._client.social_accounts)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithStreamingResponse:
        """An Audience represents a customer list uploaded to Whop for ad targeting.

        Audiences belong to an account and sync to supported ad platforms as custom audiences.

        Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
        """
        from .resources.audiences import AudiencesResourceWithStreamingResponse

        return AudiencesResourceWithStreamingResponse(self._client.audiences)

    @cached_property
    def media(self) -> media.MediaResourceWithStreamingResponse:
        """
        A Media Asset is an AI-generated image or video created from a prompt and billed from an account balance. When generation finishes, the asset includes a file that can be attached anywhere Whop accepts files.

        Use the Media API to start a generation job and retrieve the asset while it processes or after it is ready.
        """
        from .resources.media import MediaResourceWithStreamingResponse

        return MediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def people(self) -> people.PeopleResourceWithStreamingResponse:
        """
        A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

        Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
        """
        from .resources.people import PeopleResourceWithStreamingResponse

        return PeopleResourceWithStreamingResponse(self._client.people)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        """
        An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

        Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person. The resource also exposes an anonymized read mode — the pulse feed — a platform-wide snapshot of recent purchases that carries nothing identifying. The pulse feed is public; other Events endpoints require authentication and are scoped to an account.

        Events are only as good as the pixel sending them, so [Validate Pixel](/api-reference/beta/events/validate-pixel) answers whether an account's pixel is working: it reads the events the pixel has sent, and when you pass a `url` whose page hasn't sent any lately, it fetches that page and looks for the pixel in its source. Use it before launching an ad to confirm its destination is tracked, or in a setup flow to tell a merchant whether their install is live.
        """
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithStreamingResponse:
        from .resources.companies import CompaniesResourceWithStreamingResponse

        return CompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.PlansResourceWithStreamingResponse:
        """A Plan defines how customers buy a product.

        It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

        Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
        """
        from .resources.plans import PlansResourceWithStreamingResponse

        return PlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def exports(self) -> exports.ExportsResourceWithStreamingResponse:
        """
        An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

        Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
        """
        from .resources.exports import ExportsResourceWithStreamingResponse

        return ExportsResourceWithStreamingResponse(self._client.exports)

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
        """Transfers move value between identities on Whop.

        They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

        Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
        """
        from .resources.transfers import TransfersResourceWithStreamingResponse

        return TransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.LedgerAccountsResourceWithStreamingResponse:
        from .resources.ledger_accounts import LedgerAccountsResourceWithStreamingResponse

        return LedgerAccountsResourceWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.MembershipsResourceWithStreamingResponse:
        """
        A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

        Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, invite a recipient to join through a free plan, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, generate a transfer link, and update metadata.
        """
        from .resources.memberships import MembershipsResourceWithStreamingResponse

        return MembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AuthorizedUsersResourceWithStreamingResponse:
        from .resources.authorized_users import AuthorizedUsersResourceWithStreamingResponse

        return AuthorizedUsersResourceWithStreamingResponse(self._client.authorized_users)

    @cached_property
    def team_members(self) -> team_members.TeamMembersResourceWithStreamingResponse:
        """
        A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

        Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
        """
        from .resources.team_members import TeamMembersResourceWithStreamingResponse

        return TeamMembersResourceWithStreamingResponse(self._client.team_members)

    @cached_property
    def app_builds(self) -> app_builds.AppBuildsResourceWithStreamingResponse:
        """
        An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

        Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
        """
        from .resources.app_builds import AppBuildsResourceWithStreamingResponse

        return AppBuildsResourceWithStreamingResponse(self._client.app_builds)

    @cached_property
    def app_deployments(self) -> app_deployments.AppDeploymentsResourceWithStreamingResponse:
        """A Deployment builds an app's current source and ships it, producing an App Build.

        It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

        Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
        """
        from .resources.app_deployments import AppDeploymentsResourceWithStreamingResponse

        return AppDeploymentsResourceWithStreamingResponse(self._client.app_deployments)

    @cached_property
    def shipments(self) -> shipments.ShipmentsResourceWithStreamingResponse:
        """
        A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

        Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
        """
        from .resources.shipments import ShipmentsResourceWithStreamingResponse

        return ShipmentsResourceWithStreamingResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(self) -> checkout_configurations.CheckoutConfigurationsResourceWithStreamingResponse:
        """A Checkout Configuration is a reusable checkout link owned by an account.

        In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

        Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
        """
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
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        """A Payment is one charge against a buyer.

        Create it with a payment method already on file, or with a `confirmation_token` describing a method the buyer has just supplied.

        Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
        """
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
        """
        A Member is one buyer's relationship with an account — one record per customer regardless of how many memberships they hold. It carries relationship-level state: whether they have joined or left, their access level (`customer`, `admin`, or `no_access`), when they joined, and when they last opened the account's content.

        Use the Members API to list an account's members with filtering by access level, status, join date, and name or username search, and to retrieve a single member. Member rows are created and maintained by the membership lifecycle; to grant or revoke access, work with memberships instead.
        """
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
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithStreamingResponse:
        """
        A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

        Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
        """
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
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def financial_activity(self) -> financial_activity.FinancialActivityResourceWithStreamingResponse:
        """
        A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

        Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
        """
        from .resources.financial_activity import FinancialActivityResourceWithStreamingResponse

        return FinancialActivityResourceWithStreamingResponse(self._client.financial_activity)

    @cached_property
    def stats(self) -> stats.StatsResourceWithStreamingResponse:
        """Stats represent aggregated activity for an account over time.

        They help you understand revenue, transactions, disputes, members, referrals, and advertising performance across reporting periods like days, weeks, or months.

        Use the Stats API to list available metrics and their filterable properties, then retrieve time-series values for a date range.
        """
        from .resources.stats import StatsResourceWithStreamingResponse

        return StatsResourceWithStreamingResponse(self._client.stats)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        from .resources.payouts import PayoutsResourceWithStreamingResponse

        return PayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def partners(self) -> partners.PartnersResourceWithStreamingResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        from .resources.partners import PartnersResourceWithStreamingResponse

        return PartnersResourceWithStreamingResponse(self._client.partners)

    @cached_property
    def cards(self) -> cards.CardsResourceWithStreamingResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.cards import CardsResourceWithStreamingResponse

        return CardsResourceWithStreamingResponse(self._client.cards)

    @cached_property
    def card_transactions(self) -> card_transactions.CardTransactionsResourceWithStreamingResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.card_transactions import CardTransactionsResourceWithStreamingResponse

        return CardTransactionsResourceWithStreamingResponse(self._client.card_transactions)

    @cached_property
    def swaps(self) -> swaps.SwapsResourceWithStreamingResponse:
        """
        Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

        Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
        """
        from .resources.swaps import SwapsResourceWithStreamingResponse

        return SwapsResourceWithStreamingResponse(self._client.swaps)

    @cached_property
    def deposits(self) -> deposits.DepositsResourceWithStreamingResponse:
        """
        Deposits describe ways to add funds to an account balance, including hosted deposit pages, bank deposit instructions, and supported crypto wallet addresses.

        Use the Deposits API to create deposit instructions for an account.
        """
        from .resources.deposits import DepositsResourceWithStreamingResponse

        return DepositsResourceWithStreamingResponse(self._client.deposits)

    @cached_property
    def recommended_actions(self) -> recommended_actions.RecommendedActionsResourceWithStreamingResponse:
        """
        A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

        Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
        """
        from .resources.recommended_actions import RecommendedActionsResourceWithStreamingResponse

        return RecommendedActionsResourceWithStreamingResponse(self._client.recommended_actions)

    @cached_property
    def setup_intents(self) -> setup_intents.SetupIntentsResourceWithStreamingResponse:
        from .resources.setup_intents import SetupIntentsResourceWithStreamingResponse

        return SetupIntentsResourceWithStreamingResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.PaymentMethodsResourceWithStreamingResponse:
        from .resources.payment_methods import PaymentMethodsResourceWithStreamingResponse

        return PaymentMethodsResourceWithStreamingResponse(self._client.payment_methods)

    @cached_property
    def payment_method_domains(self) -> payment_method_domains.PaymentMethodDomainsResourceWithStreamingResponse:
        """
        A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

        Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
        """
        from .resources.payment_method_domains import PaymentMethodDomainsResourceWithStreamingResponse

        return PaymentMethodDomainsResourceWithStreamingResponse(self._client.payment_method_domains)

    @cached_property
    def fee_markups(self) -> fee_markups.FeeMarkupsResourceWithStreamingResponse:
        from .resources.fee_markups import FeeMarkupsResourceWithStreamingResponse

        return FeeMarkupsResourceWithStreamingResponse(self._client.fee_markups)

    @cached_property
    def verifications(self) -> verifications.VerificationsResourceWithStreamingResponse:
        """A Verification represents a legal identity for a person or business.

        Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

        Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
        """
        from .resources.verifications import VerificationsResourceWithStreamingResponse

        return VerificationsResourceWithStreamingResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.LeadsResourceWithStreamingResponse:
        from .resources.leads import LeadsResourceWithStreamingResponse

        return LeadsResourceWithStreamingResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.TopupsResourceWithStreamingResponse:
        from .resources.topups import TopupsResourceWithStreamingResponse

        return TopupsResourceWithStreamingResponse(self._client.topups)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def company_token_transactions(
        self,
    ) -> company_token_transactions.CompanyTokenTransactionsResourceWithStreamingResponse:
        from .resources.company_token_transactions import CompanyTokenTransactionsResourceWithStreamingResponse

        return CompanyTokenTransactionsResourceWithStreamingResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.DmMembersResourceWithStreamingResponse:
        from .resources.dm_members import DmMembersResourceWithStreamingResponse

        return DmMembersResourceWithStreamingResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AIChatsResourceWithStreamingResponse:
        from .resources.ai_chats import AIChatsResourceWithStreamingResponse

        return AIChatsResourceWithStreamingResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.DmChannelsResourceWithStreamingResponse:
        from .resources.dm_channels import DmChannelsResourceWithStreamingResponse

        return DmChannelsResourceWithStreamingResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.DisputeAlertsResourceWithStreamingResponse:
        """
        A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

        Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
        """
        from .resources.dispute_alerts import DisputeAlertsResourceWithStreamingResponse

        return DisputeAlertsResourceWithStreamingResponse(self._client.dispute_alerts)

    @cached_property
    def resolution_center_cases(self) -> resolution_center_cases.ResolutionCenterCasesResourceWithStreamingResponse:
        """
        A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

        Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
        """
        from .resources.resolution_center_cases import ResolutionCenterCasesResourceWithStreamingResponse

        return ResolutionCenterCasesResourceWithStreamingResponse(self._client.resolution_center_cases)

    @cached_property
    def payout_accounts(self) -> payout_accounts.PayoutAccountsResourceWithStreamingResponse:
        from .resources.payout_accounts import PayoutAccountsResourceWithStreamingResponse

        return PayoutAccountsResourceWithStreamingResponse(self._client.payout_accounts)

    @cached_property
    def affiliates(self) -> affiliates.AffiliatesResourceWithStreamingResponse:
        from .resources.affiliates import AffiliatesResourceWithStreamingResponse

        return AffiliatesResourceWithStreamingResponse(self._client.affiliates)

    @cached_property
    def bounties(self) -> bounties.BountiesResourceWithStreamingResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        from .resources.bounties import BountiesResourceWithStreamingResponse

        return BountiesResourceWithStreamingResponse(self._client.bounties)

    @cached_property
    def bounty_submissions(self) -> bounty_submissions.BountySubmissionsResourceWithStreamingResponse:
        """A Bounty Submission is one worker's attempt on a bounty.

        It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

        Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
        """
        from .resources.bounty_submissions import BountySubmissionsResourceWithStreamingResponse

        return BountySubmissionsResourceWithStreamingResponse(self._client.bounty_submissions)

    @cached_property
    def ad_campaigns(self) -> ad_campaigns.AdCampaignsResourceWithStreamingResponse:
        """An Ad Campaign is the top-level container for paid ads on an ad network.

        It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

        Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
        """
        from .resources.ad_campaigns import AdCampaignsResourceWithStreamingResponse

        return AdCampaignsResourceWithStreamingResponse(self._client.ad_campaigns)

    @cached_property
    def ad_groups(self) -> ad_groups.AdGroupsResourceWithStreamingResponse:
        """
        An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

        Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
        """
        from .resources.ad_groups import AdGroupsResourceWithStreamingResponse

        return AdGroupsResourceWithStreamingResponse(self._client.ad_groups)

    @cached_property
    def ads(self) -> ads.AdsResourceWithStreamingResponse:
        """
        An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

        Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
        """
        from .resources.ads import AdsResourceWithStreamingResponse

        return AdsResourceWithStreamingResponse(self._client.ads)

    @cached_property
    def ad_reports(self) -> ad_reports.AdReportsResourceWithStreamingResponse:
        from .resources.ad_reports import AdReportsResourceWithStreamingResponse

        return AdReportsResourceWithStreamingResponse(self._client.ad_reports)


class AsyncWhopWithStreamedResponse:
    _client: AsyncWhop

    def __init__(self, client: AsyncWhop) -> None:
        self._client = client

    @cached_property
    def apps(self) -> apps.AsyncAppsResourceWithStreamingResponse:
        """An App is software you build on Whop.

        It can be a hosted web app served at `<route>.whop.app` or an API integration installed as an experience, and it belongs to the account that owns its credentials, settings, builds, and runtime logs.

        Use the Apps API to manage app configuration and, for hosted apps, read server runtime logs for console output, uncaught exceptions, and failed requests. Logs are retained for 7 days and can be filtered by build, level, time window, and message text.
        """
        from .resources.apps import AsyncAppsResourceWithStreamingResponse

        return AsyncAppsResourceWithStreamingResponse(self._client.apps)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        """An API Key is a programmatic credential owned by an account or app.

        Each key carries its own permissions policy — explicit permission statements or an inherited system role — and can be restricted with an expiration date and an IP allowlist.

        Use the API Keys API to list an account or app's keys, create a key (the full secret is returned once, on creation), inspect a key's effective grants, update its name or restrictions, rotate its secret, and revoke it. These endpoints require a user session — they cannot be called with an API key.
        """
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def permissions(self) -> permissions.AsyncPermissionsResourceWithStreamingResponse:
        """
        A Permission is one action, such as `stats:read`, paired with whether your credential is granted it on a given resource. It answers for whatever you authenticated with, so you can decide what to show or attempt instead of discovering a `403`.

        Use the Permissions API to check an account, product, experience, or app, narrowing to the actions you care about. It reports only your own access — to manage who else can reach an account, use the Team Members API.
        """
        from .resources.permissions import AsyncPermissionsResourceWithStreamingResponse

        return AsyncPermissionsResourceWithStreamingResponse(self._client.permissions)

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
        """A Product is a digital good or service sold on Whop.

        Products may contain plans for pricing and/or experiences for content delivery.

        Use the Products API to create products, list products visible to your credentials, retrieve product details, update product metadata or merchandising fields, and delete products that should no longer be sold.
        """
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def social_accounts(self) -> social_accounts.AsyncSocialAccountsResourceWithStreamingResponse:
        """
        A Social Account represents an external profile connected to a Whop account or user, such as a Facebook page or Instagram account. Connecting a social account lets Whop run [ads](/api-reference/beta/ads/ad) under that profile's identity and promote its existing posts.

        Use the Social Accounts API to list connected accounts, create a Whop-managed Facebook page, start an OAuth connection, disconnect a social account, and list a connected profile's posts or a Facebook page's lead forms.
        """
        from .resources.social_accounts import AsyncSocialAccountsResourceWithStreamingResponse

        return AsyncSocialAccountsResourceWithStreamingResponse(self._client.social_accounts)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithStreamingResponse:
        """An Audience represents a customer list uploaded to Whop for ad targeting.

        Audiences belong to an account and sync to supported ad platforms as custom audiences.

        Use the Audiences API to create audiences from CSV uploads, monitor processing status, and list or delete audiences for an account. Created audiences are usable for targeting after processing reaches `ready` or `partial`.
        """
        from .resources.audiences import AsyncAudiencesResourceWithStreamingResponse

        return AsyncAudiencesResourceWithStreamingResponse(self._client.audiences)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithStreamingResponse:
        """
        A Media Asset is an AI-generated image or video created from a prompt and billed from an account balance. When generation finishes, the asset includes a file that can be attached anywhere Whop accepts files.

        Use the Media API to start a generation job and retrieve the asset while it processes or after it is ready.
        """
        from .resources.media import AsyncMediaResourceWithStreamingResponse

        return AsyncMediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def people(self) -> people.AsyncPeopleResourceWithStreamingResponse:
        """
        A Person is an identity-linked profile of a visitor or customer of an account, assembled from every [event](/api-reference/beta/events/event) the person generated — pixel page views, ad clicks, leads, identifies, and payments. Each profile carries the person's known identities (names, emails, phones, user IDs), purchase history and LTV, geo/device profile, traffic sources, and the first and last marketing touches that reached them.

        Use the People API to list and segment the people of an account — filter by activity, purchases, traffic source, location, or marketing touch, and sort by value — or retrieve one person by person ID, user ID, email address, or phone number.
        """
        from .resources.people import AsyncPeopleResourceWithStreamingResponse

        return AsyncPeopleResourceWithStreamingResponse(self._client.people)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        """
        An Event records conversion or engagement activity for an account, such as page views, purchases, or leads. Each event ties the action to the [person](/api-reference/beta/people/person) who took it, so activity can be attributed to the ads and links that drove it.

        Use the Events API to send new tracking events, list recent identity-linked events for an account, and inspect the events recorded for a person. The resource also exposes an anonymized read mode — the pulse feed — a platform-wide snapshot of recent purchases that carries nothing identifying. The pulse feed is public; other Events endpoints require authentication and are scoped to an account.

        Events are only as good as the pixel sending them, so [Validate Pixel](/api-reference/beta/events/validate-pixel) answers whether an account's pixel is working: it reads the events the pixel has sent, and when you pass a `url` whose page hasn't sent any lately, it fetches that page and looks for the pixel in its source. Use it before launching an ad to confirm its destination is tracked, or in a setup flow to tell a merchant whether their install is live.
        """
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithStreamingResponse:
        from .resources.companies import AsyncCompaniesResourceWithStreamingResponse

        return AsyncCompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithStreamingResponse:
        """A Plan defines how customers buy a product.

        It controls pricing, billing cadence, availability, tax behavior, checkout fields, and purchase visibility.

        Use the Plans API to create plans for products, list existing plans, retrieve or update plan configuration, calculate tax for checkout, and delete plans that should no longer be offered.
        """
        from .resources.plans import AsyncPlansResourceWithStreamingResponse

        return AsyncPlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def exports(self) -> exports.AsyncExportsResourceWithStreamingResponse:
        """
        An Export is an asynchronous CSV of one resource for one account — members, payments, disputes, ads, and the other tables the Whop dashboard can export. Generating a full table takes longer than a request, so an export is created in `pending`, moves through `processing`, and lands on `completed` with a download link. Each resource requires that resource's own export scope.

        Use the Exports API to start an export, poll it until `download_url` is set, and list the exports already requested for an account. Finished CSVs are retained for 30 days, after which the file is deleted and the export moves to `expired`.
        """
        from .resources.exports import AsyncExportsResourceWithStreamingResponse

        return AsyncExportsResourceWithStreamingResponse(self._client.exports)

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
        """Transfers move value between identities on Whop.

        They are used for account-to-account money movement, user payouts inside Whop, crypto transfers, and claim links depending on the destination type.

        Use the Transfers API to create a transfer, list previous transfers, and retrieve a transfer by ID when reconciling money movement between accounts or users.
        """
        from .resources.transfers import AsyncTransfersResourceWithStreamingResponse

        return AsyncTransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def ledger_accounts(self) -> ledger_accounts.AsyncLedgerAccountsResourceWithStreamingResponse:
        from .resources.ledger_accounts import AsyncLedgerAccountsResourceWithStreamingResponse

        return AsyncLedgerAccountsResourceWithStreamingResponse(self._client.ledger_accounts)

    @cached_property
    def memberships(self) -> memberships.AsyncMembershipsResourceWithStreamingResponse:
        """
        A Membership is a customer's purchase of a plan: the subscription or one-time grant that gives them access to a product. It tracks billing state (`active`, `trialing`, `past_due`, and so on), the current period, pending cancellations, custom metadata, and the software license key when the product includes licensing.

        Use the Memberships API to list an account's memberships or the caller's own, retrieve one by ID or license key, invite a recipient to join through a free plan, and manage the lifecycle: cancel immediately or at period end, reverse a scheduled period-end cancellation, pause and resume payment collection, extend with free days, generate a transfer link, and update metadata.
        """
        from .resources.memberships import AsyncMembershipsResourceWithStreamingResponse

        return AsyncMembershipsResourceWithStreamingResponse(self._client.memberships)

    @cached_property
    def authorized_users(self) -> authorized_users.AsyncAuthorizedUsersResourceWithStreamingResponse:
        from .resources.authorized_users import AsyncAuthorizedUsersResourceWithStreamingResponse

        return AsyncAuthorizedUsersResourceWithStreamingResponse(self._client.authorized_users)

    @cached_property
    def team_members(self) -> team_members.AsyncTeamMembersResourceWithStreamingResponse:
        """
        A Team Member is a member of an account's team: the link between a user and an account, carrying the role that controls what they can do. Roles are either system roles (like `admin` or `moderator`) or `custom` roles managed from the dashboard.

        Use the Team Members API to list an account's team, add a user to the team with a system role, change a member's role, and remove members. Adding a user who has not yet accepted sends an invitation instead.
        """
        from .resources.team_members import AsyncTeamMembersResourceWithStreamingResponse

        return AsyncTeamMembersResourceWithStreamingResponse(self._client.team_members)

    @cached_property
    def app_builds(self) -> app_builds.AsyncAppBuildsResourceWithStreamingResponse:
        """
        An App Build is a versioned artifact uploaded for an app — a hosted web archive, or an iOS/Android bundle. Builds start as drafts, go through review, and one approved build per platform is served to users as the production build.

        Use the App Builds API to upload a build for an app, list an app's builds with platform and status filters, retrieve a build, and promote a draft or approved build to production.
        """
        from .resources.app_builds import AsyncAppBuildsResourceWithStreamingResponse

        return AsyncAppBuildsResourceWithStreamingResponse(self._client.app_builds)

    @cached_property
    def app_deployments(self) -> app_deployments.AsyncAppDeploymentsResourceWithStreamingResponse:
        """A Deployment builds an app's current source and ships it, producing an App Build.

        It is a single resource per app rather than a list: retrieving it reports whether the working copy differs from what was last published, and starting one advances that same resource through `publishing` to `published` or `failed`.

        Use the App Deployments API to decide whether there is anything to publish, start a publish (optionally as a draft that appears under Versions without going live), and follow a run to completion with a progress estimate you can render.
        """
        from .resources.app_deployments import AsyncAppDeploymentsResourceWithStreamingResponse

        return AsyncAppDeploymentsResourceWithStreamingResponse(self._client.app_deployments)

    @cached_property
    def shipments(self) -> shipments.AsyncShipmentsResourceWithStreamingResponse:
        """
        A Shipment attaches a carrier tracking number to a payment and follows the package from label creation to delivery, exposing the current delivery status and a customer-facing tracking URL.

        Use the Shipments API to list an account's shipments, retrieve one by its id or the payment it fulfills, attach a tracking number to a payment, and update the tracking number on an existing shipment.
        """
        from .resources.shipments import AsyncShipmentsResourceWithStreamingResponse

        return AsyncShipmentsResourceWithStreamingResponse(self._client.shipments)

    @cached_property
    def checkout_configurations(
        self,
    ) -> checkout_configurations.AsyncCheckoutConfigurationsResourceWithStreamingResponse:
        """A Checkout Configuration is a reusable checkout link owned by an account.

        In `payment` mode it sells a specific plan; in `setup` mode it collects and saves payment details without charging. Each configuration can also override which payment methods are accepted and how 3D Secure is enforced for that checkout.

        Use the Checkout Configurations API to create checkout links for an existing or inline plan, list configurations for an account, retrieve the configuration behind a checkout URL, and delete links that should no longer be used.
        """
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
        """A User represents a person on Whop.

        Users have a public profile and can buy products, join accounts, and access experiences.

        Use the Users API to search for users, retrieve or update profiles, and check whether a user has access to an account, product, or experience.
        """
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        """A Payment is one charge against a buyer.

        Create it with a payment method already on file, or with a `confirmation_token` describing a method the buyer has just supplied.

        Collection runs in the background, so the create response is not the outcome. Poll [Retrieve status](/api-reference/beta/payments/retrieve-status) for how far the payment has got and, while it is `requires_action`, what the buyer must do next — follow a redirect, complete 3D Secure, display transfer instructions, or link a bank account. Use the return_url operation to change where they land afterwards, up until they come back.
        """
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
        """
        A Member is one buyer's relationship with an account — one record per customer regardless of how many memberships they hold. It carries relationship-level state: whether they have joined or left, their access level (`customer`, `admin`, or `no_access`), when they joined, and when they last opened the account's content.

        Use the Members API to list an account's members with filtering by access level, status, join date, and name or username search, and to retrieve a single member. Member rows are created and maintained by the membership lifecycle; to grant or revoke access, work with memberships instead.
        """
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
        """
        A Notification is a message delivered to a user — a new post, a payment, a mention. Every notification comes from an experience the user belongs to or a team they are on, and users control what they receive with notification preferences.

        Every notification belongs to a topic: the category it falls under, such as new sales or account activity. Topics carry a default, so a user only needs a preference row where they diverge from it. `GET /notifications/topics` lists the platform's visible topics, and a topic's `id` is what the notification preference endpoints take as `topic_id` — the catalog is the only place those ids come from, so read it rather than hardcoding. Each topic also carries an `identifier` such as `new-follower`, which is stable across environments and is the value to match on in code.

        Use the Notifications API to list the authenticated user's feed, read per-experience unread badges, mark an experience (or everything) as read, send notifications from your app to an experience's users or an account's team, and list the topic catalog.
        """
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithStreamingResponse:
        """
        A Dispute is a chargeback a customer files against a payment through their bank, or an inquiry that may become one. It carries the disputed payment, a deadline to respond, your evidence, and the outcome once the processor rules.

        Use the Disputes API to list disputes, edit the evidence packet while a dispute is still contestable, and submit it for review.
        """
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
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """
        An Account represents a person or business on Whop that can have its own profile, wallet, and account-scoped settings. Use accounts for customers, creators, merchants, sellers, or connected businesses your integration supports.

        Use the Accounts API to create accounts, list accounts visible to your credentials, retrieve or update an account, and retrieve the account associated with the current API key.
        """
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def financial_activity(self) -> financial_activity.AsyncFinancialActivityResourceWithStreamingResponse:
        """
        A Ledger Activity row is a single financial event on an account's ledger — a payment, withdrawal, refund, transfer, on-chain deposit, swap, or card transaction. Each row is derived from the underlying ledger lines and carries a typed `resource` and `source` so you can present and link the event without extra lookups.

        Use Ledger Activity to build a statement or transaction feed for an account or user. Reconcile against your own records with `amount` (signed, in the currency's smallest precision units) and `posted_at`, and use `available_at` to know when inflows became withdrawable.
        """
        from .resources.financial_activity import AsyncFinancialActivityResourceWithStreamingResponse

        return AsyncFinancialActivityResourceWithStreamingResponse(self._client.financial_activity)

    @cached_property
    def stats(self) -> stats.AsyncStatsResourceWithStreamingResponse:
        """Stats represent aggregated activity for an account over time.

        They help you understand revenue, transactions, disputes, members, referrals, and advertising performance across reporting periods like days, weeks, or months.

        Use the Stats API to list available metrics and their filterable properties, then retrieve time-series values for a date range.
        """
        from .resources.stats import AsyncStatsResourceWithStreamingResponse

        return AsyncStatsResourceWithStreamingResponse(self._client.stats)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithStreamingResponse:
        """
        Payouts represent money sent from an account or user balance to an external destination, such as a bank account, wallet, or other saved payout method.

        Use the Payouts API to create and track payouts, manage saved payout methods, and show expected arrival details for funds leaving Whop.
        """
        from .resources.payouts import AsyncPayoutsResourceWithStreamingResponse

        return AsyncPayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def partners(self) -> partners.AsyncPartnersResourceWithStreamingResponse:
        """
        The Partners API covers your Whop partner activity: the users you referred onto Whop, the businesses you referred and the earnings generated from their processing volume, and the partner leaderboard.

        Use it to enroll as a Whop partner, list the users you referred, list your referred businesses and review their earnings, and see the partner leaderboard.
        """
        from .resources.partners import AsyncPartnersResourceWithStreamingResponse

        return AsyncPartnersResourceWithStreamingResponse(self._client.partners)

    @cached_property
    def cards(self) -> cards.AsyncCardsResourceWithStreamingResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.cards import AsyncCardsResourceWithStreamingResponse

        return AsyncCardsResourceWithStreamingResponse(self._client.cards)

    @cached_property
    def card_transactions(self) -> card_transactions.AsyncCardTransactionsResourceWithStreamingResponse:
        """
        Cards represent Whop-issued virtual payment cards that spend from an account or user balance. Cards can be assigned to cardholders and configured with spending limits for controlled spending.

        Use the Cards API to issue cards, list cards for an account or user, and retrieve active card details such as the card number and CVC.
        """
        from .resources.card_transactions import AsyncCardTransactionsResourceWithStreamingResponse

        return AsyncCardTransactionsResourceWithStreamingResponse(self._client.card_transactions)

    @cached_property
    def swaps(self) -> swaps.AsyncSwapsResourceWithStreamingResponse:
        """
        Swaps convert value between supported tokens, chains, or wallet destinations for an account. A swap quote describes the expected output, fees, and approval requirements before you create the swap.

        Use the Swaps API to quote a conversion, create the swap, list recent swaps, and retrieve status until the transaction completes.
        """
        from .resources.swaps import AsyncSwapsResourceWithStreamingResponse

        return AsyncSwapsResourceWithStreamingResponse(self._client.swaps)

    @cached_property
    def deposits(self) -> deposits.AsyncDepositsResourceWithStreamingResponse:
        """
        Deposits describe ways to add funds to an account balance, including hosted deposit pages, bank deposit instructions, and supported crypto wallet addresses.

        Use the Deposits API to create deposit instructions for an account.
        """
        from .resources.deposits import AsyncDepositsResourceWithStreamingResponse

        return AsyncDepositsResourceWithStreamingResponse(self._client.deposits)

    @cached_property
    def recommended_actions(self) -> recommended_actions.AsyncRecommendedActionsResourceWithStreamingResponse:
        """
        A Recommended Action Chain is a short, ordered sequence of dashboard actions — create a product, price it, publish it — suggested for an account based on what it already has. Seeded chains come from hand-written presets; generated chains, produced per account, share the same shape.

        Use the Recommended Actions API to list the chains recommended for an account and to record that a chain was run. Running a chain executes nothing server-side — the client follows each step's CTA itself; the run endpoint records the `recommended_action_chain.executed` analytics event.
        """
        from .resources.recommended_actions import AsyncRecommendedActionsResourceWithStreamingResponse

        return AsyncRecommendedActionsResourceWithStreamingResponse(self._client.recommended_actions)

    @cached_property
    def setup_intents(self) -> setup_intents.AsyncSetupIntentsResourceWithStreamingResponse:
        from .resources.setup_intents import AsyncSetupIntentsResourceWithStreamingResponse

        return AsyncSetupIntentsResourceWithStreamingResponse(self._client.setup_intents)

    @cached_property
    def payment_methods(self) -> payment_methods.AsyncPaymentMethodsResourceWithStreamingResponse:
        from .resources.payment_methods import AsyncPaymentMethodsResourceWithStreamingResponse

        return AsyncPaymentMethodsResourceWithStreamingResponse(self._client.payment_methods)

    @cached_property
    def payment_method_domains(self) -> payment_method_domains.AsyncPaymentMethodDomainsResourceWithStreamingResponse:
        """
        A Payment Method Domain registers a hostname with a wallet provider so its payment methods can appear at a checkout served from that domain. The domain proves ownership by hosting the provider's association file — for Apple Pay, at `/.well-known/apple-developer-merchantid-domain-association` — and `status` reports whether verification has completed.

        Use the Payment Method Domains API to register domains for your account or its connected accounts, retry verification once the association file is hosted, and remove domains that should no longer serve wallet payments. A domain a platform shares with its connected accounts at checkout is listed on the platform's account, not on each connected account.
        """
        from .resources.payment_method_domains import AsyncPaymentMethodDomainsResourceWithStreamingResponse

        return AsyncPaymentMethodDomainsResourceWithStreamingResponse(self._client.payment_method_domains)

    @cached_property
    def fee_markups(self) -> fee_markups.AsyncFeeMarkupsResourceWithStreamingResponse:
        from .resources.fee_markups import AsyncFeeMarkupsResourceWithStreamingResponse

        return AsyncFeeMarkupsResourceWithStreamingResponse(self._client.fee_markups)

    @cached_property
    def verifications(self) -> verifications.AsyncVerificationsResourceWithStreamingResponse:
        """A Verification represents a legal identity for a person or business.

        Accounts and users complete verification when Whop needs to confirm who they are before enabling payouts or compliance-sensitive workflows.

        Use the Verifications API to start or resume a hosted verification session, check review status, and submit requested details or documents. If `requested_information` contains items, submit answers with [Update Verification](/api-reference/beta/verifications/update-verification).
        """
        from .resources.verifications import AsyncVerificationsResourceWithStreamingResponse

        return AsyncVerificationsResourceWithStreamingResponse(self._client.verifications)

    @cached_property
    def leads(self) -> leads.AsyncLeadsResourceWithStreamingResponse:
        from .resources.leads import AsyncLeadsResourceWithStreamingResponse

        return AsyncLeadsResourceWithStreamingResponse(self._client.leads)

    @cached_property
    def topups(self) -> topups.AsyncTopupsResourceWithStreamingResponse:
        from .resources.topups import AsyncTopupsResourceWithStreamingResponse

        return AsyncTopupsResourceWithStreamingResponse(self._client.topups)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def company_token_transactions(
        self,
    ) -> company_token_transactions.AsyncCompanyTokenTransactionsResourceWithStreamingResponse:
        from .resources.company_token_transactions import AsyncCompanyTokenTransactionsResourceWithStreamingResponse

        return AsyncCompanyTokenTransactionsResourceWithStreamingResponse(self._client.company_token_transactions)

    @cached_property
    def dm_members(self) -> dm_members.AsyncDmMembersResourceWithStreamingResponse:
        from .resources.dm_members import AsyncDmMembersResourceWithStreamingResponse

        return AsyncDmMembersResourceWithStreamingResponse(self._client.dm_members)

    @cached_property
    def ai_chats(self) -> ai_chats.AsyncAIChatsResourceWithStreamingResponse:
        from .resources.ai_chats import AsyncAIChatsResourceWithStreamingResponse

        return AsyncAIChatsResourceWithStreamingResponse(self._client.ai_chats)

    @cached_property
    def dm_channels(self) -> dm_channels.AsyncDmChannelsResourceWithStreamingResponse:
        from .resources.dm_channels import AsyncDmChannelsResourceWithStreamingResponse

        return AsyncDmChannelsResourceWithStreamingResponse(self._client.dm_channels)

    @cached_property
    def dispute_alerts(self) -> dispute_alerts.AsyncDisputeAlertsResourceWithStreamingResponse:
        """
        A Dispute alert is an early warning from a card issuer that a settled payment is being questioned, ahead of any chargeback. `type` separates fraud reports (`early_fraud_warning`), pre-dispute notices (`dispute_alert`), and Visa RDR cases the network already closed by refunding (`rapid_dispute_resolution`).

        Use the Dispute alerts API to list alerts for an account, filter them by type or payment, and read `actionable` to see whether refunding can still avoid the chargeback.
        """
        from .resources.dispute_alerts import AsyncDisputeAlertsResourceWithStreamingResponse

        return AsyncDisputeAlertsResourceWithStreamingResponse(self._client.dispute_alerts)

    @cached_property
    def resolution_center_cases(
        self,
    ) -> resolution_center_cases.AsyncResolutionCenterCasesResourceWithStreamingResponse:
        """
        A Resolution Center Case is opened by a buyer when something is wrong with a purchase — an unwanted renewal, an item that never arrived, or a charge they don't recognize. It is the step before a chargeback: the two sides work it out directly, and Whop decides the case if they can't. Each case carries a reason, a status naming which side it is waiting on, a timeline of events, and the actions available to whoever is reading it.

        Use the Resolution Center Cases API from either side: as the buyer, open a case, reply, appeal a decision, or withdraw it; as the merchant, accept it (refunding the payment), deny it, or ask the buyer for more information. Both sides read the same case, page its timeline, and summarize the cases they can see.
        """
        from .resources.resolution_center_cases import AsyncResolutionCenterCasesResourceWithStreamingResponse

        return AsyncResolutionCenterCasesResourceWithStreamingResponse(self._client.resolution_center_cases)

    @cached_property
    def payout_accounts(self) -> payout_accounts.AsyncPayoutAccountsResourceWithStreamingResponse:
        from .resources.payout_accounts import AsyncPayoutAccountsResourceWithStreamingResponse

        return AsyncPayoutAccountsResourceWithStreamingResponse(self._client.payout_accounts)

    @cached_property
    def affiliates(self) -> affiliates.AsyncAffiliatesResourceWithStreamingResponse:
        from .resources.affiliates import AsyncAffiliatesResourceWithStreamingResponse

        return AsyncAffiliatesResourceWithStreamingResponse(self._client.affiliates)

    @cached_property
    def bounties(self) -> bounties.AsyncBountiesResourceWithStreamingResponse:
        """A Bounty is a paid task posted by an account or user.

        The reward is held in escrow when the bounty publishes, workers submit proof of completed work, and each accepted submission is paid out until every winner slot fills.

        Use the Bounties API to create and publish a bounty, list an account's bounties for reporting or dashboards, list the bounties a user can work or has participated in, and retrieve a single bounty by ID.
        """
        from .resources.bounties import AsyncBountiesResourceWithStreamingResponse

        return AsyncBountiesResourceWithStreamingResponse(self._client.bounties)

    @cached_property
    def bounty_submissions(self) -> bounty_submissions.AsyncBountySubmissionsResourceWithStreamingResponse:
        """A Bounty Submission is one worker's attempt on a bounty.

        It starts as an in-progress attempt, enters the review queue when proof is submitted, and ends approved (paid from the bounty's escrowed pool) or denied.

        Use the Bounty Submissions API to submit proof of completed work to a bounty, list the submissions you authored, and review the submissions on your bounties — across every bounty or narrowed to one.
        """
        from .resources.bounty_submissions import AsyncBountySubmissionsResourceWithStreamingResponse

        return AsyncBountySubmissionsResourceWithStreamingResponse(self._client.bounty_submissions)

    @cached_property
    def ad_campaigns(self) -> ad_campaigns.AsyncAdCampaignsResourceWithStreamingResponse:
        """An Ad Campaign is the top-level container for paid ads on an ad network.

        It sets the platform, objective, and budget strategy shared by its [ad groups](/api-reference/beta/ad-groups/ad-group) and ads.

        Use the Ad Campaigns API to create campaigns, list campaigns for an account, retrieve or update campaign settings, and pause or resume campaign delivery.
        """
        from .resources.ad_campaigns import AsyncAdCampaignsResourceWithStreamingResponse

        return AsyncAdCampaignsResourceWithStreamingResponse(self._client.ad_campaigns)

    @cached_property
    def ad_groups(self) -> ad_groups.AsyncAdGroupsResourceWithStreamingResponse:
        """
        An Ad Group sits inside an [ad campaign](/api-reference/beta/ad-campaigns/ad-campaign) and controls delivery for [ads](/api-reference/beta/ads/ad). It sets the audience, placements, schedule, budget, and optimization goal for its ads.

        Use the Ad Groups API to create ad groups in campaigns, list or retrieve targeting and delivery settings, update budgets or targeting, delete groups that should stop running, and pause or resume delivery. It can also search the ad platform's targeting taxonomy for options to target and estimate how many people a draft targeting spec can reach.
        """
        from .resources.ad_groups import AsyncAdGroupsResourceWithStreamingResponse

        return AsyncAdGroupsResourceWithStreamingResponse(self._client.ad_groups)

    @cached_property
    def ads(self) -> ads.AsyncAdsResourceWithStreamingResponse:
        """
        An Ad is the individual creative unit delivered by an [ad group](/api-reference/beta/ad-groups/ad-group). It holds the copy, creative assets, and destination URL for one ad.

        Use the Ads API to list ads for an account, create ads inside ad groups, retrieve or update creative details, delete ads that should stop running, and pause or resume delivery.
        """
        from .resources.ads import AsyncAdsResourceWithStreamingResponse

        return AsyncAdsResourceWithStreamingResponse(self._client.ads)

    @cached_property
    def ad_reports(self) -> ad_reports.AsyncAdReportsResourceWithStreamingResponse:
        from .resources.ad_reports import AsyncAdReportsResourceWithStreamingResponse

        return AsyncAdReportsResourceWithStreamingResponse(self._client.ad_reports)


Client = Whop

AsyncClient = AsyncWhop
