from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from schemas import stdResponse,StudentBase,patchStudent


app=FastAPI()

@app.get("/student/",response_model=list[stdResponse])
async def show_all_student(db:Session=Depends(get_db)):
    try:
        students=db.query(Student).all()
        response=[]

        for stud in students:
            response.append(stdResponse(
                id=stud.id,
                name=stud.name,
                age=stud.age,
                address={
                    "street": stud.street,
                    "housenum": stud.housenum,
                    "zipcode": stud.zipcode
                }
                
            ))

        return response
        
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")

@app.get("/student/{id}",response_model=stdResponse)
async def get_student_by_id(id:int,db:Session=Depends(get_db)):
    try:
        stud=db.query(Student).filter(Student.id==id).first()
        if not stud:
            raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")
        response=[]

        return stdResponse(
                id=stud.id,
                name=stud.name,
                age=stud.age,
                address={
                    "street": stud.street,
                    "housenum": stud.housenum,
                    "zipcode": stud.zipcode
                }
                
            )

    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")


@app.post("/student/",response_model=stdResponse)
async def add_student(student:StudentBase,db:Session=Depends(get_db)):
    try:
        db_student=Student(name=student.name,
                           age=student.age,
                           street=student.address.street,
                           housenum=student.address.housenum,
                           zipcode=student.address.zipcode)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return stdResponse(
            id=db_student.id,
            name=db_student.name,
            age=db_student.age,
            address={
                "street": db_student.street,
                "housenum": db_student.housenum,
                "zipcode": db_student.zipcode
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Adding Student: {str(e)}")
    
@app.delete("/student/{id}",response_model=stdResponse)
async def del_student(id:int,db:Session=Depends(get_db)):
    try:
        stud=db.query(Student).filter(Student.id==id).first()
        if not stud:
            raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")

        db.delete(stud)
        db.commit()
        return stdResponse(
    id=stud.id,
    name=stud.name,
    age=stud.age,
    address={
        "street": stud.street,
        "housenum": stud.housenum,
        "zipcode": stud.zipcode
    }
)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Deleting Student: {str(e)}")


@app.patch("/student/{id}",response_model=stdResponse)
async def patchstudent(id:int,student_patch:patchStudent,db:Session=Depends(get_db)):
    try:
        stud=db.query(Student).filter(Student.id==id).first()
        if not stud:
            raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")
        
        if student_patch.name is not None:
            stud.name=student_patch.name
        if student_patch.age is not None:
            stud.age=student_patch.age
        if student_patch.street is not None:
            stud.street=student_patch.street
        if student_patch.housenum is not None:
            stud.housenum=student_patch.housenum
        if student_patch.zipcode is not None:
            stud.zipcode=student_patch.zipcode

        db.commit()
        db.refresh(stud)
        return stdResponse(
            id=stud.id,
            name=stud.name,
            age=stud.age,
            address={
                "street": stud.street,
                "housenum": stud.housenum,
                "zipcode": stud.zipcode
            }
            
        )

    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")

@app.put("/student/{id}",response_model=stdResponse)
async def update_student(id:int,student_update:StudentBase,db:Session=Depends(get_db)):
    try:
        stud=db.query(Student).filter(Student.id==id).first()
        if not stud:
            raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")
        stud.name = student_update.name
        stud.age = student_update.age
        stud.street=student_update.address.street
        stud.housenum=student_update.address.housenum
        stud.zipcode=student_update.address.zipcode
        


        db.commit()
        db.refresh(stud)
        return stdResponse(
            id=stud.id,
            name=stud.name,
            age=stud.age,
            address={
                "street": stud.street,
                "housenum": stud.housenum,
                "zipcode": stud.zipcode
            }
            
        )
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Error Fetching:{str(e)}")
    