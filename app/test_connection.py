from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

# Test MongoDB connection
client = MongoClient(MONGODB_URI)
db = client.fastapi_db
try:
    print("Connected to MongoDB:", db.command("ping"))  # Should return {'ok': 1.0}
except Exception as e:
    print("Error connecting to MongoDB:", e)
