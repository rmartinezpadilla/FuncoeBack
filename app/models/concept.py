from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Concept(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='concepts'    
    uuid_concept = Column(String(255), primary_key=True)    
    name = Column(String(255), nullable=False)    
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    class Config:
        orm_mode = True