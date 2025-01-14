from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class QueryRequest(BaseModel):
    model: str
    query: str

@app.post('/query')
async def query_model(request: QueryRequest):
    response = ollama.generate(model=request.model, prompt=request.query)
    return response['response']