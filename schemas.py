from pydantic import BaseModel,Field,validator
from typing import Optional
 

class StudentAddress(BaseModel):
    street:str=Field(...,min_length=1,max_length=10)
    housenum:str=Field(...,min_length=1,max_length=10)
    zipcode:int=Field(...,le=99999,ge=0)

class StudentBase(BaseModel):
    name:str
    age:int=Field(...,gt=2,lt=20)
    username:str=Field(...,min_length=3,max_length=20)
    password:str=Field(...,min_length=6,max_length=20)
    email:str=Field(...,regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    address:StudentAddress
    @validator("name")
    def name_change(cls,v):
        if any(char.isdigit() for char in v):
            raise ValueError("Name must not contain numbers")
        return v
    

class patchStudent(BaseModel):
    name:Optional[str]=None
    password:Optional[str]=None
    email:Optional[str]=None
    age:Optional[int]=None
    street: Optional[str] = None
    housenum: Optional[str] = None
    zipcode: Optional[int] = None
    class Config:
        #orm_mode=True
        from_attributes=True

class stdResponse(StudentBase):
    id:int

    class Config:
        #orm_mode
        from_attributes=True