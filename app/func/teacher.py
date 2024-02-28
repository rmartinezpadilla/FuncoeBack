from fastapi import HTTPException, status
from app.models.teacher import Teacher as teacher_models
from app.config.db import get_db,Session

def check_teacher(identification_card : str):
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(teacher_models).where(teacher_models.identification_card == identification_card).first()
            if r is None:                
                return False                
            else:
                return True
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))