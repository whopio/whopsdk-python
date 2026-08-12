# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .account_social_link import AccountSocialLink

__all__ = [
    "Account",
    "Balance",
    "BalanceBreakdown",
    "BalanceBreakdownPendingSettlement",
    "Capabilities",
    "Cards",
    "CompanyFormation",
    "CompanyFormationDocument",
    "CompanyFormationSignatures",
    "CompanyFormationSignaturesForm8821",
    "CompanyFormationSignaturesSs4",
    "Owner",
    "OwnerProfilePicture",
    "ParentAccount",
    "PaymentControls",
    "PaymentControlsDisputeAlertAutoRefund",
    "PaymentControlsReserve",
    "PaymentControlsResolutionCenterAutoRefund",
    "RecommendedAction",
    "RequiredAction",
    "StorePageConfig",
    "TaxIdentifier",
    "Wallet",
]


class BalanceBreakdownPendingSettlement(BaseModel):
    """When the pending amount is expected to settle, one entry per day, earliest first.

    Money with no scheduled settlement day, such as a transfer in flight, is left out — so these can sum to less than `pending`, never more.
    """

    amount: str
    """Amount expected that day, in native units, as a decimal string."""

    date: str
    """The day this money is expected to finish settling, as an ISO 8601 date."""


class BalanceBreakdown(BaseModel):
    """
    Balance split into available, pending, and reserve amounts, as native-unit decimal strings, with the days the pending amount is expected to settle. On-chain crypto is entirely available; good_funds and fiat cash can have pending or reserve portions.
    """

    available: str
    """
    Amount you can spend, send, or withdraw now, in native units, as a decimal
    string.
    """

    pending: str
    """
    Amount from recent payments still settling, in native units, as a decimal
    string.
    """

    pending_settlements: List[BalanceBreakdownPendingSettlement]

    reserve: str
    """Amount held back, in native units, as a decimal string.

    Retrieve the account's reserves for why it is held and when it unlocks.
    """


class Balance(BaseModel):
    """Account holdings, each with USD value. Empty when `total_usd` is `null`."""

    balance: str
    """Total amount held in native units, as a decimal string."""

    breakdown: BalanceBreakdown
    """
    Balance split into available, pending, and reserve amounts, as native-unit
    decimal strings, with the days the pending amount is expected to settle.
    On-chain crypto is entirely available; good_funds and fiat cash can have pending
    or reserve portions.
    """

    icon_url: Optional[str] = None
    """Holding icon URL."""

    name: str
    """The holding's display name"""

    price_usd: Optional[float] = None
    """USD price per unit, or `null` when no exchange rate is available."""

    symbol: str
    """Holding display symbol, such as `USDT`, `cbBTC`, or `EUR`."""

    value_usd: Optional[str] = None
    """Holding USD value, or `null` when no exchange rate is available."""


class Capabilities(BaseModel):
    """
    Payment rails enabled for this account, each `active`, `inactive`, or `pending` (onboarding or review in progress). Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    accept_bank_payments: Literal["active", "inactive", "pending"]
    """Bank payins: debits, transfers, and local bank rails"""

    accept_bnpl_payments: Literal["active", "inactive", "pending"]
    """Buy-now-pay-later payins; requires approval"""

    accept_card_payments: Literal["active", "inactive", "pending"]
    """Card payins, including Apple Pay and Google Pay"""

    bank_deposit: Literal["active", "inactive", "pending"]
    """Deposits by bank wire or ACH to the account's virtual bank account"""

    card_deposit: Literal["active", "inactive", "pending"]
    """Balance top-ups by charging a stored payment method"""

    card_issuing: Literal["active", "inactive", "pending"]
    """Issuing Whop cards; requires card application approval"""

    crypto_deposit: Literal["active", "inactive", "pending"]
    """On-chain deposits to the account's crypto wallet"""

    crypto_payout: Literal["active", "inactive", "pending"]
    """On-chain payouts to a crypto wallet"""

    instant_payout: Literal["active", "inactive", "pending"]
    """Instant payouts to an eligible payout destination"""

    run_ads: Literal["active", "inactive", "pending"]
    """Launching ad campaigns through Whop Ads.

    `inactive` while a requested ads services agreement is awaiting the account's
    signature.
    """

    standard_payout: Literal["active", "inactive", "pending"]
    """Standard payouts to an external payout destination"""

    transfer: Literal["active", "inactive", "pending"]
    """Transfers to other accounts"""


class Cards(BaseModel):
    """Whop Cards application details for the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise, or when the account has no card application.
    """

    kind: Optional[Literal["individual", "business"]] = None
    """
    Whether the card application verifies a business (`business`, KYB) or a person
    (`individual`, consumer identity). `null` when the application is not yet linked
    to a verification.
    """

    status: Literal[
        "approved",
        "pending",
        "manual_review",
        "denied",
        "locked",
        "canceled",
        "needs_verification",
        "needs_information",
    ]
    """Where the card application stands.

    `approved` means cards can be issued. `needs_verification` means the applicant
    has not completed identity verification yet; `needs_information` means they did,
    but the documents were rejected for a fixable reason and must be resubmitted.
    `pending` and `manual_review` are in flight. `denied`, `locked`, and `canceled`
    are terminal.
    """


class CompanyFormationDocument(BaseModel):
    """
    Formation documents available for download, such as the Articles of Organization and the EIN confirmation letter. Present once `status` leaves `draft`.
    """

    id: str
    """Document ID, prefixed `file_`."""

    name: str
    """Human-readable document name, such as `Articles of Organization`."""

    type: str
    """
    Document category: `articles_of_organization`, `operating_agreement`,
    `ein_letter`, `signed_ss4`, `signed_form8821`, or `mail` for postal
    correspondence received on the company's behalf.
    """

    url: str
    """CDN URL for downloading the document."""


class CompanyFormationSignaturesForm8821(BaseModel):
    """Signature state for IRS Form 8821, the tax information authorization.

    Present only while the form still needs the founder's action.
    """

    status: Literal["pending", "unknown"]
    """
    `pending` when a signing session is ready for the founder; `unknown` when the
    signature state could not be determined.
    """

    expires_at: Optional[str] = None
    """When the signing URL expires, as an ISO 8601 timestamp.

    Present while `status` is `pending`.
    """

    url: Optional[str] = None
    """Hosted signing URL where the founder completes the form.

    Present while `status` is `pending`.
    """


class CompanyFormationSignaturesSs4(BaseModel):
    """Signature state for IRS Form SS-4, the EIN application.

    Present only while the form still needs the founder's action.
    """

    status: Literal["pending", "unknown"]
    """
    `pending` when a signing session is ready for the founder; `unknown` when the
    signature state could not be determined.
    """

    expires_at: Optional[str] = None
    """When the signing URL expires, as an ISO 8601 timestamp.

    Present while `status` is `pending`.
    """

    url: Optional[str] = None
    """Hosted signing URL where the founder completes the form.

    Present while `status` is `pending`.
    """


class CompanyFormationSignatures(BaseModel):
    """IRS forms still awaiting a founder's signature, each with a hosted signing URL.

    Present once `status` leaves `draft`; empty when nothing needs signing.
    """

    form8821: Optional[CompanyFormationSignaturesForm8821] = None
    """Signature state for IRS Form 8821, the tax information authorization.

    Present only while the form still needs the founder's action.
    """

    ss4: Optional[CompanyFormationSignaturesSs4] = None
    """Signature state for IRS Form SS-4, the EIN application.

    Present only while the form still needs the founder's action.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class CompanyFormation(BaseModel):
    """
    Company formation state for the account, managed through [Form Company](/api-reference/beta/accounts/form-company). A `draft` `status` until the formation checkout is paid, then filing progress with downloadable documents and signatures awaiting action. Empty when the formation state is temporarily unavailable.
    """

    documents: Optional[List[CompanyFormationDocument]] = None

    ein_registered: Optional[bool] = None
    """Whether the company's EIN has been issued by the IRS.

    Present once `status` leaves `draft`.
    """

    legal_name: Optional[str] = None
    """Registered company name including the entity ending, for example `Acme, LLC`.

    Present once `status` leaves `draft`.
    """

    signatures: Optional[CompanyFormationSignatures] = None
    """IRS forms still awaiting a founder's signature, each with a hosted signing URL.

    Present once `status` leaves `draft`; empty when nothing needs signing.
    """

    state_registered: Optional[bool] = None
    """Whether the state formation filing is complete.

    Present once `status` leaves `draft`.
    """

    status: Optional[Literal["draft", "processing", "filed", "rejected", "completed"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OwnerProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class Owner(BaseModel):
    """The single user who owns the account, whose email is the `email` above.

    Distinct from the `owner` role on team members, which any number of them can hold.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: OwnerProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class ParentAccount(BaseModel):
    """Parent account for connected accounts, or `null` for standalone accounts."""

    id: str
    """Account ID, prefixed `biz_`."""

    logo_url: Optional[str] = None
    """Account logo image URL."""

    route: str
    """Account public route identifier."""

    title: str
    """Account display name."""


class PaymentControlsDisputeAlertAutoRefund(BaseModel):
    """Automatic refund settings for pre-chargeback dispute alerts."""

    locked: bool
    """Whether the account owner is prevented from changing this threshold."""

    threshold_usd: Optional[float] = None
    """Maximum dispute alert amount automatically refunded in USD.

    `null` when automatic refunds are disabled.
    """


class PaymentControlsReserve(BaseModel):
    """Reserve currently applied to incoming payment volume."""

    hold_period_days: int
    """Number of days reserved funds are held before release."""

    percentage: Optional[float] = None
    """Percentage of incoming payment volume held in reserve.

    `null` when no reserve is applied.
    """


class PaymentControlsResolutionCenterAutoRefund(BaseModel):
    """Automatic refund settings for resolution center cases."""

    card_threshold_usd: Optional[float] = None
    """Maximum card-funded resolution center case amount automatically refunded in USD.

    `null` when automatic refunds are disabled for cards.
    """

    financing_threshold_usd: Optional[float] = None
    """
    Maximum financing-funded resolution center case amount automatically refunded in
    USD. `null` when automatic refunds are disabled for financing.
    """

    locked: bool
    """Whether the account owner is prevented from changing these thresholds."""

    paypal_threshold_usd: Optional[float] = None
    """
    Maximum PayPal-funded resolution center case amount automatically refunded in
    USD. `null` when automatic refunds are disabled for PayPal.
    """


