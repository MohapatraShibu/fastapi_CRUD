# FastAPI Project

## Setup and Run
1. Clone the repository:

   git clone https://github.com/MohapatraShibu/fastapi_CRUD.git
   cd fastapi_project

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Create a .env file in the app/ directory with the following content:
    MONGODB_URI=mongodb+srv://username:password@cluster0.mongodb.net/fastapi_db

5. Run the application:
   uvicorn app.main:app --reload

6. Visit http://127.0.0.1:8000/docs for Swagger UI documentation.

## Endpoints
1. POST /clock-in: Create a clock-in record.
2. GET /clock-in/{id}: Get a clock-in record by ID.
3. DELETE /clock-in/{id}: Delete a clock-in record by ID.
4. PUT /clock-in/{id}: Update a clock-in record by ID.
5. GET /clock-in/filter: Filter clock-in records by email or location.