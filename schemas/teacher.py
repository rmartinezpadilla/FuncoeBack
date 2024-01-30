from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Teacher(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un profesor
    uuid_teacher:Optional[str] = None
    document_type_uuid:str
    identification_card:str    
    first_name:str
    last_name:str
    phone:str    
    user:str
    password:str
    created_at:Optional[datetime] = None
    last_connection:Optional[datetime] = None
    program_uuid:str    
    updated_at:Optional[datetime] = None
    # created_at:datetime
    # updated_at:datetime
   