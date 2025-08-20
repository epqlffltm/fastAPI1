from fastapi import Response, FastAPI

app = FastAPI()

@app.get("/")
def header(name:str, value:str, response:Response):
    response.headers[name] = value
    return "normal body"