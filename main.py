# requires: pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Run with: uvicorn main:app --reload
