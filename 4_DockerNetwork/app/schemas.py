from pydantic import BaseModel
from typing import Union

class TodoBase(BaseModel):
    title : str
    description: Union[str, None] = None

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id : int

    class Config:
        from_attributes = True
