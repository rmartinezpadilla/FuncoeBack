from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Gender(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona     
    gender:str

    class config:
        orm_mode = True
    
class Gender_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_gender:str   
    gender:str
    created_at:datetime
    updated_at:Optional[datetime] = None
    
    class config:
        orm_mode = True

#es indispensable tener en cuenta que los modelos de pydantic no son los mismos de sqlalchemy
#y que pueden variar con base a la necesidad a utilizar en todo el proyecto