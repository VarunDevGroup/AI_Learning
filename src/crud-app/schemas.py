from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class EmployeeBase(BaseModel):
    name: str
    email : EmailStr
    age: Annotated[int, Field(...,gt=0,lt=100)]

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id : int 

    class Config:
        orm_mode=True




