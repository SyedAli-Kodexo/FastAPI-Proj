from sqlalchemy import Integer,String,Column
from database import Base,engine

class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(20),index=True)
    age=Column(Integer)
    street = Column(String(50))
    housenum = Column(String(10))
    zipcode = Column(Integer)
    
    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, age={self.age}, street={self.street}, housenum={self.housenum}, zipcode={self.zipcode})>"

Base.metadata.create_all(bind=engine)
