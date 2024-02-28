from app.config.db import Base
from sqlalchemy import Column, String, DateTime

class Advisor(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='advisors'    
    uuid_advisor = Column(String(255), primary_key=True)
    document_type_uuid = Column(String(255), nullable=False, index=True)
    identification_card = Column(String(255), nullable=False, unique=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    gender_uuid = Column(String(255), nullable=False, index=True)
    phone = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    blood_type = Column(String(255), nullable=False, index=True)    
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    class Config:
        orm_mode = True