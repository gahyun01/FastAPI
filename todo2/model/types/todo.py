from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    todo_id: int
    create_time: datetime
    title: str
    content: str
    parent_id: str

    class Config:
        orm_mode = True