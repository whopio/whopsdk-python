# Shared Types

```python
from whopsdk.types import (
    AccessPass,
    AccessPassListItem,
    Company,
    CourseLessonInteraction,
    CourseLessonInteractionListItem,
    Invoice,
    InvoiceListItem,
    PageInfo,
)
```

# Invoices

Types:

```python
from whopsdk.types import (
    CollectionMethod,
    Currency,
    InvoiceStatus,
    InvoiceCreateResponse,
    InvoiceListResponse,
    InvoiceVoidResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">create</a>(\*\*<a href="src/whopsdk/types/invoice_create_params.py">params</a>) -> <a href="./src/whopsdk/types/invoice_create_response.py">Optional[InvoiceCreateResponse]</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/whopsdk/resources/invoices.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/invoice.py">Invoice</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">list</a>(\*\*<a href="src/whopsdk/types/invoice_list_params.py">params</a>) -> <a href="./src/whopsdk/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="post /invoices/{id}/void">client.invoices.<a href="./src/whopsdk/resources/invoices.py">void</a>(id) -> <a href="./src/whopsdk/types/invoice_void_response.py">Optional[InvoiceVoidResponse]</a></code>

# CourseLessonInteractions

Types:

```python
from whopsdk.types import CourseLessonInteractionListResponse
```

Methods:

- <code title="get /course_lesson_interactions/{id}">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/course_lesson_interaction.py">CourseLessonInteraction</a></code>
- <code title="get /course_lesson_interactions">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">list</a>(\*\*<a href="src/whopsdk/types/course_lesson_interaction_list_params.py">params</a>) -> <a href="./src/whopsdk/types/course_lesson_interaction_list_response.py">CourseLessonInteractionListResponse</a></code>

# AccessPasses

Types:

```python
from whopsdk.types import BusinessTypes, IndustryTypes, AccessPassListResponse
```

Methods:

- <code title="get /access_passes/{id}">client.access_passes.<a href="./src/whopsdk/resources/access_passes.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/access_pass.py">AccessPass</a></code>
- <code title="get /access_passes">client.access_passes.<a href="./src/whopsdk/resources/access_passes.py">list</a>(\*\*<a href="src/whopsdk/types/access_pass_list_params.py">params</a>) -> <a href="./src/whopsdk/types/access_pass_list_response.py">AccessPassListResponse</a></code>

# Companies

Methods:

- <code title="get /companies/{id}">client.companies.<a href="./src/whopsdk/resources/companies.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/shared/company.py">Company</a></code>
