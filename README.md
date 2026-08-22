# Whop Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fwhopio%2Fwhopsdk-python)
[![pypi](https://img.shields.io/pypi/v/whop_sdk)](https://pypi.python.org/pypi/whop_sdk)

The Whop Python library provides convenient access to the Whop APIs from Python.

## Table of Contents

- [Mcp Server](#mcp-server)
- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Usage](#async-usage)
- [Using Types](#using-types)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Nested Params](#nested-params)
- [Handling Errors](#handling-errors)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Versioning](#versioning)
- [Requirements](#requirements)
- [Contributing](#contributing)

## MCP Server

Use the Whop MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=%40whop%2Fmcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkB3aG9wL21jcCJdLCJlbnYiOnsiV0hPUF9BUElfS0VZIjoiTXkgQVBJIEtleSIsIldIT1BfV0VCSE9PS19TRUNSRVQiOiJNeSBXZWJob29rIEtleSIsIldIT1BfQVBQX0lEIjoiYXBwX3h4eHh4eHh4eHh4eHh4IiwiV0hPUF9BUElfVkVSU0lPTiI6IjIwMjYtMDctMDgtMSJ9fQ)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22%40whop%2Fmcp%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40whop%2Fmcp%22%5D%2C%22env%22%3A%7B%22WHOP_API_KEY%22%3A%22My%20API%20Key%22%2C%22WHOP_WEBHOOK_SECRET%22%3A%22My%20Webhook%20Key%22%2C%22WHOP_APP_ID%22%3A%22app_xxxxxxxxxxxxxx%22%2C%22WHOP_API_VERSION%22%3A%222026-07-08-1%22%7D%7D)

> Note: You may need to set environment variables in your MCP client.

## Documentation

The REST API documentation can be found on [docs.whop.com](https://docs.whop.com/apps). The full API of this library can be found in [api.md](api.md).

## Installation

```sh
pip install whop_sdk
```

## Reference

A full reference for this library is available [here](https://github.com/whopio/whopsdk-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from whop_sdk import Whop

client = Whop(
    token="<token>",
)

client.access_tokens.create()
```

## Async usage

Simply import `AsyncWhop` instead of `Whop` and use `await` with each API call:

```python
import os
import asyncio
from whop_sdk import AsyncWhop

client = AsyncWhop(
    api_key=os.environ.get("WHOP_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    page = await client.payments.list(
        company_id="biz_xxxxxxxxxxxxxx",
    )
    print(page.data)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install whop-sdk[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from whop_sdk import DefaultAioHttpClient
from whop_sdk import AsyncWhop


async def main() -> None:
    async with AsyncWhop(
        api_key=os.environ.get("WHOP_API_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        page = await client.payments.list(
            company_id="biz_xxxxxxxxxxxxxx",
        )
        print(page.data)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Environments

This SDK allows you to configure different environments for API requests.

```python
from whop_sdk import Whop
from whop_sdk.environment import WhopEnvironment

client = Whop(
    environment=WhopEnvironment.DEFAULT,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from whop_sdk import AsyncWhop

client = AsyncWhop(
    token="<token>",
)


async def main() -> None:
    await client.access_tokens.create()


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from whop_sdk.core.api_error import ApiError

try:
    client.access_tokens.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from whop_sdk import Whop

client = Whop(
    token="<token>",
)

client.accounts.list()
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.accounts.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from whop_sdk import Whop

client = Whop()

app = client.apps.create(
    company_id="biz_xxxxxxxxxxxxxx",
    name="name",
    icon={"id": "id"},
)
print(app.icon)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `whop_sdk.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `whop_sdk.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `whop_sdk.APIError`.

```python
import whop_sdk
from whop_sdk import Whop

client = Whop()

try:
    client.payments.list(
        company_id="biz_xxxxxxxxxxxxxx",
    )
except whop_sdk.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except whop_sdk.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except whop_sdk.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from whop_sdk import Whop

# Configure the default for all requests:
client = Whop(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).payments.list(
    company_id="biz_xxxxxxxxxxxxxx",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from whop_sdk import Whop

# Configure the default for all requests:
client = Whop(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Whop(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).payments.list(
    company_id="biz_xxxxxxxxxxxxxx",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from whop_sdk import Whop

client = Whop(...)
response = client.access_tokens.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.access_tokens.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from whop_sdk import Whop

client = Whop(..., timeout=20.0)

# Override timeout for a specific method
client.access_tokens.create(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from whop_sdk import Whop

client = Whop(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/whopio/whopsdk-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import whop_sdk
print(whop_sdk.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
