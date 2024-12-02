# models.py

from pydantic import BaseModel, Field

class Student(BaseModel):
    id: str = Field(alias="_id")  # To handle MongoDB's _id
    name: str
    email: str
    course: str
    age: int

class StudentUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    course: str | None = None
    age: int | None = None