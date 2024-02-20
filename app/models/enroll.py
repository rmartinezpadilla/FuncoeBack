from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Date, Float
from sqlalchemy.sql import func
from datetime import datetime

class Enroll(Base): #modelo de matricula que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='enrolls'    
    uuid_enroll = Column(String(255), primary_key=True)
    student_uuid = Column(String(255), nullable=False, index=True)
    program_uuid = Column(String(255), nullable=False, index=True)        
    semester_uuid = Column(String(255), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    outstanding_balance = Column(Float, nullable=False)
    positive_balance = Column(Float, nullable=False)
    dues = Column(Integer, nullable=False)
    number_of_installments = Column(Integer, nullable=False)
    installment_value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime)
    #updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
