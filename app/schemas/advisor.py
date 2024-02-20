from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Advisor(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    #uuid_advisor:Optional[str] = None
    document_type_uuid:str
    identification_card:str
    first_name:str
    last_name:str
    phone:str
    email:EmailStr
    blood_type:str
    
class Advisor_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_advisor:Optional[str] = None
    document_type_uuid:str
    identification_card:str
    first_name:str
    last_name:str
    phone:str
    email:str
    blood_type:str
    created_at:datetime
    updated_at:Optional[datetime] = None    

#class Advisor_request(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso la utilizaremos para buscar una persona por usuario y contraseña
    # usuario:str
    # password:str
    
#es indispensable tener en cuenta que los modelos de pydantic no son los mismos de sqlalchemy
#y que pueden variar con base a la necesidad a utilizar en todo el proyecto