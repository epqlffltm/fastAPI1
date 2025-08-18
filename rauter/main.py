from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    message = {"message": "Hello World"}
    return message

@app.get("/items")
def item(skip=5,limit=10):
    return {"skip": skip, "limit": limit}

@app.get("/{numder}")
def num(numder):
    return {"numder": numder}

@app.get("/hello/{numder}")
def hello(numder):
    # f-string을 사용하여 문자열과 변수를 조합합니다.
    return {"message": f"item {numder}"}