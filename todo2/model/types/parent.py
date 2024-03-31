from pydantic import BaseModel

class Parent(BaseModel):
    parent_id: str
    email: str
    password: str
    name: str

    class Config:
        orm_mode = True