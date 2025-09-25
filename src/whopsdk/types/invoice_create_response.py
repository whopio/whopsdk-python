# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceCreateResponse", "Invoice", "InvoiceCurrentPlan", "InvoiceUser"]


class InvoiceCurrentPlan(BaseModel):
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


class InvoiceUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class Invoice(BaseModel):
    id: str
    """The ID of the invoice."""

    created_at: int
    """The date the invoice was created."""

    current_plan: InvoiceCurrentPlan
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

    user: Optional[InvoiceUser] = None
    """The user that the invoice was created for."""


class InvoiceCreateResponse(BaseModel):
    checkout_job_id: Optional[str] = None
    """The ID of the checkout job that was created for this invoice."""

    invoice: Optional[Invoice] = None
    """A statement that defines an amount due by a customer."""
