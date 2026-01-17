from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import crud
from database import engine, get_db

# This creates the tables in the database if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Service is running. Go to /docs to see the API."}

# Requirement 1: POST /log_event
@app.post("/log_event", response_model=schemas.EventResponse, status_code=201)
def log_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    """
    Record a new learning event.
    """
    return crud.create_event(db, event)

# Requirement 2: GET /events/{user_id}
@app.get("/events/{user_id}", response_model=List[schemas.EventResponse])
def read_events(user_id: str, db: Session = Depends(get_db)):
    """
    Fetch all events for a given user.
    """
    events = crud.get_user_events(db, user_id)
    if not events:
        # Simple error handling if no user found
        # (Though usually returning empty list is fine too)
        print("No events found for this user")
    return events

# Requirement 3: GET /events/{user_id}/{concept_id}
@app.get("/events/{user_id}/{concept_id}", response_model=List[schemas.EventResponse])
def read_concept_events(user_id: str, concept_id: str, db: Session = Depends(get_db)):
    """
    Fetch all events related to a specific concept for a user.
    """
    return crud.get_concept_events(db, user_id, concept_id)