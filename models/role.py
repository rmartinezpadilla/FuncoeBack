from config.db import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Role(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='roles'    
    uuid_rol = Column(String(255), primary_key=True)    
    name_rol = Column(String(255), nullable=False, unique=True)    
    created_at = Column(DateTime)    
    updated_at = Column(DateTime)