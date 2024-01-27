from config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Advisor(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='advisors'    
    id = Column(String, primary_key=True)
    document_type = Column(String, nullable=False)
    identification_card = Column(String,nullable=False, unique=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    blood_type = Column(String,nullable=False)    
    created_at = Column(DateTime, default=datetime.now, nullable=False)    
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)