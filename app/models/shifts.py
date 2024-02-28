from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.sql import func
from datetime import datetime

class Shifts(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='shifts'    
    uuid_shifts = Column(String(255), primary_key=True)
    module_uuid = Column(String(255), nullable=False, index=True)
    amount_hours = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)    
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    teacher_uuid = Column(String(255), nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
    
    class Config:
        orm_mode = True