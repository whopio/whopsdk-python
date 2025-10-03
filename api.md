# Shared Types

```python
from whopsdk.types import (
    AccessPassType,
    App,
    AppStatuses,
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
    GlobalAffiliateStatus,
    IndustryTypes,
    Invoice,
    InvoiceListItem,
    InvoiceStatus,
    PageInfo,
    Plan,
    PlanType,
    Product,
    ProductListItem,
    ReleaseMethod,
    TaxType,
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

- <code title="post /apps">client.apps.<a href="./src/whopsdk/resources/apps.py">create</a>(\*\*<a href="src/whopsdk/types/app_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/app.py">Optional[App]</a></code>
- <code title="get /apps/{id}">client.apps.<a href="./src/whopsdk/resources/apps.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/app.py">Optional[App]</a></code>
- <code title="patch /apps/{id}">client.apps.<a href="./src/whopsdk/resources/apps.py">update</a>(id, \*\*<a href="src/whopsdk/types/app_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/app.py">Optional[App]</a></code>
- <code title="get /apps">client.apps.<a href="./src/whopsdk/resources/apps.py">list</a>(\*\*<a href="src/whopsdk/types/app_list_params.py">params</a>) -> <a href="./src/whopsdk/types/app_list_response.py">SyncCursorPage[Optional[AppListResponse]]</a></code>

# Invoices

Types:

```python
from whopsdk.types import InvoiceCreateResponse, InvoiceVoidResponse
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">create</a>(\*\*<a href="src/whopsdk/types/invoice_create_params.py">params</a>) -> <a href="./src/whopsdk/types/invoice_create_response.py">Optional[InvoiceCreateResponse]</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/whopsdk/resources/invoices.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/invoice.py">Optional[Invoice]</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">list</a>(\*\*<a href="src/whopsdk/types/invoice_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/invoice_list_item.py">SyncCursorPage[Optional[InvoiceListItem]]</a></code>
- <code title="post /invoices/{id}/void">client.invoices.<a href="./src/whopsdk/resources/invoices.py">void</a>(id) -> <a href="./src/whopsdk/types/invoice_void_response.py">Optional[InvoiceVoidResponse]</a></code>

# CourseLessonInteractions

Methods:

- <code title="get /course_lesson_interactions/{id}">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/course_lesson_interaction.py">Optional[CourseLessonInteraction]</a></code>
- <code title="get /course_lesson_interactions">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">list</a>(\*\*<a href="src/whopsdk/types/course_lesson_interaction_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/course_lesson_interaction_list_item.py">SyncCursorPage[Optional[CourseLessonInteractionListItem]]</a></code>

# Products

Types:

```python
from whopsdk.types import ProductDeleteResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/whopsdk/resources/products.py">create</a>(\*\*<a href="src/whopsdk/types/product_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/product.py">Optional[Product]</a></code>
- <code title="get /products/{id}">client.products.<a href="./src/whopsdk/resources/products.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/product.py">Optional[Product]</a></code>
- <code title="patch /products/{id}">client.products.<a href="./src/whopsdk/resources/products.py">update</a>(id, \*\*<a href="src/whopsdk/types/product_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/product.py">Optional[Product]</a></code>
- <code title="get /products">client.products.<a href="./src/whopsdk/resources/products.py">list</a>(\*\*<a href="src/whopsdk/types/product_list_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/product_list_item.py">SyncCursorPage[Optional[ProductListItem]]</a></code>
- <code title="delete /products/{id}">client.products.<a href="./src/whopsdk/resources/products.py">delete</a>(id) -> <a href="./src/whopsdk/types/product_delete_response.py">Optional[ProductDeleteResponse]</a></code>

# Companies

Methods:

- <code title="get /companies/{id}">client.companies.<a href="./src/whopsdk/resources/companies.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/company.py">Optional[Company]</a></code>

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

- <code title="post /plans">client.plans.<a href="./src/whopsdk/resources/plans.py">create</a>(\*\*<a href="src/whopsdk/types/plan_create_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/plan.py">Optional[Plan]</a></code>
- <code title="get /plans/{id}">client.plans.<a href="./src/whopsdk/resources/plans.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/plan.py">Optional[Plan]</a></code>
- <code title="patch /plans/{id}">client.plans.<a href="./src/whopsdk/resources/plans.py">update</a>(id, \*\*<a href="src/whopsdk/types/plan_update_params.py">params</a>) -> <a href="./src/whopsdk/types/shared/plan.py">Optional[Plan]</a></code>
- <code title="get /plans">client.plans.<a href="./src/whopsdk/resources/plans.py">list</a>(\*\*<a href="src/whopsdk/types/plan_list_params.py">params</a>) -> <a href="./src/whopsdk/types/plan_list_response.py">SyncCursorPage[Optional[PlanListResponse]]</a></code>
- <code title="delete /plans/{id}">client.plans.<a href="./src/whopsdk/resources/plans.py">delete</a>(id) -> <a href="./src/whopsdk/types/plan_delete_response.py">Optional[PlanDeleteResponse]</a></code>

# Entries

Types:

```python
from whopsdk.types import EntryListResponse, EntryApproveResponse
```

Methods:

- <code title="get /entries/{id}">client.entries.<a href="./src/whopsdk/resources/entries.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/entry.py">Optional[Entry]</a></code>
- <code title="get /entries">client.entries.<a href="./src/whopsdk/resources/entries.py">list</a>(\*\*<a href="src/whopsdk/types/entry_list_params.py">params</a>) -> <a href="./src/whopsdk/types/entry_list_response.py">SyncCursorPage[Optional[EntryListResponse]]</a></code>
- <code title="post /entries/{id}/approve">client.entries.<a href="./src/whopsdk/resources/entries.py">approve</a>(id) -> <a href="./src/whopsdk/types/entry_approve_response.py">EntryApproveResponse</a></code>
- <code title="post /entries/{id}/deny">client.entries.<a href="./src/whopsdk/resources/entries.py">deny</a>(id) -> <a href="./src/whopsdk/types/shared/entry.py">Optional[Entry]</a></code>
