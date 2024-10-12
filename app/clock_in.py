from fastapi import APIRouter, HTTPException
from app.models import ClockIn
from app.database import clock_in_collection
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument
from typing import List, Optional

router = APIRouter()

@router.post("/clock-in", response_model=ClockIn)
async def create_clock_in(clock_in: ClockIn):
    clock_in_data = clock_in.dict()
    clock_in_data['insert_datetime'] = datetime.now()  # Set the insert datetime
    result = clock_in_collection.insert_one(clock_in_data)
    clock_in_data['id'] = str(result.inserted_id)  # Add generated ID
    return clock_in_data

@router.get("/clock-in/{id}", response_model=ClockIn)
async def get_clock_in(id: str):
    record = clock_in_collection.find_one({"_id": ObjectId(id)})
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    record['id'] = str(record['_id'])
    return record

@router.get("/clock-in/filter", response_model=List[ClockIn])
async def filter_clock_ins(email: Optional[str] = None, location: Optional[str] = None):
    query = {}
    
    if email:
        query["email"] = email
    if location:
        query["location"] = location

    print(f"Filtering with query: {query}")  # Log the query for debugging

    try:
        records = list(clock_in_collection.find(query))
        for record in records:
            record['id'] = str(record['_id'])  # Add id to each record
        return records
    except Exception as e:
        print(f"Error querying database: {e}")  # Log the error
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")

@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    result = clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"status": "Record deleted"}

@router.put("/clock-in/{id}", response_model=ClockIn)
async def update_clock_in(id: str, clock_in: ClockIn):
    updated_record = clock_in_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": clock_in.dict(exclude_unset=True)},
        return_document=ReturnDocument.AFTER
    )
    if not updated_record:
        raise HTTPException(status_code=404, detail="Record not found")
    updated_record['id'] = str(updated_record['_id'])
    return updated_record
