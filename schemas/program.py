from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Program(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_program:Optional[str] = None    
    name:str
    created_at:Optional[datetime] = None
    updated_at:Optional[datetime] = None
    