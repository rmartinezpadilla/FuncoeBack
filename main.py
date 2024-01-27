from fastapi import FastAPI
from routes import advisor

app = FastAPI()

app.include_router(advisor.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}