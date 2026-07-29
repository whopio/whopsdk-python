# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PlanCalculateTaxParams", "Address", "TaxID"]


class PlanCalculateTaxParams(TypedDict, total=False):
    address: Optional[Address]
    """Buyer billing address used for tax calculation.

    Provide either `address.country` or `ip_address`; include state and postal code
    when available for more accurate results.
    """

    ip_address: str
    """Buyer IP address used to infer location when no billing address is provided."""

    tax_ids: Optional[Iterable[TaxID]]
    """Optional buyer tax ID for B2B exemptions. At most one entry is supported."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Address(TypedDict, total=False):
    """Buyer billing address used for tax calculation.

    Provide either `address.country` or `ip_address`; include state and postal code when available for more accurate results.
    """

    country: Required[str]
    """ISO 3166-1 alpha-2 country code, such as `US`, `DE`, or `GB`."""

    city: Optional[str]
    """City name."""

    line1: Optional[str]
    """First line of the street address."""

    line2: Optional[str]
    """Second line of the street address."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code, such as `CA`."""


class TaxID(TypedDict, total=False):
    type: Literal[
        "ad_nrt",
        "ao_tin",
        "ar_cuit",
        "al_tin",
        "am_tin",
        "aw_tin",
        "au_abn",
        "au_arn",
        "eu_vat",
        "az_tin",
        "bs_tin",
        "bh_vat",
        "bd_bin",
        "bb_tin",
        "by_tin",
        "bj_ifu",
        "bo_tin",
        "ba_tin",
        "br_cnpj",
        "br_cpf",
        "bg_uic",
        "bf_ifu",
        "kh_tin",
        "cm_niu",
        "ca_bn",
        "ca_gst_hst",
        "ca_pst_bc",
        "ca_pst_mb",
        "ca_pst_sk",
        "ca_qst",
        "cv_nif",
        "cl_tin",
        "cn_tin",
        "co_nit",
        "cd_nif",
        "cr_tin",
        "hr_oib",
        "do_rcn",
        "ec_ruc",
        "eg_tin",
        "sv_nit",
        "et_tin",
        "eu_oss_vat",
        "ge_vat",
        "gh_tin",
        "de_stn",
        "gb_vat",
        "gn_nif",
        "hk_br",
        "hu_tin",
        "is_vat",
        "in_gst",
        "id_npwp",
        "il_vat",
        "jp_cn",
        "jp_rn",
        "jp_trn",
        "kz_bin",
        "ke_pin",
        "kg_tin",
        "la_tin",
        "li_uid",
        "li_vat",
        "my_frp",
        "my_itn",
        "my_sst",
        "mr_nif",
        "mx_rfc",
        "md_vat",
        "me_pib",
        "ma_vat",
        "np_pan",
        "nz_gst",
        "ng_tin",
        "mk_vat",
        "no_vat",
        "no_voec",
        "om_vat",
        "pe_ruc",
        "ph_tin",
        "ro_tin",
        "ru_inn",
        "ru_kpp",
        "sa_vat",
        "sn_ninea",
        "rs_pib",
        "sg_gst",
        "sg_uen",
        "si_tin",
        "za_vat",
        "kr_brn",
        "es_cif",
        "ch_uid",
        "ch_vat",
        "tw_vat",
        "tj_tin",
        "tz_vat",
        "th_vat",
        "tr_tin",
        "ug_tin",
        "ua_vat",
        "ae_trn",
        "us_ein",
        "uy_ruc",
        "uz_tin",
        "uz_vat",
        "ve_rif",
        "vn_tin",
        "zm_tin",
        "zw_tin",
        "sr_fin",
    ]
    """Tax ID type, such as `eu_vat` for an EU VAT number."""

    value: str
    """Tax ID value, for example `DE123456789`."""
