# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .audience import Audience

__all__ = ["AudienceCreateResponse", "Data"]


class Data(BaseModel):
    data: List[Audience]


AudienceCreateResponse: TypeAlias = Union[Audience, Data]
