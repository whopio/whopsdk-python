# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AppLogsResponse", "Data", "PageInfo"]


class Data(BaseModel):
    app_build_id: str

    app_id: str

    created_at: datetime

    level: Literal["log", "debug", "info", "warn", "error"]

    message: str

    request_id: str

    source: Literal["console", "exception", "request"]

    cpu_time_ms: Optional[int] = None

    outcome: Optional[str] = None

    request_method: Optional[str] = None

    request_path: Optional[str] = None

    response_status: Optional[int] = None

    stack: Optional[str] = None

    truncated: Optional[bool] = None

    wall_time_ms: Optional[int] = None


class PageInfo(BaseModel):
    has_next_page: bool

    has_previous_page: bool

    end_cursor: Optional[str] = None

    start_cursor: Optional[str] = None


class AppLogsResponse(BaseModel):
    data: List[Data]

    page_info: PageInfo
