from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Role(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona    
    rol :str       
    
    
class Role_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_rol:str
    rol :str
    created_at:datetime
    updated_at:Optional[datetime] = None

#class Advisor_request(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso la utilizaremos para buscar una persona por usuario y contraseña
    # usuario:str
    # password:str
    
#es indispensable tener en cuenta que los modelos de pydantic no son los mismos de sqlalchemy
#y que pueden variar con base a la necesidad a utilizar en todo el proyecto