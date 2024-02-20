from app.config.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.sql import func
from datetime import datetime

class Student(Base): #modelo de estudiante que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='students'    
    uuid_student = Column(String(255), primary_key=True)
    document_type_uuid = Column(String(255), nullable=False, index=True)
    identification_card = Column(String(255),nullable=False, unique=True)
    birthdate = Column(Date, default=datetime.now, nullable=False) 
    first_name = Column(String(255),nullable=False)
    last_name = Column(String(255),nullable=False)
    municipality = Column(String(255),nullable=False)
    address = Column(String(255),nullable=False)
    phone = Column(String(255),nullable=False)
    gender = Column(String(255),nullable=False)
    blood_type = Column(String(255), nullable=False, index=True)
    recommendation = Column(String(255),nullable=False)
    advertising_medium = Column(String(255),nullable=False)
    day_uuid = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    working_day = Column(String(255), nullable=False, index=True)
    registration_number = Column(Integer, nullable=False)
    advisor_uuid = Column(String(255), nullable=False, index=True)
    updated_at = Column(DateTime)