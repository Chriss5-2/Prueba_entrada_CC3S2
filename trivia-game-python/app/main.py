from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

class Question(BaseModel):
    description: str
    options: List[str]
    correct_answer: str

@app.get("/")
def read_root():
    return {"message": "Trivia Game API is running!"}

@app.post("/questions/", status_code=201)
def create_question(question: Question):
    return {"message": "Question created", "question":question}
