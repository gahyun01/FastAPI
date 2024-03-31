from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from model.types.todo import Todo

class CreateTodoInput(BaseModel):
    create_time: datetime
    title: str
    content: str

class CreateTodoOutput(BaseModel):
    success: int
    todo: Optional[Todo]

class GetUserTodos(BaseModel):
    todos: List[Todo]

class GetTodoById(BaseModel):
    create_time: datetime
    title: str
    content: str
    parent_id: str