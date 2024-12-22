from fastapi import FastAPI, UploadFile, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from LLM_Engine import chat

# Instantiate fastapi
app = FastAPI()

# Define CORS middleware to allow all origins, credentials, methods, and headers
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input format for the api
class Input(BaseModel):
    question: str

# this path is for the chat process, the input is the user's question in json format
@app.post("/extract")
async def chatbot(user_input: Input):
    o = chat(user_input.question)
    return o

# this path is for creating a new CSV file specified for each conversation
@app.get("/new_chat")
async def new_chat():
    pd.DataFrame({'questions':[],'history':[]}).to_csv('database.csv')
    df = pd.read_csv('database.csv', usecols=["questions","history"])
    df.to_csv('database.csv', index=False)
    
    return {'New Chat Initialized'}