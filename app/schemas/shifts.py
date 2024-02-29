from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Shifts(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    #uuid_advisor:Optional[str] = None
    module_uuid :str
    amount_hours:int
    salary:float
    teacher_uuid :str 

    class config:
        orm_mode = True    

class Shifts_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_shifts:Optional[str] = None
    module_uuid :str
    amount_hours:int
    salary:float
    teacher_uuid :str
    created_at:datetime
    updated_at:Optional[datetime] = None

    class config:
        orm_mode = True 
    
#es indispensable tener en cuenta que los modelos de pydantic no son los mismos de sqlalchemy
#y que pueden variar con base a la necesidad a utilizar en todo el proyecto