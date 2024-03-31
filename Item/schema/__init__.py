from pydantic import BaseModel
from typing import List
from model.types.item import user, item

class GetAllItemOutput(BaseModel):
    items: List[item]

class CreateUserInput(BaseModel):
    name: str

class CreateItemInput(BaseModel):
    name: str
    user_id: int

class GetUsersOutput(BaseModel):
    user_id: int