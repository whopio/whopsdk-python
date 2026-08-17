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
    ShipmentStatus,
    ShipmentSubstatus,
    SupportChannel,
    TaxType,
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
from whop_sdk.types import AppType, AppListResponse, AppDeleteResponse, AppLogsResponse
```

Methods:

- <code title="post /apps">client.apps.<a href="./src/whop_sdk/resources/apps.py">create</a>(\*\*<a href="src/whop_sdk/types/app_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>
- <code title="get /apps/{id}">client.apps.<a href="./src/whop_sdk/resources/apps.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>
- <code title="patch /apps/{id}">client.apps.<a href="./src/whop_sdk/resources/apps.py">update</a>(id, \*\*<a href="src/whop_sdk/types/app_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>
- <code title="get /apps">client.apps.<a href="./src/whop_sdk/resources/apps.py">list</a>(\*\*<a href="src/whop_sdk/types/app_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/app_list_response.py">SyncCursorPage[AppListResponse]</a></code>
- <code title="delete /apps/{id}">client.apps.<a href="./src/whop_sdk/resources/apps.py">delete</a>(id) -> <a href="./src/whop_sdk/types/app_delete_response.py">AppDeleteResponse</a></code>
- <code title="get /apps/{id}/logs">client.apps.<a href="./src/whop_sdk/resources/apps.py">logs</a>(id, \*\*<a href="src/whop_sdk/types/app_logs_params.py">params</a>) -> <a href="./src/whop_sdk/types/app_logs_response.py">AppLogsResponse</a></code>
- <code title="patch /apps/{id}/permissions">client.apps.<a href="./src/whop_sdk/resources/apps.py">update_permissions</a>(id, \*\*<a href="src/whop_sdk/types/app_update_permissions_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app.py">App</a></code>

# APIKeys

Types:

```python
from whop_sdk.types import APIKey, Permission, APIKeyDeleteResponse, APIKeyListPermissionsResponse
```

Methods:

- <code title="post /api_keys">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">create</a>(\*\*<a href="src/whop_sdk/types/api_key_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/api_key.py">APIKey</a></code>
- <code title="get /api_keys/{id}">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/api_key.py">APIKey</a></code>
- <code title="patch /api_keys/{id}">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">update</a>(id, \*\*<a href="src/whop_sdk/types/api_key_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/api_key.py">APIKey</a></code>
- <code title="get /api_keys">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">list</a>(\*\*<a href="src/whop_sdk/types/api_key_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/api_key.py">SyncCursorPage[APIKey]</a></code>
- <code title="delete /api_keys/{id}">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">delete</a>(id) -> <a href="./src/whop_sdk/types/api_key_delete_response.py">APIKeyDeleteResponse</a></code>
- <code title="get /api_keys/permissions">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">list_permissions</a>() -> <a href="./src/whop_sdk/types/api_key_list_permissions_response.py">APIKeyListPermissionsResponse</a></code>
- <code title="post /api_keys/{id}/rotate">client.api_keys.<a href="./src/whop_sdk/resources/api_keys.py">rotate</a>(id) -> <a href="./src/whop_sdk/types/api_key.py">APIKey</a></code>

# Permissions

Types:

```python
from whop_sdk.types import PermissionAction, PermissionListResponse
```

Methods:

- <code title="get /permissions">client.permissions.<a href="./src/whop_sdk/resources/permissions.py">list</a>(\*\*<a href="src/whop_sdk/types/permission_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/permission_list_response.py">PermissionListResponse</a></code>

# Invoices

Types:

```python
from whop_sdk.types import (
    TaxIdentifierType,
    InvoiceDeleteResponse,
    InvoiceMarkPaidResponse,
    InvoiceMarkUncollectibleResponse,
    InvoiceResendResponse,
    InvoiceVoidResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">create</a>(\*\*<a href="src/whop_sdk/types/invoice_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/invoice.py">Invoice</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/invoice.py">Invoice</a></code>
- <code title="patch /invoices/{id}">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">update</a>(id, \*\*<a href="src/whop_sdk/types/invoice_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/invoice.py">Invoice</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">list</a>(\*\*<a href="src/whop_sdk/types/invoice_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/invoice_list_item.py">SyncCursorPage[InvoiceListItem]</a></code>
- <code title="delete /invoices/{id}">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">delete</a>(id) -> <a href="./src/whop_sdk/types/invoice_delete_response.py">InvoiceDeleteResponse</a></code>
- <code title="post /invoices/{id}/mark_paid">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">mark_paid</a>(id) -> <a href="./src/whop_sdk/types/invoice_mark_paid_response.py">InvoiceMarkPaidResponse</a></code>
- <code title="post /invoices/{id}/mark_uncollectible">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">mark_uncollectible</a>(id) -> <a href="./src/whop_sdk/types/invoice_mark_uncollectible_response.py">InvoiceMarkUncollectibleResponse</a></code>
- <code title="post /invoices/{id}/resend">client.invoices.<a href="./src/whop_sdk/resources/invoices.py">resend</a>(id) -> <a href="./src/whop_sdk/types/invoice_resend_response.py">InvoiceResendResponse</a></code>
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
- <code title="post /products/{id}/publish">client.products.<a href="./src/whop_sdk/resources/products.py">publish</a>(id) -> <a href="./src/whop_sdk/types/shared/product.py">Product</a></code>
- <code title="post /products/{id}/unpublish">client.products.<a href="./src/whop_sdk/resources/products.py">unpublish</a>(id) -> <a href="./src/whop_sdk/types/shared/product.py">Product</a></code>

# SocialAccounts

Types:

```python
from whop_sdk.types import (
    SocialAccount,
    SocialAccountPost,
    SocialAccountDeleteResponse,
    SocialAccountConnectResponse,
    SocialAccountLeadFormsResponse,
    SocialAccountPostsResponse,
)
```

Methods:

- <code title="post /social_accounts">client.social_accounts.<a href="./src/whop_sdk/resources/social_accounts.py">create</a>(\*\*<a href="src/whop_sdk/types/social_account_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/social_account.py">SocialAccount</a></code>
- <code title="get /social_accounts">client.social_accounts.<a href="./src/whop_sdk/resources/social_accounts.py">list</a>(\*\*<a href="src/whop_sdk/types/social_account_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/social_account.py">SyncCursorPage[SocialAccount]</a></code>
- <code title="delete /social_accounts/{id}">client.social_accounts.<a href="./src/whop_sdk/resources/social_accounts.py">delete</a>(id, \*\*<a href="src/whop_sdk/types/social_account_delete_params.py">params</a>) -> <a href="./src/whop_sdk/types/social_account_delete_response.py">SocialAccountDeleteResponse</a></code>
- <code title="post /social_accounts/connect">client.social_accounts.<a href="./src/whop_sdk/resources/social_accounts.py">connect</a>(\*\*<a href="src/whop_sdk/types/social_account_connect_params.py">params</a>) -> <a href="./src/whop_sdk/types/social_account_connect_response.py">SocialAccountConnectResponse</a></code>
- <code title="get /social_accounts/{id}/lead_forms">client.social_accounts.<a href="./src/whop_sdk/resources/social_accounts.py">lead_forms</a>(id, \*\*<a href="src/whop_sdk/types/social_account_lead_forms_params.py">params</a>) -> <a href="./src/whop_sdk/types/social_account_lead_forms_response.py">SocialAccountLeadFormsResponse</a></code>
- <code title="get /social_accounts/{id}/posts">client.social_accounts.<a href="./src/whop_sdk/resources/social_accounts.py">posts</a>(id, \*\*<a href="src/whop_sdk/types/social_account_posts_params.py">params</a>) -> <a href="./src/whop_sdk/types/social_account_posts_response.py">SocialAccountPostsResponse</a></code>

# Audiences

Types:

```python
from whop_sdk.types import Audience, AudienceCreateResponse, AudienceDeleteResponse
```

Methods:

- <code title="post /audiences">client.audiences.<a href="./src/whop_sdk/resources/audiences.py">create</a>(\*\*<a href="src/whop_sdk/types/audience_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/audience_create_response.py">AudienceCreateResponse</a></code>
- <code title="patch /audiences/{id}">client.audiences.<a href="./src/whop_sdk/resources/audiences.py">update</a>(id, \*\*<a href="src/whop_sdk/types/audience_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/audience.py">Audience</a></code>
- <code title="get /audiences">client.audiences.<a href="./src/whop_sdk/resources/audiences.py">list</a>(\*\*<a href="src/whop_sdk/types/audience_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/audience.py">SyncCursorPage[Audience]</a></code>
- <code title="delete /audiences/{id}">client.audiences.<a href="./src/whop_sdk/resources/audiences.py">delete</a>(id) -> <a href="./src/whop_sdk/types/audience_delete_response.py">AudienceDeleteResponse</a></code>
- <code title="post /audiences/{id}/add_people">client.audiences.<a href="./src/whop_sdk/resources/audiences.py">add_people</a>(id, \*\*<a href="src/whop_sdk/types/audience_add_people_params.py">params</a>) -> <a href="./src/whop_sdk/types/audience.py">Audience</a></code>

# Media

Types:

```python
from whop_sdk.types import MediaAsset
```

Methods:

- <code title="get /media/{id}">client.media.<a href="./src/whop_sdk/resources/media.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/media_asset.py">MediaAsset</a></code>
- <code title="post /media/generate">client.media.<a href="./src/whop_sdk/resources/media.py">generate</a>(\*\*<a href="src/whop_sdk/types/media_generate_params.py">params</a>) -> <a href="./src/whop_sdk/types/media_asset.py">MediaAsset</a></code>

# People

Types:

```python
from whop_sdk.types import PersonRetrieveResponse, PersonListResponse
```

Methods:

- <code title="get /people/{id}">client.people.<a href="./src/whop_sdk/resources/people.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/person_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/person_retrieve_response.py">PersonRetrieveResponse</a></code>
- <code title="get /people">client.people.<a href="./src/whop_sdk/resources/people.py">list</a>(\*\*<a href="src/whop_sdk/types/person_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/person_list_response.py">SyncCursorPage[PersonListResponse]</a></code>

# Events

Types:

```python
from whop_sdk.types import (
    PixelValidation,
    EventCreateResponse,
    EventListResponse,
    EventPulseResponse,
)
```

Methods:

- <code title="post /events">client.events.<a href="./src/whop_sdk/resources/events.py">create</a>(\*\*<a href="src/whop_sdk/types/event_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/event_create_response.py">EventCreateResponse</a></code>
- <code title="get /events">client.events.<a href="./src/whop_sdk/resources/events.py">list</a>(\*\*<a href="src/whop_sdk/types/event_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/event_list_response.py">SyncCursorPage[EventListResponse]</a></code>
- <code title="get /events/pulse">client.events.<a href="./src/whop_sdk/resources/events.py">pulse</a>(\*\*<a href="src/whop_sdk/types/event_pulse_params.py">params</a>) -> <a href="./src/whop_sdk/types/event_pulse_response.py">EventPulseResponse</a></code>
- <code title="post /events/validate_pixel">client.events.<a href="./src/whop_sdk/resources/events.py">validate_pixel</a>(\*\*<a href="src/whop_sdk/types/event_validate_pixel_params.py">params</a>) -> <a href="./src/whop_sdk/types/pixel_validation.py">PixelValidation</a></code>

# Companies

Types:

```python
from whop_sdk.types import SocialLinkWebsites, CompanyListResponse, CompanyCreateAPIKeyResponse
```

Methods:

- <code title="post /companies">client.companies.<a href="./src/whop_sdk/resources/companies.py">create</a>(\*\*<a href="src/whop_sdk/types/company_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/company.py">Company</a></code>
- <code title="get /companies/{id}">client.companies.<a href="./src/whop_sdk/resources/companies.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/company.py">Company</a></code>
- <code title="patch /companies/{id}">client.companies.<a href="./src/whop_sdk/resources/companies.py">update</a>(id, \*\*<a href="src/whop_sdk/types/company_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/company.py">Company</a></code>
- <code title="get /companies">client.companies.<a href="./src/whop_sdk/resources/companies.py">list</a>(\*\*<a href="src/whop_sdk/types/company_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/company_list_response.py">SyncCursorPage[CompanyListResponse]</a></code>
- <code title="post /companies/{parent_company_id}/api_keys">client.companies.<a href="./src/whop_sdk/resources/companies.py">create_api_key</a>(parent_company_id, \*\*<a href="src/whop_sdk/types/company_create_api_key_params.py">params</a>) -> <a href="./src/whop_sdk/types/company_create_api_key_response.py">CompanyCreateAPIKeyResponse</a></code>

# Webhooks

Types:

```python
from whop_sdk.types import (
    APIVersion,
    Webhook,
    WebhookEvent,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookListDeliveriesResponse,
    WebhookReplayResponse,
    WebhookReplayDeliveryResponse,
    WebhookTestResponse,
    AdCampaignPaymentFailedWebhookEvent,
    CardCanceledWebhookEvent,
    CardCreatedWebhookEvent,
    CardFrozenWebhookEvent,
    CardUpdatedWebhookEvent,
    CardApplicationApprovedWebhookEvent,
    CardApplicationCreatedWebhookEvent,
    CardApplicationDeniedWebhookEvent,
    CardApplicationUpdatedWebhookEvent,
    CardTransactionCompletedWebhookEvent,
    CardTransactionCreatedWebhookEvent,
    CardTransactionDeclinedWebhookEvent,
    CardTransactionReversedWebhookEvent,
    CardTransactionUpdatedWebhookEvent,
    ChatMessageCreatedWebhookEvent,
    ChatReactionCreatedWebhookEvent,
    CourseLessonInteractionCompletedWebhookEvent,
    DepositSucceededWebhookEvent,
    DisputeCreatedWebhookEvent,
    DisputeUpdatedWebhookEvent,
    DisputeAlertCreatedWebhookEvent,
    EntryApprovedWebhookEvent,
    EntryCreatedWebhookEvent,
    EntryDeletedWebhookEvent,
    EntryDeniedWebhookEvent,
    ExportCompletedWebhookEvent,
    ExportFailedWebhookEvent,
    IdentityProfileUpdatedWebhookEvent,
    InvoiceCreatedWebhookEvent,
    InvoiceMarkedUncollectibleWebhookEvent,
    InvoicePaidWebhookEvent,
    InvoicePastDueWebhookEvent,
    InvoiceVoidedWebhookEvent,
    LedgerAccountFundsAvailableWebhookEvent,
    MemberCreatedWebhookEvent,
    MembershipActivatedWebhookEvent,
    MembershipCancelAtPeriodEndChangedWebhookEvent,
    MembershipDeactivatedWebhookEvent,
    MembershipTrialEndingSoonWebhookEvent,
    PaymentCreatedWebhookEvent,
    PaymentFailedWebhookEvent,
    PaymentPendingWebhookEvent,
    PaymentSucceededWebhookEvent,
    PayoutAccountStatusUpdatedWebhookEvent,
    PayoutMethodCreatedWebhookEvent,
    PlanCreatedWebhookEvent,
    PlanDeletedWebhookEvent,
    PlanUpdatedWebhookEvent,
    ProductCreatedWebhookEvent,
    ProductDeletedWebhookEvent,
    ProductPublishedWebhookEvent,
    ProductUnpublishedWebhookEvent,
    ProductUpdatedWebhookEvent,
    RefundCreatedWebhookEvent,
    RefundUpdatedWebhookEvent,
    ResolutionCenterCaseCreatedWebhookEvent,
    ResolutionCenterCaseDecidedWebhookEvent,
    ResolutionCenterCaseUpdatedWebhookEvent,
    SetupIntentCanceledWebhookEvent,
    SetupIntentRequiresActionWebhookEvent,
    SetupIntentSucceededWebhookEvent,
    ShipmentCreatedWebhookEvent,
    ShipmentUpdatedWebhookEvent,
    SwapCompletedWebhookEvent,
    TransferCompletedWebhookEvent,
    TransferCreatedWebhookEvent,
    TransferFailedWebhookEvent,
    VerificationSucceededWebhookEvent,
    WithdrawalCreatedWebhookEvent,
    WithdrawalUpdatedWebhookEvent,
    UnwrapWebhookEvent,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">create</a>(\*\*<a href="src/whop_sdk/types/webhook_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks/{id}">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/webhook.py">Webhook</a></code>
- <code title="patch /webhooks/{id}">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">update</a>(id, \*\*<a href="src/whop_sdk/types/webhook_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">list</a>(\*\*<a href="src/whop_sdk/types/webhook_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/webhook_list_response.py">SyncCursorPage[WebhookListResponse]</a></code>
- <code title="delete /webhooks/{id}">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">delete</a>(id) -> <a href="./src/whop_sdk/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /webhooks/{id}/deliveries">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">list_deliveries</a>(id, \*\*<a href="src/whop_sdk/types/webhook_list_deliveries_params.py">params</a>) -> <a href="./src/whop_sdk/types/webhook_list_deliveries_response.py">SyncCursorPage[WebhookListDeliveriesResponse]</a></code>
- <code title="post /webhooks/{id}/replay">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">replay</a>(id, \*\*<a href="src/whop_sdk/types/webhook_replay_params.py">params</a>) -> <a href="./src/whop_sdk/types/webhook_replay_response.py">WebhookReplayResponse</a></code>
- <code title="post /webhooks/{id}/deliveries/{delivery_id}/replay">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">replay_delivery</a>(delivery_id, \*, id) -> <a href="./src/whop_sdk/types/webhook_replay_delivery_response.py">WebhookReplayDeliveryResponse</a></code>
- <code title="post /webhooks/{id}/test">client.webhooks.<a href="./src/whop_sdk/resources/webhooks.py">test</a>(id, \*\*<a href="src/whop_sdk/types/webhook_test_params.py">params</a>) -> <a href="./src/whop_sdk/types/webhook_test_response.py">WebhookTestResponse</a></code>

# Plans

Types:

```python
from whop_sdk.types import (
    CheckoutFont,
    CheckoutShape,
    PlanListResponse,
    PlanDeleteResponse,
    PlanCalculateTaxResponse,
)
```

Methods:

- <code title="post /plans">client.plans.<a href="./src/whop_sdk/resources/plans.py">create</a>(\*\*<a href="src/whop_sdk/types/plan_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/plan.py">Plan</a></code>
- <code title="get /plans/{id}">client.plans.<a href="./src/whop_sdk/resources/plans.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/plan.py">Plan</a></code>
- <code title="patch /plans/{id}">client.plans.<a href="./src/whop_sdk/resources/plans.py">update</a>(id, \*\*<a href="src/whop_sdk/types/plan_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/plan.py">Plan</a></code>
- <code title="get /plans">client.plans.<a href="./src/whop_sdk/resources/plans.py">list</a>(\*\*<a href="src/whop_sdk/types/plan_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/plan_list_response.py">SyncCursorPage[PlanListResponse]</a></code>
- <code title="delete /plans/{id}">client.plans.<a href="./src/whop_sdk/resources/plans.py">delete</a>(id) -> <a href="./src/whop_sdk/types/plan_delete_response.py">PlanDeleteResponse</a></code>
- <code title="post /plans/{id}/calculate_tax">client.plans.<a href="./src/whop_sdk/resources/plans.py">calculate_tax</a>(id, \*\*<a href="src/whop_sdk/types/plan_calculate_tax_params.py">params</a>) -> <a href="./src/whop_sdk/types/plan_calculate_tax_response.py">PlanCalculateTaxResponse</a></code>

# Exports

Types:

```python
from whop_sdk.types import Export, ExportListResponse
```

Methods:

- <code title="post /exports">client.exports.<a href="./src/whop_sdk/resources/exports.py">create</a>(\*\*<a href="src/whop_sdk/types/export_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/export.py">Export</a></code>
- <code title="get /exports/{id}">client.exports.<a href="./src/whop_sdk/resources/exports.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/export.py">Export</a></code>
- <code title="get /exports">client.exports.<a href="./src/whop_sdk/resources/exports.py">list</a>(\*\*<a href="src/whop_sdk/types/export_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/export_list_response.py">ExportListResponse</a></code>

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
from whop_sdk.types import (
    TransferCreateResponse,
    TransferRetrieveResponse,
    TransferListResponse,
    TransferListRecipientsResponse,
)
```

Methods:

- <code title="post /transfers">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">create</a>(\*\*<a href="src/whop_sdk/types/transfer_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/transfer_create_response.py">TransferCreateResponse</a></code>
- <code title="get /transfers/{id}">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/transfer_retrieve_response.py">TransferRetrieveResponse</a></code>
- <code title="get /transfers">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">list</a>(\*\*<a href="src/whop_sdk/types/transfer_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/transfer_list_response.py">SyncCursorPage[TransferListResponse]</a></code>
- <code title="get /transfers/recipients">client.transfers.<a href="./src/whop_sdk/resources/transfers.py">list_recipients</a>(\*\*<a href="src/whop_sdk/types/transfer_list_recipients_params.py">params</a>) -> <a href="./src/whop_sdk/types/transfer_list_recipients_response.py">SyncCursorPage[TransferListRecipientsResponse]</a></code>

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
from whop_sdk.types import CancelOptions, MembershipInviteResponse
```

Methods:

- <code title="get /memberships/{id}">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="patch /memberships/{id}">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">update</a>(id, \*\*<a href="src/whop_sdk/types/membership_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">list</a>(\*\*<a href="src/whop_sdk/types/membership_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">SyncCursorPage[Membership]</a></code>
- <code title="post /memberships/{id}/cancel">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">cancel</a>(id, \*\*<a href="src/whop_sdk/types/membership_cancel_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="post /memberships/{id}/extend">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">extend</a>(id, \*\*<a href="src/whop_sdk/types/membership_extend_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="post /memberships/invite">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">invite</a>(\*\*<a href="src/whop_sdk/types/membership_invite_params.py">params</a>) -> <a href="./src/whop_sdk/types/membership_invite_response.py">MembershipInviteResponse</a></code>
- <code title="post /memberships/{id}/pause">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">pause</a>(id, \*\*<a href="src/whop_sdk/types/membership_pause_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>
- <code title="post /memberships/{id}/resume">client.memberships.<a href="./src/whop_sdk/resources/memberships.py">resume</a>(id) -> <a href="./src/whop_sdk/types/shared/membership.py">Membership</a></code>

# AuthorizedUsers

Types:

```python
from whop_sdk.types import AuthorizedUser, AuthorizedUserListResponse, AuthorizedUserDeleteResponse
```

Methods:

- <code title="post /authorized_users">client.authorized_users.<a href="./src/whop_sdk/resources/authorized_users.py">create</a>(\*\*<a href="src/whop_sdk/types/authorized_user_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/authorized_user.py">AuthorizedUser</a></code>
- <code title="get /authorized_users/{id}">client.authorized_users.<a href="./src/whop_sdk/resources/authorized_users.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/authorized_user.py">AuthorizedUser</a></code>
- <code title="get /authorized_users">client.authorized_users.<a href="./src/whop_sdk/resources/authorized_users.py">list</a>(\*\*<a href="src/whop_sdk/types/authorized_user_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/authorized_user_list_response.py">SyncCursorPage[AuthorizedUserListResponse]</a></code>
- <code title="delete /authorized_users/{id}">client.authorized_users.<a href="./src/whop_sdk/resources/authorized_users.py">delete</a>(id, \*\*<a href="src/whop_sdk/types/authorized_user_delete_params.py">params</a>) -> <a href="./src/whop_sdk/types/authorized_user_delete_response.py">AuthorizedUserDeleteResponse</a></code>

# TeamMembers

Types:

```python
from whop_sdk.types import TeamMember, TeamMemberDeleteResponse
```

Methods:

- <code title="post /team_members">client.team_members.<a href="./src/whop_sdk/resources/team_members.py">create</a>(\*\*<a href="src/whop_sdk/types/team_member_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/team_member.py">TeamMember</a></code>
- <code title="get /team_members/{id}">client.team_members.<a href="./src/whop_sdk/resources/team_members.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/team_member.py">TeamMember</a></code>
- <code title="patch /team_members/{id}">client.team_members.<a href="./src/whop_sdk/resources/team_members.py">update</a>(id, \*\*<a href="src/whop_sdk/types/team_member_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/team_member.py">TeamMember</a></code>
- <code title="get /team_members">client.team_members.<a href="./src/whop_sdk/resources/team_members.py">list</a>(\*\*<a href="src/whop_sdk/types/team_member_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/team_member.py">SyncCursorPage[TeamMember]</a></code>
- <code title="delete /team_members/{id}">client.team_members.<a href="./src/whop_sdk/resources/team_members.py">delete</a>(id) -> <a href="./src/whop_sdk/types/team_member_delete_response.py">TeamMemberDeleteResponse</a></code>

# AppBuilds

Methods:

- <code title="post /app_builds">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">create</a>(\*\*<a href="src/whop_sdk/types/app_build_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app_build.py">AppBuild</a></code>
- <code title="get /app_builds/{id}">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/app_build.py">AppBuild</a></code>
- <code title="get /app_builds">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">list</a>(\*\*<a href="src/whop_sdk/types/app_build_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/app_build.py">SyncCursorPage[AppBuild]</a></code>
- <code title="post /app_builds/{id}/promote">client.app_builds.<a href="./src/whop_sdk/resources/app_builds.py">promote</a>(id) -> <a href="./src/whop_sdk/types/shared/app_build.py">AppBuild</a></code>

# AppDeployments

Types:

```python
from whop_sdk.types import AppDeploymentCreateResponse, AppDeploymentRetrieveResponse
```

Methods:

- <code title="post /apps/{app_id}/deployment">client.app_deployments.<a href="./src/whop_sdk/resources/app_deployments.py">create</a>(app_id, \*\*<a href="src/whop_sdk/types/app_deployment_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/app_deployment_create_response.py">AppDeploymentCreateResponse</a></code>
- <code title="get /apps/{app_id}/deployment">client.app_deployments.<a href="./src/whop_sdk/resources/app_deployments.py">retrieve</a>(app_id) -> <a href="./src/whop_sdk/types/app_deployment_retrieve_response.py">AppDeploymentRetrieveResponse</a></code>

# Shipments

Methods:

- <code title="post /shipments">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">create</a>(\*\*<a href="src/whop_sdk/types/shipment_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/shipment.py">Shipment</a></code>
- <code title="get /shipments/{id}">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/shipment.py">Shipment</a></code>
- <code title="patch /shipments/{id}">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">update</a>(id, \*\*<a href="src/whop_sdk/types/shipment_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/shipment.py">Shipment</a></code>
- <code title="get /shipments">client.shipments.<a href="./src/whop_sdk/resources/shipments.py">list</a>(\*\*<a href="src/whop_sdk/types/shipment_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/shipment.py">SyncCursorPage[Shipment]</a></code>

# CheckoutConfigurations

Types:

```python
from whop_sdk.types import (
    CheckoutModes,
    CheckoutConfigurationCreateResponse,
    CheckoutConfigurationRetrieveResponse,
    CheckoutConfigurationListResponse,
    CheckoutConfigurationDeleteResponse,
)
```

Methods:

- <code title="post /checkout_configurations">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">create</a>(\*\*<a href="src/whop_sdk/types/checkout_configuration_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/checkout_configuration_create_response.py">CheckoutConfigurationCreateResponse</a></code>
- <code title="get /checkout_configurations/{id}">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/checkout_configuration_retrieve_response.py">CheckoutConfigurationRetrieveResponse</a></code>
- <code title="get /checkout_configurations">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">list</a>(\*\*<a href="src/whop_sdk/types/checkout_configuration_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/checkout_configuration_list_response.py">SyncCursorPage[CheckoutConfigurationListResponse]</a></code>
- <code title="delete /checkout_configurations/{id}">client.checkout_configurations.<a href="./src/whop_sdk/resources/checkout_configurations.py">delete</a>(id) -> <a href="./src/whop_sdk/types/checkout_configuration_delete_response.py">CheckoutConfigurationDeleteResponse</a></code>

# Messages

Types:

```python
from whop_sdk.types import MessageListResponse, MessageDeleteResponse
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/whop_sdk/resources/messages.py">create</a>(\*\*<a href="src/whop_sdk/types/message_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/message.py">Message</a></code>
- <code title="get /messages/{id}">client.messages.<a href="./src/whop_sdk/resources/messages.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/message.py">Message</a></code>
- <code title="patch /messages/{id}">client.messages.<a href="./src/whop_sdk/resources/messages.py">update</a>(id, \*\*<a href="src/whop_sdk/types/message_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/message.py">Message</a></code>
- <code title="get /messages">client.messages.<a href="./src/whop_sdk/resources/messages.py">list</a>(\*\*<a href="src/whop_sdk/types/message_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/message_list_response.py">SyncCursorPage[MessageListResponse]</a></code>
- <code title="delete /messages/{id}">client.messages.<a href="./src/whop_sdk/resources/messages.py">delete</a>(id) -> <a href="./src/whop_sdk/types/message_delete_response.py">MessageDeleteResponse</a></code>

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
from whop_sdk.types import User, UserBalance, UserCheckAccessResponse, UserRecommendActionsResponse
```

Methods:

- <code title="get /users/{id}">client.users.<a href="./src/whop_sdk/resources/users/users.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/user_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/user.py">User</a></code>
- <code title="patch /users/{id}">client.users.<a href="./src/whop_sdk/resources/users/users.py">update</a>(id, \*\*<a href="src/whop_sdk/types/user_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/whop_sdk/resources/users/users.py">list</a>(\*\*<a href="src/whop_sdk/types/user_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/user.py">SyncCursorPage[User]</a></code>
- <code title="get /users/{id}/access/{resource_id}">client.users.<a href="./src/whop_sdk/resources/users/users.py">check_access</a>(resource_id, \*, id) -> <a href="./src/whop_sdk/types/user_check_access_response.py">UserCheckAccessResponse</a></code>
- <code title="get /users/me">client.users.<a href="./src/whop_sdk/resources/users/users.py">me</a>(\*\*<a href="src/whop_sdk/types/user_me_params.py">params</a>) -> <a href="./src/whop_sdk/types/user.py">User</a></code>
- <code title="get /users/{id}/recommend_actions">client.users.<a href="./src/whop_sdk/resources/users/users.py">recommend_actions</a>(id) -> <a href="./src/whop_sdk/types/user_recommend_actions_response.py">UserRecommendActionsResponse</a></code>
- <code title="patch /users/me">client.users.<a href="./src/whop_sdk/resources/users/users.py">update_me</a>(\*\*<a href="src/whop_sdk/types/user_update_me_params.py">params</a>) -> <a href="./src/whop_sdk/types/user.py">User</a></code>

## OAuthGrants

Types:

```python
from whop_sdk.types.users import OAuthGrant
```

Methods:

- <code title="post /users/me/oauth_grants">client.users.oauth_grants.<a href="./src/whop_sdk/resources/users/oauth_grants.py">create</a>(\*\*<a href="src/whop_sdk/types/users/oauth_grant_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/oauth_grant.py">OAuthGrant</a></code>
- <code title="get /users/me/oauth_grants">client.users.oauth_grants.<a href="./src/whop_sdk/resources/users/oauth_grants.py">list</a>(\*\*<a href="src/whop_sdk/types/users/oauth_grant_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/oauth_grant.py">SyncCursorPage[OAuthGrant]</a></code>

## Passkeys

Types:

```python
from whop_sdk.types.users import Passkey, PasskeyDeleteResponse, PasskeyChallengeResponse
```

Methods:

- <code title="post /users/me/passkeys">client.users.passkeys.<a href="./src/whop_sdk/resources/users/passkeys.py">create</a>(\*\*<a href="src/whop_sdk/types/users/passkey_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/passkey.py">Passkey</a></code>
- <code title="get /users/me/passkeys">client.users.passkeys.<a href="./src/whop_sdk/resources/users/passkeys.py">list</a>(\*\*<a href="src/whop_sdk/types/users/passkey_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/passkey.py">SyncCursorPage[Passkey]</a></code>
- <code title="delete /users/me/passkeys/{id}">client.users.passkeys.<a href="./src/whop_sdk/resources/users/passkeys.py">delete</a>(id, \*\*<a href="src/whop_sdk/types/users/passkey_delete_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/passkey_delete_response.py">PasskeyDeleteResponse</a></code>
- <code title="post /users/me/passkeys/challenge">client.users.passkeys.<a href="./src/whop_sdk/resources/users/passkeys.py">challenge</a>(\*\*<a href="src/whop_sdk/types/users/passkey_challenge_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/passkey_challenge_response.py">PasskeyChallengeResponse</a></code>

## Preferences

Types:

```python
from whop_sdk.types.users import PreferenceRetrieveResponse, PreferenceUpdateResponse
```

Methods:

- <code title="get /users/me/preferences">client.users.preferences.<a href="./src/whop_sdk/resources/users/preferences/preferences.py">retrieve</a>() -> <a href="./src/whop_sdk/types/users/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="patch /users/me/preferences">client.users.preferences.<a href="./src/whop_sdk/resources/users/preferences/preferences.py">update</a>(\*\*<a href="src/whop_sdk/types/users/preference_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/preference_update_response.py">PreferenceUpdateResponse</a></code>

### Notifications

Types:

```python
from whop_sdk.types.users.preferences import NotificationSetResponse
```

Methods:

- <code title="patch /users/me/preferences/notifications">client.users.preferences.notifications.<a href="./src/whop_sdk/resources/users/preferences/notifications/notifications.py">set</a>(\*\*<a href="src/whop_sdk/types/users/preferences/notification_set_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/preferences/notification_set_response.py">NotificationSetResponse</a></code>

#### Topics

Types:

```python
from whop_sdk.types.users.preferences.notifications import TopicListResponse
```

Methods:

- <code title="get /users/me/preferences/notifications/topics">client.users.preferences.notifications.topics.<a href="./src/whop_sdk/resources/users/preferences/notifications/topics.py">list</a>(\*\*<a href="src/whop_sdk/types/users/preferences/notifications/topic_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/preferences/notifications/topic_list_response.py">SyncCursorPage[TopicListResponse]</a></code>

#### Experiences

Types:

```python
from whop_sdk.types.users.preferences.notifications import ExperienceListResponse
```

Methods:

- <code title="get /users/me/preferences/notifications/experiences">client.users.preferences.notifications.experiences.<a href="./src/whop_sdk/resources/users/preferences/notifications/experiences.py">list</a>(\*\*<a href="src/whop_sdk/types/users/preferences/notifications/experience_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/users/preferences/notifications/experience_list_response.py">SyncCursorPage[ExperienceListResponse]</a></code>

# Payments

Types:

```python
from whop_sdk.types import (
    BillingReasons,
    CardBrands,
    PaymentMethodType,
    ReceiptTaxBehavior,
    PaymentListResponse,
    PaymentListFeesResponse,
    PaymentRetrieveStatusResponse,
    PaymentUpdateReturnURLResponse,
)
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/whop_sdk/resources/payments.py">create</a>(\*\*<a href="src/whop_sdk/types/payment_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="get /payments/{id}">client.payments.<a href="./src/whop_sdk/resources/payments.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="get /payments">client.payments.<a href="./src/whop_sdk/resources/payments.py">list</a>(\*\*<a href="src/whop_sdk/types/payment_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_list_response.py">SyncCursorPage[PaymentListResponse]</a></code>
- <code title="get /payments/{id}/fees">client.payments.<a href="./src/whop_sdk/resources/payments.py">list_fees</a>(id, \*\*<a href="src/whop_sdk/types/payment_list_fees_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_list_fees_response.py">SyncCursorPage[PaymentListFeesResponse]</a></code>
- <code title="post /payments/{id}/refund">client.payments.<a href="./src/whop_sdk/resources/payments.py">refund</a>(id, \*\*<a href="src/whop_sdk/types/payment_refund_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="get /payments/{payment_id}/status">client.payments.<a href="./src/whop_sdk/resources/payments.py">retrieve_status</a>(payment_id) -> <a href="./src/whop_sdk/types/payment_retrieve_status_response.py">PaymentRetrieveStatusResponse</a></code>
- <code title="post /payments/{id}/retry">client.payments.<a href="./src/whop_sdk/resources/payments.py">retry</a>(id) -> <a href="./src/whop_sdk/types/shared/payment.py">Payment</a></code>
- <code title="patch /payments/{payment_id}/return_url">client.payments.<a href="./src/whop_sdk/resources/payments.py">update_return_url</a>(payment_id, \*\*<a href="src/whop_sdk/types/payment_update_return_url_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_update_return_url_response.py">PaymentUpdateReturnURLResponse</a></code>
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
from whop_sdk.types import ReactionListResponse, ReactionDeleteResponse
```

Methods:

- <code title="post /reactions">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">create</a>(\*\*<a href="src/whop_sdk/types/reaction_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/shared/reaction.py">Reaction</a></code>
- <code title="get /reactions/{id}">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/shared/reaction.py">Reaction</a></code>
- <code title="get /reactions">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">list</a>(\*\*<a href="src/whop_sdk/types/reaction_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/reaction_list_response.py">SyncCursorPage[ReactionListResponse]</a></code>
- <code title="delete /reactions/{id}">client.reactions.<a href="./src/whop_sdk/resources/reactions.py">delete</a>(id, \*\*<a href="src/whop_sdk/types/reaction_delete_params.py">params</a>) -> <a href="./src/whop_sdk/types/reaction_delete_response.py">ReactionDeleteResponse</a></code>

# Members

Types:

```python
from whop_sdk.types import Member
```

Methods:

- <code title="get /members/{id}">client.members.<a href="./src/whop_sdk/resources/members/members.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/member.py">Member</a></code>
- <code title="get /members">client.members.<a href="./src/whop_sdk/resources/members/members.py">list</a>(\*\*<a href="src/whop_sdk/types/member_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/member.py">SyncCursorPage[Member]</a></code>

## Logs

Types:

```python
from whop_sdk.types.members import LogListResponse
```

Methods:

- <code title="get /members/{id}/logs">client.members.logs.<a href="./src/whop_sdk/resources/members/logs.py">list</a>(id, \*\*<a href="src/whop_sdk/types/members/log_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/members/log_list_response.py">SyncCursorPage[LogListResponse]</a></code>

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
- <code title="post /promo_codes/{id}/activate">client.promo_codes.<a href="./src/whop_sdk/resources/promo_codes.py">activate</a>(id) -> <a href="./src/whop_sdk/types/promo_code.py">PromoCode</a></code>
- <code title="post /promo_codes/{id}/deactivate">client.promo_codes.<a href="./src/whop_sdk/resources/promo_codes.py">deactivate</a>(id) -> <a href="./src/whop_sdk/types/promo_code.py">PromoCode</a></code>

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
from whop_sdk.types import (
    Notification,
    NotificationBadge,
    NotificationCreateResponse,
    NotificationBadgesResponse,
    NotificationMarkReadResponse,
)
```

Methods:

- <code title="post /notifications">client.notifications.<a href="./src/whop_sdk/resources/notifications/notifications.py">create</a>(\*\*<a href="src/whop_sdk/types/notification_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/notification_create_response.py">NotificationCreateResponse</a></code>
- <code title="get /notifications/{id}">client.notifications.<a href="./src/whop_sdk/resources/notifications/notifications.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/notification.py">Notification</a></code>
- <code title="get /notifications">client.notifications.<a href="./src/whop_sdk/resources/notifications/notifications.py">list</a>(\*\*<a href="src/whop_sdk/types/notification_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/notification.py">SyncCursorPage[Notification]</a></code>
- <code title="get /notifications/badges">client.notifications.<a href="./src/whop_sdk/resources/notifications/notifications.py">badges</a>(\*\*<a href="src/whop_sdk/types/notification_badges_params.py">params</a>) -> <a href="./src/whop_sdk/types/notification_badges_response.py">NotificationBadgesResponse</a></code>
- <code title="post /notifications/mark_read">client.notifications.<a href="./src/whop_sdk/resources/notifications/notifications.py">mark_read</a>(\*\*<a href="src/whop_sdk/types/notification_mark_read_params.py">params</a>) -> <a href="./src/whop_sdk/types/notification_mark_read_response.py">NotificationMarkReadResponse</a></code>

## Topics

Types:

```python
from whop_sdk.types.notifications import NotificationTopic
```

Methods:

- <code title="get /notifications/topics">client.notifications.topics.<a href="./src/whop_sdk/resources/notifications/topics.py">list</a>(\*\*<a href="src/whop_sdk/types/notifications/topic_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/notifications/notification_topic.py">SyncCursorPage[NotificationTopic]</a></code>

# Disputes

Types:

```python
from whop_sdk.types import Dispute, DisputeStatuses, DisputeSummaryResponse
```

Methods:

- <code title="get /disputes/{id}">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/dispute.py">Dispute</a></code>
- <code title="patch /disputes/{id}">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">update</a>(id, \*\*<a href="src/whop_sdk/types/dispute_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/dispute.py">Dispute</a></code>
- <code title="get /disputes">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">list</a>(\*\*<a href="src/whop_sdk/types/dispute_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/dispute.py">SyncCursorPage[Dispute]</a></code>
- <code title="post /disputes/{id}/submit">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">submit</a>(id) -> <a href="./src/whop_sdk/types/dispute.py">Dispute</a></code>
- <code title="get /disputes/summary">client.disputes.<a href="./src/whop_sdk/resources/disputes.py">summary</a>(\*\*<a href="src/whop_sdk/types/dispute_summary_params.py">params</a>) -> <a href="./src/whop_sdk/types/dispute_summary_response.py">DisputeSummaryResponse</a></code>

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
    Withdrawal,
    WithdrawalFeeTypes,
    WithdrawalSpeeds,
    WithdrawalStatus,
    WithdrawalListResponse,
    WithdrawalGeneratePdfResponse,
)
```

Methods:

- <code title="post /withdrawals">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">create</a>(\*\*<a href="src/whop_sdk/types/withdrawal_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/withdrawal.py">Withdrawal</a></code>
- <code title="get /withdrawals/{id}">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/withdrawal.py">Withdrawal</a></code>
- <code title="get /withdrawals">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">list</a>(\*\*<a href="src/whop_sdk/types/withdrawal_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/withdrawal_list_response.py">SyncCursorPage[WithdrawalListResponse]</a></code>
- <code title="post /withdrawals/{id}/generate_pdf">client.withdrawals.<a href="./src/whop_sdk/resources/withdrawals.py">generate_pdf</a>(id) -> <a href="./src/whop_sdk/types/withdrawal_generate_pdf_response.py">WithdrawalGeneratePdfResponse</a></code>

# AccountLinks

Types:

```python
from whop_sdk.types import AccountLinkCreateResponse
```

Methods:

- <code title="post /account_links">client.account_links.<a href="./src/whop_sdk/resources/account_links.py">create</a>(\*\*<a href="src/whop_sdk/types/account_link_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/account_link_create_response.py">AccountLinkCreateResponse</a></code>

# Accounts

Types:

```python
from whop_sdk.types import (
    Account,
    AccountSocialLink,
    AccountFormCompanyResponse,
    AccountTransferOwnershipResponse,
)
```

Methods:

- <code title="post /accounts">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">create</a>(\*\*<a href="src/whop_sdk/types/account_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/account.py">Account</a></code>
- <code title="get /accounts/{id}">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/account.py">Account</a></code>
- <code title="patch /accounts/{id}">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">update</a>(id, \*\*<a href="src/whop_sdk/types/account_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">list</a>(\*\*<a href="src/whop_sdk/types/account_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/account.py">SyncCursorPage[Account]</a></code>
- <code title="post /accounts/{id}/form_company">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">form_company</a>(id, \*\*<a href="src/whop_sdk/types/account_form_company_params.py">params</a>) -> <a href="./src/whop_sdk/types/account_form_company_response.py">AccountFormCompanyResponse</a></code>
- <code title="get /accounts/me">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">me</a>() -> <a href="./src/whop_sdk/types/account.py">Account</a></code>
- <code title="post /accounts/{id}/transfer_ownership">client.accounts.<a href="./src/whop_sdk/resources/accounts/accounts.py">transfer_ownership</a>(id, \*\*<a href="src/whop_sdk/types/account_transfer_ownership_params.py">params</a>) -> <a href="./src/whop_sdk/types/account_transfer_ownership_response.py">AccountTransferOwnershipResponse</a></code>

## Preferences

Types:

```python
from whop_sdk.types.accounts import PreferenceRetrieveResponse, PreferenceUpdateResponse
```

Methods:

- <code title="get /accounts/{account_id}/preferences">client.accounts.preferences.<a href="./src/whop_sdk/resources/accounts/preferences.py">retrieve</a>(account_id) -> <a href="./src/whop_sdk/types/accounts/preference_retrieve_response.py">PreferenceRetrieveResponse</a></code>
- <code title="patch /accounts/{account_id}/preferences">client.accounts.preferences.<a href="./src/whop_sdk/resources/accounts/preferences.py">update</a>(account_id, \*\*<a href="src/whop_sdk/types/accounts/preference_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/accounts/preference_update_response.py">PreferenceUpdateResponse</a></code>

## Reserves

Types:

```python
from whop_sdk.types.accounts import AccountReserve, ReserveListResponse
```

Methods:

- <code title="get /accounts/{account_id}/reserves">client.accounts.reserves.<a href="./src/whop_sdk/resources/accounts/reserves.py">list</a>(account_id) -> <a href="./src/whop_sdk/types/accounts/reserve_list_response.py">ReserveListResponse</a></code>

# FinancialActivity

Types:

```python
from whop_sdk.types import FinancialActivityListResponse
```

Methods:

- <code title="get /financial-activity">client.financial_activity.<a href="./src/whop_sdk/resources/financial_activity.py">list</a>(\*\*<a href="src/whop_sdk/types/financial_activity_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/financial_activity_list_response.py">FinancialActivityListResponse</a></code>

# Stats

Types:

```python
from whop_sdk.types import StatRetrieveResponse, StatListResponse
```

Methods:

- <code title="get /stats/{metric}">client.stats.<a href="./src/whop_sdk/resources/stats.py">retrieve</a>(metric, \*\*<a href="src/whop_sdk/types/stat_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/stat_retrieve_response.py">StatRetrieveResponse</a></code>
- <code title="get /stats">client.stats.<a href="./src/whop_sdk/resources/stats.py">list</a>() -> <a href="./src/whop_sdk/types/stat_list_response.py">StatListResponse</a></code>

# Payouts

Types:

```python
from whop_sdk.types import PayoutCreateResponse, PayoutRetrieveResponse, PayoutListResponse
```

Methods:

- <code title="post /payouts">client.payouts.<a href="./src/whop_sdk/resources/payouts/payouts.py">create</a>(\*\*<a href="src/whop_sdk/types/payout_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/payout_create_response.py">PayoutCreateResponse</a></code>
- <code title="get /payouts/{id}">client.payouts.<a href="./src/whop_sdk/resources/payouts/payouts.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/payout_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/payout_retrieve_response.py">PayoutRetrieveResponse</a></code>
- <code title="get /payouts">client.payouts.<a href="./src/whop_sdk/resources/payouts/payouts.py">list</a>(\*\*<a href="src/whop_sdk/types/payout_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payout_list_response.py">SyncCursorPage[PayoutListResponse]</a></code>

## Methods

Types:

```python
from whop_sdk.types.payouts import (
    MethodCreateResponse,
    MethodUpdateResponse,
    MethodListResponse,
    MethodDeleteResponse,
)
```

Methods:

- <code title="post /payouts/methods">client.payouts.methods.<a href="./src/whop_sdk/resources/payouts/methods.py">create</a>(\*\*<a href="src/whop_sdk/types/payouts/method_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/payouts/method_create_response.py">MethodCreateResponse</a></code>
- <code title="patch /payouts/methods/{id}">client.payouts.methods.<a href="./src/whop_sdk/resources/payouts/methods.py">update</a>(id, \*\*<a href="src/whop_sdk/types/payouts/method_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/payouts/method_update_response.py">MethodUpdateResponse</a></code>
- <code title="get /payouts/methods">client.payouts.methods.<a href="./src/whop_sdk/resources/payouts/methods.py">list</a>(\*\*<a href="src/whop_sdk/types/payouts/method_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payouts/method_list_response.py">SyncCursorPageWithLimits[MethodListResponse]</a></code>
- <code title="delete /payouts/methods/{id}">client.payouts.methods.<a href="./src/whop_sdk/resources/payouts/methods.py">delete</a>(id) -> <a href="./src/whop_sdk/types/payouts/method_delete_response.py">MethodDeleteResponse</a></code>

## SupportedMethods

Types:

```python
from whop_sdk.types.payouts import SupportedMethodListResponse
```

Methods:

- <code title="get /payouts/supported_methods">client.payouts.supported_methods.<a href="./src/whop_sdk/resources/payouts/supported_methods.py">list</a>(\*\*<a href="src/whop_sdk/types/payouts/supported_method_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payouts/supported_method_list_response.py">SyncCursorPage[SupportedMethodListResponse]</a></code>

# Partners

Types:

```python
from whop_sdk.types import (
    PartnerCreateResponse,
    PartnerLeaderboardResponse,
    PartnerReferredUsersResponse,
)
```

Methods:

- <code title="post /partners">client.partners.<a href="./src/whop_sdk/resources/partners/partners.py">create</a>() -> <a href="./src/whop_sdk/types/partner_create_response.py">PartnerCreateResponse</a></code>
- <code title="get /partners/leaderboard">client.partners.<a href="./src/whop_sdk/resources/partners/partners.py">leaderboard</a>(\*\*<a href="src/whop_sdk/types/partner_leaderboard_params.py">params</a>) -> <a href="./src/whop_sdk/types/partner_leaderboard_response.py">PartnerLeaderboardResponse</a></code>
- <code title="get /partners/referred_users">client.partners.<a href="./src/whop_sdk/resources/partners/partners.py">referred_users</a>(\*\*<a href="src/whop_sdk/types/partner_referred_users_params.py">params</a>) -> <a href="./src/whop_sdk/types/partner_referred_users_response.py">PartnerReferredUsersResponse</a></code>

## Businesses

Types:

```python
from whop_sdk.types.partners import BusinessRetrieveResponse, BusinessListResponse
```

Methods:

- <code title="get /partners/businesses/{id}">client.partners.businesses.<a href="./src/whop_sdk/resources/partners/businesses/businesses.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/partners/business_retrieve_response.py">BusinessRetrieveResponse</a></code>
- <code title="get /partners/businesses">client.partners.businesses.<a href="./src/whop_sdk/resources/partners/businesses/businesses.py">list</a>(\*\*<a href="src/whop_sdk/types/partners/business_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/partners/business_list_response.py">SyncCursorPage[BusinessListResponse]</a></code>

### Earnings

Types:

```python
from whop_sdk.types.partners.businesses import EarningListResponse
```

Methods:

- <code title="get /partners/businesses/{id}/earnings">client.partners.businesses.earnings.<a href="./src/whop_sdk/resources/partners/businesses/earnings.py">list</a>(id, \*\*<a href="src/whop_sdk/types/partners/businesses/earning_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/partners/businesses/earning_list_response.py">SyncCursorPage[EarningListResponse]</a></code>

# Cards

Types:

```python
from whop_sdk.types import (
    CardCreateResponse,
    CardRetrieveResponse,
    CardUpdateResponse,
    CardListResponse,
)
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/whop_sdk/resources/cards.py">create</a>(\*\*<a href="src/whop_sdk/types/card_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/card_create_response.py">CardCreateResponse</a></code>
- <code title="get /cards/{id}">client.cards.<a href="./src/whop_sdk/resources/cards.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/card_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/card_retrieve_response.py">CardRetrieveResponse</a></code>
- <code title="patch /cards/{id}">client.cards.<a href="./src/whop_sdk/resources/cards.py">update</a>(id, \*\*<a href="src/whop_sdk/types/card_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/card_update_response.py">CardUpdateResponse</a></code>
- <code title="get /cards">client.cards.<a href="./src/whop_sdk/resources/cards.py">list</a>(\*\*<a href="src/whop_sdk/types/card_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/card_list_response.py">CardListResponse</a></code>

# CardTransactions

Types:

```python
from whop_sdk.types import CardTransaction
```

Methods:

- <code title="get /card_transactions/{id}">client.card_transactions.<a href="./src/whop_sdk/resources/card_transactions.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/card_transaction_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/card_transaction.py">CardTransaction</a></code>
- <code title="get /card_transactions">client.card_transactions.<a href="./src/whop_sdk/resources/card_transactions.py">list</a>(\*\*<a href="src/whop_sdk/types/card_transaction_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/card_transaction.py">SyncCursorPage[CardTransaction]</a></code>

# Swaps

Types:

```python
from whop_sdk.types import (
    SwapCreateResponse,
    SwapRetrieveResponse,
    SwapListResponse,
    SwapCreateQuoteResponse,
)
```

Methods:

- <code title="post /swaps">client.swaps.<a href="./src/whop_sdk/resources/swaps.py">create</a>(\*\*<a href="src/whop_sdk/types/swap_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/swap_create_response.py">SwapCreateResponse</a></code>
- <code title="get /swaps/{id}">client.swaps.<a href="./src/whop_sdk/resources/swaps.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/swap_retrieve_response.py">SwapRetrieveResponse</a></code>
- <code title="get /swaps">client.swaps.<a href="./src/whop_sdk/resources/swaps.py">list</a>(\*\*<a href="src/whop_sdk/types/swap_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/swap_list_response.py">SwapListResponse</a></code>
- <code title="post /swaps/quote">client.swaps.<a href="./src/whop_sdk/resources/swaps.py">create_quote</a>(\*\*<a href="src/whop_sdk/types/swap_create_quote_params.py">params</a>) -> <a href="./src/whop_sdk/types/swap_create_quote_response.py">SwapCreateQuoteResponse</a></code>

# Deposits

Types:

```python
from whop_sdk.types import DepositCreateResponse
```

Methods:

- <code title="post /deposits">client.deposits.<a href="./src/whop_sdk/resources/deposits.py">create</a>(\*\*<a href="src/whop_sdk/types/deposit_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/deposit_create_response.py">DepositCreateResponse</a></code>

# RecommendedActions

Types:

```python
from whop_sdk.types import (
    RecommendedActionRetrieveResponse,
    RecommendedActionListResponse,
    RecommendedActionListExecutionsResponse,
    RecommendedActionRunResponse,
)
```

Methods:

- <code title="get /recommended_actions/{id}">client.recommended_actions.<a href="./src/whop_sdk/resources/recommended_actions.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/recommended_action_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/recommended_action_retrieve_response.py">RecommendedActionRetrieveResponse</a></code>
- <code title="get /recommended_actions">client.recommended_actions.<a href="./src/whop_sdk/resources/recommended_actions.py">list</a>(\*\*<a href="src/whop_sdk/types/recommended_action_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/recommended_action_list_response.py">RecommendedActionListResponse</a></code>
- <code title="get /recommended_actions/{id}/executions">client.recommended_actions.<a href="./src/whop_sdk/resources/recommended_actions.py">list_executions</a>(id, \*\*<a href="src/whop_sdk/types/recommended_action_list_executions_params.py">params</a>) -> <a href="./src/whop_sdk/types/recommended_action_list_executions_response.py">RecommendedActionListExecutionsResponse</a></code>
- <code title="post /recommended_actions/{id}">client.recommended_actions.<a href="./src/whop_sdk/resources/recommended_actions.py">run</a>(id, \*\*<a href="src/whop_sdk/types/recommended_action_run_params.py">params</a>) -> <a href="./src/whop_sdk/types/recommended_action_run_response.py">RecommendedActionRunResponse</a></code>

# SetupIntents

Types:

```python
from whop_sdk.types import (
    SetupIntent,
    SetupIntentStatus,
    SetupIntentCreateResponse,
    SetupIntentListResponse,
    SetupIntentRetrieveStatusResponse,
    SetupIntentUpdateReturnURLResponse,
)
```

Methods:

- <code title="post /setup_intents">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">create</a>(\*\*<a href="src/whop_sdk/types/setup_intent_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/setup_intent_create_response.py">SetupIntentCreateResponse</a></code>
- <code title="get /setup_intents/{id}">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/setup_intent.py">SetupIntent</a></code>
- <code title="get /setup_intents">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">list</a>(\*\*<a href="src/whop_sdk/types/setup_intent_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/setup_intent_list_response.py">SyncCursorPage[SetupIntentListResponse]</a></code>
- <code title="get /setup_intents/{setup_intent_id}/status">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">retrieve_status</a>(setup_intent_id) -> <a href="./src/whop_sdk/types/setup_intent_retrieve_status_response.py">SetupIntentRetrieveStatusResponse</a></code>
- <code title="patch /setup_intents/{setup_intent_id}/return_url">client.setup_intents.<a href="./src/whop_sdk/resources/setup_intents.py">update_return_url</a>(setup_intent_id, \*\*<a href="src/whop_sdk/types/setup_intent_update_return_url_params.py">params</a>) -> <a href="./src/whop_sdk/types/setup_intent_update_return_url_response.py">SetupIntentUpdateReturnURLResponse</a></code>

# PaymentMethods

Types:

```python
from whop_sdk.types import PaymentMethodRetrieveResponse, PaymentMethodListResponse
```

Methods:

- <code title="get /payment_methods/{id}">client.payment_methods.<a href="./src/whop_sdk/resources/payment_methods.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/payment_method_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_method_retrieve_response.py">PaymentMethodRetrieveResponse</a></code>
- <code title="get /payment_methods">client.payment_methods.<a href="./src/whop_sdk/resources/payment_methods.py">list</a>(\*\*<a href="src/whop_sdk/types/payment_method_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_method_list_response.py">SyncCursorPage[PaymentMethodListResponse]</a></code>

# PaymentMethodDomains

Types:

```python
from whop_sdk.types import PaymentMethodDomain, PaymentMethodDomainDeleteResponse
```

Methods:

- <code title="post /payment_method_domains">client.payment_method_domains.<a href="./src/whop_sdk/resources/payment_method_domains.py">create</a>(\*\*<a href="src/whop_sdk/types/payment_method_domain_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_method_domain.py">PaymentMethodDomain</a></code>
- <code title="get /payment_method_domains/{id}">client.payment_method_domains.<a href="./src/whop_sdk/resources/payment_method_domains.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/payment_method_domain.py">PaymentMethodDomain</a></code>
- <code title="get /payment_method_domains">client.payment_method_domains.<a href="./src/whop_sdk/resources/payment_method_domains.py">list</a>(\*\*<a href="src/whop_sdk/types/payment_method_domain_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/payment_method_domain.py">SyncCursorPage[PaymentMethodDomain]</a></code>
- <code title="delete /payment_method_domains/{id}">client.payment_method_domains.<a href="./src/whop_sdk/resources/payment_method_domains.py">delete</a>(id) -> <a href="./src/whop_sdk/types/payment_method_domain_delete_response.py">PaymentMethodDomainDeleteResponse</a></code>
- <code title="post /payment_method_domains/{id}/verify">client.payment_method_domains.<a href="./src/whop_sdk/resources/payment_method_domains.py">verify</a>(id) -> <a href="./src/whop_sdk/types/payment_method_domain.py">PaymentMethodDomain</a></code>

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

# Verifications

Types:

```python
from whop_sdk.types import (
    VerificationErrorCode,
    VerificationStatus,
    VerificationCreateResponse,
    VerificationRetrieveResponse,
    VerificationUpdateResponse,
    VerificationListResponse,
)
```

Methods:

- <code title="post /verifications">client.verifications.<a href="./src/whop_sdk/resources/verifications.py">create</a>(\*\*<a href="src/whop_sdk/types/verification_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/verification_create_response.py">VerificationCreateResponse</a></code>
- <code title="get /verifications/{id}">client.verifications.<a href="./src/whop_sdk/resources/verifications.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/verification_retrieve_response.py">VerificationRetrieveResponse</a></code>
- <code title="patch /verifications/{id}">client.verifications.<a href="./src/whop_sdk/resources/verifications.py">update</a>(id, \*\*<a href="src/whop_sdk/types/verification_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/verification_update_response.py">VerificationUpdateResponse</a></code>
- <code title="get /verifications">client.verifications.<a href="./src/whop_sdk/resources/verifications.py">list</a>(\*\*<a href="src/whop_sdk/types/verification_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/verification_list_response.py">VerificationListResponse</a></code>

# Leads

Types:

```python
from whop_sdk.types import Lead, LeadListResponse
```

Methods:

- <code title="post /leads">client.leads.<a href="./src/whop_sdk/resources/leads.py">create</a>(\*\*<a href="src/whop_sdk/types/lead_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/lead.py">Lead</a></code>
- <code title="get /leads/{id}">client.leads.<a href="./src/whop_sdk/resources/leads.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/lead.py">Lead</a></code>
- <code title="patch /leads/{id}">client.leads.<a href="./src/whop_sdk/resources/leads.py">update</a>(id, \*\*<a href="src/whop_sdk/types/lead_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/lead.py">Lead</a></code>
- <code title="get /leads">client.leads.<a href="./src/whop_sdk/resources/leads.py">list</a>(\*\*<a href="src/whop_sdk/types/lead_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/lead_list_response.py">SyncCursorPage[LeadListResponse]</a></code>

# Topups

Types:

```python
from whop_sdk.types import TopupCreateResponse
```

Methods:

- <code title="post /topups">client.topups.<a href="./src/whop_sdk/resources/topups.py">create</a>(\*\*<a href="src/whop_sdk/types/topup_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/topup_create_response.py">TopupCreateResponse</a></code>

# Files

Types:

```python
from whop_sdk.types import FileVisibility, UploadStatus, FileCreateResponse, FileRetrieveResponse
```

Methods:

- <code title="post /files">client.files.<a href="./src/whop_sdk/resources/files.py">create</a>(\*\*<a href="src/whop_sdk/types/file_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /files/{id}">client.files.<a href="./src/whop_sdk/resources/files.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/file_retrieve_response.py">FileRetrieveResponse</a></code>

# CompanyTokenTransactions

Types:

```python
from whop_sdk.types import (
    CompanyTokenTransaction,
    CompanyTokenTransactionType,
    CompanyTokenTransactionListResponse,
)
```

Methods:

- <code title="post /company_token_transactions">client.company_token_transactions.<a href="./src/whop_sdk/resources/company_token_transactions.py">create</a>(\*\*<a href="src/whop_sdk/types/company_token_transaction_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/company_token_transaction.py">CompanyTokenTransaction</a></code>
- <code title="get /company_token_transactions/{id}">client.company_token_transactions.<a href="./src/whop_sdk/resources/company_token_transactions.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/company_token_transaction.py">CompanyTokenTransaction</a></code>
- <code title="get /company_token_transactions">client.company_token_transactions.<a href="./src/whop_sdk/resources/company_token_transactions.py">list</a>(\*\*<a href="src/whop_sdk/types/company_token_transaction_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/company_token_transaction_list_response.py">SyncCursorPage[CompanyTokenTransactionListResponse]</a></code>

# DmMembers

Types:

```python
from whop_sdk.types import (
    DmFeedMemberNotificationPreferences,
    DmFeedMemberStatuses,
    DmMember,
    DmMemberListResponse,
    DmMemberDeleteResponse,
)
```

Methods:

- <code title="post /dm_members">client.dm_members.<a href="./src/whop_sdk/resources/dm_members.py">create</a>(\*\*<a href="src/whop_sdk/types/dm_member_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/dm_member.py">DmMember</a></code>
- <code title="get /dm_members/{id}">client.dm_members.<a href="./src/whop_sdk/resources/dm_members.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/dm_member.py">DmMember</a></code>
- <code title="patch /dm_members/{id}">client.dm_members.<a href="./src/whop_sdk/resources/dm_members.py">update</a>(id, \*\*<a href="src/whop_sdk/types/dm_member_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/dm_member.py">DmMember</a></code>
- <code title="get /dm_members">client.dm_members.<a href="./src/whop_sdk/resources/dm_members.py">list</a>(\*\*<a href="src/whop_sdk/types/dm_member_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/dm_member_list_response.py">SyncCursorPage[DmMemberListResponse]</a></code>
- <code title="delete /dm_members/{id}">client.dm_members.<a href="./src/whop_sdk/resources/dm_members.py">delete</a>(id) -> <a href="./src/whop_sdk/types/dm_member_delete_response.py">DmMemberDeleteResponse</a></code>

# AIChats

Types:

```python
from whop_sdk.types import AIChat, NotificationPreferences, AIChatListResponse, AIChatDeleteResponse
```

Methods:

- <code title="post /ai_chats">client.ai_chats.<a href="./src/whop_sdk/resources/ai_chats.py">create</a>(\*\*<a href="src/whop_sdk/types/ai_chat_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/ai_chat.py">AIChat</a></code>
- <code title="get /ai_chats/{id}">client.ai_chats.<a href="./src/whop_sdk/resources/ai_chats.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/ai_chat.py">AIChat</a></code>
- <code title="patch /ai_chats/{id}">client.ai_chats.<a href="./src/whop_sdk/resources/ai_chats.py">update</a>(id, \*\*<a href="src/whop_sdk/types/ai_chat_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/ai_chat.py">AIChat</a></code>
- <code title="get /ai_chats">client.ai_chats.<a href="./src/whop_sdk/resources/ai_chats.py">list</a>(\*\*<a href="src/whop_sdk/types/ai_chat_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/ai_chat_list_response.py">SyncCursorPage[AIChatListResponse]</a></code>
- <code title="delete /ai_chats/{id}">client.ai_chats.<a href="./src/whop_sdk/resources/ai_chats.py">delete</a>(id) -> <a href="./src/whop_sdk/types/ai_chat_delete_response.py">AIChatDeleteResponse</a></code>

# DmChannels

Types:

```python
from whop_sdk.types import DmChannel, DmChannelListResponse, DmChannelDeleteResponse
```

Methods:

- <code title="post /dm_channels">client.dm_channels.<a href="./src/whop_sdk/resources/dm_channels.py">create</a>(\*\*<a href="src/whop_sdk/types/dm_channel_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/dm_channel.py">DmChannel</a></code>
- <code title="get /dm_channels/{id}">client.dm_channels.<a href="./src/whop_sdk/resources/dm_channels.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/dm_channel.py">DmChannel</a></code>
- <code title="patch /dm_channels/{id}">client.dm_channels.<a href="./src/whop_sdk/resources/dm_channels.py">update</a>(id, \*\*<a href="src/whop_sdk/types/dm_channel_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/dm_channel.py">DmChannel</a></code>
- <code title="get /dm_channels">client.dm_channels.<a href="./src/whop_sdk/resources/dm_channels.py">list</a>(\*\*<a href="src/whop_sdk/types/dm_channel_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/dm_channel_list_response.py">SyncCursorPage[DmChannelListResponse]</a></code>
- <code title="delete /dm_channels/{id}">client.dm_channels.<a href="./src/whop_sdk/resources/dm_channels.py">delete</a>(id) -> <a href="./src/whop_sdk/types/dm_channel_delete_response.py">DmChannelDeleteResponse</a></code>

# DisputeAlerts

Types:

```python
from whop_sdk.types import DisputeAlert, DisputeAlertType
```

Methods:

- <code title="get /dispute_alerts/{id}">client.dispute_alerts.<a href="./src/whop_sdk/resources/dispute_alerts.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/dispute_alert.py">DisputeAlert</a></code>
- <code title="get /dispute_alerts">client.dispute_alerts.<a href="./src/whop_sdk/resources/dispute_alerts.py">list</a>(\*\*<a href="src/whop_sdk/types/dispute_alert_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/dispute_alert.py">SyncCursorPage[DisputeAlert]</a></code>

# ResolutionCenterCases

Types:

```python
from whop_sdk.types import (
    ResolutionCenterCaseCreateResponse,
    ResolutionCenterCaseRetrieveResponse,
    ResolutionCenterCaseListResponse,
    ResolutionCenterCaseAcceptResponse,
    ResolutionCenterCaseAppealResponse,
    ResolutionCenterCaseDenyResponse,
    ResolutionCenterCaseEventsResponse,
    ResolutionCenterCaseReplyResponse,
    ResolutionCenterCaseRequestInfoResponse,
    ResolutionCenterCaseSummaryResponse,
    ResolutionCenterCaseWithdrawResponse,
)
```

Methods:

- <code title="post /resolution_center_cases">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">create</a>(\*\*<a href="src/whop_sdk/types/resolution_center_case_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_create_response.py">ResolutionCenterCaseCreateResponse</a></code>
- <code title="get /resolution_center_cases/{id}">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/resolution_center_case_retrieve_response.py">ResolutionCenterCaseRetrieveResponse</a></code>
- <code title="get /resolution_center_cases">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">list</a>(\*\*<a href="src/whop_sdk/types/resolution_center_case_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_list_response.py">SyncCursorPage[ResolutionCenterCaseListResponse]</a></code>
- <code title="post /resolution_center_cases/{id}/accept">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">accept</a>(id, \*\*<a href="src/whop_sdk/types/resolution_center_case_accept_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_accept_response.py">ResolutionCenterCaseAcceptResponse</a></code>
- <code title="post /resolution_center_cases/{id}/appeal">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">appeal</a>(id, \*\*<a href="src/whop_sdk/types/resolution_center_case_appeal_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_appeal_response.py">ResolutionCenterCaseAppealResponse</a></code>
- <code title="post /resolution_center_cases/{id}/deny">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">deny</a>(id, \*\*<a href="src/whop_sdk/types/resolution_center_case_deny_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_deny_response.py">ResolutionCenterCaseDenyResponse</a></code>
- <code title="get /resolution_center_cases/{id}/events">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">events</a>(id, \*\*<a href="src/whop_sdk/types/resolution_center_case_events_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_events_response.py">ResolutionCenterCaseEventsResponse</a></code>
- <code title="post /resolution_center_cases/{id}/reply">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">reply</a>(id, \*\*<a href="src/whop_sdk/types/resolution_center_case_reply_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_reply_response.py">ResolutionCenterCaseReplyResponse</a></code>
- <code title="post /resolution_center_cases/{id}/request_info">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">request_info</a>(id, \*\*<a href="src/whop_sdk/types/resolution_center_case_request_info_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_request_info_response.py">ResolutionCenterCaseRequestInfoResponse</a></code>
- <code title="get /resolution_center_cases/summary">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">summary</a>(\*\*<a href="src/whop_sdk/types/resolution_center_case_summary_params.py">params</a>) -> <a href="./src/whop_sdk/types/resolution_center_case_summary_response.py">ResolutionCenterCaseSummaryResponse</a></code>
- <code title="post /resolution_center_cases/{id}/withdraw">client.resolution_center_cases.<a href="./src/whop_sdk/resources/resolution_center_cases.py">withdraw</a>(id) -> <a href="./src/whop_sdk/types/resolution_center_case_withdraw_response.py">ResolutionCenterCaseWithdrawResponse</a></code>

# PayoutAccounts

Types:

```python
from whop_sdk.types import PayoutAccountCalculatedStatuses, PayoutAccountRetrieveResponse
```

Methods:

- <code title="get /payout_accounts/{id}">client.payout_accounts.<a href="./src/whop_sdk/resources/payout_accounts.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/payout_account_retrieve_response.py">PayoutAccountRetrieveResponse</a></code>

# Affiliates

Types:

```python
from whop_sdk.types import (
    Affiliate,
    Status,
    AffiliateListResponse,
    AffiliateArchiveResponse,
    AffiliateUnarchiveResponse,
)
```

Methods:

- <code title="post /affiliates">client.affiliates.<a href="./src/whop_sdk/resources/affiliates/affiliates.py">create</a>(\*\*<a href="src/whop_sdk/types/affiliate_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/affiliate.py">Affiliate</a></code>
- <code title="get /affiliates/{id}">client.affiliates.<a href="./src/whop_sdk/resources/affiliates/affiliates.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/affiliate.py">Affiliate</a></code>
- <code title="get /affiliates">client.affiliates.<a href="./src/whop_sdk/resources/affiliates/affiliates.py">list</a>(\*\*<a href="src/whop_sdk/types/affiliate_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/affiliate_list_response.py">SyncCursorPage[AffiliateListResponse]</a></code>
- <code title="post /affiliates/{id}/archive">client.affiliates.<a href="./src/whop_sdk/resources/affiliates/affiliates.py">archive</a>(id) -> <a href="./src/whop_sdk/types/affiliate_archive_response.py">AffiliateArchiveResponse</a></code>
- <code title="post /affiliates/{id}/unarchive">client.affiliates.<a href="./src/whop_sdk/resources/affiliates/affiliates.py">unarchive</a>(id) -> <a href="./src/whop_sdk/types/affiliate_unarchive_response.py">AffiliateUnarchiveResponse</a></code>

## Overrides

Types:

```python
from whop_sdk.types.affiliates import (
    AffiliateAppliesToPayments,
    AffiliateAppliesToProducts,
    AffiliateOverrideRoles,
    AffiliatePayoutTypes,
    AffiliateRevenueBases,
    OverrideCreateResponse,
    OverrideRetrieveResponse,
    OverrideUpdateResponse,
    OverrideListResponse,
    OverrideDeleteResponse,
)
```

Methods:

- <code title="post /affiliates/{id}/overrides">client.affiliates.overrides.<a href="./src/whop_sdk/resources/affiliates/overrides.py">create</a>(path_id, \*\*<a href="src/whop_sdk/types/affiliates/override_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/affiliates/override_create_response.py">OverrideCreateResponse</a></code>
- <code title="get /affiliates/{id}/overrides/{override_id}">client.affiliates.overrides.<a href="./src/whop_sdk/resources/affiliates/overrides.py">retrieve</a>(override_id, \*, id) -> <a href="./src/whop_sdk/types/affiliates/override_retrieve_response.py">OverrideRetrieveResponse</a></code>
- <code title="patch /affiliates/{id}/overrides/{override_id}">client.affiliates.overrides.<a href="./src/whop_sdk/resources/affiliates/overrides.py">update</a>(override_id, \*, id, \*\*<a href="src/whop_sdk/types/affiliates/override_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/affiliates/override_update_response.py">OverrideUpdateResponse</a></code>
- <code title="get /affiliates/{id}/overrides">client.affiliates.overrides.<a href="./src/whop_sdk/resources/affiliates/overrides.py">list</a>(id, \*\*<a href="src/whop_sdk/types/affiliates/override_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/affiliates/override_list_response.py">SyncCursorPage[OverrideListResponse]</a></code>
- <code title="delete /affiliates/{id}/overrides/{override_id}">client.affiliates.overrides.<a href="./src/whop_sdk/resources/affiliates/overrides.py">delete</a>(override_id, \*, id) -> <a href="./src/whop_sdk/types/affiliates/override_delete_response.py">OverrideDeleteResponse</a></code>

# Bounties

Types:

```python
from whop_sdk.types import Bounty, BountyListItem
```

Methods:

- <code title="post /bounties">client.bounties.<a href="./src/whop_sdk/resources/bounties/bounties.py">create</a>(\*\*<a href="src/whop_sdk/types/bounty_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounty.py">Bounty</a></code>
- <code title="get /bounties/{id}">client.bounties.<a href="./src/whop_sdk/resources/bounties/bounties.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/bounty.py">Bounty</a></code>
- <code title="patch /bounties/{id}">client.bounties.<a href="./src/whop_sdk/resources/bounties/bounties.py">update</a>(id, \*\*<a href="src/whop_sdk/types/bounty_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounty.py">Bounty</a></code>
- <code title="get /bounties">client.bounties.<a href="./src/whop_sdk/resources/bounties/bounties.py">list</a>(\*\*<a href="src/whop_sdk/types/bounty_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounty_list_item.py">SyncCursorPage[BountyListItem]</a></code>
- <code title="post /bounties/{id}/cancel">client.bounties.<a href="./src/whop_sdk/resources/bounties/bounties.py">cancel</a>(id) -> <a href="./src/whop_sdk/types/bounty.py">Bounty</a></code>

## Submissions

Types:

```python
from whop_sdk.types.bounties import PublicBountySubmission
```

Methods:

- <code title="get /bounties/{bounty_id}/submissions">client.bounties.submissions.<a href="./src/whop_sdk/resources/bounties/submissions.py">list</a>(bounty_id, \*\*<a href="src/whop_sdk/types/bounties/submission_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounties/public_bounty_submission.py">SyncCursorPage[PublicBountySubmission]</a></code>

# BountySubmissions

Types:

```python
from whop_sdk.types import BountyCaptureClip, BountySubmission, BountySubmissionDeleteResponse
```

Methods:

- <code title="post /bounty_submissions">client.bounty_submissions.<a href="./src/whop_sdk/resources/bounty_submissions.py">create</a>(\*\*<a href="src/whop_sdk/types/bounty_submission_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounty_submission.py">BountySubmission</a></code>
- <code title="get /bounty_submissions/{id}">client.bounty_submissions.<a href="./src/whop_sdk/resources/bounty_submissions.py">retrieve</a>(id) -> <a href="./src/whop_sdk/types/bounty_submission.py">BountySubmission</a></code>
- <code title="get /bounty_submissions">client.bounty_submissions.<a href="./src/whop_sdk/resources/bounty_submissions.py">list</a>(\*\*<a href="src/whop_sdk/types/bounty_submission_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounty_submission.py">SyncCursorPage[BountySubmission]</a></code>
- <code title="delete /bounty_submissions/{id}">client.bounty_submissions.<a href="./src/whop_sdk/resources/bounty_submissions.py">delete</a>(id) -> <a href="./src/whop_sdk/types/bounty_submission_delete_response.py">BountySubmissionDeleteResponse</a></code>
- <code title="post /bounty_submissions/{id}/submit">client.bounty_submissions.<a href="./src/whop_sdk/resources/bounty_submissions.py">submit</a>(id, \*\*<a href="src/whop_sdk/types/bounty_submission_submit_params.py">params</a>) -> <a href="./src/whop_sdk/types/bounty_submission.py">BountySubmission</a></code>

# AdCampaigns

Types:

```python
from whop_sdk.types import AdCampaign, AdCampaignDeleteResponse, AdCampaignDuplicateResponse
```

Methods:

- <code title="post /ad_campaigns">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">create</a>(\*\*<a href="src/whop_sdk/types/ad_campaign_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_campaign.py">AdCampaign</a></code>
- <code title="get /ad_campaigns/{id}">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/ad_campaign_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_campaign.py">AdCampaign</a></code>
- <code title="patch /ad_campaigns/{id}">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">update</a>(id, \*\*<a href="src/whop_sdk/types/ad_campaign_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_campaign.py">AdCampaign</a></code>
- <code title="get /ad_campaigns">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">list</a>(\*\*<a href="src/whop_sdk/types/ad_campaign_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_campaign.py">SyncCursorPage[AdCampaign]</a></code>
- <code title="delete /ad_campaigns/{id}">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">delete</a>(id) -> <a href="./src/whop_sdk/types/ad_campaign_delete_response.py">AdCampaignDeleteResponse</a></code>
- <code title="post /ad_campaigns/{id}/duplicate">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">duplicate</a>(id, \*\*<a href="src/whop_sdk/types/ad_campaign_duplicate_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_campaign_duplicate_response.py">AdCampaignDuplicateResponse</a></code>
- <code title="post /ad_campaigns/{id}/pause">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">pause</a>(id) -> <a href="./src/whop_sdk/types/ad_campaign.py">AdCampaign</a></code>
- <code title="post /ad_campaigns/{id}/retry_payment">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">retry_payment</a>(id) -> <a href="./src/whop_sdk/types/ad_campaign.py">AdCampaign</a></code>
- <code title="post /ad_campaigns/{id}/unpause">client.ad_campaigns.<a href="./src/whop_sdk/resources/ad_campaigns.py">unpause</a>(id) -> <a href="./src/whop_sdk/types/ad_campaign.py">AdCampaign</a></code>

# AdGroups

Types:

```python
from whop_sdk.types import (
    AdGroup,
    ReachEstimate,
    TargetingOption,
    AdGroupDeleteResponse,
    AdGroupDuplicateResponse,
    AdGroupSearchTargetingOptionsResponse,
)
```

Methods:

- <code title="post /ad_groups">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">create</a>(\*\*<a href="src/whop_sdk/types/ad_group_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_group.py">AdGroup</a></code>
- <code title="get /ad_groups/{id}">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/ad_group_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_group.py">AdGroup</a></code>
- <code title="patch /ad_groups/{id}">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">update</a>(id, \*\*<a href="src/whop_sdk/types/ad_group_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_group.py">AdGroup</a></code>
- <code title="get /ad_groups">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">list</a>(\*\*<a href="src/whop_sdk/types/ad_group_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_group.py">SyncCursorPage[AdGroup]</a></code>
- <code title="delete /ad_groups/{id}">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">delete</a>(id) -> <a href="./src/whop_sdk/types/ad_group_delete_response.py">AdGroupDeleteResponse</a></code>
- <code title="post /ad_groups/{id}/duplicate">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">duplicate</a>(id, \*\*<a href="src/whop_sdk/types/ad_group_duplicate_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_group_duplicate_response.py">AdGroupDuplicateResponse</a></code>
- <code title="post /ad_groups/estimate_reach">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">estimate_reach</a>(\*\*<a href="src/whop_sdk/types/ad_group_estimate_reach_params.py">params</a>) -> <a href="./src/whop_sdk/types/reach_estimate.py">ReachEstimate</a></code>
- <code title="post /ad_groups/{id}/pause">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">pause</a>(id) -> <a href="./src/whop_sdk/types/ad_group.py">AdGroup</a></code>
- <code title="get /ad_groups/targeting_options">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">search_targeting_options</a>(\*\*<a href="src/whop_sdk/types/ad_group_search_targeting_options_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_group_search_targeting_options_response.py">AdGroupSearchTargetingOptionsResponse</a></code>
- <code title="post /ad_groups/{id}/unpause">client.ad_groups.<a href="./src/whop_sdk/resources/ad_groups.py">unpause</a>(id) -> <a href="./src/whop_sdk/types/ad_group.py">AdGroup</a></code>

# Ads

Types:

```python
from whop_sdk.types import Ad, AdDeleteResponse, AdDuplicateResponse
```

Methods:

- <code title="post /ads">client.ads.<a href="./src/whop_sdk/resources/ads.py">create</a>(\*\*<a href="src/whop_sdk/types/ad_create_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad.py">Ad</a></code>
- <code title="get /ads/{id}">client.ads.<a href="./src/whop_sdk/resources/ads.py">retrieve</a>(id, \*\*<a href="src/whop_sdk/types/ad_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad.py">Ad</a></code>
- <code title="patch /ads/{id}">client.ads.<a href="./src/whop_sdk/resources/ads.py">update</a>(id, \*\*<a href="src/whop_sdk/types/ad_update_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad.py">Ad</a></code>
- <code title="get /ads">client.ads.<a href="./src/whop_sdk/resources/ads.py">list</a>(\*\*<a href="src/whop_sdk/types/ad_list_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad.py">SyncCursorPage[Ad]</a></code>
- <code title="delete /ads/{id}">client.ads.<a href="./src/whop_sdk/resources/ads.py">delete</a>(id) -> <a href="./src/whop_sdk/types/ad_delete_response.py">AdDeleteResponse</a></code>
- <code title="post /ads/{id}/duplicate">client.ads.<a href="./src/whop_sdk/resources/ads.py">duplicate</a>(id, \*\*<a href="src/whop_sdk/types/ad_duplicate_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_duplicate_response.py">AdDuplicateResponse</a></code>
- <code title="post /ads/{id}/pause">client.ads.<a href="./src/whop_sdk/resources/ads.py">pause</a>(id) -> <a href="./src/whop_sdk/types/ad.py">Ad</a></code>
- <code title="post /ads/{id}/unpause">client.ads.<a href="./src/whop_sdk/resources/ads.py">unpause</a>(id) -> <a href="./src/whop_sdk/types/ad.py">Ad</a></code>

# AdReports

Types:

```python
from whop_sdk.types import Granularities, ResultLabelKeys, AdReportRetrieveResponse
```

Methods:

- <code title="get /ad_reports">client.ad_reports.<a href="./src/whop_sdk/resources/ad_reports.py">retrieve</a>(\*\*<a href="src/whop_sdk/types/ad_report_retrieve_params.py">params</a>) -> <a href="./src/whop_sdk/types/ad_report_retrieve_response.py">AdReportRetrieveResponse</a></code>
