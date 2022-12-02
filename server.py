from flask import Flask, request 
from pydantic import BaseModel

app = Flask(__name__)

class Person(BaseModel):
    nombre: str
    cargo: str
    entrada: str
    salida: str

def PersonToCSV(json):
    return f"{json.nombre},{json.cargo},{json.entrada},{json.salida}"

# adds person to a excel file person
@app.route("/add_person", methods=["POST"])
def add_person(person: Person):
    #open file
    file = open("database.csv", "a")
    #write person
    file.write(PersonToCSV(person) + "\n")
    #close file
    file.close()
    return {"message": "Persona agregada"}

#returns the excel file
@app.route("/excel", methods=["GET"])
def excel():
    file = open("database.csv", "r")
    return file.read()

#returns index.html
@app.route("/", methods=["GET"])
def read_root():
    #index.html is in the same folder as main.py
    file = open("index.html", "r")
    return file.read()


#returns qr librery
@app.route("/getLibrery", methods=["GET"])
def getLibrery():
    return open("node_modules/html5-qrcode/html5-qrcode.min.js", "r").read()
