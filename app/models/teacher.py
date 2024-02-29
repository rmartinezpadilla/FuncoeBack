from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Date
from datetime import datetime

class Teacher(Base): #modelo de estudiante que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='teachers'    
    uuid_teacher = Column(String(255), primary_key=True)
    document_type_uuid = Column(String(255), nullable=False, index=True)
    identification_card = Column(String(255),nullable=False, unique=True)
    first_name = Column(String(255),nullable=False)
    last_name = Column(String(255),nullable=False)
    blood_type_uuid = Column(String(255), nullable=False, index=True)
    gender_uuid = Column(String(255), nullable=False, index=True)
    phone = Column(String(255),nullable=False)
    user = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    last_connection = Column(DateTime)
    program_uuid = Column(String(255), nullable=False, index=True)
    updated_at = Column(DateTime)
    
    class Config:
        from_attributes = True
        orm_mode = True