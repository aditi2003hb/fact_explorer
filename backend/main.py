from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud, database

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ROUTES

@app.get("/facts", response_model=list[schemas.FactOut])
def read_facts(db: Session = Depends(get_db)):
    return crud.get_all_facts(db)

@app.get("/facts/random/{category}", response_model=schemas.FactOut)
def get_random_fact(category: str, db: Session = Depends(get_db)):
    fact = crud.get_random_fact_by_category(db, category)
    if not fact:
        raise HTTPException(status_code=404, detail="No facts found in this category")
    return fact

@app.post("/facts", response_model=schemas.FactOut)
def create_fact(fact: schemas.FactCreate, db: Session = Depends(get_db)):
    return crud.create_fact(db, fact)

@app.delete("/facts/{fact_id}")
def delete_fact(fact_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_fact(db, fact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Fact not found")
    return {"message": "Fact deleted"}
