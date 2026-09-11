# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AccountFinancingApprovedWebhookEvent",
    "Data",
    "DataBalance",
    "DataBalanceBreakdown",
    "DataBalanceBreakdownPendingSettlement",
    "DataCapabilities",
    "DataCards",
    "DataCompanyFormation",
    "DataCompanyFormationDocument",
    "DataCompanyFormationSignatures",
    "DataCompanyFormationSignaturesForm8821",
    "DataCompanyFormationSignaturesSs4",
    "DataEula",
    "DataEulaMultipartUploadURL",
    "DataOwner",
    "DataOwnerProfilePicture",
    "DataParentAccount",
    "DataParentAccountFees",
    "DataPaymentControls",
    "DataPaymentControlsDisputeAlertAutoRefund",
    "DataPaymentControlsReserve",
    "DataPaymentControlsResolutionCenterAutoRefund",
    "DataPaymentControlsWithdrawalSchedule",
    "DataPrivacyPolicy",
    "DataPrivacyPolicyMultipartUploadURL",
    "DataRecommendedAction",
    "DataRequiredAction",
    "DataReturnPolicy",
    "DataReturnPolicyMultipartUploadURL",
    "DataSocialLink",
    "DataStorePageConfig",
    "DataTaxIdentifier",
    "DataTermsOfService",
    "DataTermsOfServiceMultipartUploadURL",
    "DataWallet",
]


class DataBalanceBreakdownPendingSettlement(BaseModel):
    """When the pending amount is expected to settle, one entry per day, earliest first.

    Money with no scheduled settlement day, such as a transfer in flight, is left out — so these can sum to less than `pending`, never more.
    """

    amount: str
    """Amount expected that day, in native units, as a decimal string."""

    date: str
    """The day this money is expected to finish settling, as an ISO 8601 date."""


class DataBalanceBreakdown(BaseModel):
    """
    Balance split into available, pending, and reserve amounts, as native-unit decimal strings, with the days the pending amount is expected to settle. On-chain crypto is entirely available; good_funds and fiat cash can have pending or reserve portions.
    """

    available: str
    """
    Amount you can spend, send, or withdraw now, in native units, as a decimal
    string.
    """

    in_transit: str
    """
    Amount moving between the account's own destinations, such as a treasury sweep
    to its crypto wallet or a card top-up. In native units, as a decimal string.
    """

    pending: str
    """
    Amount from recent payments still settling, in native units, as a decimal
    string.
    """

    pending_settlements: List[DataBalanceBreakdownPendingSettlement]

    reserve: str
    """Amount held back, in native units, as a decimal string.

    Retrieve the account's reserves for why it is held and when it unlocks.
    """


class DataBalance(BaseModel):
    """Account holdings, each with USD value. Empty when `total_usd` is `null`."""

    balance: str
    """Total amount held in native units, as a decimal string."""

    breakdown: DataBalanceBreakdown
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


class DataCapabilities(BaseModel):
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


class DataCards(BaseModel):
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


class DataCompanyFormationDocument(BaseModel):
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


class DataCompanyFormationSignaturesForm8821(BaseModel):
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


class DataCompanyFormationSignaturesSs4(BaseModel):
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


class DataCompanyFormationSignatures(BaseModel):
    """IRS forms still awaiting a founder's signature, each with a hosted signing URL.

    Present once `status` leaves `draft`; empty when nothing needs signing.
    """

    form8821: Optional[DataCompanyFormationSignaturesForm8821] = None
    """Signature state for IRS Form 8821, the tax information authorization.

    Present only while the form still needs the founder's action.
    """

    ss4: Optional[DataCompanyFormationSignaturesSs4] = None
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


class DataCompanyFormation(BaseModel):
    """
    Company formation state for the account, managed through [Form Company](/api-reference/beta/accounts/form-company). A `draft` `status` until the formation checkout is paid, then filing progress with downloadable documents and signatures awaiting action. Empty when the formation state is temporarily unavailable.
    """

    documents: Optional[List[DataCompanyFormationDocument]] = None

    ein_registered: Optional[bool] = None
    """Whether the company's EIN has been issued by the IRS.

    Present once `status` leaves `draft`.
    """

    legal_name: Optional[str] = None
    """Registered company name including the entity ending, for example `Acme, LLC`.

    Present once `status` leaves `draft`.
    """

    signatures: Optional[DataCompanyFormationSignatures] = None
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


