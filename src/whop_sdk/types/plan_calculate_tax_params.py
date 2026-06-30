# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlanCalculateTaxParams", "Address", "TaxID"]


class PlanCalculateTaxParams(TypedDict, total=False):
    address: Optional[Address]
    """The buyer's billing address. Provide this or ip_address."""

    ip_address: str
    """
    The buyer's IP address, used to resolve their location when no address is
    provided.
    """

    tax_ids: Optional[Iterable[TaxID]]
    """
    The buyer's tax IDs, such as a VAT number, used to apply B2B reverse-charge
    exemptions.
    """


class Address(TypedDict, total=False):
    """The buyer's billing address. Provide this or ip_address."""

    country: Required[str]
    """The two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    city: Optional[str]
    """The city name."""

    line1: Optional[str]
    """The first line of the street address."""

    line2: Optional[str]
    """The second line of the street address."""

    postal_code: Optional[str]
    """The postal or ZIP code."""

    state: Optional[str]
    """The state, province, or region code, for example `CA`."""


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
    """Tax ID type, for example `eu_vat`."""

    value: str
    """Tax ID number, for example `DE123456789`."""
