from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://zealous-bay-00b26030f.6.azurestaticapps.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/people/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = models.Person(name=person.name, age=person.age)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


@app.get("/people/", response_model=list[schemas.Person])
def read_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    people = db.query(models.Person).offset(skip).limit(limit).all()
    return people


@app.get("/people/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@app.put("/people/{person_id}", response_model=schemas.Person)
def update_person(person_id: int, person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    db_person.name = person.name
    db_person.age = person.age
    db.commit()
    db.refresh(db_person)
    return db_person


@app.delete("/people/{person_id}", response_model=schemas.Person)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(db_person)
    db.commit()
    return db_person
