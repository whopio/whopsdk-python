# Invoices

Types:

```python
from whopsdk.types import (
    InvoiceCreateResponse,
    InvoiceRetrieveResponse,
    InvoiceListResponse,
    InvoiceVoidResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">create</a>() -> <a href="./src/whopsdk/types/invoice_create_response.py">Optional[InvoiceCreateResponse]</a></code>
- <code title="get /invoices/{:id}">client.invoices.<a href="./src/whopsdk/resources/invoices.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/whopsdk/resources/invoices.py">list</a>() -> <a href="./src/whopsdk/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="post /invoices/{:id}/void">client.invoices.<a href="./src/whopsdk/resources/invoices.py">void</a>(id) -> <a href="./src/whopsdk/types/invoice_void_response.py">Optional[InvoiceVoidResponse]</a></code>

# CourseLessonInteractions

Types:

```python
from whopsdk.types import (
    CourseLessonInteractionRetrieveResponse,
    CourseLessonInteractionListResponse,
)
```

Methods:

- <code title="get /course_lesson_interactions/{:id}">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">retrieve</a>(id) -> <a href="./src/whopsdk/types/course_lesson_interaction_retrieve_response.py">CourseLessonInteractionRetrieveResponse</a></code>
- <code title="get /course_lesson_interactions">client.course_lesson_interactions.<a href="./src/whopsdk/resources/course_lesson_interactions.py">list</a>() -> <a href="./src/whopsdk/types/course_lesson_interaction_list_response.py">CourseLessonInteractionListResponse</a></code>
