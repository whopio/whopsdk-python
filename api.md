# Shared Types

```python
from whopsdk.types import (
    AccessPassType,
    App,
    AppBuild,
    AppBuildPlatforms,
    AppBuildStatuses,
    AppStatuses,
    AppViewType,
    AuthorizedUserRoles,
    BusinessTypes,
    CollectionMethod,
    Company,
    CourseLessonInteraction,
    CourseLessonInteractionListItem,
    Currency,
    CustomCta,
    Direction,
    Entry,
    EntryStatus,
    ForumPost,
    GlobalAffiliateStatus,
    IndustryTypes,
    Invoice,
    InvoiceListItem,
    InvoiceStatus,
    Membership,
    MembershipStatus,
    PageInfo,
    Plan,
    PlanType,
    Product,
    ProductListItem,
    ReleaseMethod,
    Shipment,
    ShipmentCarrier,
    ShipmentStatus,
    ShipmentSubstatus,
    TaxType,
    Transfer,
    Visibility,
    VisibilityFilter,
)
```

# Apps

Types:

```python
from whopsdk.types import AppListResponse
```

Methods:

- <code title="post /apps">client.apps.<a href="./src/whopsdk/resources/apps.py">create</a>(\*\*<a href="src/whopsdk/types/app_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/app.py">App</a></code>
- <code title="get /apps/{id}">client.apps.<a href="./src/whopsdk/resources/apps.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/app.py">App</a></code>
- <code title="patch /apps/{id}">client.apps.<a href="./src/whopsdk/resources/apps.py">update</a>(id, \*\*<a href="src/whopsdk/types/app_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/app.py">App</a></code>
- <code title="get /apps">client.apps.<a href="./src/whopsdk/resources/apps.py">list</a>(\*\*<a href="src/whopsdk/types/app_list_params.py">params</a>) -> <a href="./src/whopsdk/types/app_list_response.py">SyncCursorPage[Optional[AppListResponse]]</a></code>

# Invoices

Types:

```python
from whopsdk.types import InvoiceCreateResponse, InvoiceVoidResponse
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">create</a>(\*\*<a href="src/whopsdk/types/invoice_create_params.py">params</a>) -> <a href="./src/whopsdk/types/invoice_create_response.py">InvoiceCreateResponse</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/whopsdk/resources/invoices.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/invoice.py">Invoice</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">list</a>(\*\*<a href="src/whopsdk/types/invoice_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/invoice_list_item.py">SyncCursorPage[Optional[InvoiceListItem]]</a></code>
- <code title="post /invoices/{id}/void">client.invoices.<a href="./src/whopsdk/resources/invoices.py">void</a>(id) -> <a href="./src/whopsdk/types/invoice_void_response.py">InvoiceVoidResponse</a></code>

# CourseLessonInteractions

Methods:

- <code title="get /course_lesson_interactions/{id}">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/course_lesson_interaction.py">CourseLessonInteraction</a></code>
- <code title="get /course_lesson_interactions">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">list</a>(\*\*<a href="src/whopsdk/types/course_lesson_interaction_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/course_lesson_interaction_list_item.py">SyncCursorPage[Optional[CourseLessonInteractionListItem]]</a></code>

# Products

Types:

```python
from whopsdk.types import ProductDeleteResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/whopsdk/resources/products.py">create</a>(\*\*<a href="src/whopsdk/types/product_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/product.py">Product</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/whopsdk/resources/products.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/product.py">Product</a></code>
- <code title="patch /products/{id}">client.products.<a href="./src/whopsdk/resources/products.py">update</a>(id, \*\*<a href="src/whopsdk/types/product_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/product.py">Product</a></code>
- <code title="get /products">client.products.<a href="./src/whopsdk/resources/products.py">list</a>(\*\*<a href="src/whopsdk/types/product_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/product_list_item.py">SyncCursorPage[Optional[ProductListItem]]</a></code>
- <code title="delete /products/{id}">client.products.<a href="./src/whopsdk/resources/products.py">delete</a>(id) -> <a href="./src/whopsdk/types/product_delete_response.py">ProductDeleteResponse</a></code>

# Companies

Methods:

- <code title="get /companies/{id}">client.companies.<a href="./src/whopsdk/resources/companies.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/company.py">Company</a></code>

# Webhooks

Types:

```python
from whopsdk.types import (
    InvoiceCreatedWebhookEvent,
    InvoicePaidWebhookEvent,
    InvoicePastDueWebhookEvent,
    InvoiceVoidedWebhookEvent,
    UnwrapWebhookEvent,
)
```

# Plans

Types:

```python
from whopsdk.types import PlanListResponse, PlanDeleteResponse
```

Methods:

- <code title="post /plans">client.plans.<a href="./src/whopsdk/resources/plans.py">create</a>(\*\*<a href="src/whopsdk/types/plan_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/plan.py">Plan</a></code>
- <code title="get /plans/{id}">client.plans.<a href="./src/whopsdk/resources/plans.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/plan.py">Plan</a></code>
- <code title="patch /plans/{id}">client.plans.<a href="./src/whopsdk/resources/plans.py">update</a>(id, \*\*<a href="src/whopsdk/types/plan_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/plan.py">Plan</a></code>
- <code title="get /plans">client.plans.<a href="./src/whopsdk/resources/plans.py">list</a>(\*\*<a href="src/whopsdk/types/plan_list_params.py">params</a>) -> <a href="./src/whopsdk/types/plan_list_response.py">SyncCursorPage[Optional[PlanListResponse]]</a></code>
- <code title="delete /plans/{id}">client.plans.<a href="./src/whopsdk/resources/plans.py">delete</a>(id) -> <a href="./src/whopsdk/types/plan_delete_response.py">PlanDeleteResponse</a></code>

# Entries

Types:

```python
from whopsdk.types import EntryListResponse, EntryApproveResponse
```

Methods:

- <code title="get /entries/{id}">client.entries.<a href="./src/whopsdk/resources/entries.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/entry.py">Entry</a></code>
- <code title="get /entries">client.entries.<a href="./src/whopsdk/resources/entries.py">list</a>(\*\*<a href="src/whopsdk/types/entry_list_params.py">params</a>) -> <a href="./src/whopsdk/types/entry_list_response.py">SyncCursorPage[Optional[EntryListResponse]]</a></code>
- <code title="post /entries/{id}/approve">client.entries.<a href="./src/whopsdk/resources/entries.py">approve</a>(id) -> <a href="./src/whopsdk/types/entry_approve_response.py">EntryApproveResponse</a></code>
- <code title="post /entries/{id}/deny">client.entries.<a href="./src/whopsdk/resources/entries.py">deny</a>(id) -> <a href="./src/whopsdk/types/shared/entry.py">Entry</a></code>

# ForumPosts

Types:

```python
from whopsdk.types import ForumPostListResponse
```

Methods:

- <code title="post /forum_posts">client.forum_posts.<a href="./src/whopsdk/resources/forum_posts.py">create</a>(\*\*<a href="src/whopsdk/types/forum_post_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/forum_post.py">ForumPost</a></code>
- <code title="get /forum_posts/{id}">client.forum_posts.<a href="./src/whopsdk/resources/forum_posts.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/forum_post.py">ForumPost</a></code>
- <code title="get /forum_posts">client.forum_posts.<a href="./src/whopsdk/resources/forum_posts.py">list</a>(\*\*<a href="src/whopsdk/types/forum_post_list_params.py">params</a>) -> <a href="./src/whopsdk/types/forum_post_list_response.py">SyncCursorPage[Optional[ForumPostListResponse]]</a></code>

# Transfers

Types:

```python
from whopsdk.types import TransferListResponse
```

Methods:

- <code title="post /transfers">client.transfers.<a href="./src/whopsdk/resources/transfers.py">create</a>(\*\*<a href="src/whopsdk/types/transfer_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/transfer.py">Transfer</a></code>
- <code title="get /transfers/{id}">client.transfers.<a href="./src/whopsdk/resources/transfers.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/transfer.py">Transfer</a></code>
- <code title="get /transfers">client.transfers.<a href="./src/whopsdk/resources/transfers.py">list</a>(\*\*<a href="src/whopsdk/types/transfer_list_params.py">params</a>) -> <a href="./src/whopsdk/types/transfer_list_response.py">SyncCursorPage[Optional[TransferListResponse]]</a></code>

# LedgerAccounts

Types:

```python
from whopsdk.types import LedgerAccountRetrieveResponse
```

Methods:

- <code title="get /ledger_accounts/{id}">client.ledger_accounts.<a href="./src/whopsdk/resources/ledger_accounts.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/ledger_account_retrieve_response.py">LedgerAccountRetrieveResponse</a></code>

# Memberships

Types:

```python
from whopsdk.types import MembershipListResponse
```

Methods:

- <code title="get /memberships/{id}">client.memberships.<a href="./src/whopsdk/resources/memberships.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/membership.py">Membership</a></code>
- <code title="patch /memberships/{id}">client.memberships.<a href="./src/whopsdk/resources/memberships.py">update</a>(id, \*\*<a href="src/whopsdk/types/membership_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/membership.py">Membership</a></code>
- <code title="get /memberships">client.memberships.<a href="./src/whopsdk/resources/memberships.py">list</a>(\*\*<a href="src/whopsdk/types/membership_list_params.py">params</a>) -> <a href="./src/whopsdk/types/membership_list_response.py">SyncCursorPage[Optional[MembershipListResponse]]</a></code>
- <code title="post /memberships/{id}/cancel">client.memberships.<a href="./src/whopsdk/resources/memberships.py">cancel</a>(id, \*\*<a href="src/whopsdk/types/membership_cancel_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/membership.py">Membership</a></code>

# AuthorizedUsers

Types:

```python
from whopsdk.types import AuthorizedUserRetrieveResponse, AuthorizedUserListResponse
```

Methods:

- <code title="get /authorized_users/{id}">client.authorized_users.<a href="./src/whopsdk/resources/authorized_users.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/authorized_user_retrieve_response.py">AuthorizedUserRetrieveResponse</a></code>
- <code title="get /authorized_users">client.authorized_users.<a href="./src/whopsdk/resources/authorized_users.py">list</a>(\*\*<a href="src/whopsdk/types/authorized_user_list_params.py">params</a>) -> <a href="./src/whopsdk/types/authorized_user_list_response.py">SyncCursorPage[Optional[AuthorizedUserListResponse]]</a></code>

# AppBuilds

Types:

```python
from whopsdk.types import AppBuildListResponse
```

Methods:

- <code title="post /app_builds">client.app_builds.<a href="./src/whopsdk/resources/app_builds.py">create</a>(\*\*<a href="src/whopsdk/types/app_build_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/app_build.py">AppBuild</a></code>
- <code title="get /app_builds/{id}">client.app_builds.<a href="./src/whopsdk/resources/app_builds.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/app_build.py">AppBuild</a></code>
- <code title="get /app_builds">client.app_builds.<a href="./src/whopsdk/resources/app_builds.py">list</a>(\*\*<a href="src/whopsdk/types/app_build_list_params.py">params</a>) -> <a href="./src/whopsdk/types/app_build_list_response.py">SyncCursorPage[Optional[AppBuildListResponse]]</a></code>
- <code title="post /app_builds/{id}/promote">client.app_builds.<a href="./src/whopsdk/resources/app_builds.py">promote</a>(id) -> <a href="./src/whopsdk/types/shared/app_build.py">AppBuild</a></code>

# Shipments

Types:

```python
from whopsdk.types import ShipmentListResponse
```

Methods:

- <code title="post /shipments">client.shipments.<a href="./src/whopsdk/resources/shipments.py">create</a>(\*\*<a href="src/whopsdk/types/shipment_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/shipment.py">Shipment</a></code>
- <code title="get /shipments/{id}">client.shipments.<a href="./src/whopsdk/resources/shipments.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/shipment.py">Shipment</a></code>
- <code title="get /shipments">client.shipments.<a href="./src/whopsdk/resources/shipments.py">list</a>(\*\*<a href="src/whopsdk/types/shipment_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shipment_list_response.py">SyncCursorPage[Optional[ShipmentListResponse]]</a></code>
