from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

@app.get("/")
def Hello():
    return {'message':'Patient Management API System!!'}

@app.get("/about")
def About():
    return {'message':'Fully Manage API System'}

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
        
    return data
    
@app.get("/view")
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

    raise HTTPException( status_code=499, detail="NO DATA FOUND")

@app.get('/sort')
def sort_patient(
    sort_by:str=Query(...,description="sort on data"),
    sort_order:str=Query('asc',description="sort order")):

    data=load_data()
    sortOrder=False if sort_order=='asc' else True
    sortdata=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sortOrder)
    return sortdata

