from aioredis import create_redis_pool
from randutils import formatstring
from asyncio import get_event_loop

from fastapi.exceptions import HTTPException
from starlette.responses import PlainTextResponse


class LogDriver:
    def __init__(self):
        self.pool = None

    async def init(self):
        if not self.pool:
            self.pool = await create_redis_pool("redis://redis")

    async def create_log(self, text: str) -> str:
        await self.init()
        _id = formatstring("xxxxxx-xxxxxxxxxxxx-xxxxxx")

        await self.pool.set("logs_" + _id, text, expire=86400 * 14) # Logs expire after 14 days

        return _id

    async def get_log(self, logid: str):
        await self.init()
        log = await self.pool.get("logs_" + logid)

        if not log:
            raise HTTPException(404, "Log not found.")

        return PlainTextResponse(log)