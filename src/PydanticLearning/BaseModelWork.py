from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List,Dict, Optional, Annotated
#FieldValidator is required for custom validator


class Teacher(BaseModel):
    TeacherID : int
    TacherName : str
    TeacherSubject : str
    TeacherClass : int
    TeacherEmail : EmailStr

    @field_validator('TeacherEmail')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['dpsnt.com','dpsmc.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("not a valid domain")

        return value
            


class Employee(BaseModel):

    EmpName: Annotated[str, Field(max_length=50, title="Emploee Name",description="enter full name")]
    EmpDepartment: str
    EmpID : Annotated[str, Field(min_length=6,strict=True,title="LTM Employee ID")]
    Age : int = Field(gt=0, le=100)
    Gender : Optional[str] =None
    Email : EmailStr
    Skills : List[str]
    Contacts : Dict[str,str]
    LinkedIn : AnyUrl

    @field_validator('Email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['dpsnt.com','dpsmc.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("not a valid domain. Valid domains are", valid_domains)
    
        return value


def insert_into_database(empData: Employee):
    print("Name:" , empData.EmpName)
    print("Department:", empData.EmpDepartment)
    print("Employee ID:", empData.EmpID)
    print("Gender", empData.Gender)
    print("Email", empData.Email)
    print("SKills", empData.Skills)
    print("Contacts", empData.Contacts)



emp_raw_data={'EmpID':'123456','EmpName':'Varun Sharma',
              'EmpDepartment':'BFS','Email':'varun@dpsnt.com','Age':12,
              'Skills':['c#','python','ml'],
              'Contacts':{'primary':'9831410307','alternative':'8583058336'},
              'LinkedIn':'http://google.om'}

emp=Employee(**emp_raw_data)

insert_into_database(emp)
