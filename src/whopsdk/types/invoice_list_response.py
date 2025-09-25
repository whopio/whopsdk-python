# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceListResponse", "Data", "DataCurrentPlan", "DataUser", "PageInfo"]


class DataCurrentPlan(BaseModel):
    id: str
    """The internal ID of the plan."""

    currency: Optional[
        Literal[
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
    ] = None
    """The respective currency identifier for the plan."""

    formatted_price: str
    """The formatted price (including currency) for the plan."""


class DataUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Data(BaseModel):
    id: str
    """The ID of the invoice."""

    created_at: int
    """The date the invoice was created."""

    current_plan: DataCurrentPlan
    """The plan that the invoice was created for."""

    due_date: Optional[int] = None
    """The date the invoice is due."""

    email_address: Optional[str] = None
    """The email address that the invoice was created for."""

    fetch_invoice_token: str
    """The token to fetch the invoice."""

    number: str
    """The number of the invoice."""

    status: Optional[Literal["open", "paid", "past_due", "void"]] = None
    """The status of the invoice."""

    user: Optional[DataUser] = None
    """The user that the invoice was created for."""


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None
    """When paginating forwards, the cursor to continue."""

    has_next_page: bool
    """When paginating forwards, are there more items?"""

    has_previous_page: bool
    """When paginating backwards, are there more items?"""

    start_cursor: Optional[str] = None
    """When paginating backwards, the cursor to continue."""


class InvoiceListResponse(BaseModel):
    data: Optional[List[Optional[Data]]] = None
    """A list of nodes."""

    page_info: PageInfo
    """Information to aid in pagination."""
