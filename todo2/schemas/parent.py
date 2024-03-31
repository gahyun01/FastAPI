from pydantic import BaseModel
from typing import List, Optional
from model.types.parent import Parent

class CreateParentInput(BaseModel):
    parent_id: str
    email: str
    password: str
    name: str

class CreateParentOutput(BaseModel):
    success: int
    parent: Optional[Parent]

class GetParentById(BaseModel):
    parent_id: str
    email: str
    password: str
    name: str

class GetParentByEmail(BaseModel):
    parent_id: str
    email: str
    password: str
    name: str

class UpdateParentInput(BaseModel):
    parent_id: str
    email: str
    password: str
    name: str

class UpdateParentOutput(BaseModel):
    success: int
    parent: Optional[Parent]

class DeleteParentInput(BaseModel):
    parent_id: str

class DeleteParentOutput(BaseModel):
    success: int
    parent: Optional[Parent]