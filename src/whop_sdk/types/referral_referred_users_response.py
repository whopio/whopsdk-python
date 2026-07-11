# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ReferralReferredUsersResponse", "Data", "DataUser", "DataUserProfilePicture", "PageInfo"]


class DataUserProfilePicture(BaseModel):
    url: Optional[str] = None


class DataUser(BaseModel):
    id: str

    username: str

    city: Optional[str] = None

    country: Optional[str] = None

    name: Optional[str] = None

    profile_picture: Optional[DataUserProfilePicture] = None


class Data(BaseModel):
    total_earnings_usd: str

    total_volume_usd: str

    user: DataUser


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class ReferralReferredUsersResponse(BaseModel):
    data: List[Data]

    page_info: PageInfo
