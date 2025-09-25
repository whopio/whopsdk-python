# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPagePageInfo", "SyncCursorPage", "AsyncCursorPage"]

_T = TypeVar("_T")


class CursorPagePageInfo(BaseModel):
    end_cursor: Optional[str] = None


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    page_info: Optional[CursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        end_cursor = None
        if self.page_info is not None:
            if self.page_info.end_cursor is not None:
                end_cursor = self.page_info.end_cursor
        if not end_cursor:
            return None

        return PageInfo(params={"after": end_cursor})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    page_info: Optional[CursorPagePageInfo] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        end_cursor = None
        if self.page_info is not None:
            if self.page_info.end_cursor is not None:
                end_cursor = self.page_info.end_cursor
        if not end_cursor:
            return None

        return PageInfo(params={"after": end_cursor})