class PaymentControls(BaseModel):
    """Payment health controls currently applied to the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    dispute_alert_auto_refund: PaymentControlsDisputeAlertAutoRefund
    """Automatic refund settings for pre-chargeback dispute alerts."""

    dispute_alert_fee_usd: Optional[float] = None
    """Fee charged for each dispute alert in USD. `null` when unavailable."""

    enforce_3ds: bool
    """Whether 3-D Secure is forced on every card payment at checkout.

    The account cannot bypass it while set.
    """

    financing_disabled: bool
    """Whether payment health controls explicitly disable financing.

    This is independent of financing approval in
    `capabilities.accept_bnpl_payments`.
    """

    high_risk_processing_fee_percentage: float
    """Additional processing fee percentage for high-risk processing."""

    pending_auto_topup_fee_percentage: float
    """
    Percentage fee charged when pending, not-yet-settled balance is advanced to fund
    the account's cards balance, where `2` means 2%. `0` when the account is exempt.
    """

    pending_balance_delay_days: int
    """Additional days payments remain pending before becoming available."""

    reserve: PaymentControlsReserve
    """Reserve currently applied to incoming payment volume."""

    resolution_center_auto_refund: PaymentControlsResolutionCenterAutoRefund
    """Automatic refund settings for resolution center cases."""

    restricted_payment_methods: List[
        Literal["card_visa", "card_mastercard", "card_american_express", "card_discover_global_network"]
    ]


class RecommendedAction(BaseModel):
    """
    Deprecated: use the `GET /accounts/{account_id}/recommend_actions` endpoint instead. Optional actions that unlock capabilities or grow the account, same shape as `required_actions`. Computed only on `retrieve` and `me`; `null` otherwise.
    """

    action: Literal[
        "theme_business",
        "create_product",
        "create_plan",
        "verify_identity",
        "connect_affiliate_program",
        "create_promotion",
        "setup_tracking_pixel",
        "migrate_from_stripe",
        "accept_first_payment",
        "launch_first_ad",
        "launch_draft_campaign",
        "increase_ad_budget",
        "refresh_ad_creatives",
        "fix_ad_billing",
        "exclude_customers_from_ads",
        "retarget_abandoned_checkouts",
        "fix_funnel_dropoff",
        "invite_team_member",
        "enable_tax_collection",
        "create_card",
        "apply_for_financing",
    ]
    """
    The recommendation; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: str
    """The URL the call-to-action links to"""

    cta_label: str
    """Button label"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """Illustration icon URL, or `null`"""

    impact_score: Optional[int] = None
    """Estimated impact from 0-100, or `null` when not ranked"""

    reasoning: Optional[str] = None
    """Why this action was recommended, or `null`"""

    status: Literal["optional"]
    """Always optional — never blocking"""

    title: str
    """Headline for the recommendation"""


class RequiredAction(BaseModel):
    """
    Actions the account owner must take to unblock capabilities like payouts and card spend, ordered by display priority. Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    action: Literal[
        "deposit_funds",
        "submit_information_request",
        "verify_identity",
        "sign_formation_documents",
        "connect_fulfillment_tracker",
        "setup_apple_pay_domains",
        "configure_tax_remitter",
        "add_vat_registration",
    ]
    """
    What the holder must do; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: Optional[str] = None
    """The URL the call-to-action links to, or null when there is no button"""

    cta_label: str
    """Button label, or empty when there is no button"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """The URL of the action's illustration icon, or null if it has none"""

    status: Literal["required", "pending"]
    """required (act now) or pending (under review)"""

    title: str
    """Headline for the action"""


class StorePageConfig(BaseModel):
    """Account store page display configuration."""

    accent_color: Optional[
        Literal[
            "ruby",
            "tomato",
            "red",
            "crimson",
            "pink",
            "plum",
            "purple",
            "violet",
            "iris",
            "cyan",
            "teal",
            "jade",
            "green",
            "grass",
            "brown",
            "blue",
            "orange",
            "indigo",
            "sky",
            "mint",
            "yellow",
            "amber",
            "lime",
            "lemon",
            "magenta",
            "gold",
            "bronze",
            "gray",
        ]
    ] = None
    """Accent color used on the account store page."""

    layout: Optional[Literal["featured", "compact"]] = None
    """Layout used on the account store page."""

    profile_variant: Optional[Literal["personal", "business"]] = None
    """Profile presentation used on the account store page."""

    whop_affiliate_link: bool
    """Whether the account store page shows a Whop affiliate link."""


class TaxIdentifier(BaseModel):
    """Account tax/VAT registrations. Empty when none are set."""

    id: str
    """Tax identifier ID."""

    tax_id_type: Literal[
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
        "pl_nip",
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
        "xi_vat",
    ]
    """Tax ID type."""

    tax_id_value: str
    """Tax ID value."""


class Wallet(BaseModel):
    """Account primary crypto wallet, or `null` if none has been provisioned."""

    id: str
    """Wallet ID, prefixed `wallet_`."""

    address: str
    """The on-chain address of the wallet"""

    network: Literal["solana", "ethereum", "bitcoin"]
    """The blockchain network the wallet lives on"""


