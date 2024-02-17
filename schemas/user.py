from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    document_type_uuid :str
    identification_card:str
    first_name:str
    rol_uuid:str
    user:str
    password:str

class User_login(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona    
    user:str
    password:str

class User_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_user:str
    document_type_uuid :str
    identification_card:str
    first_name:str
    rol_uuid:str
    user:str
    password:str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    last_connection: Optional[datetime]
    #password:str 
    