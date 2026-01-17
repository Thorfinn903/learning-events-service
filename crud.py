from sqlalchemy.orm import Session
import models
import schemas
import uuid
import datetime


# 1. Log a new event
def create_event(db: Session, event: schemas.EventCreate):
    # Generating a random UUID for the event_id
    new_id = str(uuid.uuid4())
    print("Saving event with ID:", new_id)  # debug print

    db_event = models.LearningEvent(
        event_id=new_id,
        user_id=event.user_id,
        event_type=event.event_type,
        concept_id=event.concept_id,
        timestamp=datetime.datetime.now(),
        event_details=event.event_details
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# 2. Get all events for a user
def get_user_events(db: Session, user_id: str):
    print("Fetching events for user:", user_id)
    return db.query(models.LearningEvent).filter(models.LearningEvent.user_id == user_id).all()


# 3. Get events for a user AND a specific concept
def get_concept_events(db: Session, user_id: str, concept_id: str):
    print("Fetching specific concept events...")
    return db.query(models.LearningEvent).filter(
        models.LearningEvent.user_id == user_id,
        models.LearningEvent.concept_id == concept_id
    ).all()