# Shared Types

```python
from whop_sdk.types import (
    AccessLevel,
    AccessPassType,
    App,
    AppBuild,
    AppBuildPlatforms,
    AppBuildStatuses,
    AppStatuses,
    AppViewType,
    AuthorizedUserRoles,
    BusinessTypes,
    ChatChannel,
    CheckoutConfiguration,
    CollectionMethod,
    Company,
    CourseLessonInteraction,
    CourseLessonInteractionListItem,
    Currency,
    CustomCta,
    Direction,
    DmsPostTypes,
    EmailNotificationPreferences,
    Entry,
    EntryStatus,
    Experience,
    Forum,
    ForumPost,
    FriendlyReceiptStatus,
    GlobalAffiliateStatus,
    IndustryTypes,
    Invoice,
    InvoiceListItem,
    InvoiceStatus,
    MemberMostRecentActions,
    MemberStatuses,
    Membership,
    MembershipStatus,
    Message,
    PageInfo,
    Payment,
    Plan,
    PlanType,
    Product,
    ProductListItem,
    PromoType,
    Reaction,
    ReceiptStatus,
    ReleaseMethod,
    Shipment,
    ShipmentCarrier,
    ShipmentStatus,
    ShipmentSubstatus,
    SupportChannel,
    TaxType,
    Transfer,
    Visibility,
    VisibilityFilter,
    WhoCanCommentTypes,
    WhoCanPost,
    WhoCanPostTypes,
    WhoCanReact,
)
```

# Apps

Types:

```python
from whop_sdk.types import AppType, AppListResponse
```

Methods:

