from fastapi import APIRouter, Response, HTTPException, status, Depends
from app.schemas.module import Module as module_schema
from app.schemas.module import Module_response as module_schema_response
from app.config.db import get_db,Session
from app.models.module import Module as module_model
from datetime import datetime
from app.auth.auth_bearer import JWTBearer
from uuid import uuid4

router =  APIRouter(prefix='/modules', dependencies=[Depends(JWTBearer())], tags=['Modules'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model=module_schema_response)
def create_module(module_obj:module_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #module_obj["id"] = uuid.uuid4() 
            # print(type('esto es', module_obj))           
            module_obj = module_model(**module_obj.model_dump())            
            #añade el recurso persona para subirse a la base de datos
            db.add(module_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(module_obj)
            return module_obj
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/", response_model = list[module_schema_response])
def get_modules():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(module_model)
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/{uuid_module}", response_model = module_schema_response)
def read_module(uuid_module: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(module_model).where(module_model.uuid_module == uuid_module).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
    
@router.get("/{module_name}", response_model = module_schema_response)
def read_module(module_name: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
        #¡inicio try!
            session = get_db()
            db:Session
            for db in session:
                #se usa la instrucción where para buscar por el id y se ejecuta el first para
                #encontrar la primera coincidencia, esto es posible porque el id es un 
                #identificador unico
                r=db.query(module_model).where(module_model.name == module_name).first()
                #r=db.select(module_model).where(module_model.identification_card == id_card)
                return r
        #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
            #se debe controlar siempre que nos conectamos a una base de datos con un try - except
            #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
            #y es muy posible que la conexión falle por lo cual debemos responder que paso
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
            #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
            #un error, en este caso el error esta contenido en HTTPException

@router.patch("/update/{uuid_module}", response_model = module_schema_response)
async def update_module(module_uuid: str, module_model_2: module_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #session.query(advisor_model).filter(adv_models.uuid_advisor == advisor_uuid).update(advisor_model)
            #db.execute(adv_models).update().values(module_model_2)).where(adv_models.uuid_advisor == adv_uuid)
            module_model_2 = module_model(**module_model_2.model_dump())
            r = db.query(module_model).where(module_model.uuid_module == module_uuid).first()        
            if r is not None:               
                r.name = module_model_2.name                
                r.program_uuid = module_model_2.program_uuid
                r.semester_uuid = module_model_2.semester_uuid          
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='el id del modulo no existe')

    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
        
# @router.delete("/{uuid_module}")
# def delete_module(uuid_module: str):
#     try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
#     #¡inicio try!
#         #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
#         session = get_db()
#         db:Session
#         for db in session:
#             #one or none es una instrucción que nos permite encontrar uno o ningún recurso
#             #en caso que sea un recurso lo añadiremos al delete ya que es el que vamos a borrar
#             #en caso que sea None se lanza un error, ya que no tenemos un dato con el id a borrar
#             #si intentamos borrar algo que no existe (en el caso que sea None) nos lanzará una 
#             #excepción y será atrapada en el except
#             r=db.query(module_model).where(module_model.uuid_module == uuid_module).one_or_none()
#             if r is not None:
#                 db.delete(r)#instruccion para borrar un recurso
#                 db.commit()
#                 return Response(status_code=status.HTTP_200_OK)
#             else:
#                 return Response(status_code=status.HTTP_404_NOT_FOUND)
#     #¡fin try!
#     except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
#         #se debe controlar siempre que nos conectamos a una base de datos con un try - except
#         #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
#         #y es muy posible que la conexión falle por lo cual debemos responder que paso
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
#         #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
#         #un error, en este caso el error esta contenido en HTTPException            }