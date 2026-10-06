from pydantic import BaseModel
from typing import Dict, List


class AddressDetail (BaseModel):
    Line1 : str
    Line2 : str

    
class Emp(BaseModel):
    Name : str
   
    Address: List[AddressDetail]



empData = {
    'Name': 'Varun',
    'Address': [
        {
            'Line1': 'Home Address',
            'Line2': 'Kolkata'
        },
        {
            'Line1': 'Office Address',
            'Line2': 'Salt Lake'
        }
    ]
}
cls = Emp(**empData)

print(cls.Name)
print(cls.Address[0].Line1,',', cls.Address[0].Line2)
print(cls.Address[1].Line1,',', cls.Address[1].Line2)

#AddObject=AddressDetail(**addDetails)

#empData={'Name':'Varun', 'Address':[AddObject]}

#cls= Emp(**empData)

#print(cls.Name)
#print(cls.Address[0].Line1)
#print(cls.Address[0].Line2)
