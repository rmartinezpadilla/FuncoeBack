from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Documents_types(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='documents_types'    
    uuid_document_type = Column(String(255), primary_key=True)
    document_type = Column(String(255), nullable=False)       
    created_at = Column(DateTime, default=datetime.now, nullable=False)    
    updated_at = Column(DateTime)

    class Config:
        orm_mode = True