from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int 
    weight : float
    married : bool
    allergies : List[str]
    contact_details: Dict[str,str]

    @computed_field()
    @property
    def AgeCategory(self) -> str:
        if (self.age>60):
            AgeCategory='Sr. Citizen'
        elif (self.age<18):
            AgeCategory='Minor'
        else:
            AgeCategory='Adult'
        return AgeCategory
      

userData={'name':'Varun Sharma', 'email':'cont.varun@gmail.com', 'age':61,
          'weight':83.2,'married':True,'allergies':['a1','a2'],
          'contact_details':{'primary':'9831410307','emergency':'8583058336'}}

pateint=Patient(**userData)

print('Name:', pateint.name)
print('email:', pateint.email)
print('age:', pateint.age)
print('Age Category:', pateint.AgeCategory)

print('Weight:', pateint.weight)
print('Allergies:', pateint.allergies)
print('Contacts:', pateint.contact_details)
