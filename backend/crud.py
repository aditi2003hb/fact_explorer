from sqlalchemy.orm import Session
import random
from . import models, schemas

def get_all_facts(db: Session):
    return db.query(models.Fact).all()

def get_random_fact_by_category(db: Session, category: str):
    facts = db.query(models.Fact).filter(models.Fact.category == category).all()
    return random.choice(facts) if facts else None

def create_fact(db: Session, fact: schemas.FactCreate):
    db_fact = models.Fact(category=fact.category, content=fact.content)
    db.add(db_fact)
    db.commit()
    db.refresh(db_fact)
    return db_fact

def delete_fact(db: Session, fact_id: int):
    fact = db.query(models.Fact).filter(models.Fact.id == fact_id).first()
    if fact:
        db.delete(fact)
        db.commit()
    return fact
