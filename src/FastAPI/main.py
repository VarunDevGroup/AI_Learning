from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
from model import PatientUpdate, Patient



app = FastAPI()

@app.get('/')
def Hello():
    return {'message':'Patient Management API System!!'}

@app.get('/about')
def About():
    return {'message':'Fully Manage API System'}

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
        
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

    
@app.get('/view')
def view():
    data=load_data()

    return data

@app.get('/patient/{pateint_id}')
def view_patient(pateint_id: str):
    
    data=load_data()
    #return data
    #patient = pateint_id.upper()
    if pateint_id.upper() in data:
        return data[pateint_id.upper()]

    raise HTTPException( status_code=499, detail='NO DATA FOUND')

@app.get('/sort')
def sort_patient(
    sort_by:str=Query(...,description='sort on data'),
    sort_order:str=Query('asc',description='sort order')):

    data=load_data()
    sortOrder=False if sort_order=='asc' else True
    sortdata=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sortOrder)
    return sortdata


@app.post('/create')
def create_patient(patient: Patient):

    dbData=load_data()

    if patient.pid in dbData:
        raise HTTPException(status_code=401,detail='Patient already exists')

    dbData[patient.pid]= patient.model_dump(exclude=['pid'])

    save_data(dbData)

    return JSONResponse(status_code=201, content={'message':'Patient Created Successully'})

@app.patch("/update/{patient_id}")
def update_patient(patient_id: str, patient: PatientUpdate):
    data = load_data()

    # Normalize the patient ID
    patient_id = patient_id.upper()

    # Check whether the patient exists
    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient does not exist"
        )

    # Extract only fields explicitly supplied by the client
    updates = patient.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=422,
            detail="At least one field must be provided"
        )

    # Merge updated fields with existing data
    existing_patient_data = {
        **data[patient_id],
        **updates,
        "pid": patient_id
    }

    # Validate the complete updated patient
    updated_patient = Patient.model_validate(existing_patient_data)

    # Save the validated data
    data[patient_id] = updated_patient.model_dump(exclude={"pid"})

    save_data(data)

    return {
        "message": "Patient updated successfully",
        "patient": updated_patient.model_dump()
    }

@app.put('/update/{patient_id}')
def update_patient(patient_id: str, patient:PatientUpdate):
    data=load_data()

    if patient_id not in data:
            raise HTTPException(status_code=401,detail='Patient does not exists')
    
    existing_patient_data=data[patient_id]

    updated_patient_info=patient.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_data[key]=value

    existing_patient_data['pid']=patient_id
    updateDate=Patient(**existing_patient_data)
    
    existing_patient_data=updateDate.model_dump(exclude=['pid'])

    data[patient_id]=existing_patient_data

    save_data(data)

    return JSONResponse(status_code=200,content={'Message':'Patient Updated'})


@app.delete('/delete/{pid}')
def delete_patient(pid :str):
    data=load_data()

    if pid in data:
        del data[pid]
        save_data(data)
        return JSONResponse(status_code=200,content={'Message':'Patient Deleted'})

    else:
        raise HTTPException(status_code=401,detail='Patient does not exist')