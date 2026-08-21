# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PasskeyChallengeResponse"]


class PasskeyChallengeResponse(BaseModel):
    challenge: str
    """
    The challenge to pass to the WebAuthn ceremony, base64url-encoded without
    padding.
    """
