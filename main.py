from fastapi import FastAPI
from app.routes import advisor, blood_type, gender, day, document_type, concept, program, student, teacher, module, semester, enroll, payment, pensum, shifts, role, user
import uvicorn

app = FastAPI(title="Api funcoe",debug=True)
app.include_router(user.router)
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
app.include_router(shifts.router)
app.include_router(role.router)
app.include_router(blood_type.router)
app.include_router(day.router)
app.include_router(gender.router)

@app.get("/")
async def root():
    return {"message": "Api Funcoe"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",port=8000, reload= True, log_level="info")