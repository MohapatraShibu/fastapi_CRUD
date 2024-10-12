from pydantic import BaseModel
from datetime import datetime

class ClockIn(BaseModel):
    id: str = None  # ID to be populated when retrieved from the database
    email: str
    location: str
    insert_datetime: datetime = None  # Optional, will be set automatically

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class Item(BaseModel):
    id: str = None  # ID to be populated when retrieved from the database
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime = None  # Optional, will be set automatically

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
