from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.sql import func
from datetime import datetime

class Payment(Base): #modelo de pagos que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='payments'    
    uuid_pay = Column(String(255), primary_key=True)
    enroll_uuid = Column(String(255), nullable=False, index=True)
    concept_uuid = Column(String(255), nullable=False, index=True)
    amount = Column(Float, nullable=False)       
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime)
    
    class Config:
        from_attributes = True
        orm_mode = True