from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import clock_in_collection, items_collection
from app.clock_in import router as clock_in_router
from app.items import router as items_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(clock_in_router)
app.include_router(items_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
