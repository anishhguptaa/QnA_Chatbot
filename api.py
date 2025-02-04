from dotenv import load_dotenv
load_dotenv()

import uvicorn, os
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from utils.llm_utils import get_answer
from utils.chroma_utils import retrieve_docs, initialise_vector_store

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

app = FastAPI()

@app.get("/")
def hello():
    return("The chatbot is up and running!")
    
@app.get("/setup")
def setup_db():
    res= initialise_vector_store()
    if res:
        return("Vector DB setup successfully!")
    else:
        return HTTPException(500, "No data directory found with the given name of ", os.getenv("DIRECTORY"))

@app.post("/chat")
def get_chat(data: Question):
    question= data.question
    context= retrieve_docs(question=question)
    return Answer(answer=get_answer(question=question, context=context, stream=False))

if __name__ == "__main__":
    uvicorn.run("api:app", port=8000, reload=True)