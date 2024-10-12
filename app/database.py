from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection URI
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)

# Access the fastapi_db database
db = client.fastapi_db  # Use your actual database name

# Define your collections
clock_in_collection = db.fastapi  # Reference to your collection for clock-in records
items_collection = db.fastapi  # Update this if you create a separate collection for items

# Test MongoDB connection
print("Connected to MongoDB:", db.command("ping"))
