from fastapi import FastAPI
from routes import advisor, document_type, concept, program, student, teacher, module, semester, enroll, payment, pensum

app = FastAPI()

app.include_router(advisor.router)
app.include_router(document_type.router)
app.include_router(concept.router)
app.include_router(program.router)
app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(module.router)
app.include_router(semester.router)
app.include_router(enroll.router)
app.include_router(payment.router)
app.include_router(pensum.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}