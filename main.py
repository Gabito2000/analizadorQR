#https://www.peopleperhour.com/freelance-jobs/technology-programming/programming-coding/i-need-a-weather-python-program-coded-3729938
from fastapi import FastAPI
from pydantic import BaseModel
import math 
import numpy as np
from fastapi.responses import HTMLResponse

app = FastAPI()

class Person(BaseModel):
    nombre: str
    cargo: str
    entrada: str
    salida: str

def PersonToCSV(json):
    return f"{json.nombre},{json.cargo},{json.entrada},{json.salida}"



#adds person to a excel file person comes as a string
@app.post("/add_person")
def add_person(person: Person):
    #open file
    file = open("database.csv", "a")
    #write person
    file.write(PersonToCSV(person) + "\n")
    #close file
    file.close()
    return {"message": "Persona agregada"}

#returns the excel file
@app.get("/excel")
def excel():
    file = open("database.csv", "r")
    return HTMLResponse(content=file.read(), status_code=200)

#returns index.html
@app.get("/")
def read_root():
    #index.html is in the same folder as main.py
    html_content =  open("index.html", "r").read()
    return HTMLResponse(content=html_content, status_code=200)



    