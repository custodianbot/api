from fastapi import FastAPI, Request

from data.models import LogCreate
from data.logdriver import LogDriver
from src.response import ok
from src.auth.auth import authenticate

app = FastAPI(docs_url=None)
logs = LogDriver()

@app.get('/')
async def get_root():
    return ok()

@app.post("/logs")
async def create_log(data: LogCreate, request: Request):
    authenticate(request)

    _id = await logs.create_log(data.text)

    return ok(id=_id)

@app.get("/logs/{logid}")
async def get_log(logid: str):
    return await logs.get_log(logid)