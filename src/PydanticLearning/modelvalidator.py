from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int 
    weight : float
    married : bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    @classmethod
    def validate_contact(cls, model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient with age > 60 must have emergecny contact")
        return model
        


    @field_validator('age')
    @classmethod
    def ValidateAge(cls, value):
        if (value>100):
            raise ValueError("Invalid age")
        return value


userData={'name':'Varun Sharma', 'email':'cont.varun@gmail.com', 'age':61,
          'weight':83.2,'married':True,'allergies':['a1','a2'],
          'contact_details':{'primary':'9831410307','emergency':'8583058336'}}

pateint=Patient(**userData)

print('Name:', pateint.name)
print('email:', pateint.email)
print('age:', pateint.age)
print('Weight:', pateint.weight)
print('Allergies:', pateint.allergies)
print('Contacts:', pateint.contact_details)
