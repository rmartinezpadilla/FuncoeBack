from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

class Program(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='programs'    
    uuid_program = Column(String(255), primary_key=True)    
    name = Column(String(255), nullable=False)    
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    class Config:
        from_attributes = True
        orm_mode = True