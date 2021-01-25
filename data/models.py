from pydantic import BaseModel


class LogCreate(BaseModel):
    text: str