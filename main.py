from fastapi import FastAPI
from routes import advisor, document_type

app = FastAPI()

app.include_router(advisor.router)
app.include_router(document_type.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}