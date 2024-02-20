from app.config.db import Base
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.sql import func
from datetime import datetime

class User(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='users'    
    uuid_user = Column(String(255), primary_key=True)     
    user = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    rol_uuid = Column(String(255), index=True)
    is_active = Column(Boolean, default=True)
    last_connection = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime)
    