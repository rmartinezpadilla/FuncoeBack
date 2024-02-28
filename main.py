from fastapi import FastAPI
<<<<<<< HEAD
from routes import advisor, blood_type, day, document_type, concept, program, student, teacher, module, semester, enroll, payment, pensum, shifts, role, user
=======
from app.routes import advisor, blood_type, gender, day, document_type, concept, program, student, teacher, module, semester, enroll, payment, pensum, shifts, role, user
>>>>>>> 9237c4bae302fe405a1538e9d8d4248f65035b1d
import uvicorn

app = FastAPI()
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
<<<<<<< HEAD
    return {"message": "Hello World"}
=======
    return {"message": "Api Funcoe"}
>>>>>>> 9237c4bae302fe405a1538e9d8d4248f65035b1d

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8000, reload= True, log_level="info")
