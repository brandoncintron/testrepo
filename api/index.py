from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def helloworld():
    return {"message": "helloworld"}

@app.get("/api/health")
async def health():
    return {"status": "ok"}