class DataEulaMultipartUploadURL(BaseModel):
    """The presigned URL for each part.

    Present only on create, and only for multipart uploads.
    """

    part_number: int
    """The 1-based index of this part within the multipart upload."""

    url: str
    """The presigned URL to PUT this part's bytes to."""


class DataEula(BaseModel):
    """
    The account's end-user license agreement document, or `null` if they have not published one.
    """

    id: str
    """The file's ID, prefixed `file_`."""

    content_type: Optional[str] = None
    """The file's MIME type, e.g. `application/pdf`."""

    created_at: str
    """When the file was created, as an ISO 8601 timestamp."""

    filename: Optional[str] = None
    """The original filename, including its extension."""

    object: str
    """The type of this object, always `file`."""

    size: Optional[int] = None
    """The file size in bytes. `null` until the upload has finished."""

    upload_status: Literal["pending", "processing", "ready", "failed"]
    """Where the file is in its upload lifecycle."""

    url: Optional[str] = None
    """
    A URL to download the file: a permanent CDN URL for public files, a signed
    expiring URL for private ones. `null` until the upload has finished.
    """

    visibility: Literal["public", "private"]
    """
    `public` files are served via an unsigned CDN URL; `private` files via a signed,
    expiring URL.
    """

    multipart_chunk_size: Optional[int] = None
    """The byte size each part (except the last) must be.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_id: Optional[str] = None
    """The ID of the multipart upload, passed back to `complete`.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_urls: Optional[List[DataEulaMultipartUploadURL]] = None

    upload_headers: Optional[builtins.object] = None
    """Headers to send with the upload PUT. Present only on create."""

    upload_url: Optional[str] = None
    """Presigned URL to PUT the file's bytes to.

    Present only on create, and only for single-part uploads.
    """


class DataOwnerProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class DataOwner(BaseModel):
    """The single user who owns the account, whose email is the `email` above.

    Distinct from the `owner` role on team members, which any number of them can hold.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: DataOwnerProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class DataParentAccountFees(BaseModel):
    fixed_fee_usd: float
    """Fixed markup in US dollars per transaction."""

    percentage_fee: float
    """Percentage of the transaction charged as markup."""


class DataParentAccount(BaseModel):
    """Parent account for connected accounts, or `null` for standalone accounts."""

    id: str
    """Account ID, prefixed `biz_`."""

    logo_url: Optional[str] = None
    """Account logo image URL."""

    route: str
    """Account public route identifier."""

    title: str
    """Account display name."""

    fees: Optional[Dict[str, DataParentAccountFees]] = None
    """
    Markup rates this parent charges the connected account being read, keyed by fee
    type (for example `crypto_deposit_markup`), each with `percentage_fee` and
    `fixed_fee_usd`. Resolved with the connected account's own overrides winning
    over the platform default.
    """


class DataPaymentControlsDisputeAlertAutoRefund(BaseModel):
    """Automatic refund settings for pre-chargeback dispute alerts."""

    locked: bool
    """Whether the account owner is prevented from changing this threshold."""

    threshold_usd: Optional[float] = None
    """Maximum dispute alert amount automatically refunded in USD.

    `null` when automatic refunds are disabled.
    """


class DataPaymentControlsReserve(BaseModel):
    """Reserve currently applied to incoming payment volume."""

    hold_period_days: int
    """Number of days reserved funds are held before release."""

    percentage: Optional[float] = None
    """Percentage of incoming payment volume held in reserve.

    `null` when no reserve is applied.
    """


class DataPaymentControlsResolutionCenterAutoRefund(BaseModel):
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


class DataPaymentControlsWithdrawalSchedule(BaseModel):
    """How the account's balance automatically withdraws."""

    day: Optional[int] = None
    """
    Day the automatic withdrawal runs on: 0-6 (Sunday-Saturday) for `weekly`, 1-31
    for `monthly`. `null` for `manual` and `daily`.
    """

    frequency: Literal["manual", "daily", "weekly", "monthly"]
    """How often the account's balance automatically withdraws."""

    next_payout_date: Optional[str] = None
    """Next date the automatic withdrawal is scheduled to run, as an ISO 8601 date.

    `null` for `manual` and `daily`, where no single next date applies.
    """


