# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.langchain_agent import ask_agent

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional: Allow frontend clients (like React or browser) to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

@app.post("/ask", response_model=ChatResponse)
async def ask_bot(req: QueryRequest):
    result = ask_agent(req.query)
    return {"response": result}

@app.get("/")
def health_check():
    return {"status": "OK"}
