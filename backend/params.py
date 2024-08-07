from fastapi import FastAPI

app = FastAPI()


@app.get('/api/test/')
async def test():
    data = {
        "message": "Welcome to CodePRO LK",
    }
    return data
