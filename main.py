from fastapi import FastAPI
from routes import advisor, document_type, concept, program, student

app = FastAPI()

app.include_router(advisor.router)
app.include_router(document_type.router)
app.include_router(concept.router)
app.include_router(program.router)
app.include_router(student.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}