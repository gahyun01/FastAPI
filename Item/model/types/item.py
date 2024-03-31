from pydantic import BaseModel

class user(BaseModel):
    user_id : int
    name : str

class item(BaseModel):
    item_id : int
    iname : str
    user_id : int