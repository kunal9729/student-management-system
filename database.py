# database.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI) 
db = client["student_database"]  # Replace with your database name
student_collection = db["students"]  # Replace with your collection name