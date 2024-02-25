from fastapi import HTTPException, status
from app.models.advisor import Advisor as adv_models
from app.config.db import get_db,Session

def check_identification_card(identification_card : str):
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(adv_models).where(adv_models.identification_card == identification_card).first()
            if r is None:                
                return False                
            else:
                return True
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))