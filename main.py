#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#Fast api
from fastapi import FastAPI, Path, Query
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
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description= "This is the person name. It's between 1 and 50 characters"
        ), 
    age: Optional[str] = Query(
        ...,
        title="Person Age",
        description="This is the person age, It's required"
        )
):
    return {name: age}

#validaciones : Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(...,
                          title="Person id",
                          description="Este es el id de la persona",
                          gt=0)
):
    return {person_id: "Existe"}