- <code title="post /apps">client.apps.<a href="./src/whop_sdk/resources/apps.py">create</a>(\*\*<a href="src/whop_sdk/types/app_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>
- <code title="get /apps/{id}">client.apps.<a href="./src/whop_sdk/resources/apps.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>
- <code title="patch /apps/{id}">client.apps.<a href="./src/whop_sdk/resources/apps.py">update</a>(id, \*\*<a href="src/whop_sdk/types/app_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>
- <code title="get /apps">client.apps.<a href="./src/whop_sdk/resources/apps.py">list</a>(\*\*<a href="src/whop_sdk/types/app_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/app_list_response.py">SyncCursorPage[AppListResponse]</a></code>

# Invoices

Types:

```python
from whop_sdk.types import InvoiceVoidResponse
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">create</a>(\*\*<a href="src/whop_sdk/types/invoice_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/invoice.py">Invoice</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/invoice.py">Invoice</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">list</a>(\*\*<a href="src/whop_sdk/types/invoice_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/invoice_list_item.py">SyncCursorPage[InvoiceListItem]</a></code>
- <code title="post /invoices/{id}/void">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">void</a>(id) -> <a href="./src/whop_sdk/types/invoice_void_response.py">InvoiceVoidResponse</a></code>

# CourseLessonInteractions

Methods:

- <code title="get /course_lesson_interactions/{id}">client.course_lesson_interactions.<a href="./src/whop_sdk/resources/course_lesson_interactions.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/course_lesson_interaction.py">CourseLessonInteraction</a></code>
- <code title="get /course_lesson_interactions">client.course_lesson_interactions.<a href="./src/whop_sdk/resources/course_lesson_interactions.py">list</a>(\*\*<a href="src/whop_sdk/types/course_lesson_interaction_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/course_lesson_interaction_list_item.py">SyncCursorPage[CourseLessonInteractionListItem]</a></code>

# Products

Types:

```python
from whop_sdk.types import ProductDeleteResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/whop_sdk/resources/products.py">create</a>(\*\*<a href="src/whop_sdk/types/product_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/product.py">Product</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/whop_sdk/resources/products.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/product.py">Product</a></code>
- <code title="patch /products/{id}">client.products.<a href="./src/whop_sdk/resources/products.py">update</a>(id, \*\*<a href="src/whop_sdk/types/product_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/product.py">Product</a></code>
- <code title="get /products">client.products.<a href="./src/whop_sdk/resources/products.py">list</a>(\*\*<a href="src/whop_sdk/types/product_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/product_list_item.py">SyncCursorPage[ProductListItem]</a></code>
- <code title="delete /products/{id}">client.products.<a href="./src/whop_sdk/resources/products.py">delete</a>(id) -> <a href="./src/whop_sdk/types/product_delete_response.py">ProductDeleteResponse</a></code>

# Companies

Types:

```python
from whop_sdk.types import CompanyListResponse
```

Methods:

- <code title="post /companies">client.companies.<a href="./src/whop_sdk/resources/companies.py">create</a>(\*\*<a href="src/whop_sdk/types/company_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/company.py">Company</a></code>
- <code title="get /companies/{id}">client.companies.<a href="./src/whop_sdk/resources/companies.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/company.py">Company</a></code>
- <code title="patch /companies/{id}">client.companies.<a href="./src/whop_sdk/resources/companies.py">update</a>(id, \*\*<a href="src/whop_sdk/types/company_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/company.py">Company</a></code>
- <code title="get /companies">client.companies.<a href="./src/whop_sdk/resources/companies.py">list</a>(\*\*<a href="src/whop_sdk/types/company_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/company_list_response.py">SyncCursorPage[CompanyListResponse]</a></code>

# Webhooks

Types:

```python
from whop_sdk.types import (
    InvoiceCreatedWebhookEvent,
    InvoicePaidWebhookEvent,
    InvoicePastDueWebhookEvent,
    InvoiceVoidedWebhookEvent,
    MembershipActivatedWebhookEvent,
    MembershipDeactivatedWebhookEvent,
    EntryCreatedWebhookEvent,
    EntryApprovedWebhookEvent,
    EntryDeniedWebhookEvent,
    EntryDeletedWebhookEvent,
    SetupIntentRequiresActionWebhookEvent,
    SetupIntentSucceededWebhookEvent,
    SetupIntentCanceledWebhookEvent,
    WithdrawalCreatedWebhookEvent,
    WithdrawalUpdatedWebhookEvent,
    CourseLessonInteractionCompletedWebhookEvent,
    PayoutMethodCreatedWebhookEvent,
    VerificationSucceededWebhookEvent,
    PaymentCreatedWebhookEvent,
    PaymentSucceededWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentPendingWebhookEvent,
    DisputeCreatedWebhookEvent,
    DisputeUpdatedWebhookEvent,
    RefundCreatedWebhookEvent,
    RefundUpdatedWebhookEvent,
    MembershipCancelAtPeriodEndChangedWebhookEvent,
    UnwrapWebhookEvent,
)
```

# Plans

Types:

```python
from whop_sdk.types import PlanListResponse, PlanDeleteResponse
```

Methods:

- <code title="post /plans">client.plans.<a href="./src/whop_sdk/resources/plans.py">create</a>(\*\*<a href="src/whop_sdk/types/plan_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/plan.py">Plan</a></code>
- <code title="get /plans/{id}">client.plans.<a href="./src/whop_sdk/resources/plans.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/plan.py">Plan</a></code>
- <code title="patch /plans/{id}">client.plans.<a href="./src/whop_sdk/resources/plans.py">update</a>(id, \*\*<a href="src/whop_sdk/types/plan_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/plan.py">Plan</a></code>
- <code title="get /plans">client.plans.<a href="./src/whop_sdk/resources/plans.py">list</a>(\*\*<a href="src/whop_sdk/types/plan_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/plan_list_response.py">SyncCursorPage[PlanListResponse]</a></code>
- <code title="delete /plans/{id}">client.plans.<a href="./src/whop_sdk/resources/plans.py">delete</a>(id) -> <a href="./src/whop_sdk/types/plan_delete_response.py">PlanDeleteResponse</a></code>

# Entries

Types:

```python
from whop_sdk.types import EntryListResponse, EntryApproveResponse
```

Methods:

- <code title="get /entries/{id}">client.entries.<a href="./src/whop_sdk/resources/entries.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/entry.py">Entry</a></code>
- <code title="get /entries">client.entries.<a href="./src/whop_sdk/resources/entries.py">list</a>(\*\*<a href="src/whop_sdk/types/entry_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/entry_list_response.py">SyncCursorPage[EntryListResponse]</a></code>
- <code title="post /entries/{id}/approve">client.entries.<a href="./src/whop_sdk/resources/entries.py">approve</a>(id) -> <a href="./src/whop_sdk/types/entry_approve_response.py">EntryApproveResponse</a></code>
- <code title="post /entries/{id}/deny">client.entries.<a href="./src/whop_sdk/resources/entries.py">deny</a>(id) -> <a href="./src/whop_sdk/types/shared/entry.py">Entry</a></code>

# ForumPosts

Types:

```python
from whop_sdk.types import ForumPostVisibilityType, ForumPostListResponse
```

Methods:

- <code title="post /forum_posts">client.forum_posts.<a href="./src/whop_sdk/resources/forum_posts.py">create</a>(\*\*<a href="src/whop_sdk/types/forum_post_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/forum_post.py">ForumPost</a></code>
- <code title="get /forum_posts/{id}">client.forum_posts.<a href="./src/whop_sdk/resources/forum_posts.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/forum_post.py">ForumPost</a></code>
- <code title="patch /forum_posts/{id}">client.forum_posts.<a href="./src/whop_sdk/resources/forum_posts.py">update</a>(id, \*\*<a href="src/whop_sdk/types/forum_post_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/forum_post.py">ForumPost</a></code>
- <code title="get /forum_posts">client.forum_posts.<a href="./src/whop_sdk/resources/forum_posts.py">list</a>(\*\*<a href="src/whop_sdk/types/forum_post_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/forum_post_list_response.py">SyncCursorPage[ForumPostListResponse]</a></code>

# Transfers

Types:

```python
from whop_sdk.types import TransferListResponse
```

Methods:

- <code title="post /transfers">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">create</a>(\*\*<a href="src/whop_sdk/types/transfer_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/transfer.py">Transfer</a></code>
- <code title="get /transfers/{id}">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/transfer.py">Transfer</a></code>
- <code title="get /transfers">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">list</a>(\*\*<a href="src/whop_sdk/types/transfer_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/transfer_list_response.py">SyncCursorPage[TransferListResponse]</a></code>

# LedgerAccounts

Types:

```python
from whop_sdk.types import LedgerAccountRetrieveResponse
```

Methods:

- <code title="get /ledger_accounts/{id}">client.ledger_accounts.<a href="./src/whop_sdk/resources/ledger_accounts.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/ledger_account_retrieve_response.py">LedgerAccountRetrieveResponse</a></code>

# Memberships

Types:

```python
from whop_sdk.types import MembershipListResponse
```

Methods:

- <code title="get /memberships/{id}">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="patch /memberships/{id}">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">update</a>(id, \*\*<a href="src/whop_sdk/types/membership_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">list</a>(\*\*<a href="src/whop_sdk/types/membership_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/membership_list_response.py">SyncCursorPage[MembershipListResponse]</a></code>
- <code title="post /memberships/{id}/cancel">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">cancel</a>(id, \*\*<a href="src/whop_sdk/types/membership_cancel_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="post /memberships/{id}/pause">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">pause</a>(id, \*\*<a href="src/whop_sdk/types/membership_pause_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="post /memberships/{id}/resume">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">resume</a>(id) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>

# AuthorizedUsers

Types:

```python
from whop_sdk.types import AuthorizedUserRetrieveResponse, AuthorizedUserListResponse
```

Methods:

- <code title="get /authorized_users/{id}">client.authorized_users.<a href="./src/whop_sdk/resources/authorized_users.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/authorized_user_retrieve_response.py">AuthorizedUserRetrieveResponse</a></code>
- <code title="get /authorized_users">client.authorized_users.<a href="./src/whop_sdk/resources/authorized_users.py">list</a>(\*\*<a href="src/whop_sdk/types/authorized_user_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/authorized_user_list_response.py">SyncCursorPage[AuthorizedUserListResponse]</a></code>

# AppBuilds

Types:

```python
from whop_sdk.types import AppBuildListResponse
```

Methods:

- <code title="post /app_builds">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">create</a>(\*\*<a href="src/whop_sdk/types/app_build_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app_build.py">AppBuild</a></code>
- <code title="get /app_builds/{id}">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/app_build.py">AppBuild</a></code>
- <code title="get /app_builds">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">list</a>(\*\*<a href="src/whop_sdk/types/app_build_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/app_build_list_response.py">SyncCursorPage[AppBuildListResponse]</a></code>
- <code title="post /app_builds/{id}/promote">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">promote</a>(id) -> <a href="./src/whop_sdk/types/shared/app_build.py">AppBuild</a></code>

# Shipments

Types:

```python
from whop_sdk.types import ShipmentListResponse
```

Methods:

- <code title="post /shipments">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">create</a>(\*\*<a href="src/whop_sdk/types/shipment_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/shipment.py">Shipment</a></code>
- <code title="get /shipments/{id}">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/shipment.py">Shipment</a></code>
- <code title="get /shipments">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">list</a>(\*\*<a href="src/whop_sdk/types/shipment_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shipment_list_response.py">SyncCursorPage[ShipmentListResponse]</a></code>

# CheckoutConfigurations

Types:

```python
from whop_sdk.types import CheckoutModes, CheckoutConfigurationListResponse
```

Methods:

- <code title="post /checkout_configurations">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">create</a>(\*\*<a href="src/whop_sdk/types/checkout_configuration_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/checkout_configuration.py">CheckoutConfiguration</a></code>
- <code title="get /checkout_configurations/{id}">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/checkout_configuration.py">CheckoutConfiguration</a></code>
- <code title="get /checkout_configurations">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">list</a>(\*\*<a href="src/whop_sdk/types/checkout_configuration_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/checkout_configuration_list_response.py">SyncCursorPage[CheckoutConfigurationListResponse]</a></code>

# Messages

Types:

```python
from whop_sdk.types import MessageListResponse
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/whop_sdk/resources/messages.py">create</a>(\*\*<a href="src/whop_sdk/types/message_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/message.py">Message</a></code>
- <code title="get /messages/{id}">client.messages.<a href="./src/whop_sdk/resources/messages.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/message.py">Message</a></code>
- <code title="patch /messages/{id}">client.messages.<a href="./src/whop_sdk/resources/messages.py">update</a>(id, \*\*<a href="src/whop_sdk/types/message_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/message.py">Message</a></code>
- <code title="get /messages">client.messages.<a href="./src/whop_sdk/resources/messages.py">list</a>(\*\*<a href="src/whop_sdk/types/message_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/message_list_response.py">SyncCursorPage[MessageListResponse]</a></code>

# ChatChannels

Types:

```python
from whop_sdk.types import ChatChannelListResponse
```

Methods:

- <code title="get /chat_channels/{id}">client.chat_channels.<a href="./src/whop_sdk/resources/chat_channels.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/chat_channel.py">ChatChannel</a></code>
- <code title="patch /chat_channels/{id}">client.chat_channels.<a href="./src/whop_sdk/resources/chat_channels.py">update</a>(id, \*\*<a href="src/whop_sdk/types/chat_channel_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/chat_channel.py">ChatChannel</a></code>
- <code title="get /chat_channels">client.chat_channels.<a href="./src/whop_sdk/resources/chat_channels.py">list</a>(\*\*<a href="src/whop_sdk/types/chat_channel_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/chat_channel_list_response.py">SyncCursorPage[ChatChannelListResponse]</a></code>

# Users

Types:

```python
from whop_sdk.types import UserRetrieveResponse, UserCheckAccessResponse
```

Methods:

- <code title="get /users/{id}">client.users.<a href="./src/whop_sdk/resources/users.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="get /users/{id}/access/{resource_id}">client.users.<a href="./src/whop_sdk/resources/users.py">check_access</a>(resource_id, \*, id) -> <a href="./src/whop_sdk/types/user_check_access_response.py">UserCheckAccessResponse</a></code>

# Payments

Types:

```python
from whop_sdk.types import (
    BillingReasons,
    CardBrands,
    PaymentMethodTypes,
    PaymentListResponse,
    PaymentListFeesResponse,
)
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/whop_sdk/resources/payments.py">create</a>(\*\*<a href="src/whop_sdk/types/payment_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="get /payments/{id}">client.payments.<a href="./src/whop_sdk/resources/payments.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="get /payments">client.payments.<a href="./src/whop_sdk/resources/payments.py">list</a>(\*\*<a href="src/whop_sdk/types/payment_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_list_response.py">SyncCursorPage[PaymentListResponse]</a></code>
- <code title="get /payments/{id}/fees">client.payments.<a href="./src/whop_sdk/resources/payments.py">list_fees</a>(id, \*\*<a href="src/whop_sdk/types/payment_list_fees_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_list_fees_response.py">SyncCursorPage[PaymentListFeesResponse]</a></code>
- <code title="post /payments/{id}/refund">client.payments.<a href="./src/whop_sdk/resources/payments.py">refund</a>(id, \*\*<a href="src/whop_sdk/types/payment_refund_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="post /payments/{id}/retry">client.payments.<a href="./src/whop_sdk/resources/payments.py">retry</a>(id) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="post /payments/{id}/void">client.payments.<a href="./src/whop_sdk/resources/payments.py">void</a>(id) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>

# SupportChannels

Types:

```python
from whop_sdk.types import SupportChannelListResponse
```

Methods:

- <code title="post /support_channels">client.support_channels.<a href="./src/whop_sdk/resources/support_channels.py">create</a>(\*\*<a href="src/whop_sdk/types/support_channel_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/support_channel.py">SupportChannel</a></code>
- <code title="get /support_channels/{id}">client.support_channels.<a href="./src/whop_sdk/resources/support_channels.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/support_channel.py">SupportChannel</a></code>
- <code title="get /support_channels">client.support_channels.<a href="./src/whop_sdk/resources/support_channels.py">list</a>(\*\*<a href="src/whop_sdk/types/support_channel_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/support_channel_list_response.py">SyncCursorPage[SupportChannelListResponse]</a></code>

# Experiences

Types:

```python
from whop_sdk.types import ExperienceListResponse, ExperienceDeleteResponse
```

Methods:

- <code title="post /experiences">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">create</a>(\*\*<a href="src/whop_sdk/types/experience_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/experience.py">Experience</a></code>
- <code title="get /experiences/{id}">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/experience.py">Experience</a></code>
- <code title="patch /experiences/{id}">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">update</a>(id, \*\*<a href="src/whop_sdk/types/experience_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/experience.py">Experience</a></code>
- <code title="get /experiences">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">list</a>(\*\*<a href="src/whop_sdk/types/experience_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/experience_list_response.py">SyncCursorPage[ExperienceListResponse]</a></code>
- <code title="delete /experiences/{id}">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">delete</a>(id) -> <a href="./src/whop_sdk/types/experience_delete_response.py">ExperienceDeleteResponse</a></code>
- <code title="post /experiences/{id}/attach">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">attach</a>(id, \*\*<a href="src/whop_sdk/types/experience_attach_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/experience.py">Experience</a></code>
- <code title="post /experiences/{id}/detach">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">detach</a>(id, \*\*<a href="src/whop_sdk/types/experience_detach_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/experience.py">Experience</a></code>
- <code title="post /experiences/{id}/duplicate">client.experiences.<a href="./src/whop_sdk/resources/experiences.py">duplicate</a>(id, \*\*<a href="src/whop_sdk/types/experience_duplicate_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/experience.py">Experience</a></code>

# Reactions

Types:

```python
from whop_sdk.types import ReactionListResponse
```

Methods:

- <code title="post /reactions">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">create</a>(\*\*<a href="src/whop_sdk/types/reaction_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/reaction.py">Reaction</a></code>
- <code title="get /reactions/{id}">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/reaction.py">Reaction</a></code>
- <code title="get /reactions">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">list</a>(\*\*<a href="src/whop_sdk/types/reaction_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/reaction_list_response.py">SyncCursorPage[ReactionListResponse]</a></code>

# Members

Types:

```python
from whop_sdk.types import MemberRetrieveResponse, MemberListResponse
```

Methods:

- <code title="get /members/{id}">client.members.<a href="./src/whop_sdk/resources/members.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/member_retrieve_response.py">MemberRetrieveResponse</a></code>
- <code title="get /members">client.members.<a href="./src/whop_sdk/resources/members.py">list</a>(\*\*<a href="src/whop_sdk/types/member_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/member_list_response.py">SyncCursorPage[MemberListResponse]</a></code>

# Forums

Types:

```python
from whop_sdk.types import ForumListResponse
```

Methods:

- <code title="get /forums/{id}">client.forums.<a href="./src/whop_sdk/resources/forums.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/forum.py">Forum</a></code>
- <code title="patch /forums/{id}">client.forums.<a href="./src/whop_sdk/resources/forums.py">update</a>(id, \*\*<a href="src/whop_sdk/types/forum_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/forum.py">Forum</a></code>
- <code title="get /forums">client.forums.<a href="./src/whop_sdk/resources/forums.py">list</a>(\*\*<a href="src/whop_sdk/types/forum_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/forum_list_response.py">SyncCursorPage[ForumListResponse]</a></code>

# PromoCodes

Types:

```python
from whop_sdk.types import (
    PromoCode,
    PromoCodeStatus,
    PromoDuration,
    PromoCodeListResponse,
    PromoCodeDeleteResponse,
)
```

Methods:

- <code title="post /promo_codes">client.promo_codes.<a href="./src/whop_sdk/resources/promo_codes.py">create</a>(\*\*<a href="src/whop_sdk/types/promo_code_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/promo_code.py">PromoCode</a></code>
- <code title="get /promo_codes/{id}">client.promo_codes.<a href="./src/whop_sdk/resources/promo_codes.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/promo_code.py">PromoCode</a></code>
- <code title="get /promo_codes">client.promo_codes.<a href="./src/whop_sdk/resources/promo_codes.py">list</a>(\*\*<a href="src/whop_sdk/types/promo_code_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/promo_code_list_response.py">SyncCursorPage[PromoCodeListResponse]</a></code>
- <code title="delete /promo_codes/{id}">client.promo_codes.<a href="./src/whop_sdk/resources/promo_codes.py">delete</a>(id) -> <a href="./src/whop_sdk/types/promo_code_delete_response.py">PromoCodeDeleteResponse</a></code>

# Courses

Types:

```python
from whop_sdk.types import (
    Course,
    CourseVisibilities,
    Languages,
    CourseListResponse,
    CourseDeleteResponse,
)
```

Methods:

- <code title="post /courses">client.courses.<a href="./src/whop_sdk/resources/courses.py">create</a>(\*\*<a href="src/whop_sdk/types/course_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/course.py">Course</a></code>
- <code title="get /courses/{id}">client.courses.<a href="./src/whop_sdk/resources/courses.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/course.py">Course</a></code>
- <code title="patch /courses/{id}">client.courses.<a href="./src/whop_sdk/resources/courses.py">update</a>(id, \*\*<a href="src/whop_sdk/types/course_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/course.py">Course</a></code>
- <code title="get /courses">client.courses.<a href="./src/whop_sdk/resources/courses.py">list</a>(\*\*<a href="src/whop_sdk/types/course_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_list_response.py">SyncCursorPage[CourseListResponse]</a></code>
- <code title="delete /courses/{id}">client.courses.<a href="./src/whop_sdk/resources/courses.py">delete</a>(id) -> <a href="./src/whop_sdk/types/course_delete_response.py">CourseDeleteResponse</a></code>

# CourseChapters

Types:

```python
from whop_sdk.types import CourseChapter, CourseChapterListResponse, CourseChapterDeleteResponse
```

Methods:

- <code title="post /course_chapters">client.course_chapters.<a href="./src/whop_sdk/resources/course_chapters.py">create</a>(\*\*<a href="src/whop_sdk/types/course_chapter_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_chapter.py">CourseChapter</a></code>
- <code title="get /course_chapters/{id}">client.course_chapters.<a href="./src/whop_sdk/resources/course_chapters.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/course_chapter.py">CourseChapter</a></code>
- <code title="patch /course_chapters/{id}">client.course_chapters.<a href="./src/whop_sdk/resources/course_chapters.py">update</a>(id, \*\*<a href="src/whop_sdk/types/course_chapter_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_chapter.py">CourseChapter</a></code>
- <code title="get /course_chapters">client.course_chapters.<a href="./src/whop_sdk/resources/course_chapters.py">list</a>(\*\*<a href="src/whop_sdk/types/course_chapter_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_chapter_list_response.py">SyncCursorPage[CourseChapterListResponse]</a></code>
- <code title="delete /course_chapters/{id}">client.course_chapters.<a href="./src/whop_sdk/resources/course_chapters.py">delete</a>(id) -> <a href="./src/whop_sdk/types/course_chapter_delete_response.py">CourseChapterDeleteResponse</a></code>

# CourseLessons

Types:

```python
from whop_sdk.types import (
    AssessmentQuestionTypes,
    EmbedType,
    Lesson,
    LessonTypes,
    LessonVisibilities,
    CourseLessonListResponse,
    CourseLessonDeleteResponse,
    CourseLessonMarkAsCompletedResponse,
    CourseLessonStartResponse,
    CourseLessonSubmitAssessmentResponse,
)
```

Methods:

- <code title="post /course_lessons">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">create</a>(\*\*<a href="src/whop_sdk/types/course_lesson_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/lesson.py">Lesson</a></code>
- <code title="get /course_lessons/{id}">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/lesson.py">Lesson</a></code>
- <code title="patch /course_lessons/{id}">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">update</a>(id, \*\*<a href="src/whop_sdk/types/course_lesson_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/lesson.py">Lesson</a></code>
- <code title="get /course_lessons">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">list</a>(\*\*<a href="src/whop_sdk/types/course_lesson_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_lesson_list_response.py">SyncCursorPage[CourseLessonListResponse]</a></code>
- <code title="delete /course_lessons/{id}">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">delete</a>(id) -> <a href="./src/whop_sdk/types/course_lesson_delete_response.py">CourseLessonDeleteResponse</a></code>
- <code title="post /course_lessons/{lesson_id}/mark_as_completed">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">mark_as_completed</a>(lesson_id) -> <a href="./src/whop_sdk/types/course_lesson_mark_as_completed_response.py">CourseLessonMarkAsCompletedResponse</a></code>
- <code title="post /course_lessons/{lesson_id}/start">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">start</a>(lesson_id) -> <a href="./src/whop_sdk/types/course_lesson_start_response.py">CourseLessonStartResponse</a></code>
- <code title="post /course_lessons/{lesson_id}/submit_assessment">client.course_lessons.<a href="./src/whop_sdk/resources/course_lessons.py">submit_assessment</a>(lesson_id, \*\*<a href="src/whop_sdk/types/course_lesson_submit_assessment_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_lesson_submit_assessment_response.py">CourseLessonSubmitAssessmentResponse</a></code>

# Reviews

Types:

```python
from whop_sdk.types import ReviewStatus, ReviewRetrieveResponse, ReviewListResponse
```

Methods:

- <code title="get /reviews/{id}">client.reviews.<a href="./src/whop_sdk/resources/reviews.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/review_retrieve_response.py">ReviewRetrieveResponse</a></code>
- <code title="get /reviews">client.reviews.<a href="./src/whop_sdk/resources/reviews.py">list</a>(\*\*<a href="src/whop_sdk/types/review_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/review_list_response.py">SyncCursorPage[ReviewListResponse]</a></code>

# CourseStudents

Types:

```python
from whop_sdk.types import CourseStudentRetrieveResponse, CourseStudentListResponse
```

Methods:

- <code title="get /course_students/{id}">client.course_students.<a href="./src/whop_sdk/resources/course_students.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/course_student_retrieve_response.py">CourseStudentRetrieveResponse</a></code>
- <code title="get /course_students">client.course_students.<a href="./src/whop_sdk/resources/course_students.py">list</a>(\*\*<a href="src/whop_sdk/types/course_student_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/course_student_list_response.py">SyncCursorPage[CourseStudentListResponse]</a></code>

# AccessTokens

Types:

```python
from whop_sdk.types import AccessTokenCreateResponse
```

Methods:

- <code title="post /access_tokens">client.access_tokens.<a href="./src/whop_sdk/resources/access_tokens.py">create</a>(\*\*<a href="src/whop_sdk/types/access_token_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/access_token_create_response.py">AccessTokenCreateResponse</a></code>

# Notifications

Types:

```python
from whop_sdk.types import NotificationCreateResponse
```

Methods:

- <code title="post /notifications">client.notifications.<a href="./src/whop_sdk/resources/notifications.py">create</a>(\*\*<a href="src/whop_sdk/types/notification_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/notification_create_response.py">NotificationCreateResponse</a></code>

# Disputes

Types:

```python
from whop_sdk.types import Dispute, DisputeStatuses, DisputeListResponse
```

Methods:

- <code title="get /disputes/{id}">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/dispute.py">Dispute</a></code>
- <code title="get /disputes">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">list</a>(\*\*<a href="src/whop_sdk/types/dispute_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/dispute_list_response.py">SyncCursorPage[DisputeListResponse]</a></code>
- <code title="post /disputes/{id}/submit_evidence">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">submit_evidence</a>(id) -> <a href="./src/whop_sdk/types/dispute.py">Dispute</a></code>
- <code title="post /disputes/{id}/update_evidence">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">update_evidence</a>(id, \*\*<a href="src/whop_sdk/types/dispute_update_evidence_params.py">params</a>) -> <a href="./src/whop_sdk/types/dispute.py">Dispute</a></code>

# Refunds

Types:

```python
from whop_sdk.types import (
    PaymentProvider,
    RefundReferenceStatus,
    RefundReferenceType,
    RefundStatus,
    RefundRetrieveResponse,
    RefundListResponse,
)
```

Methods:

- <code title="get /refunds/{id}">client.refunds.<a href="./src/whop_sdk/resources/refunds.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/refund_retrieve_response.py">RefundRetrieveResponse</a></code>
- <code title="get /refunds">client.refunds.<a href="./src/whop_sdk/resources/refunds.py">list</a>(\*\*<a href="src/whop_sdk/types/refund_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/refund_list_response.py">SyncCursorPage[RefundListResponse]</a></code>

# Withdrawals

Types:

```python
from whop_sdk.types import (
    WithdrawalFeeTypes,
    WithdrawalSpeeds,
    WithdrawalStatus,
    WithdrawalTypes,
    WithdrawalCreateResponse,
    WithdrawalRetrieveResponse,
    WithdrawalListResponse,
)
```

Methods:

- <code title="post /withdrawals">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">create</a>(\*\*<a href="src/whop_sdk/types/withdrawal_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/withdrawal_create_response.py">WithdrawalCreateResponse</a></code>
- <code title="get /withdrawals/{id}">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/withdrawal_retrieve_response.py">WithdrawalRetrieveResponse</a></code>
- <code title="get /withdrawals">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">list</a>(\*\*<a href="src/whop_sdk/types/withdrawal_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/withdrawal_list_response.py">SyncCursorPage[WithdrawalListResponse]</a></code>

# AccountLinks

Types:

```python
from whop_sdk.types import AccountLinkCreateResponse
```

Methods:

- <code title="post /account_links">client.account_links.<a href="./src/whop_sdk/resources/account_links.py">create</a>(\*\*<a href="src/whop_sdk/types/account_link_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/account_link_create_response.py">AccountLinkCreateResponse</a></code>

# SetupIntents

Types:

```python
from whop_sdk.types import SetupIntent, SetupIntentStatus, SetupIntentListResponse
```

Methods:

- <code title="get /setup_intents/{id}">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/setup_intent.py">SetupIntent</a></code>
- <code title="get /setup_intents">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">list</a>(\*\*<a href="src/whop_sdk/types/setup_intent_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/setup_intent_list_response.py">SyncCursorPage[SetupIntentListResponse]</a></code>

# PaymentMethods

Types:

```python
from whop_sdk.types import PaymentMethodRetrieveResponse, PaymentMethodListResponse
```

Methods:

- <code title="get /payment_methods/{id}">client.payment_methods.<a href="./src/whop_sdk/resources/payment_methods.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/payment_method_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_method_retrieve_response.py">PaymentMethodRetrieveResponse</a></code>
- <code title="get /payment_methods">client.payment_methods.<a href="./src/whop_sdk/resources/payment_methods.py">list</a>(\*\*<a href="src/whop_sdk/types/payment_method_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_method_list_response.py">SyncCursorPage[PaymentMethodListResponse]</a></code>

# FeeMarkups

Types:

```python
from whop_sdk.types import (
    FeeMarkupType,
    FeeMarkupCreateResponse,
    FeeMarkupListResponse,
    FeeMarkupDeleteResponse,
)
```

Methods:

- <code title="post /fee_markups">client.fee_markups.<a href="./src/whop_sdk/resources/fee_markups.py">create</a>(\*\*<a href="src/whop_sdk/types/fee_markup_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/fee_markup_create_response.py">FeeMarkupCreateResponse</a></code>
- <code title="get /fee_markups">client.fee_markups.<a href="./src/whop_sdk/resources/fee_markups.py">list</a>(\*\*<a href="src/whop_sdk/types/fee_markup_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/fee_markup_list_response.py">SyncCursorPage[FeeMarkupListResponse]</a></code>
- <code title="delete /fee_markups/{id}">client.fee_markups.<a href="./src/whop_sdk/resources/fee_markups.py">delete</a>(id) -> <a href="./src/whop_sdk/types/fee_markup_delete_response.py">FeeMarkupDeleteResponse</a></code>

# PayoutMethods

Types:

```python
from whop_sdk.types import PayoutMethodRetrieveResponse, PayoutMethodListResponse
```

Methods:

- <code title="get /payout_methods/{id}">client.payout_methods.<a href="./src/whop_sdk/resources/payout_methods.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/payout_method_retrieve_response.py">PayoutMethodRetrieveResponse</a></code>
- <code title="get /payout_methods">client.payout_methods.<a href="./src/whop_sdk/resources/payout_methods.py">list</a>(\*\*<a href="src/whop_sdk/types/payout_method_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payout_method_list_response.py">SyncCursorPage[PayoutMethodListResponse]</a></code>

# Verifications

Types:

```python
from whop_sdk.types import VerificationRetrieveResponse
```

Methods:

- <code title="get /verifications/{id}">client.verifications.<a href="./src/whop_sdk/resources/verifications.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/verification_retrieve_response.py">VerificationRetrieveResponse</a></code>

# Leads

Types:

```python
from whop_sdk.types import (
    LeadCreateResponse,
    LeadRetrieveResponse,
    LeadUpdateResponse,
    LeadListResponse,
)
```

Methods:

- <code title="post /leads">client.leads.<a href="./src/whop_sdk/resources/leads.py">create</a>(\*\*<a href="src/whop_sdk/types/lead_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/lead_create_response.py">LeadCreateResponse</a></code>
- <code title="get /leads/{id}">client.leads.<a href="./src/whop_sdk/resources/leads.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/lead_retrieve_response.py">LeadRetrieveResponse</a></code>
- <code title="patch /leads/{id}">client.leads.<a href="./src/whop_sdk/resources/leads.py">update</a>(id, \*\*<a href="src/whop_sdk/types/lead_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/lead_update_response.py">LeadUpdateResponse</a></code>
- <code title="get /leads">client.leads.<a href="./src/whop_sdk/resources/leads.py">list</a>(\*\*<a href="src/whop_sdk/types/lead_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/lead_list_response.py">SyncCursorPage[LeadListResponse]</a></code>

# Topups

Types:

```python
from whop_sdk.types import TopupCreateResponse
```

Methods:

- <code title="post /topups">client.topups.<a href="./src/whop_sdk/resources/topups.py">create</a>(\*\*<a href="src/whop_sdk/types/topup_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/topup_create_response.py">TopupCreateResponse</a></code>
