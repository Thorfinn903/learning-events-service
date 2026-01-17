from pydantic import BaseModel
from datetime import datetime

# This handles the input validation
class EventCreate(BaseModel):
    user_id: str
    event_type: str
    concept_id: str
    # This expects a dictionary (JSON)
    event_details: dict = {}

# This handles the output format (what the user sees)
class EventResponse(BaseModel):
    event_id: str
    user_id: str
    timestamp: datetime
    event_type: str
    concept_id: str
    event_details: dict

    class Config:
        from_attributes = True