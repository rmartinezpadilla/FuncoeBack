from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Blood_type(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api    
    uuid_blood_type:str
    blood_type:str
    
    class config:
        orm_mode = True