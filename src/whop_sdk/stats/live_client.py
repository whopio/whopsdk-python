from __future__ import annotations

import whop_sdk.stats.client as generated
from whop_sdk.lib.live import resource
from whop_sdk.stats.time_series.live_client import AsyncTimeSeriesClient, TimeSeriesClient


class StatsClient(generated.StatsClient):
    @property
    def time_series(self) -> TimeSeriesClient:
        return resource(self, TimeSeriesClient)


class AsyncStatsClient(generated.AsyncStatsClient):
    @property
    def time_series(self) -> AsyncTimeSeriesClient:
        return resource(self, AsyncTimeSeriesClient)
