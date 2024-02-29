from app.config.db import get_db, Session
from fastapi import HTTPException, status
from app.models.program import Program as program_models


def check_uuid_program(uuid : str):
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(program_models).where(program_models.uuid_program == uuid).first()
            if r is None:                
                return False                
            else:
                return True
             
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))