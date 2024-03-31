from pydantic import BaseModel

#type checking
class Todo(BaseModel):
    id: int
    todo : str