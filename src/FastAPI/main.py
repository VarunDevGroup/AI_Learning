from fastapi import FastAPI, HTTPException
from models import  Employee
import json
from typing import List


employee_db: List[Employee]=[]

app=FastAPI()

@app.get('/employees', response_model=List[Employee])
def get_employees():
    return employee_db

@app.get('/employee/{id}', response_model=Employee)
def get_employee(id:int):
    for index,emp in  enumerate(employee_db):
        if emp.id==id:
            return employee_db[index]

    raise HTTPException(status_code=401, detail="Employee not found")   

@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employee_db:
        if employee.id==new_emp.id:
            raise HTTPException(status_code=401,detail="Employee ID duplicate")
    employee_db.append(new_emp)
    return new_emp

@app.put('/update_employee/{id}')
def update_employee(id:int, updated_employee:Employee):
    for index, emp in enumerate(employee_db):
        if emp.id== id:
            employee_db[index]=updated_employee
            return updated_employee

    raise HTTPException(status_code=401,detail='Employee not found')

@app.delete('/delete_employee/{id}')
def delete_employee(id:int):
    for index, emp in enumerate(employee_db):
        if emp.id==id:
            del employee_db[index]
            return {'message':{'Employee deleted successfully'}}

    raise HTTPException(status_code=401,detail='Employee not found')
