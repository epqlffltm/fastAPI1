import uvicorn
from fastapi import FastAPI,Header

app=FastAPI()

@app.get("/hi")
def index(num:str=Header(None)):
    return f"{num}"
