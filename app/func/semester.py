from app.config.db import get_db, Session
from fastapi import HTTPException, status
from app.models.semester import Semester as semester_models

def check_uuid_semester(uuid : str):    
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(semester_models).where(semester_models.uuid_semester == uuid).first()
            if r is None:                
                return False                
            else:
                return True
             
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))