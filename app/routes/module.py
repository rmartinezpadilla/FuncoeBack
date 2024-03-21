from fastapi import APIRouter, Response, HTTPException, status, Depends
from app.schemas.module import Module as module_schema
from app.schemas.module import Module_update
from app.schemas.module import Module_response as module_schema_response
from app.config.db import get_db,Session
from app.models.module import Module as module_model
from datetime import datetime
from app.func.program import check_uuid_program
from app.func.semester import check_uuid_semester
from app.auth.auth_bearer import JWTBearer
import uuid
from sqlalchemy import desc
import typing

router =  APIRouter(prefix='/modules', dependencies=[Depends(JWTBearer())], tags=['Modules'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model=module_schema_response)
def create_module(module_obj:module_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:                   
            if not check_uuid_program(module_obj.program_uuid):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'uuid {module_obj.program_uuid} program not exist')
            if not check_uuid_semester(module_obj.semester_uuid):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'uuid {module_obj.semester_uuid} semester not exist')            
            else:
                module_obj = module_model(**module_obj.model_dump())  
                module_obj.uuid_module = uuid.uuid4()
                module_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                #añade el recurso persona para subirse a la base de datos
                db.add(module_obj)
                #se sube a la base de datos
                db.commit()
                #se refresca la información en la variable persona para poderla devolver
                #en el servicio
                db.refresh(module_obj)
                return module_obj
    #¡fin try!
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/", response_model = typing.List[module_schema_response])
def get_modules():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(module_model).order_by(desc(module_model.created_at)).all()
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
                r=db.query(module_model).where(module_model.name == module_name).first()
                #r=db.select(module_model).where(module_model.identification_card == id_card)
                return r
        #¡fin try!
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.patch("/{uuid_module}", response_model = module_schema_response)
def update_module(uuid:str, module_my_model: Module_update):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:                        
            r = db.query(module_model).filter_by(uuid_module = uuid).first()
            if not r:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id module not exist!')
            else:                
                for key, value in module_my_model.model_dump(exclude_unset=True).items():
                    setattr(r, key, value)                           
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')                    
                db.commit()
                db.refresh(r)
                return r

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

# @router.delete("/{uuid_module}")
# def delete_module(uuid_module: str):
#     try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
#     #¡inicio try!
#         #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
#         session = get_db()
#         db:Session
#         for db in session:
#             r=db.query(module_model).where(module_model.uuid_module == uuid_module).one_or_none()
#             if r is not None:
#                 db.delete(r)#instruccion para borrar un recurso
#                 db.commit()
#                 return Response(status_code=status.HTTP_204_NO_CONTENT)
#             else:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id module not exist!')
#     #¡fin try!
#     except Exception as e: 
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
#         #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
#         #un error, en este caso el error esta contenido en HTTPException            }