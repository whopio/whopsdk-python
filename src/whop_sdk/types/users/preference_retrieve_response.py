# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PreferenceRetrieveResponse"]


class PreferenceRetrieveResponse(BaseModel):
    investigation_enabled: bool
    """Whether investigation mode is enabled for the user.

    Only meaningful for staff users with investigation access.
    """
