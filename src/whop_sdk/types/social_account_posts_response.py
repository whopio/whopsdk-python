# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .social_account_post import SocialAccountPost

__all__ = ["SocialAccountPostsResponse", "PageInfo"]


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool


class SocialAccountPostsResponse(BaseModel):
    data: List[SocialAccountPost]

    page_info: PageInfo
