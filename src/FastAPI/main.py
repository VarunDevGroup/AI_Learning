from fastapi import FastAPI
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

