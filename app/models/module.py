from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Module(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='modules'    
    uuid_module = Column(String(255), primary_key=True)    
    name = Column(String(255),nullable=False, unique=True)
    program_uuid = Column(String(255), nullable=False, index=True)    
    semester_uuid = Column(String(255),nullable=False)    
    created_at = Column(DateTime)    
    updated_at = Column(DateTime)
    
    class Config:
        from_attributes = True
        orm_mode = True