class DataPaymentControls(BaseModel):
    """Payment health controls currently applied to the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    dispute_alert_auto_refund: DataPaymentControlsDisputeAlertAutoRefund
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

    reserve: DataPaymentControlsReserve
    """Reserve currently applied to incoming payment volume."""

    resolution_center_auto_refund: DataPaymentControlsResolutionCenterAutoRefund
    """Automatic refund settings for resolution center cases."""

    restricted_payment_methods: List[
        Literal["card_visa", "card_mastercard", "card_american_express", "card_discover_global_network"]
    ]

    undated_pending_reason: Optional[
        Literal["kyc_incomplete", "pending_information_request", "withdrawals_disabled"]
    ] = None
    """Why pending funds without a settlement date aren't moving yet.

    `kyc_incomplete` and `pending_information_request` are things the merchant can
    act on. `withdrawals_disabled` means Whop has blocked withdrawals, so these
    funds cannot become available. `null` when there's no reason to show — still
    clearing, or held for a reason that isn't named here.
    """

    withdrawal_schedule: DataPaymentControlsWithdrawalSchedule
    """How the account's balance automatically withdraws."""


class DataPrivacyPolicyMultipartUploadURL(BaseModel):
    """The presigned URL for each part.

    Present only on create, and only for multipart uploads.
    """

    part_number: int
    """The 1-based index of this part within the multipart upload."""

    url: str
    """The presigned URL to PUT this part's bytes to."""


class DataPrivacyPolicy(BaseModel):
    """
    The account's privacy policy document, or `null` if they have not published one.
    """

    id: str
    """The file's ID, prefixed `file_`."""

    content_type: Optional[str] = None
    """The file's MIME type, e.g. `application/pdf`."""

    created_at: str
    """When the file was created, as an ISO 8601 timestamp."""

    filename: Optional[str] = None
    """The original filename, including its extension."""

    object: str
    """The type of this object, always `file`."""

    size: Optional[int] = None
    """The file size in bytes. `null` until the upload has finished."""

    upload_status: Literal["pending", "processing", "ready", "failed"]
    """Where the file is in its upload lifecycle."""

    url: Optional[str] = None
    """
    A URL to download the file: a permanent CDN URL for public files, a signed
    expiring URL for private ones. `null` until the upload has finished.
    """

    visibility: Literal["public", "private"]
    """
    `public` files are served via an unsigned CDN URL; `private` files via a signed,
    expiring URL.
    """

    multipart_chunk_size: Optional[int] = None
    """The byte size each part (except the last) must be.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_id: Optional[str] = None
    """The ID of the multipart upload, passed back to `complete`.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_urls: Optional[List[DataPrivacyPolicyMultipartUploadURL]] = None

    upload_headers: Optional[builtins.object] = None
    """Headers to send with the upload PUT. Present only on create."""

    upload_url: Optional[str] = None
    """Presigned URL to PUT the file's bytes to.

    Present only on create, and only for single-part uploads.
    """


