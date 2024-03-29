from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Document_type(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_document_type:str
    document_type:str    
    created_at:Optional[datetime] = None
    updated_at:Optional[datetime] = None