from config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class User(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='users'    
    uuid_user = Column(String(255), primary_key=True) 
    document_type_uuid = Column(String(255), index=True)
    identification_card = Column(String(255), nullable=False, unique=True)
    first_name = Column(String(255), nullable=False)
    rol_uuid = Column(String(255), index=True)
    user = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_connection = Column(DateTime)