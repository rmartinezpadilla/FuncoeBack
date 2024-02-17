from config.db import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func

class Blood_type(Base): #modelo de asesor que representa la tabla en la base de datos
    #es necesaria para que la herramienta sqlalchemy pueda conocer las tablas
    __tablename__='blood_type'    
    uuid_blood_type = Column(String(255), primary_key=True)    
    blood_type = Column(String(255),nullable=False)    