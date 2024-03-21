from fastapi import APIRouter, Response, HTTPException, status, Depends
from app.schemas.shifts import Shifts as shifts_schema
from app.config.db import get_db,Session
from app.models.shifts import Shifts as shifts_model
from app.auth.auth_bearer import JWTBearer
import uuid
from datetime import datetime
import typing
from sqlalchemy import desc


router =  APIRouter(prefix='/shifts', dependencies=[Depends(JWTBearer())], tags=['Shifts'], responses={404 : {'message' : 'Not found'}})


@router.post("/")
def create_shifts(shifts_obj:shifts_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #shifts_obj["id"] = uuid.uuid4() 
            # print(type('esto es', shifts_obj))           
            shifts_obj = shifts_model(**shifts_obj.model_dump())  
            shifts_obj.uuid_shifts = uuid.uuid4()
            shifts_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')          
            #añade el recurso persona para subirse a la base de datos
            db.add(shifts_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(shifts_obj)
            return shifts_obj
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/", response_model = typing.List[shifts_schema])
def get_shifts():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(shifts_model).order_by(desc(shifts_model.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/{uuid_shifts}", response_model = shifts_schema)
def read_shifts(uuid_shifts: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(shifts_model).where(shifts_model.uuid_shifts == uuid_shifts).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
    
# @router.get("/{identification_card}", response_model = shifts_schema)
# def read_advisor_identification_card(id_card: str):
#     try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
#         #¡inicio try!
#             session = get_db()
#             db:Session
#             for db in session:
#                 #se usa la instrucción where para buscar por el id y se ejecuta el first para
#                 #encontrar la primera coincidencia, esto es posible porque el id es un 
#                 #identificador unico
#                 r=db.query(shifts_model).where(shifts_model.identification_card == id_card).first()
#                 #r=db.select(shifts_model).where(shifts_model.identification_card == id_card)
#                 return r
#         #¡fin try!
#     except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
#             #se debe controlar siempre que nos conectamos a una base de datos con un try - except
#             #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
#             #y es muy posible que la conexión falle por lo cual debemos responder que paso
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
#             #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
#             #un error, en este caso el error esta contenido en HTTPException
    
@router.delete("/{uuid_shifts}")
def delete_shifts(uuid_shifts: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:
            #one or none es una instrucción que nos permite encontrar uno o ningún recurso
            #en caso que sea un recurso lo añadiremos al delete ya que es el que vamos a borrar
            #en caso que sea None se lanza un error, ya que no tenemos un dato con el id a borrar
            #si intentamos borrar algo que no existe (en el caso que sea None) nos lanzará una 
            #excepción y será atrapada en el except
            r=db.query(shifts_model).where(shifts_model.uuid_shifts == uuid_shifts).one_or_none()
            if r is not None:
                db.delete(r)#instruccion para borrar un recurso
                db.commit()
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status_code=status.HTTP_404_NOT_FOUND)
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException            }