from __future__ import annotations

import whop_sdk.base_client as generated
from whop_sdk.lib.live import resource
from whop_sdk.stats.live_client import AsyncStatsClient, StatsClient


class Whop(generated.BaseWhop):
    @property
    def stats(self) -> StatsClient:
        return resource(self, StatsClient)


class AsyncWhop(generated.AsyncBaseWhop):
    @property
    def stats(self) -> AsyncStatsClient:
        return resource(self, AsyncStatsClient)
