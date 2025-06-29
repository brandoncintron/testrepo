from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def helloworld():
    return {"message": "helloworld"}
