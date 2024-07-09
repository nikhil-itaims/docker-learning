from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud
from app import models
from app import schemas
from app.database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()

@app.post("/users/{user_id}/todos/",response_model=schemas.Todo)
def post_todo_for_user(todo:schemas.TodoCreate, db:Session=Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.get("/todos/", response_model=List[schemas.Todo])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = crud.get_todos(db,skip=skip,limit=limit)
    return todos
