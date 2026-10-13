from sqlalchemy.orm import Session
import models, schemas

#return all the rows
def get_all(db: Session):
    return (
        db
        .query(models.Employee)
        .all()
    )

def get_employee(db:Session, emp_id:int):
    #return db.query(models.Employee).get(emp_id)
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id==emp_id)
        .first()
    )

def create_employee(db:Session, emp:schemas.EmployeeCreate) -> models.Employee:
    db_employee=models.Employee(
        name=emp.name,
        email=emp.email,
        age=emp.age
        )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db:Session, emp_id:int, emp:schemas.EmployeeUpdate) ->models.Employee:
    db_employee= get_employee(db, emp_id)
    
    if db_employee:
        db_employee.name=emp.name
        db_employee.email= emp.email
        db_employee.age=emp.age
        db.commit()
        db.refresh(db_employee)
        return db_employee

def delete_employee(db:Session, emp_id:int):
    db_employee= get_employee(db, emp_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()



    