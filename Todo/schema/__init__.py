from pydantic import BaseModel
from typing import List
from model.types.todo import Todo

class GetAllTodoOutput(BaseModel):
    todos : List[Todo]

class CreateTodoInput(BaseModel):
    todo : str

class GetTodoOutput(BaseModel):
    id: int