from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api    
    user:str
    password:str
    rol_uuid:str

    class config:
        orm_mode = True

class User_login(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona    
    user:str
    password:str

    class config:
        orm_mode = True

class User_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_user:str    
    user:str
    password:str
    rol_uuid:str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    last_connection: Optional[datetime]
    
    class config:
        orm_mode = True
    