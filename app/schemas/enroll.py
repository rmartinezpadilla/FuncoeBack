from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Enroll(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un estudiante
    uuid_enroll:Optional[str] = None
    student_uuid:str
    program_uuid:str
    semester_uuid:str
    amount:float
    outstanding_balance:float
    positive_balance:float
    dues:int
    number_of_installments:int
    installment_value:float

    # created_at:datetime
    # updated_at:datetime
    class config:
        orm_mode = True
   
class Enroll_response(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un estudiante
    uuid_enroll:str
    student_uuid:str
    program_uuid:str
    semester_uuid:str
    amount:float
    outstanding_balance:float
    positive_balance:float
    dues:int
    number_of_installments:int
    installment_value:float   
    created_at:datetime
    updated_at:Optional[datetime] = None
    
    class config:
        orm_mode = True
    