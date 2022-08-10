from datetime import date
from pydantic import BaseModel


class Record(BaseModel):
    key: int
    value: str

    class Config:
        orm_mode = False