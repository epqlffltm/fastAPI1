from fastapi import FastAPI
import asyncio
import uvicorn

app=FastAPI()

@app.get("/")
async def root():
    await asyncio.sleep(1)
    return {"hello":"world"}

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)