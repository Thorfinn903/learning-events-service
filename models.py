from sqlalchemy import Column, String, DateTime, JSON
import datetime
from database import Base


class LearningEvent(Base):
    __tablename__ = "learning_events"

    # The requirement asked for these specific columns
    event_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    event_type = Column(String)  # e.g. quiz_attempt, video_watched
    concept_id = Column(String)

    # Auto-generating the timestamp when the event is created
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    # Requirement asked for 'metadata', but that is a reserved word in SQLAlchemy
    # so I renamed it to 'event_details' to avoid errors.
    event_details = Column(JSON)