from fastapi import FastAPI, HTTPException, Path, Query, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import session
from database import engine, SessionLocal, Base
import  schemas, crud
from typing import List


Base.metadata.create_all(bind=engine)

app=FastAPI()

#DB Dependency 
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', response_model=List[schemas.EmployeeOut])
def GetAll(db: session =Depends(get_db)):
    return crud.get_all(db)


@app.get('/{emp_id}', response_model=schemas.EmployeeOut)
def GetEmpDetails(emp_id:int, db: session =Depends(get_db)):
    employee=crud.get_employee(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=401, detail='employee not found')
    return employee


@app.post('/create', response_model=schemas.EmployeeOut)
def create(empData : schemas.EmployeeCreate,db: session =Depends(get_db)):
    return crud.create_employee(db,empData)
    #return {'message',f'Employee created succesfully with ID {createdData.id}'}

@app.patch('/update/{emp_id}', response_model=schemas.EmployeeOut)
def update(emp_id:int, empData : schemas.EmployeeCreate,db: session =Depends(get_db)):
    
    employee=crud.get_employee(db,emp_id)
    if employee is None:
            raise HTTPException(status_code=401, detail='employee not found')
    
    return crud.update_employee(db,emp_id, empData)
    return {'message',f'Employee updated succesfully with ID {updatedData.id}'}

@app.delete('/remove/{emp_id}', response_model=dict)
def delete(emp_id:int,db: session =Depends(get_db)):
    employee=crud.get_employee(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=401, detail='employee not found')
    
    crud.delete_employee(db,emp_id)
    return {'message':f'Employee deleted succesfully with ID {emp_id}'}