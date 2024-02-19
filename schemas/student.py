from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date

class Student(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un estudiante
    uuid_student:Optional[str] = None
    document_type_uuid:str
    identification_card:str
    birthdate:date
    first_name:str
    last_name:str
    municipality:str
    address:str
    phone:str
    gender:str
    blood_type:str
    recommendation:str
    advertising_medium:str    
    day_uuid:str
    created_at:Optional[datetime] = None
    working_day:str
    registration_number:int
    advisor_uuid:str
    updated_at:Optional[datetime] = None
    # created_at:datetime
    # updated_at:datetime
   