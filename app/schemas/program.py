from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Program(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona    
    name:str

class Program_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_program:str   
    name:str
    created_at:datetime
    updated_at:Optional[datetime] = None