class DataRecommendedAction(BaseModel):
    """
    Deprecated: use the `GET /economic_intelligence?account_id={account_id}` endpoint instead. Optional actions that unlock capabilities or grow the account, same shape as `required_actions`. Computed only on `retrieve` and `me`; `null` otherwise.
    """

    action: Literal[
        "theme_business",
        "create_product",
        "create_plan",
        "verify_identity",
        "connect_affiliate_program",
        "create_promotion",
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


class DataRequiredAction(BaseModel):
    """
    Actions the account owner must take to unblock capabilities like payouts and card spend, ordered by display priority. Computed only on `retrieve` and `me` for callers with `company:balance:read` scope; `null` otherwise.
    """

    action: Literal[
        "deposit_funds",
        "accept_airwallex_terms",
        "submit_information_request",
        "update_automatic_withdrawal_method",
        "reauthorize_payout_methods",
        "update_payout_profile",
        "card_usage_review",
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


class DataReturnPolicyMultipartUploadURL(BaseModel):
    """The presigned URL for each part.

    Present only on create, and only for multipart uploads.
    """

    part_number: int
    """The 1-based index of this part within the multipart upload."""

    url: str
    """The presigned URL to PUT this part's bytes to."""


class DataReturnPolicy(BaseModel):
    """The account's return policy document, or `null` if they have not published one."""

    id: str
    """The file's ID, prefixed `file_`."""

    content_type: Optional[str] = None
    """The file's MIME type, e.g. `application/pdf`."""

    created_at: str
    """When the file was created, as an ISO 8601 timestamp."""

    filename: Optional[str] = None
    """The original filename, including its extension."""

    object: str
    """The type of this object, always `file`."""

    size: Optional[int] = None
    """The file size in bytes. `null` until the upload has finished."""

    upload_status: Literal["pending", "processing", "ready", "failed"]
    """Where the file is in its upload lifecycle."""

    url: Optional[str] = None
    """
    A URL to download the file: a permanent CDN URL for public files, a signed
    expiring URL for private ones. `null` until the upload has finished.
    """

    visibility: Literal["public", "private"]
    """
    `public` files are served via an unsigned CDN URL; `private` files via a signed,
    expiring URL.
    """

    multipart_chunk_size: Optional[int] = None
    """The byte size each part (except the last) must be.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_id: Optional[str] = None
    """The ID of the multipart upload, passed back to `complete`.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_urls: Optional[List[DataReturnPolicyMultipartUploadURL]] = None

    upload_headers: Optional[builtins.object] = None
    """Headers to send with the upload PUT. Present only on create."""

    upload_url: Optional[str] = None
    """Presigned URL to PUT the file's bytes to.

    Present only on create, and only for single-part uploads.
    """


class DataSocialLink(BaseModel):
    """Account social links."""

    id: str
    """The ID of the social link"""

    title: Optional[str] = None
    """The optional display title for the social link"""

    url: str
    """The social link URL"""

    website: Literal["x", "instagram", "facebook", "tiktok", "youtube", "linkedin", "twitch", "website", "custom"]
    """The social platform for this link"""


class DataStorePageConfig(BaseModel):
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


class DataTaxIdentifier(BaseModel):
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


class DataTermsOfServiceMultipartUploadURL(BaseModel):
    """The presigned URL for each part.

    Present only on create, and only for multipart uploads.
    """

    part_number: int
    """The 1-based index of this part within the multipart upload."""

    url: str
    """The presigned URL to PUT this part's bytes to."""


class DataTermsOfService(BaseModel):
    """
    The account's terms of service document, or `null` if they have not published one.
    """

    id: str
    """The file's ID, prefixed `file_`."""

    content_type: Optional[str] = None
    """The file's MIME type, e.g. `application/pdf`."""

    created_at: str
    """When the file was created, as an ISO 8601 timestamp."""

    filename: Optional[str] = None
    """The original filename, including its extension."""

    object: str
    """The type of this object, always `file`."""

    size: Optional[int] = None
    """The file size in bytes. `null` until the upload has finished."""

    upload_status: Literal["pending", "processing", "ready", "failed"]
    """Where the file is in its upload lifecycle."""

    url: Optional[str] = None
    """
    A URL to download the file: a permanent CDN URL for public files, a signed
    expiring URL for private ones. `null` until the upload has finished.
    """

    visibility: Literal["public", "private"]
    """
    `public` files are served via an unsigned CDN URL; `private` files via a signed,
    expiring URL.
    """

    multipart_chunk_size: Optional[int] = None
    """The byte size each part (except the last) must be.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_id: Optional[str] = None
    """The ID of the multipart upload, passed back to `complete`.

    Present only on create, and only for multipart uploads.
    """

    multipart_upload_urls: Optional[List[DataTermsOfServiceMultipartUploadURL]] = None

    upload_headers: Optional[builtins.object] = None
    """Headers to send with the upload PUT. Present only on create."""

    upload_url: Optional[str] = None
    """Presigned URL to PUT the file's bytes to.

    Present only on create, and only for single-part uploads.
    """


class DataWallet(BaseModel):
    """Account primary crypto wallet, or `null` if none has been provisioned."""

    id: str
    """Wallet ID, prefixed `wallet_`."""

    address: str
    """The on-chain address of the wallet"""

    network: Literal["solana", "ethereum", "bitcoin"]
    """The blockchain network the wallet lives on"""


class Data(BaseModel):
    id: str
    """Account ID, prefixed `biz_`."""

    balances: List[DataBalance]

    banner_image_url: Optional[str] = None
    """Account banner image URL."""

    business_address: Optional[object] = None
    """
    Account business address used to calculate tax, with `line1`, `line2`, `city`,
    `state`, `postal_code`, and `country`. `null` when no address is set.
    """

    business_name: Optional[str] = None
    """The account's legal business name used with its tax address."""

    business_type: Optional[str] = None
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

    capabilities: Optional[DataCapabilities] = None
    """
    Payment rails enabled for this account, each `active`, `inactive`, or `pending`
    (onboarding or review in progress). Computed only on `retrieve` and `me` for
    callers with `company:balance:read` scope; `null` otherwise.
    """

    cards: Optional[DataCards] = None
    """Whop Cards application details for the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read`
    scope; `null` otherwise, or when the account has no card application.
    """

    collect_vat_id: bool
    """Whether checkout shows a VAT/tax ID field for buyers to optionally enter.

    Does not require a VAT ID to purchase.
    """

    company_formation: DataCompanyFormation
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

    economic_intelligence: bool
    """Whether economic intelligence is enabled for the account."""

    email: Optional[str] = None
    """Account owner email address."""

    eula: Optional[DataEula] = None
    """
    The account's end-user license agreement document, or `null` if they have not
    published one.
    """

    home_preferences: List[Literal["hide_member_count", "hide_members_card"]]

    industry_group: Optional[str] = None
    """Account industry group.

    See the
    [business types and industries glossary](/api-reference/beta/accounts/account#business-types-and-industries-glossary)
    for valid values.
    """

    industry_type: Optional[str] = None
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

    owner: DataOwner
    """The single user who owns the account, whose email is the `email` above.

    Distinct from the `owner` role on team members, which any number of them can
    hold.
    """

    parent_account: Optional[DataParentAccount] = None
    """Parent account for connected accounts, or `null` for standalone accounts."""

    payment_controls: Optional[DataPaymentControls] = None
    """Payment health controls currently applied to the account.

    Computed only on `retrieve` and `me` for callers with `company:balance:read`
    scope; `null` otherwise.
    """

    privacy_policy: Optional[DataPrivacyPolicy] = None
    """
    The account's privacy policy document, or `null` if they have not published one.
    """

    product_tax_code: Optional[object] = None
    """
    Tax classification code applied by default to the account's products, with `id`,
    `name`, and `product_type`. `null` when no default is set.
    """

    recommended_actions: Optional[List[DataRecommendedAction]] = None
    """
    DEPRECATED: Use the `GET /economic_intelligence?account_id={account_id}`
    endpoint instead.
    """

    require_2fa: bool
    """Whether authorized users must enable two-factor authentication."""

    required_actions: Optional[List[DataRequiredAction]] = None

    return_policy: Optional[DataReturnPolicy] = None
    """The account's return policy document, or `null` if they have not published one."""

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

    social_links: List[DataSocialLink]

    stablecoin_rails: bool
    """
    Whether the account settles on stablecoin rails — its balance is held on-chain
    as USDT and paid out over crypto, rather than as fiat cash.
    """

    status: Optional[str] = None
    """Whether the account can operate on Whop: `active` or `suspended`.

    Computed on `list`, `retrieve`, `me`, and `suspend`; `null` otherwise.
    """

    status_reason: Optional[str] = None
    """Why the account was suspended, in language safe to show the account owner.

    Computed on `retrieve`, `me`, and `suspend`; `null` otherwise, when `status` is
    not `suspended`, and when the suspension was recorded without a reason.
    """

    store_page_config: DataStorePageConfig
    """Account store page display configuration."""

    target_audience: Optional[str] = None
    """Target audience for this account."""

    tax_collection_enabled_states: List[str]

    tax_identifiers: List[DataTaxIdentifier]

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

    terms_of_service: Optional[DataTermsOfService] = None
    """
    The account's terms of service document, or `null` if they have not published
    one.
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

    wallet: Optional[DataWallet] = None
    """Account primary crypto wallet, or `null` if none has been provisioned."""


class AccountFinancingApprovedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["account.financing_approved"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
