from sqlalchemy import Integer,String,Column
from pydantic import BaseModel
from database import Base,engine

class Student(Base):
    __tablename__="student"
    username = Column(String(50), unique=True, index=True)
    password = Column(String)
    email = Column(String(50), unique=True, index=True)
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(20),index=True)
    age=Column(Integer)
    street = Column(String(50))
    housenum = Column(String(10))
    zipcode = Column(Integer)
    
    def __repr__(self):
        return f"<Student(id={self.id},username:{self.username},password={self.password},email={self.email}, name={self.name}, age={self.age}, street={self.street}, housenum={self.housenum}, zipcode={self.zipcode})>"

Base.metadata.create_all(bind=engine)


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type:str
