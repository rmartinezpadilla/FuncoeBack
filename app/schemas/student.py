from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date

class Student(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un estudiante    
    document_type_uuid:str
    identification_card:str
    birthdate:date
    first_name:str
    last_name:str
    municipality:str
    address:str
    phone:str
    email:EmailStr
    gender_uuid:str
    blood_type_uuid:str
    recommendation:str
    advertising_medium:str    
    day_uuid:str    
    working_day:str
    registration_number:int
    advisor_uuid:str       

class Student_update(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear un estudiante        
    first_name:str
    last_name:str       
    address:str
    phone:str
    email:Optional[EmailStr]    
    advisor_uuid: Optional[str] = None

class Student_response(BaseModel):
    uuid_student:Optional[str] = None
    document_type_uuid:str
    identification_card:str
    birthdate:date
    first_name:str
    last_name:str
    municipality:str
    address:str
    phone:str
    email:EmailStr
    gender_uuid:str
    blood_type_uuid:str
    recommendation:str
    advertising_medium:str    
    day_uuid:str    
    working_day:str
    registration_number:int
    advisor_uuid:str
    created_at:Optional[datetime] = None
    updated_at:Optional[datetime] = None