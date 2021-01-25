from os import environ as env
from hmac import compare_digest

from fastapi import Request
from fastapi.exceptions import HTTPException

def authenticate(request: Request):
    token = request.headers.get("X-Api-Token", None)

    if not token:
        raise HTTPException(403, "Invalid token passed.")

    if not compare_digest(token, env["API_TOKEN"]):
        raise HTTPException(403, "Invalid token passed.")
