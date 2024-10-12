from fastapi import APIRouter, HTTPException
from app.models import Item
from app.database import items_collection
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument
from typing import List, Optional

router = APIRouter()

@router.post("/items", response_model=Item)
async def create_item(item: Item):
    try:
        item_data = item.dict()
        item_data['insert_date'] = datetime.now()  # Automatically set
        result = items_collection.insert_one(item_data)
        item_data['id'] = str(result.inserted_id)
        return item_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {str(e)}")

@router.get("/items/{id}", response_model=Item)
async def get_item(id: str):
    record = items_collection.find_one({"_id": ObjectId(id)})
    if not record:
        raise HTTPException(status_code=404, detail="Item not found")
    record['id'] = str(record['_id'])
    return record

@router.get("/items/filter", response_model=List[Item])
async def filter_items(email: Optional[str] = None, expiry_date: Optional[str] = None, 
                       insert_date: Optional[str] = None, quantity: Optional[int] = None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": expiry_date}  # Expiry date must be after the provided date
    if insert_date:
        query["insert_date"] = {"$gt": insert_date}  # Insert date must be after the provided date
    if quantity is not None:
        query["quantity"] = {"$gte": quantity}  # Quantity must be greater than or equal to provided number

    records = list(items_collection.find(query))
    for record in records:
        record['id'] = str(record['_id'])
    return records

@router.delete("/items/{id}")
async def delete_item(id: str):
    result = items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"status": "Item deleted"}

@router.put("/items/{id}", response_model=Item)
async def update_item(id: str, item: Item):
    updated_record = items_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": item.dict(exclude_unset=True)},
        return_document=ReturnDocument.AFTER
    )
    if not updated_record:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_record['id'] = str(updated_record['_id'])
    return updated_record
