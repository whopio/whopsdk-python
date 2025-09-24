# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceListResponse", "Data", "DataCurrentPlan", "DataMember", "PageInfo"]


class DataCurrentPlan(BaseModel):
    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    base_currency: Literal[
        "usd",
        "sgd",
        "inr",
        "aud",
        "brl",
        "cad",
        "dkk",
        "eur",
        "nok",
        "gbp",
        "sek",
        "chf",
        "hkd",
        "huf",
        "jpy",
        "mxn",
        "myr",
        "pln",
        "czk",
        "nzd",
        "aed",
        "eth",
        "ape",
        "cop",
        "ron",
        "thb",
        "bgn",
        "idr",
        "dop",
        "php",
        "try",
        "krw",
        "twd",
        "vnd",
        "pkr",
        "clp",
        "uyu",
        "ars",
        "zar",
        "dzd",
        "tnd",
        "mad",
        "kes",
        "kwd",
        "jod",
        "all",
        "xcd",
        "amd",
        "bsd",
        "bhd",
        "bob",
        "bam",
        "khr",
        "crc",
        "xof",
        "egp",
        "etb",
        "gmd",
        "ghs",
        "gtq",
        "gyd",
        "ils",
        "jmd",
        "mop",
        "mga",
        "mur",
        "mdl",
        "mnt",
        "nad",
        "ngn",
        "mkd",
        "omr",
        "pyg",
        "pen",
        "qar",
        "rwf",
        "sar",
        "rsd",
        "lkr",
        "tzs",
        "ttd",
        "uzs",
        "rub",
        "btc",
    ]
    """The available currencies on the platform"""

    formatted_price: str
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class DataMember(BaseModel):
    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    email: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    name: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    username: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class Data(BaseModel):
    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: int
    """A valid timestamp in seconds, transported as an integer"""

    current_plan: DataCurrentPlan
    """A plan for an access pass."""

    due_date: Optional[int] = None
    """A valid timestamp in seconds, transported as an integer"""

    email_address: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    fetch_invoice_token: str
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    member: Optional[DataMember] = None
    """A user of the site."""

    number: str
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    status: Literal["open", "paid", "past_due", "void"]
    """The different statuses an invoice can be in"""


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    has_next_page: bool
    """Represents `true` or `false` values."""

    has_previous_page: bool
    """Represents `true` or `false` values."""

    start_cursor: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class InvoiceListResponse(BaseModel):
    data: Optional[List[Optional[Data]]] = None

    page_info: PageInfo
    """Information about pagination in a connection."""
