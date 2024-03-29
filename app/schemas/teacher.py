from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Teacher(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un profesor
    document_type_uuid:str
    identification_card:str    
    first_name:str
    last_name:str
    blood_type_uuid:str
    gender_uuid:str
    phone:str    
    user:str
    password:str    
    program_uuid:str        

class Teacher_update(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un profesor        
    first_name:str
    last_name:str    
    phone:str    
    program_uuid:Optional[str] = None

class Teacher_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un profesor
    uuid_teacher:str
    document_type_uuid:str
    identification_card:str
    first_name:str
    last_name:str
    blood_type_uuid:str
    gender_uuid:str
    phone:str
    user:str
    password:str
    created_at:datetime
    last_connection:Optional[datetime] = None
    program_uuid:str    
    updated_at:Optional[datetime] = None    
