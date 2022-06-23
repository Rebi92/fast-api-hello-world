#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#Fast api
from fastapi import FastAPI, Query
from fastapi import Body

app= FastAPI()

#Models
#definimos el modelo de datos
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    #asigandole None decimos que el valor puede ser nulo
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

#path operation decoration
@app.get("/")
def home():
    return {"Hello": "World"}

#Request and Response Body
@app.post("/person/new")
def create_person(person: Person= Body(...)):
    #al incluir los ... decimos que el  parametro es obligatorio
    return person

#validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50), 
    age: Optional[str] = Query(...)
):
    return {name: age}