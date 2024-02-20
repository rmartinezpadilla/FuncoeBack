from app.config.db import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Semester(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='semesters'    
    uuid_semester = Column(String(255), primary_key=True)    
    name = Column(String(255),nullable=False)    
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime)