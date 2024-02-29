from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Module(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona   
    name:str
    program_uuid:str
    semester_uuid:str

    class config:
        orm_mode = True  
    
class Module_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_module:str   
    name:str
    program_uuid:str
    semester_uuid:str
    created_at:datetime
    updated_at:Optional[datetime] = None

    class config:
        orm_mode = True
    
#es indispensable tener en cuenta que los modelos de pydantic no son los mismos de sqlalchemy
#y que pueden variar con base a la necesidad a utilizar en todo el proyecto