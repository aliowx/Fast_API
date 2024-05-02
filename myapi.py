from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
""" This is the framework for the pyhton test """
app = FastAPI()


class Studants_a(BaseModel):
    name : str
    age : int
    year : str 

class Update_studants(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None
    
    
    
    
studans = {
    1 :{
        "name":"ali",
        "age":22,
        "year":'12'
        
    }
}

@app.get("/")
def index():
    return {
        'links' : 'https://github.com/aliowx' 
    }


@app.get("/get-studans/{password}")
def get_studant(password:int):
    return studans[password]


@app.get('/get-by-name')
def get_sudant(*,studants_id:int,name:str,test:int):
    for studants_id in studans:
        if studans[studants_id]['name']== name: 
            return studans[studants_id]
    return {"Data":"Not found"}


@app.post("/creat_studants/{studants_id}")
def crea_studants(studants_id:int,studant:Studants_a):
    if studants_id in studans:
        return {"Error":"Studants exists"}
    
    studans[studants_id] = studant
    return studans[studants_id]

@app.put('/update-srudant_id/{studants_id}')
def updata_studants(studants_id:int,studant:Update_studants):
    if studants_id not in studant:
        return {"Error" : "Studants dosen't exits "}

    studans[studants_id] = studant
    return studans[studants_id]

# print("_ALi_")