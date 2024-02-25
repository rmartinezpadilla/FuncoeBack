from app.models.document_type import Documents_types as doc_type_models
from app.config.db import get_db, Session
from fastapi import HTTPException, status

def check_uuid_document_type(uuid_document_type : str):
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(doc_type_models).where(doc_type_models.uuid_document_type == uuid_document_type).first()
            if r is None:                
                return False                
            else:
                return True
             
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))