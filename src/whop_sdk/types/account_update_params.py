# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountUpdateParams", "BusinessAddress", "TaxIdentifier"]


class AccountUpdateParams(TypedDict, total=False):
    affiliate_application_required: bool
    """
    Whether prospective affiliates must submit an application before promoting this
    account.
    """

    affiliate_instructions: Optional[str]
    """Guidelines shown to affiliates promoting this account."""

    banner_image: Optional[Dict[str, object]]
    """Attachment input for the account banner image."""

    business_address: BusinessAddress
    """Account business address used to calculate tax.

    A complete address in a supported country is required when `tax_remitted_by` is
    `self`.
    """

    business_type: Optional[str]
    """High-level business category for the account."""

    country: Optional[str]
    """Country where the account is located."""

    description: Optional[str]
    """Account promotional description."""

    featured_affiliate_product_id: Optional[str]
    """The ID of the product to feature for affiliates. Pass `null` to clear."""

    home_preferences: SequenceNotStr[str]
    """Public account home page preferences."""

    industry_group: Optional[str]
    """Account industry group."""

    industry_type: Optional[str]
    """Specific industry vertical for the account."""

    invoice_prefix: Optional[str]
    """Prefix used for account invoices."""

    logo: Optional[Dict[str, object]]
    """Attachment input for the account logo."""

    metadata: Dict[str, object]
    """Arbitrary key/value metadata to store on the account."""

    onboarding_type: Optional[str]
    """The type of onboarding the account has completed."""

    opengraph_image: Optional[Dict[str, object]]
    """Attachment input for the account Open Graph image."""

    opengraph_image_variant: Optional[str]
    """The account Open Graph image variant."""

    other_business_description: Optional[str]
    """The description of the business type when business_type is other."""

    other_industry_description: Optional[str]
    """The description of the industry type when industry_type is other."""

    product_tax_code_id: Optional[str]
    """ID of the tax classification code applied by default to the account's products.

    See the available
    [product categories](https://docs.numeral.com/essentials/product-categories).
    """

    require_2fa: bool
    """
    Whether the account requires authorized users to have two-factor authentication
    enabled.
    """

    route: Optional[str]
    """The unique URL slug for the account."""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account."""

    show_joined_whops: bool
    """Whether the account appears in joined whops on other accounts."""

    show_reviews_dtc: bool
    """Whether reviews are displayed on direct-to-consumer product pages."""

    show_user_directory: bool
    """Whether the account shows users in the user directory."""

    social_links: Iterable[Dict[str, object]]
    """The full list of social links to display for the account."""

    store_page_config: Optional[Dict[str, object]]
    """Account store page display configuration."""

    target_audience: Optional[str]
    """The target audience for this account."""

    tax_collection_enabled_states: List[
        Literal[
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "DC",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY",
        ]
    ]
    """US state codes (50 states plus `DC`) where the account collects tax.

    Replaces the full set on update. Only settable when `tax_remitted_by` is `self`.
    """

    tax_identifiers: Iterable[TaxIdentifier]
    """Account tax/VAT registrations to add or update.

    When `tax_remitted_by` is `self`, tax is calculated and collected only in the
    countries where the account holds a registration.
    """

    tax_remitted_by: Literal["whop", "self", "none"]
    """
    Who calculates and remits tax for the account: `whop` (Whop calculates and
    remits), `self` (Whop calculates; the account collects and remits), or `none`
    (neither; the account is responsible). `self` requires a `business_address` in a
    supported country.
    """

    title: Optional[str]
    """The display name of the account."""

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image."""


class BusinessAddress(TypedDict, total=False):
    """Account business address used to calculate tax.

    A complete address in a supported country is required when `tax_remitted_by` is `self`.
    """

    city: Optional[str]
    """City name."""

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: str
    """First line of the street address."""

    line2: Optional[str]
    """Second line of the street address."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code, for example `CA`."""


class TaxIdentifier(TypedDict, total=False):
    tax_id_type: Required[
        Literal[
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
    ]
    """Tax ID type, for example `eu_vat`, `gb_vat`, or `us_ein`."""

    tax_id_value: Required[str]
    """Tax ID value, for example `DE123456789`."""
