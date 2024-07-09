from sqlalchemy.orm import Session
from app import models
from app import schemas

def get_todos(db: Session, skip:int=0, limit: int=100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db:Session, todo:schemas.TodoCreate):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
