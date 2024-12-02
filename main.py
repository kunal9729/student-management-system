# main.py
from fastapi import FastAPI, HTTPException, status
from pymongo.errors import DuplicateKeyError
from models import Student, StudentUpdate
from database import student_collection
from bson import ObjectId

app = FastAPI()  # This line should be at the beginning

# Helper function to convert ObjectId to string
def object_id_to_str(obj):
    obj["id"] = str(obj.pop("_id"))
    return obj

@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    try:
        student_dict = student.dict(by_alias=True)
        result = student_collection.insert_one(student_dict)
        inserted_student = student_collection.find_one({"_id": result.inserted_id})
        return object_id_to_str(inserted_student)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Student with this ID already exists")

# ... (rest of your code - the same as before)
@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    try:
        student_dict = student.dict(by_alias=True)  # Use by_alias=True 
        result = student_collection.insert_one(student_dict)
        inserted_student = student_collection.find_one({"_id": result.inserted_id})
        return object_id_to_str(inserted_student)  # Return the modified student
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Student with this ID already exists")
        @app.get("/test")
async def test_endpoint():
    return {"message": "This is a test endpoint!"}
