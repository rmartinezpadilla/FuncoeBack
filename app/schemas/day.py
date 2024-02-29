from pydantic import BaseModel

class Day(BaseModel):
    #modelo de pydantic que sirve para recibir los datos de entrada de la api
    #en este caso lo utilizaremos para crear una persona
    uuid_day:str
    name:str    
    
    class config:
        orm_mode = True