from app.models.blood_type import Blood_type as blood_type_model
from app.config.db import get_db, Session
from fastapi import HTTPException, status

def check_uuid_blood_type(uuid_blood_type : str):
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(blood_type_model).where(blood_type_model.uuid_blood_type == uuid_blood_type).first()
            if r is None:                
                return False                
            else:
                return True
             
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))