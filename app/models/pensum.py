from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.sql import func
from datetime import datetime

class Pensum(Base): #modelo de pagos que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='pensum'    
    uuid_pensum = Column(String(255), primary_key=True)
    program_uuid  = Column(String(255), nullable=False, index=True)
    semester_uuid  = Column(String(255), nullable=False, index=True)
    quantity_classes = Column(Integer, nullable=False)
    amount_to_paid = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime)
    
    class Config:
        orm_mode = True