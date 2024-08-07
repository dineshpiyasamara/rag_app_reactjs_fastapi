from fastapi import FastAPI

app = FastAPI()


@app.get("/api/test")
async def test():
    return {"message": "Welcome to CodePRO LK!"}
