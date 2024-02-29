from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Payment(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    #uuid_advisor:Optional[str] = None
    enroll_uuid:str
    concept_uuid :str  
    amount:float 
    
    class config:
        orm_mode = True    
    # created_at:datetime
    # updated_at:datetime
    #created_at:Optional[datetime] = None
    #updated_at:Optional[datetime] = None
    

class Payment_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    #uuid_advisor:Optional[str] = None
    uuid_pay:str
    enroll_uuid:str
    concept_uuid :str  
    amount:float
    created_at:datetime
    updated_at:Optional[datetime] = None
    
    class config:
        orm_mode = True 
    
#es indispensable tener en cuenta que los modelos de pydantic no son los mismos de sqlalchemy
#y que pueden variar con base a la necesidad a utilizar en todo el proyecto