class Account(BaseModel):
    id: str
    """Account ID, prefixed `biz_`."""

    balances: List[Balance]

    banner_image_url: Optional[str] = None
    """Account banner image URL."""

    business_address: Optional[object] = None
    """
    Account business address used to calculate tax, with `line1`, `line2`, `city`,
    `state`, `postal_code`, and `country`. `null` when no address is set.
    """

    business_type: Optional[
        Literal[
            "education_program",
            "coaching",
            "software",
            "paid_group",
            "newsletter",
            "agency",
            "physical_products",
            "brick_and_mortar",
            "events",
            "coaching_and_courses",
            "other",
            "services",
            "gig_economy",
            "marketplace",
            "telehealth",
            "class_action_settlement",
            "physical_product",
            "saas",
            "course",
            "community",
        ]
    ] = None
    """High-level business category for the account.

    See the
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary)
    for valid values.
    """

    can_transfer_pending_balance_to_children: bool
    """
    Whether pending funds may be transferred from this platform account to its
    connected accounts.
    """

    capabilities: Optional[Capabilities] = None
    """
    Payment rails enabled for this account, each `active`, `inactive`, or `pending`
    (onboarding or review in progress). Computed only on `retrieve` and `me` for
    callers with `company:balance:read` scope; `null` otherwise.
    """

    cards: Optional[Cards] = None
    """Whop Cards application details for the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read`
    scope; `null` otherwise, or when the account has no card application.
    """

    collect_vat_id: bool
    """Whether checkout shows a VAT/tax ID field for buyers to optionally enter.

    Does not require a VAT ID to purchase.
    """

    company_formation: CompanyFormation
    """
    Company formation state for the account, managed through
    [Form Company](/api-reference/beta/accounts/form-company). A `draft` `status`
    until the formation checkout is paid, then filing progress with downloadable
    documents and signatures awaiting action. Empty when the formation state is
    temporarily unavailable.
    """

    country: Optional[str] = None
    """Country where the account is located."""

    created_at: str
    """When the account was created, as an ISO 8601 timestamp."""

    description: Optional[str] = None
    """Account promotional description."""

    email: Optional[str] = None
    """Account owner email address."""

    home_preferences: List[Literal["hide_member_count", "hide_members_card"]]

    industry_group: Optional[
        Literal[
            "academic_and_test_prep",
            "accessories",
            "agriculture_and_farming",
            "ai_and_automation_agencies",
            "ai_and_automation_software",
            "arts_and_crafts",
            "automotive",
            "b2b_and_professional_marketplaces",
            "baby_and_kids",
            "bars_and_breweries",
            "beauty_and_personal_care",
            "beauty_and_wellness",
            "business_and_entrepreneurship",
            "business_and_money_groups",
            "cafes_and_quick_service",
            "career_and_professional",
            "charity_and_cause_events",
            "class_action_settlement",
            "clothing_and_apparel",
            "communication_and_messaging_software",
            "community_and_education_software",
            "conference_and_expo_events",
            "consulting",
            "content_and_clipping_agencies",
            "creative_and_content_creation",
            "creative_and_content_groups",
            "creative_and_education",
            "creative_gigs",
            "creative_services",
            "customer_support_agencies",
            "dating_and_relationships",
            "delivery_and_logistics",
            "dental_and_vision",
            "dermatology_and_skin",
            "design_and_creative_agencies",
            "developer_and_technical_tools",
            "development_agencies",
            "digital_and_education_marketplaces",
            "digital_goods_and_accounts",
            "e_commerce_software",
            "education_and_childcare",
            "educational_training_events",
            "electronics_and_gadgets",
            "entertainment_and_leisure",
            "family_and_community_events",
            "finance_and_investing",
            "fitness_and_athletics",
            "fitness_and_health_groups",
            "fitness_and_recreation",
            "fitness_equipment_and_gear",
            "food_and_beverages",
            "food_and_hospitality_marketplaces",
            "funeral_and_death_care",
            "gaming_and_entertainment_software",
            "gaming_groups",
            "genetic_and_specialized",
            "government_and_public",
            "health_and_wellness",
            "health_and_wellness_services",
            "healthcare",
            "healthcare_and_wellness_software",
            "hobbies_and_lifestyle",
            "hobby_and_interest_groups",
            "home_and_living",
            "home_and_trade_services",
            "home_and_trade_storefronts",
            "home_improvement_and_tools",
            "home_services_gigs",
            "hospitality_and_lodging",
            "industrial_and_manufacturing",
            "industry_specific_software",
            "language_and_communication",
            "legal_and_compliance",
            "lifestyle_and_culture",
            "lifestyle_and_personal_growth",
            "lifestyle_and_personal_growth_groups",
            "lifestyle_and_wellness_events",
            "logistics_and_transportation_services",
            "marketing_agencies",
            "marketing_and_advertising",
            "marketing_and_sales_software",
            "media_and_publishing_companies",
            "mental_health_and_behavioral",
            "miscellaneous",
            "music_and_performing_arts",
            "news_and_politics",
            "nonprofit_and_charity",
            "office_and_business_supplies",
            "outdoor_and_sports",
            "performance_and_show_events",
            "personal_development",
            "personal_finance",
            "personal_services",
            "pet_services",
            "pets_and_animals",
            "primary_and_general_care",
            "product_marketplaces",
            "productivity_and_business_ops",
            "professional_gigs",
            "professional_services",
            "professional_services_storefront",
            "publishing_and_info_products",
            "real_estate",
            "real_estate_software",
            "recruiting_and_staffing",
            "rehabilitation_and_therapy",
            "religion_and_faith",
            "rental_marketplaces",
            "restaurants",
            "retail",
            "sales_agencies",
            "sales_and_revenue",
            "security_and_investigations",
            "security_and_privacy_software",
            "service_marketplaces",
            "sleep_and_chronic_conditions",
            "social_and_networking_events",
            "social_entertainment_events",
            "specialized_gigs",
            "specialty_medical_care",
            "spirituality_and_mindfulness",
            "spirituality_and_personal_growth",
            "sports_and_fitness_events",
            "sports_betting_and_gambling",
            "sports_betting_groups",
            "supplements_and_nutrition",
            "sustainability_and_eco_products",
            "task_and_errands",
            "tech_and_ai",
            "tech_and_dev_groups",
            "tech_and_development",
            "trading_and_finance_software",
            "trading_and_investing",
            "trading_and_investing_groups",
            "transportation",
            "veterinary",
            "video_games_and_esports",
            "weight_and_metabolic_health",
            "wellness_and_alternative",
            "womens_and_mens_health",
        ]
    ] = None
    """Account industry group.

    See the
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary)
    for valid values.
    """

    industry_type: Optional[
        Literal[
            "trading",
            "sports_betting",
            "reselling",
            "fitness",
            "amazon_fba",
            "real_estate",
            "kindle_book_publishing",
            "dating",
            "agencies",
            "health_and_wellness",
            "social_media",
            "sales",
            "business",
            "ecommerce",
            "video_games",
            "home_services",
            "ai",
            "public_speaking",
            "personal_finance",
            "careers",
            "travel",
            "clipping",
            "spirituality",
            "vas",
            "personal_development",
            "software",
            "other",
            "marketing_agency",
            "sales_agency",
            "ai_agency",
            "design_agency",
            "coaching_agency",
            "development_agency",
            "recruiting_agency",
            "customer_support_agency",
            "clipping_agency",
            "clothing",
            "supplements",
            "beauty_and_personal_care",
            "fitness_gear",
            "accessories",
            "home_goods",
            "electronics_and_gadgets",
            "food_and_beverages",
            "gym",
            "restaurant",
            "retail_store",
            "coffee_shop",
            "salon_spa",
            "medical_dentist_office",
            "hotel_lodging",
            "auto_repair_shop",
            "masterminds",
            "webinars",
            "bootcamps",
            "convention",
            "concerts",
            "meetups",
            "parties",
            "forex_trading",
            "stock_trading",
            "options_trading",
            "crypto_trading",
            "futures_trading",
            "day_trading",
            "swing_trading",
            "algorithmic_trading",
            "prop_firm_trading",
            "value_investing",
            "real_estate_investing",
            "alternative_investments",
            "penny_stock_trading",
            "dividend_investing",
            "index_fund_investing",
            "gold_precious_metals",
            "venture_capital_education",
            "private_equity_education",
            "technical_analysis",
            "forex_scalping",
            "ict_smc_trading",
            "personalized_investment_advice",
            "forex_signals_group",
            "stock_signals_group",
            "crypto_signals_group",
            "options_alerts_group",
            "futures_signals_group",
            "trading_education_group",
            "investing_community",
            "prediction_markets_group",
            "nft_alpha_group",
            "penny_stock_group",
            "dividend_investing_group",
            "real_estate_investing_group",
            "prop_firm_group",
            "forex_trading_bot",
            "stock_trading_platform",
            "crypto_trading_bot",
            "futures_trading_bot",
            "options_flow_tool",
            "portfolio_tracker",
            "financial_modeling_software",
            "accounting_software",
            "invoicing_software",
            "tax_software",
            "risk_management_software",
            "prop_trading_platform",
            "backtesting_software",
            "trading_indicators",
            "market_data_feed",
            "stock_research_tool",
            "banking_software",
            "lending_platform",
            "insurance_software",
            "bnpl_service",
            "check_cashing_service",
            "cloud_mining_schemes",
            "consumer_lending",
            "credit_repair_service",
            "crypto_exchange_brokerage",
            "crypto_trading_tools_software",
            "debt_collection_agency",
            "debt_relief_settlement",
            "escrow_service",
            "foreign_exchange_service",
            "non_custodial_wallet_tools",
            "payment_facilitation",
            "prediction_market_exchange",
            "stablecoin_issuance",
            "token_sales_ico",
            "tokenized_rwa",
            "yield_staking_products",
            "sports_betting_picks",
            "fantasy_sports",
            "horse_racing",
            "poker_coaching",
            "esports_betting",
            "sports_analytics",
            "nfl_betting",
            "nba_betting",
            "mlb_betting",
            "soccer_betting",
            "mma_ufc_betting",
            "sports_picks_group",
            "dfs_group",
            "horse_racing_group",
            "esports_picks_group",
            "nfl_picks_group",
            "nba_picks_group",
            "soccer_picks_group",
            "mlb_picks_group",
            "mma_picks_group",
            "prop_bets_group",
            "fantasy_sports_free_to_play",
            "licensed_gambling_operations",
            "unlicensed_gambling",
            "bodybuilding_coaching",
            "strength_training",
            "weight_loss_coaching",
            "athletic_performance",
            "yoga_instruction",
            "martial_arts_instruction",
            "running_coaching",
            "calisthenics",
            "flexibility_mobility",
            "nutrition_coaching",
            "swimming_coaching",
            "cycling_coaching",
            "boxing_coaching",
            "mma_coaching",
            "jiu_jitsu_coaching",
            "wrestling_coaching",
            "gymnastics_coaching",
            "pilates_instruction",
            "sports_nutrition",
            "body_recomposition",
            "golf_coaching",
            "tennis_coaching",
            "basketball_training",
            "soccer_training",
            "racket_sports_coaching",
            "fitness_accountability",
            "nutrition_community",
            "weight_loss_group",
            "bodybuilding_community",
            "running_community",
            "martial_arts_community",
            "mental_health_group",
            "biohacking_community",
            "addiction_support_group",
            "yoga_community",
            "crossfit_community",
            "longevity_community",
            "womens_fitness_community",
            "postpartum_fitness_group",
            "chronic_illness_support",
            "skincare_community",
            "mental_health_coaching",
            "life_coaching",
            "biohacking",
            "holistic_health",
            "addiction_recovery_coaching",
            "breathwork",
            "meditation_mindfulness",
            "gut_health_coaching",
            "longevity_coaching",
            "womens_health_coaching",
            "mens_health_coaching",
            "fertility_wellness",
            "stress_management",
            "grief_coaching",
            "trauma_recovery_coaching",
            "adhd_coaching",
            "biomarker_health_coaching",
            "telehealth_platform",
            "ehr_software",
            "practice_management",
            "mental_health_app",
            "fitness_app",
            "nutrition_tracking_app",
            "wellness_app",
            "patient_engagement",
            "medical_billing_software",
            "pharmacy_management",
            "lab_management",
            "clinical_trial_software",
            "dental_software",
            "veterinary_software",
            "health_data_platform",
            "fitness_newsletter",
            "mental_health_newsletter",
            "longevity_newsletter",
            "medical_newsletter",
            "biohacking_newsletter",
            "womens_health_newsletter",
            "mens_health_newsletter",
            "pharma_biotech_newsletter",
            "ecommerce_education",
            "amazon_fba_coaching",
            "dropshipping_coaching",
            "print_on_demand_coaching",
            "retail_arbitrage",
            "wholesale_coaching",
            "startup_coaching",
            "business_strategy",
            "agency_building",
            "smma_coaching",
            "consulting_business",
            "saas_entrepreneurship",
            "local_business_coaching",
            "cleaning_business_coaching",
            "trucking_business_coaching",
            "vending_machine_business",
            "atm_business_coaching",
            "car_wash_business",
            "airbnb_business_coaching",
            "private_label_coaching",
            "etsy_coaching",
            "merch_business_coaching",
            "licensing_business",
            "business_acquisition",
            "women_entrepreneurship",
            "affiliate_marketing_education",
            "coaching_business_coaching",
            "ecommerce_community",
            "agency_community",
            "saas_community",
            "saas_marketing_community",
            "real_estate_community",
            "sales_community",
            "affiliate_community",
            "reselling_community",
            "amazon_seller_community",
            "dropshipping_community",
            "freelancer_community",
            "startup_founder_community",
            "ceo_executive_community",
            "women_business_community",
            "marketing_community",
            "ai_business_community",
            "content_business_community",
            "local_business_community",
            "private_equity_community",
            "wholesaling_community",
            "coaching_business_community",
            "make_money_online_community",
            "startup_newsletter",
            "ecommerce_newsletter",
            "marketing_newsletter",
            "sales_newsletter",
            "small_business_newsletter",
            "leadership_newsletter",
            "agency_newsletter",
            "saas_newsletter",
            "hr_people_newsletter",
            "legal_business_newsletter",
            "real_estate_business_newsletter",
            "solopreneur_newsletter",
            "high_ticket_sales",
            "b2b_sales_coaching",
            "door_to_door_sales",
            "sales_funnel_coaching",
            "appointment_setting_coaching",
            "insurance_sales_coaching",
            "car_sales_coaching",
            "retail_sales_coaching",
            "solar_sales_coaching",
            "lead_generation_agency",
            "cold_email_agency",
            "cold_calling_agency",
            "sales_outsourcing",
            "crm_implementation",
            "appointment_setting_agency",
            "sales_training_agency",
            "revenue_operations_agency",
            "inbound_teleservices",
            "outbound_telemarketing",
            "facebook_ads",
            "google_ads",
            "tiktok_marketing",
            "youtube_marketing",
            "instagram_growth",
            "seo_coaching",
            "email_marketing_coaching",
            "copywriting_coaching",
            "affiliate_marketing",
            "local_seo",
            "ai_marketing",
            "webinar_marketing",
            "event_marketing",
            "saas_marketing_coaching",
            "digital_marketing",
            "smma",
            "performance_marketing_agency",
            "seo_agency",
            "content_marketing_agency",
            "email_marketing_agency",
            "influencer_marketing_agency",
            "pr_agency",
            "branding_agency",
            "video_marketing_agency",
            "amazon_marketing_agency",
            "podcast_marketing_agency",
            "tiktok_agency",
            "linkedin_agency",
            "local_marketing_agency",
            "dental_marketing_agency",
            "real_estate_marketing_agency",
            "restaurant_marketing_agency",
            "ecommerce_marketing_agency",
            "b2b_marketing_agency",
            "growth_marketing_agency",
            "affiliate_management_agency",
            "conversion_optimization_agency",
            "event_marketing_agency",
            "click_farm_service",
            "data_scraping_service",
            "lead_list_sales",
            "social_media_bot_farm",
            "crm_software",
            "email_marketing_software",
            "sms_marketing_software",
            "seo_tool",
            "landing_page_builder",
            "ad_management_tool",
            "affiliate_tracking",
            "review_management",
            "analytics_dashboard",
            "lead_gen_software",
            "link_in_bio_tool",
            "influencer_platform",
            "webinar_platform",
            "ab_testing_tool",
            "chatbot_marketing",
            "video_sales_tool",
            "proposal_software",
            "competitive_intelligence",
            "social_listening_tool",
            "whatsapp_marketing_tool",
            "standalone_tipping",
            "video_editing_education",
            "photography_coaching",
            "music_production",
            "ui_ux_design_education",
            "clipping_education",
            "ugc_creation",
            "3d_modeling_education",
            "dj_education",
            "youtube_automation",
            "blog_monetization",
            "wedding_photography_education",
            "calligraphy_lettering",
            "illustration_education",
            "fashion_design_education",
            "interior_design_education",
            "influencer_education",
            "ai_content_creator_education",
            "ai_nsfw_content_generation_education",
            "web_design_agency",
            "graphic_design_agency",
            "ui_ux_agency",
            "motion_design_agency",
            "product_design_agency",
            "logo_design_agency",
            "presentation_design_agency",
            "3d_visualization_agency",
            "fashion_design_agency",
            "video_clipping_agency",
            "video_production_agency",
            "ugc_agency",
            "content_writing_agency",
            "translation_agency",
            "social_media_management",
            "ghostwriting_agency",
            "podcast_editing_agency",
            "thumbnail_design_agency",
            "scriptwriting_agency",
            "seo_content_agency",
            "technical_writing_agency",
            "photography_service",
            "videography_service",
            "music_production_service",
            "voice_over_service",
            "event_photography",
            "drone_services",
            "commercial_photography",
            "portrait_photography_service",
            "real_estate_photography",
            "food_photography_service",
            "live_event_production",
            "podcast_production_service",
            "freelance_design_gig",
            "freelance_writing_gig",
            "freelance_dev_gig",
            "music_performance_gig",
            "event_staffing_gig",
            "model_talent_gig",
            "photography_gig",
            "videography_gig",
            "voiceover_gig",
            "illustration_gig",
            "social_media_gig",
            "dj_gig",
            "face_painting_gig",
            "clipping_gig",
            "content_creator_community",
            "video_editing_community",
            "music_producer_community",
            "photography_community",
            "writing_community",
            "design_community",
            "youtube_creator_community",
            "tiktok_creator_community",
            "podcast_community",
            "filmmaker_community",
            "clipping_community",
            "youtube_automation_community",
            "pirated_digital_content",
            "web_development_education",
            "ai_ml_education",
            "data_science_education",
            "cybersecurity_education",
            "cloud_computing_education",
            "blockchain_education",
            "no_code_education",
            "automation_education",
            "game_development_education",
            "prompt_engineering",
            "python_programming",
            "javascript_programming",
            "react_development",
            "database_engineering",
            "aws_certification",
            "data_engineering",
            "robotics_education",
            "vr_ar_development",
            "linux_sysadmin",
            "wordpress_development",
            "ai_agent_building",
            "web_development_agency",
            "mobile_app_agency",
            "saas_development_agency",
            "ecommerce_development",
            "blockchain_development_agency",
            "game_development_agency",
            "devops_agency",
            "ai_development_agency",
            "wordpress_agency",
            "shopify_agency",
            "api_integration_agency",
            "cybersecurity_agency",
            "data_engineering_agency",
            "vr_ar_development_agency",
            "hacking_tools_malware",
            "stalkerware_monitoring",
            "developer_community",
            "ai_community",
            "cybersecurity_community",
            "no_code_community",
            "indie_hacker_community",
            "devops_community",
            "data_science_community",
            "product_community",
            "open_source_community",
            "api_management",
            "hosting_platform",
            "database_tool",
            "devops_tool",
            "monitoring_tool",
            "testing_tool",
            "code_editor",
            "no_code_builder",
            "cdn_platform",
            "error_tracking",
            "documentation_tool",
            "webhook_tool",
            "3d_weapon_files",
            "background_check_services",
            "document_falsification",
            "fake_id_services",
            "fake_reference_services",
            "real_estate_wholesaling",
            "house_flipping",
            "property_development",
            "rental_property",
            "airbnb_str",
            "commercial_real_estate",
            "land_investing",
            "section_8_housing",
            "mobile_home_investing",
            "multifamily_investing",
            "self_storage_investing",
            "property_management_education",
            "vacation_rental_management",
            "real_estate_crm",
            "property_management_software",
            "deal_analysis_tool",
            "mls_search_tool",
            "virtual_tour_software",
            "real_estate_marketing_software",
            "construction_management",
            "home_valuation_tool",
            "credit_repair_education",
            "budgeting_coaching",
            "tax_strategy_education",
            "wealth_building",
            "student_loan_strategy",
            "credit_card_optimization",
            "career_coaching",
            "executive_coaching",
            "management_coaching",
            "tech_career_coaching",
            "medical_career_coaching",
            "trade_skills_education",
            "va_training",
            "bookkeeping_education",
            "data_career_coaching",
            "cybersecurity_career",
            "consulting_career",
            "investment_banking_career",
            "law_career_coaching",
            "nursing_career_coaching",
            "teaching_career_coaching",
            "personal_branding_career",
            "mens_dating_coaching",
            "womens_dating_coaching",
            "relationship_coaching",
            "marriage_coaching",
            "communication_coaching",
            "masculinity_coaching",
            "femininity_coaching",
            "breakup_recovery",
            "manifestation_coaching",
            "astrology_coaching",
            "energy_healing",
            "spiritual_coaching",
            "faith_based_coaching",
            "psychic_development",
            "numerology_coaching",
            "chakra_healing",
            "shamanic_healing",
            "biblical_coaching",
            "islamic_coaching",
            "productivity_coaching",
            "public_speaking_coaching",
            "mindset_coaching",
            "stoicism_philosophy",
            "mens_self_improvement",
            "womens_self_improvement",
            "leadership_development",
            "anger_management",
            "neurolinguistic_programming",
            "appearance_and_grooming_coaching",
            "amazon_kdp",
            "self_publishing",
            "audiobook_publishing",
            "course_creation",
            "digital_product_creation",
            "ghostwriting_business",
            "template_creation",
            "ai_book_publishing",
            "language_learning",
            "tutoring",
            "college_admissions_coaching",
            "cpa_exam_prep",
            "bar_exam_prep",
            "real_estate_exam_prep",
            "medical_board_prep",
            "pmp_certification_prep",
            "aws_certification_prep",
            "comptia_certification",
            "ap_exam_prep",
            "graduate_school_prep",
            "scholarship_coaching",
            "homeschool_education",
            "stem_education",
            "financial_certification",
            "coding_bootcamp_prep",
            "cooking_culinary",
            "travel_coaching",
            "parenting_coaching",
            "pet_training",
            "gardening_education",
            "diy_crafts",
            "survival_prepping",
            "baking_pastry",
            "wine_sommelier",
            "beer_brewing",
            "mixology_bartending",
            "woodworking",
            "pottery_ceramics",
            "knitting_crocheting",
            "jewelry_making",
            "aquarium_fishkeeping",
            "bird_watching",
            "astronomy_education",
            "magic_illusion",
            "car_restoration",
            "motorcycle_riding",
            "sailing_boating",
            "scuba_diving",
            "rock_climbing",
            "skiing_snowboarding",
            "surfing_education",
            "homesteading",
            "tiny_house_living",
            "van_life",
            "fashion_styling",
            "floral_design",
            "travel_planning_service",
            "collectibles_coaching",
            "car_enthusiast_community",
            "sneakerhead_community",
            "watch_collector_community",
            "wine_enthusiast_community",
            "cigar_community",
            "cooking_community",
            "gardening_community",
            "fishing_community",
            "hunting_community",
            "diy_maker_community",
            "golf_community",
            "collectibles_community",
            "sweepstakes_raffles",
            "event_ticket_community",
            "esports_coaching",
            "game_specific_coaching",
            "gaming_community",
            "game_account_selling",
            "unauthorized_ingame_currency",
            "legal_education",
            "music_theory",
            "music_business",
            "acting_coaching",
            "dance_instruction",
            "voice_acting",
            "english_coaching",
            "spanish_coaching",
            "mandarin_coaching",
            "french_coaching",
            "german_coaching",
            "japanese_coaching",
            "korean_coaching",
            "arabic_coaching",
            "sign_language_education",
            "accent_reduction",
            "business_english",
            "ai_chatbot_agency",
            "ai_automation_agency",
            "ai_consulting",
            "workflow_automation_agency",
            "data_analytics_agency",
            "ai_voice_agent_agency",
            "ai_content_agency",
            "machine_learning_agency",
            "computer_vision_agency",
            "tech_recruiting_agency",
            "executive_recruiting",
            "staffing_agency",
            "remote_staffing",
            "healthcare_recruiting",
            "va_placement_agency",
            "sales_recruiting",
            "creative_recruiting",
            "finance_recruiting",
            "legal_recruiting",
            "construction_staffing",
            "hospitality_staffing",
            "customer_support_outsourcing",
            "live_chat_agency",
            "technical_support_agency",
            "call_center_agency",
            "multilingual_support_agency",
            "community_management_agency",
            "management_consulting",
            "financial_consulting",
            "hr_consulting",
            "operations_consulting",
            "it_consulting",
            "sustainability_consulting",
            "legal_consulting",
            "compliance_consulting",
            "supply_chain_consulting",
            "change_management_consulting",
            "digital_transformation_consulting",
            "healthcare_consulting",
            "real_estate_consulting",
            "franchise_consulting",
            "export_trade_consulting",
            "nonprofit_consulting",
            "education_consulting",
            "cannabis_consulting",
            "restaurant_consulting",
            "m_and_a_consulting",
            "pricing_strategy_consulting",
            "brand_strategy_consulting",
            "saas_marketing_consulting",
            "done_for_you_services",
            "prop_firm_passing_service",
            "trading_account_management",
            "done_for_you_trading",
            "accounting_bookkeeping",
            "tax_preparation",
            "legal_services",
            "notary_services",
            "insurance_brokerage",
            "financial_planning_service",
            "real_estate_services",
            "property_management",
            "mortgage_brokerage",
            "immigration_services",
            "patent_trademark_services",
            "business_formation_services",
            "shell_company_formation",
            "payroll_services",
            "audit_services",
            "forensic_accounting",
            "actuarial_services",
            "appraisal_services",
            "mediation_arbitration",
            "bail_bond_services",
            "crowdfunding_platform",
            "essay_mill_paper_mill",
            "government_service_facilitation",
            "immigration_services_unlicensed",
            "licensed_legal_services",
            "personalized_tax_services",
            "private_investigation",
            "repossession_services",
            "unlicensed_legal_services",
            "record_label",
            "book_publishing_house",
            "news_media_outlet",
            "radio_broadcasting",
            "tv_production_company",
            "film_studio",
            "magazine_publisher",
            "music_licensing_agency",
            "talent_management_agency",
            "advertising_network",
            "ad_tech_platform",
            "cleaning_service",
            "landscaping_service",
            "plumbing_service",
            "electrical_service",
            "hvac_service",
            "roofing_service",
            "painting_service",
            "moving_service",
            "handyman_service",
            "pest_control",
            "pool_service",
            "solar_installation",
            "home_renovation",
            "pressure_washing",
            "junk_removal",
            "garage_door_service",
            "fencing_service",
            "concrete_masonry",
            "tree_service",
            "window_cleaning",
            "gutter_service",
            "flooring_service",
            "cabinet_countertop",
            "home_inspection",
            "septic_service",
            "waterproofing_service",
            "insulation_service",
            "chimney_service",
            "locksmith_service",
            "glass_window_service",
            "epoxy_coating",
            "private_security_guard_service",
            "armored_car_transport",
            "executive_protection_bodyguard",
            "event_security_service",
            "alarm_system_installation",
            "cctv_installation",
            "private_investigation_agency",
            "background_check_provider",
            "locksmith_commercial",
            "bounty_hunter_bail_enforcement",
            "personal_styling",
            "personal_chef",
            "personal_assistant_service",
            "tutoring_service",
            "pet_services",
            "wedding_planning",
            "concierge_service",
            "personal_training_service",
            "nanny_service",
            "elder_care_service",
            "errand_service",
            "life_organization",
            "relocation_service",
            "adult_dating_services",
            "escort_services",
            "hotel_accommodation_bookings",
            "mail_order_spouse",
            "psychic_fortune_telling",
            "timeshare_sales",
            "freight_brokerage",
            "courier_service",
            "warehousing_service",
            "last_mile_delivery",
            "auto_transport",
            "international_shipping",
            "cold_chain_logistics",
            "commercial_airline_tickets",
            "cruise_line_bookings",
            "contract_manufacturing",
            "cnc_machining_service",
            "3d_printing_service_commercial",
            "plastic_injection_molding",
            "metal_fabrication",
            "pcba_assembly",
            "chemical_manufacturing",
            "textile_manufacturing",
            "food_processing_facility",
            "packaging_manufacturing",
            "industrial_automation_integrator",
            "mining_and_extraction",
            "oil_and_gas_services",
            "renewable_energy_generation",
            "waste_management_recycling",
            "hazardous_waste_disposal",
            "aerospace_defense_contracting",
            "personal_training_studio",
            "nutrition_consulting",
            "mental_health_counseling",
            "physical_therapy_service",
            "occupational_therapy_service",
            "speech_therapy_service",
            "chiropractic_service",
            "acupuncture_service",
            "massage_therapy_service",
            "midwifery_doula",
            "lactation_consulting",
            "dietitian_service",
            "addiction_recovery_services",
            "dtc_lab_testing",
            "iv_therapy_infusion",
            "medspa_aesthetic_services",
            "prescription_delivery_services",
            "registered_dietitian_services",
            "unlicensed_therapy_counseling",
            "streetwear",
            "athleisure",
            "luxury_fashion",
            "kids_clothing",
            "custom_apparel",
            "workwear",
            "swimwear",
            "lingerie_intimates",
            "vintage_clothing",
            "plus_size_fashion",
            "maternity_clothing",
            "sleepwear_loungewear",
            "denim_brand",
            "outerwear_jackets",
            "socks_hosiery",
            "costumes_cosplay",
            "scrubs_medical_apparel",
            "dance_performance_wear",
            "hunting_camo_apparel",
            "casual_everyday_clothing",
            "protein_supplements",
            "vitamins_minerals",
            "pre_workout",
            "nootropics",
            "herbal_supplements",
            "weight_management_supplements",
            "gut_health",
            "cbd_products",
            "mushroom_supplements",
            "collagen_supplements",
            "testosterone_boosters",
            "sleep_supplements",
            "immune_support",
            "joint_bone_health",
            "greens_powder",
            "creatine_supplements",
            "electrolyte_hydration",
            "prenatal_supplements",
            "kids_supplements",
            "pet_supplements",
            "ayurvedic_supplements",
            "keto_supplements",
            "cannabis_thc_products",
            "cbd_hemp_products_compliant",
            "delta8_thc_products",
            "dietary_supplements",
            "drug_precursor_chemicals",
            "illegal_drugs",
            "kratom_kava_products",
            "medical_treatment_claims_product",
            "nutraceutical_products",
            "otc_medication_sales",
            "performance_enhancing_drugs",
            "research_chemicals_dangerous",
            "research_peptides",
            "sexual_enhancement_products",
            "tobacco_products",
            "unlicensed_rx_sales",
            "skincare",
            "haircare",
            "cosmetics_makeup",
            "mens_grooming",
            "fragrance",
            "oral_care",
            "sunscreen_spf",
            "hair_growth_products",
            "body_care",
            "deodorant",
            "lip_care",
            "acne_treatment",
            "men_skincare",
            "baby_skincare",
            "tattoo_aftercare",
            "intimate_care",
            "home_gym_equipment",
            "yoga_equipment",
            "combat_sports_gear",
            "outdoor_fitness_gear",
            "wearable_fitness",
            "recovery_equipment",
            "weightlifting_equipment",
            "cardio_equipment",
            "gymnastics_equipment",
            "swimming_gear",
            "jump_rope_equipment",
            "grip_strength_tools",
            "sauna_cold_plunge",
            "posture_correctors",
            "jewelry",
            "sunglasses_eyewear",
            "bags_wallets",
            "hats_headwear",
            "phone_accessories",
            "travel_accessories",
            "scarves_wraps",
            "belts",
            "hair_accessories",
            "tech_accessories",
            "keychains_charms",
            "custom_engraved_accessories",
            "cannabis_accessories_non_drug",
            "drug_paraphernalia",
            "high_value_goods_over_500",
            "precious_metals_stones",
            "replica_counterfeit_goods",
            "home_decor",
            "candles_scents",
            "kitchenware",
            "bedding_linens",
            "smart_home",
            "cleaning_products",
            "outdoor_furniture",
            "organization_storage",
            "wall_art_prints",
            "rugs_carpets",
            "lighting_fixtures",
            "planters_garden_decor",
            "bathroom_accessories",
            "luxury_home_goods",
            "seasonal_holiday_decor",
            "pet_home_products",
            "home_fragrance_diffusers",
            "hazardous_chemicals_b2c",
            "pre_orders_delayed_delivery",
            "audio_equipment",
            "camera_equipment",
            "gaming_hardware",
            "drones_robotics",
            "ev_accessories",
            "charging_power",
            "smart_wearables",
            "home_security_devices",
            "3d_printers",
            "projectors_displays",
            "streaming_devices",
            "vr_headsets",
            "e_readers",
            "portable_tech",
            "hardware_wallets",
            "regulated_medical_devices",
            "signal_jamming_devices",
            "spy_cameras_hidden_recording",
            "specialty_coffee_tea",
            "health_food",
            "snacks_treats",
            "sauces_condiments",
            "alcohol_spirits",
            "meal_kits",
            "baked_goods",
            "beverages",
            "pet_food_treats",
            "protein_bars_snacks",
            "jerky_meat_snacks",
            "chocolate_confections",
            "honey_sweeteners",
            "olive_oil_vinegar",
            "hot_sauce",
            "dried_fruit_nuts",
            "baby_food",
            "plant_based_food",
            "gluten_free_food",
            "keto_food_products",
            "subscription_food_box",
            "kombucha_fermented",
            "alcohol_sales",
            "baby_products",
            "kids_toys",
            "kids_educational",
            "baby_clothing_accessories",
            "nursery_decor",
            "kids_outdoor_play",
            "kids_books",
            "baby_safety_products",
            "kids_arts_crafts",
            "camping_hiking",
            "fishing_gear",
            "hunting_gear",
            "cycling_gear",
            "water_sports_gear",
            "golf_equipment",
            "snow_sports_gear",
            "climbing_gear",
            "archery_equipment",
            "skateboarding_gear",
            "pickleball_equipment",
            "tennis_equipment",
            "equestrian_gear",
            "tactical_gear",
            "overlanding_gear",
            "explosives_fireworks",
            "firearms_sales",
            "self_defense_products",
            "weapon_components",
            "craft_kits",
            "sewing_textiles",
            "stationery",
            "scrapbooking_supplies",
            "beading_jewelry_supplies",
            "pottery_supplies",
            "printmaking_supplies",
            "car_accessories",
            "detailing_products",
            "motorcycle_gear",
            "truck_accessories",
            "off_road_parts",
            "car_audio_electronics",
            "performance_parts",
            "car_care_products",
            "ev_charging_accessories",
            "auto_repair_service",
            "auto_body_shop",
            "car_dealership",
            "car_wash",
            "tire_shop",
            "oil_change_shop",
            "auto_parts_store",
            "motorcycle_shop",
            "ev_charging_station",
            "transmission_shop",
            "muffler_exhaust_shop",
            "auto_glass_shop",
            "auto_upholstery_shop",
            "car_audio_shop",
            "smog_emissions_shop",
            "truck_repair_shop",
            "rv_repair_shop",
            "boat_repair_shop",
            "used_car_lot",
            "auto_auction",
            "dog_products",
            "cat_products",
            "aquarium_supplies",
            "bird_supplies",
            "reptile_supplies",
            "horse_supplies",
            "pet_apparel",
            "pet_tech",
            "pet_grooming_products",
            "hand_tools",
            "power_tools_and_accessories",
            "hardware_and_fasteners",
            "workshop_equipment_and_storage",
            "safety_and_work_gear",
            "painting_and_building_supplies",
            "office_supplies",
            "desk_accessories",
            "printing_supplies",
            "shipping_packaging",
            "reusable_products",
            "solar_powered_products",
            "christian_books_bibles",
            "christian_apparel",
            "christian_jewelry",
            "christian_home_decor",
            "jewish_judaica",
            "jewish_books_torah",
            "jewish_apparel",
            "islamic_books_quran",
            "islamic_apparel",
            "islamic_prayer_goods",
            "hindu_puja_supplies",
            "hindu_books_texts",
            "buddhist_meditation_goods",
            "buddhist_books_texts",
            "sikh_religious_goods",
            "other_religious_products",
            "handmade_goods_marketplace",
            "vintage_resale_marketplace",
            "electronics_marketplace",
            "auto_parts_marketplace",
            "luxury_goods_marketplace",
            "collectibles_marketplace",
            "wholesale_marketplace",
            "local_goods_marketplace",
            "sneaker_marketplace",
            "book_marketplace",
            "furniture_marketplace",
            "musical_instrument_marketplace",
            "art_marketplace",
            "ticket_marketplace",
            "industrial_equipment_marketplace",
            "craft_supply_marketplace",
            "baby_kids_marketplace",
            "outdoor_gear_marketplace",
            "pet_marketplace",
            "sustainable_goods_marketplace",
            "cultural_artifacts_looted",
            "dropshipping_operations",
            "endangered_animal_products",
            "human_body_parts_tissue",
            "nft_marketplace",
            "penny_auction",
            "primary_event_ticketing",
            "freelancer_marketplace",
            "home_services_marketplace",
            "tutoring_marketplace",
            "legal_services_marketplace",
            "healthcare_marketplace",
            "wedding_services_marketplace",
            "creative_and_content_creation_marketplace",
            "beauty_services_marketplace",
            "fitness_trainer_marketplace",
            "pet_services_marketplace",
            "childcare_marketplace",
            "elder_care_marketplace",
            "translation_marketplace",
            "coaching_marketplace",
            "therapy_marketplace",
            "photography_marketplace",
            "dj_entertainment_marketplace",
            "auto_services_marketplace",
            "freelance_marketplace_operator",
            "equipment_rental_marketplace",
            "vehicle_rental_marketplace",
            "space_rental_marketplace",
            "vacation_rental_marketplace",
            "clothing_rental_marketplace",
            "camera_gear_rental",
            "rv_camper_rental",
            "boat_rental_marketplace",
            "storage_rental_marketplace",
            "office_coworking_rental",
            "parking_rental_marketplace",
            "restaurant_marketplace",
            "grocery_marketplace",
            "catering_marketplace",
            "homemade_food_marketplace",
            "meal_prep_marketplace",
            "bakery_marketplace",
            "farm_produce_marketplace",
            "chef_booking_marketplace",
            "course_marketplace",
            "template_marketplace",
            "stock_media_marketplace",
            "music_beats_marketplace",
            "ebook_marketplace",
            "plugin_theme_marketplace",
            "3d_model_marketplace",
            "prompt_marketplace",
            "code_snippet_marketplace",
            "affiliate_marketing_platform",
            "game_cheats_hacks",
            "weapon_blueprint_distribution",
            "saas_marketplace",
            "agency_marketplace",
            "manufacturing_marketplace",
            "logistics_marketplace",
            "commercial_real_estate_marketplace",
            "business_for_sale_marketplace",
            "food_delivery",
            "grocery_delivery",
            "package_delivery",
            "moving_labor",
            "alcohol_delivery",
            "pharmacy_delivery",
            "flower_delivery_gig",
            "furniture_delivery_gig",
            "catering_delivery",
            "rideshare",
            "chauffeur_service",
            "bike_scooter_rental",
            "boat_charter_gig",
            "moving_truck_rental_gig",
            "assembly_installation",
            "waiting_line_service",
            "personal_shopping",
            "grocery_shopping_gig",
            "gift_wrapping_gig",
            "notary_gig",
            "laundry_gig",
            "car_wash_gig",
            "cleaning_gig",
            "lawn_care_gig",
            "handyman_gig",
            "pet_care_gig",
            "childcare_gig",
            "elder_care_gig",
            "painting_gig",
            "snow_removal_gig",
            "pool_cleaning_gig",
            "organizing_gig",
            "pressure_washing_gig",
            "junk_removal_gig",
            "consulting_gig",
            "accounting_gig",
            "legal_gig",
            "healthcare_gig",
            "teaching_gig",
            "translation_gig",
            "data_entry_gig",
            "research_gig",
            "virtual_assistant_gig",
            "sales_gig",
            "recruiting_gig",
            "mystery_shopping",
            "focus_group_gig",
            "product_testing_gig",
            "drone_pilot_gig",
            "fitness_instruction_gig",
            "tour_guide_gig",
            "dating_community",
            "personal_development_community",
            "spirituality_community",
            "parenting_community",
            "travel_community",
            "networking_community",
            "faith_community",
            "mens_community",
            "womens_community",
            "expat_community",
            "adult_community_nsfw",
            "hate_violence_communities",
            "personal_fundraising",
            "political_fundraising",
            "political_organizations",
            "pornographic_content",
            "registered_501c3",
            "religious_organization",
            "unregistered_charities",
            "ai_outreach_tool",
            "ai_chatbot_software",
            "ai_writing_tool",
            "ai_image_generator",
            "ai_video_tool",
            "ai_voice_tool",
            "ai_data_analysis",
            "ai_code_assistant",
            "ai_meeting_assistant",
            "workflow_automation_software",
            "ai_sales_tool",
            "ai_customer_support",
            "ai_recruiting_tool",
            "ai_translation_tool",
            "ai_music_tool",
            "ai_presentation_tool",
            "ai_research_tool",
            "ai_seo_tool",
            "ai_social_media_tool",
            "ai_phone_agent",
            "ai_legal_tool",
            "ai_healthcare_tool",
            "llm_api_platform",
            "ai_agent_platform",
            "generative_ai_platform",
            "celebrity_impersonation",
            "deepfake_service",
            "ai_nsfw_content_generator",
            "ecommerce_platform",
            "product_research_tool",
            "price_tracker",
            "shipping_software",
            "print_on_demand_software",
            "marketplace_seller_tool",
            "resale_arbitrage_tool",
            "reseller_management_tool",
            "product_review_software",
            "returns_management",
            "product_feed_management",
            "checkout_optimization",
            "wholesale_ordering",
            "project_management_software",
            "team_communication",
            "video_conferencing",
            "document_collaboration",
            "time_tracking_software",
            "scheduling_software",
            "hr_software",
            "knowledge_base_software",
            "form_survey_builder",
            "note_taking_app",
            "task_management",
            "contract_management",
            "expense_management",
            "okr_goal_tracking",
            "employee_engagement",
            "onboarding_software",
            "applicant_tracking",
            "asset_management",
            "facility_management",
            "visitor_management",
            "community_platform",
            "event_management_software",
            "webinar_software",
            "school_management",
            "newsletter_platform",
            "podcast_hosting",
            "forum_software",
            "virtual_classroom",
            "restaurant_pos",
            "salon_software",
            "gym_management_software",
            "auto_shop_software",
            "legal_practice_software",
            "church_management",
            "nonprofit_software",
            "logistics_software",
            "agriculture_software",
            "field_service_software",
            "marina_management",
            "hotel_pms",
            "childcare_management",
            "cleaning_business_software",
            "roofing_software",
            "landscaping_software",
            "pest_control_software",
            "tattoo_studio_software",
            "cannabis_software",
            "password_manager",
            "cybersecurity_software",
            "identity_verification",
            "backup_recovery",
            "endpoint_protection",
            "email_security",
            "access_management",
            "compliance_software",
            "data_privacy_tool",
            "vpn_services",
            "people_search_tool",
            "game_mod_tool",
            "streaming_tool",
            "game_server_hosting",
            "music_software",
            "video_editing_software",
            "photo_editing_software",
            "animation_software",
            "audio_editing_software",
            "screen_recording_software",
            "sports_betting_tool",
            "fantasy_sports_paid_entry",
            "iptv_pirated_streaming",
            "loot_boxes_gacha",
            "skill_contests_free_entry",
            "skill_contests_paid_entry",
            "only_fans_management_software",
            "pornography_platform",
            "business_phone_system",
            "customer_messaging",
            "digital_key_reselling",
            "streaming_account_reselling",
            "subscription_account_sharing",
            "account_generation_tool",
            "primary_care_telehealth",
            "urgent_care_telehealth",
            "pediatric_telehealth",
            "geriatric_telehealth",
            "family_medicine_telehealth",
            "internal_medicine_telehealth",
            "preventive_care_telehealth",
            "licensed_online_pharmacy",
            "telemedicine_practitioner_services",
            "dermatology_telehealth",
            "acne_telehealth",
            "psoriasis_eczema_telehealth",
            "skin_cancer_screening_tele",
            "cosmetic_dermatology_tele",
            "therapy_telehealth",
            "psychiatry_telehealth",
            "addiction_telehealth",
            "couples_therapy_telehealth",
            "child_psychology_telehealth",
            "eating_disorder_telehealth",
            "ptsd_trauma_telehealth",
            "adhd_telehealth",
            "anxiety_depression_telehealth",
            "ocd_telehealth",
            "grief_counseling_telehealth",
            "anger_management_telehealth",
            "family_therapy_telehealth",
            "group_therapy_telehealth",
            "licensed_psychedelic_therapy",
            "womens_health_telehealth",
            "mens_health_telehealth",
            "sexual_health_telehealth",
            "fertility_telehealth",
            "hormone_therapy_telehealth",
            "menopause_telehealth",
            "prenatal_telehealth",
            "postpartum_telehealth",
            "erectile_dysfunction_tele",
            "hair_loss_telehealth",
            "birth_control_telehealth",
            "sti_testing_telehealth",
            "dental_telehealth",
            "orthodontics_telehealth",
            "optometry_telehealth",
            "oral_surgery_consultation",
            "vision_therapy_telehealth",
            "cardiology_telehealth",
            "endocrinology_telehealth",
            "neurology_telehealth",
            "orthopedic_telehealth",
            "allergy_telehealth",
            "ent_telehealth",
            "rheumatology_telehealth",
            "gastroenterology_telehealth",
            "infectious_disease_telehealth",
            "pulmonology_telehealth",
            "nephrology_telehealth",
            "oncology_telehealth",
            "hematology_telehealth",
            "urology_telehealth",
            "weight_management_telehealth",
            "glp1_weight_loss_tele",
            "diabetes_management_tele",
            "metabolic_health_tele",
            "bariatric_telehealth",
            "physical_therapy_telehealth",
            "occupational_therapy_tele",
            "speech_therapy_telehealth",
            "pain_management_telehealth",
            "cardiac_rehab_telehealth",
            "pelvic_floor_telehealth",
            "vestibular_telehealth",
            "sleep_medicine_telehealth",
            "chronic_disease_management",
            "chronic_pain_telehealth",
            "migraine_telehealth",
            "asthma_copd_telehealth",
            "nutrition_telehealth",
            "naturopathic_telehealth",
            "functional_medicine_telehealth",
            "acupuncture_telehealth",
            "health_coaching_telehealth",
            "integrative_medicine_tele",
            "ayurvedic_telehealth",
            "genetic_counseling_telehealth",
            "pharmacogenomics_tele",
            "rare_disease_telehealth",
            "second_opinion_telehealth",
            "vet_telehealth",
            "pet_behavior_telehealth",
            "exotic_pet_telehealth",
            "equine_telehealth",
            "veterinary_services",
            "class_action_settlement",
            "mastermind_event",
            "webinar_event",
            "virtual_summit",
            "bootcamp_event",
            "workshop_seminar",
            "hackathon",
            "corporate_training_event",
            "training_certification_event",
            "convention_expo",
            "conference_summit",
            "industry_awards_event",
            "product_launch_event",
            "investor_demo_day",
            "panel_discussion_event",
            "pitch_competition",
            "meetup_event",
            "dinner_event",
            "alumni_event",
            "community_gathering",
            "singles_event",
            "professional_happy_hour",
            "women_networking_event",
            "founders_dinner",
            "industry_mixer",
            "concert_event",
            "comedy_show",
            "theater_performance",
            "film_screening",
            "music_festival",
            "cultural_festival",
            "fashion_show",
            "drag_show",
            "magic_show",
            "dance_performance",
            "poetry_spoken_word",
            "art_exhibition",
            "party_event",
            "trivia_night",
            "wine_tasting_event",
            "beer_festival",
            "car_show",
            "food_festival",
            "fitness_challenge_event",
            "marathon_race",
            "tournament_event",
            "fight_event",
            "yoga_retreat_event",
            "outdoor_adventure_event",
            "esports_tournament",
            "obstacle_course_race",
            "cycling_event",
            "swim_meet",
            "golf_tournament",
            "pickleball_tournament",
            "crossfit_competition",
            "martial_arts_tournament",
            "surfing_competition",
            "wellness_retreat",
            "spiritual_retreat",
            "couples_retreat",
            "plant_medicine_retreat",
            "luxury_experience_event",
            "detox_retreat",
            "silent_retreat",
            "creative_retreat",
            "leadership_retreat",
            "mens_retreat",
            "womens_retreat",
            "digital_detox_retreat",
            "fundraiser_event",
            "awareness_event",
            "volunteer_event",
            "charity_auction",
            "benefit_concert",
            "charity_run_walk",
            "environmental_cleanup",
            "family_festival",
            "kids_event",
            "holiday_event",
            "farmers_market_event",
            "block_party",
            "graduation_ceremony",
            "memorial_event",
            "stock_market_newsletter",
            "crypto_newsletter",
            "personal_finance_newsletter",
            "real_estate_newsletter",
            "fintech_newsletter",
            "venture_capital_newsletter",
            "options_trading_newsletter",
            "forex_newsletter",
            "macro_economics_newsletter",
            "alternative_investing_newsletter",
            "tax_strategy_newsletter",
            "ai_newsletter",
            "tech_industry_newsletter",
            "cybersecurity_newsletter",
            "developer_newsletter",
            "product_newsletter",
            "devops_newsletter",
            "open_source_newsletter",
            "robotics_newsletter",
            "climate_tech_newsletter",
            "travel_newsletter",
            "fashion_newsletter",
            "parenting_newsletter",
            "sports_newsletter",
            "gaming_newsletter",
            "music_entertainment_newsletter",
            "book_reading_newsletter",
            "dating_relationships_newsletter",
            "home_design_newsletter",
            "pet_newsletter",
            "wine_spirits_newsletter",
            "automotive_newsletter",
            "political_newsletter",
            "geopolitics_newsletter",
            "media_journalism_newsletter",
            "defense_security_newsletter",
            "legal_policy_newsletter",
            "design_newsletter",
            "education_newsletter",
            "science_newsletter",
            "philosophy_newsletter",
            "sustainability_newsletter",
            "architecture_newsletter",
            "history_newsletter",
            "psychology_newsletter",
            "career_newsletter",
            "spirituality_newsletter",
            "self_improvement_newsletter",
            "productivity_newsletter",
            "faith_newsletter",
            "gym_facility",
            "crossfit_box",
            "yoga_studio",
            "pilates_studio",
            "martial_arts_gym",
            "boxing_gym",
            "climbing_gym",
            "dance_studio",
            "swimming_pool",
            "sports_facility",
            "golf_course",
            "bowling_alley",
            "skating_rink",
            "trampoline_park",
            "tennis_club",
            "pickleball_facility",
            "gymnastics_center",
            "spin_studio",
            "barre_studio",
            "personal_training_studio_bm",
            "recovery_studio",
            "indoor_soccer",
            "batting_cage",
            "shooting_range",
            "archery_range",
            "equestrian_center",
            "fine_dining",
            "fast_casual_restaurant",
            "steakhouse",
            "seafood_restaurant",
            "pizza_shop",
            "sushi_restaurant",
            "deli_sandwich_shop",
            "bbq_restaurant",
            "mexican_restaurant",
            "italian_restaurant",
            "chinese_restaurant",
            "indian_restaurant",
            "thai_restaurant",
            "korean_restaurant",
            "mediterranean_restaurant",
            "vegan_vegetarian_restaurant",
            "brunch_restaurant",
            "ramen_noodle_shop",
            "poke_bowl_shop",
            "ethnic_restaurant",
            "coffee_shop_cafe",
            "bakery",
            "juice_smoothie_bar",
            "ice_cream_shop",
            "donut_shop",
            "bubble_tea_shop",
            "food_truck",
            "fast_food",
            "ghost_kitchen",
            "food_hall_vendor",
            "catering_kitchen",
            "butcher_shop",
            "cheese_shop",
            "farmers_market_stall",
            "bar_lounge",
            "brewery_taproom",
            "winery_tasting",
            "wine_bar",
            "cocktail_bar",
            "sports_bar",
            "hookah_lounge",
            "distillery",
            "commercial_farming",
            "livestock_ranching",
            "hydroponic_vertical_farming",
            "forestry_logging",
            "aquaculture_fisheries",
            "vineyard_winery_production",
            "cannabis_cultivation",
            "hemp_farming",
            "grain_production",
            "agricultural_cooperative",
            "fertilizer_pesticide_sales",
            "farm_equipment_sales",
            "boutique_store",
            "clothing_store",
            "shoe_store",
            "jewelry_store",
            "electronics_store",
            "bookstore",
            "pet_store",
            "toy_store",
            "sporting_goods_store",
            "thrift_store",
            "smoke_shop",
            "cannabis_dispensary",
            "convenience_store",
            "grocery_store",
            "liquor_store",
            "florist",
            "gift_shop",
            "furniture_store",
            "home_improvement_store",
            "art_gallery_retail",
            "music_instrument_store",
            "outdoor_recreation_store",
            "phone_repair_store",
            "watch_store",
            "bridal_shop",
            "maternity_store",
            "kids_store",
            "sneaker_store",
            "vintage_store",
            "comic_book_store",
            "record_store",
            "craft_supply_store",
            "fabric_store",
            "health_food_store",
            "vitamin_supplement_store",
            "optical_store",
            "mattress_store",
            "appliance_store",
            "kitchen_bath_store",
            "tile_flooring_store",
            "paint_store",
            "garden_center",
            "gun_store",
            "pawn_shop",
            "dollar_store",
            "hair_salon",
            "nail_salon",
            "day_spa",
            "med_spa",
            "massage_studio",
            "tattoo_parlor",
            "tanning_salon",
            "beauty_supply_store",
            "lash_brow_studio",
            "waxing_studio",
            "sauna_bathhouse",
            "cryotherapy_studio",
            "float_sensory_studio",
            "iv_therapy_lounge",
            "teeth_whitening_studio",
            "microblading_studio",
            "spray_tan_studio",
            "blowout_bar",
            "mens_barbershop",
            "kids_salon",
            "medical_office",
            "dental_office",
            "chiropractic_office",
            "physical_therapy_clinic",
            "optometry_office",
            "dermatology_clinic",
            "urgent_care_clinic",
            "pharmacy",
            "veterinary_clinic",
            "mental_health_clinic",
            "fertility_clinic",
            "acupuncture_clinic",
            "hearing_aid_center",
            "orthopedic_clinic",
            "pediatric_clinic",
            "cosmetic_surgery_center",
            "allergy_clinic",
            "pain_management_clinic",
            "dialysis_center",
            "imaging_center",
            "lab_testing_center",
            "sleep_clinic",
            "weight_loss_clinic",
            "hormone_therapy_clinic",
            "addiction_treatment_center",
            "rehabilitation_center",
            "occupational_therapy_clinic",
            "speech_therapy_clinic",
            "wound_care_center",
            "funeral_home_mortuary",
            "crematory_service",
            "cemetery_memorial_park",
            "casket_urn_retailer",
            "pet_cremation_service",
            "biohazard_cleanup",
            "estate_liquidation",
            "hotel",
            "motel",
            "boutique_hotel",
            "bed_and_breakfast",
            "hostel",
            "resort",
            "campground_rv",
            "vacation_rental_property",
            "extended_stay",
            "glamping_site",
            "cabin_rental",
            "eco_lodge",
            "retreat_center",
            "tutoring_center",
            "daycare_center",
            "preschool",
            "learning_center",
            "music_school",
            "art_school",
            "driving_school",
            "language_school",
            "trade_school",
            "coding_bootcamp_location",
            "montessori_school",
            "after_school_program",
            "swim_school",
            "cooking_school",
            "test_prep_center",
            "special_needs_center",
            "adult_education_center",
            "flight_school",
            "cosmetology_school",
            "movie_theater",
            "escape_room",
            "arcade",
            "mini_golf",
            "laser_tag",
            "go_kart",
            "amusement_park",
            "museum",
            "zoo_aquarium",
            "theater_venue",
            "nightclub",
            "karaoke_bar",
            "comedy_club",
            "live_music_venue",
            "axe_throwing",
            "virtual_reality_arcade",
            "board_game_cafe",
            "cat_cafe",
            "haunted_house",
            "water_park",
            "indoor_playground",
            "concert_venue",
            "drive_in_theater",
            "billiards_hall",
            "dart_bar",
            "indoor_skydiving",
            "law_office",
            "real_estate_office",
            "insurance_office",
            "accounting_office",
            "bank_credit_union",
            "printing_shop",
            "shipping_center",
            "dry_cleaner",
            "laundromat",
            "storage_facility",
            "coworking_space",
            "check_cashing",
            "title_company",
            "travel_agency_storefront",
            "staffing_office",
            "financial_advisor_office",
            "immigration_office",
            "bail_bonds_office",
            "pet_grooming",
            "dog_daycare",
            "pet_boarding",
            "dog_training_facility",
            "pet_spa",
            "aquatic_pet_store",
            "pet_bakery",
            "pet_photography_studio",
            "plumbing_showroom",
            "hvac_showroom",
            "solar_showroom",
            "kitchen_design_showroom",
            "bath_design_showroom",
            "window_door_showroom",
            "pool_spa_showroom",
            "fireplace_showroom",
            "countertop_showroom",
            "nonprofit_organization",
            "charity_foundation",
            "political_campaign",
            "community_organization",
            "environmental_nonprofit",
            "education_nonprofit",
            "health_nonprofit",
            "animal_welfare_nonprofit",
            "arts_culture_nonprofit",
            "social_justice_nonprofit",
            "veterans_nonprofit",
            "youth_nonprofit",
            "disaster_relief_nonprofit",
            "food_bank",
            "housing_nonprofit",
            "government_agency",
            "public_utility",
            "public_library",
            "public_school",
            "municipal_service",
            "military_installation",
            "embassy_consulate",
            "niche_service",
            "niche_product",
            "hybrid_business",
            "other_general",
            "holding_company",
            "family_office",
            "cooperative",
            "social_enterprise",
            "incubator_accelerator",
            "coworking_community",
            "media_company",
            "research_lab",
        ]
    ] = None
    """Specific industry vertical for the account.

    See the
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary)
    for valid values.
    """

    invoice_prefix: Optional[str] = None
    """Prefix used for account invoices."""

    logo_url: Optional[str] = None
    """Account logo image URL."""

    metadata: object
    """Arbitrary key/value metadata supplied at account creation."""

    onboarding_type: Optional[Literal["platform", "seller"]] = None
    """Type of onboarding the account has completed."""

    opengraph_image_url: Optional[str] = None
    """Account Open Graph image URL."""

    opengraph_image_variant: Optional[Literal["white", "black", "orange"]] = None
    """Account Open Graph image variant."""

    other_business_description: Optional[str] = None
    """Business type details when business_type is `other`."""

    other_industry_description: Optional[str] = None
    """Industry details when industry_type is `other`."""

    owner: Owner
    """The single user who owns the account, whose email is the `email` above.

    Distinct from the `owner` role on team members, which any number of them can
    hold.
    """

    parent_account: Optional[ParentAccount] = None
    """Parent account for connected accounts, or `null` for standalone accounts."""

    payment_controls: Optional[PaymentControls] = None
    """Payment health controls currently applied to the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read`
    scope; `null` otherwise.
    """

    product_tax_code: Optional[object] = None
    """
    Tax classification code applied by default to the account's products, with `id`,
    `name`, and `product_type`. `null` when no default is set.
    """

    recommended_actions: Optional[List[RecommendedAction]] = None
    """
    DEPRECATED: Use the `GET /accounts/{account_id}/recommend_actions` endpoint
    instead.
    """

    require_2fa: bool
    """Whether authorized users must enable two-factor authentication."""

    required_actions: Optional[List[RequiredAction]] = None

    route: str
    """Account public route identifier."""

    send_customer_emails: bool
    """Whether Whop sends transactional emails to customers on behalf of this account."""

    show_joined_whops: bool
    """Whether the account appears in joined whops on other accounts."""

    show_reviews_dtc: bool
    """Whether reviews are displayed on direct-to-consumer product pages."""

    show_user_directory: bool
    """Whether the account shows users in the user directory."""

    social_links: List[AccountSocialLink]

    stablecoin_rails: bool
    """
    Whether the account settles on stablecoin rails — its balance is held on-chain
    as USDT and paid out over crypto, rather than as fiat cash.
    """

    status: Optional[str] = None
    """Whether the account can operate on Whop: `active` or `suspended`.

    Computed on `list`, `retrieve`, and `me`; `null` otherwise.
    """

    status_reason: Optional[str] = None
    """Why the account was suspended, in language safe to show the account owner.

    Computed only on `retrieve` and `me`; `null` otherwise, when `status` is not
    `suspended`, and when the suspension was recorded without a reason.
    """

    store_page_config: StorePageConfig
    """Account store page display configuration."""

    target_audience: Optional[str] = None
    """Target audience for this account."""

    tax_collection_enabled_states: List[str]

    tax_identifiers: List[TaxIdentifier]

    tax_remitted_by: Optional[Literal["whop", "self", "none"]] = None
    """
    Who calculates and remits tax for the account: `whop` (Whop calculates and
    remits), `self` (Whop calculates; the account collects and remits), or `none`
    (neither; the account is responsible). `null` until the account enrolls in the
    Whop tax service.
    """

    tax_type: Optional[Literal["inclusive", "exclusive"]] = None
    """
    How tax is applied to the account's prices: `inclusive` (tax included in the
    listed price) or `exclusive` (tax added on top). Defaults to `exclusive` when
    unset; `null` only when the account has no payment connection.
    """

    three_ds_level: Optional[Literal["mandate_challenge"]] = None
    """Account-level 3D Secure behavior.

    `mandate_challenge` requires cardholder verification on supported card payments;
    `null` uses the standard checkout flow.
    """

    title: str
    """Account display name."""

    total_earned_usd: Optional[float] = None
    """Account lifetime sales, normalized to USD.

    Computed only on `retrieve` and `me` for callers with `stats:read` scope; `null`
    otherwise.
    """

    total_usd: Optional[str] = None
    """Total USD value across balances with known exchange rates.

    Computed only on single-account reads (`retrieve` and `me`); `null` on list
    responses, writes, missing balance-read permission, or unavailable balance
    source.
    """

    use_logo_as_opengraph_image_fallback: bool
    """Whether the account uses its logo as the fallback Open Graph image."""

    verification: object
    """
    Account identity verification status for the `individual` (KYC) and `business`
    (KYB) profiles. Each is `null` until created, otherwise a `status` of
    `not_started`, `pending`, `manual_review`, `approved`, or `rejected`.
    """

    volume_usd: Optional[float] = None
    """
    Lifetime volume through the account — sales plus transfers received — normalized
    to USD. Computed only on `list` for callers with `stats:read` on the account;
    `null` otherwise.
    """

    wallet: Optional[Wallet] = None
    """Account primary crypto wallet, or `null` if none has been provisioned."""
