# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceCreateResponse", "Invoice", "InvoiceCurrentPlan", "InvoiceMember"]


class InvoiceCurrentPlan(BaseModel):
    id: str

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

    formatted_price: str


class InvoiceMember(BaseModel):
    id: str

    email: Optional[str] = None

    name: Optional[str] = None

    username: Optional[str] = None


class Invoice(BaseModel):
    id: str

    created_at: int

    current_plan: InvoiceCurrentPlan

    due_date: Optional[int] = None

    email_address: Optional[str] = None

    fetch_invoice_token: str

    member: Optional[InvoiceMember] = None

    number: str

    status: Literal["open", "paid", "past_due", "void"]


class InvoiceCreateResponse(BaseModel):
    checkout_job_id: Optional[str] = None

    invoice: Optional[Invoice] = None
