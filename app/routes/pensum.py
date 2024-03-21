from fastapi import APIRouter, Response, HTTPException, status, Depends
from app.schemas.pensum import Pensum as pensum_schema
from app.schemas.pensum import Pensum_response as pensum_schema_response
from app.config.db import get_db,Session
from app.models.pensum import Pensum as pensum_model
import uuid
from datetime import datetime
import typing
from app.auth.auth_bearer import JWTBearer
from sqlalchemy import desc

router =  APIRouter(prefix='/pensum', dependencies=[Depends(JWTBearer())], tags=['Pensum'], responses={404 : {'message' : 'Not found'}})

@router.get("/", response_model = typing.List[pensum_schema_response])
def get_pensums():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            r=db.query(pensum_model).order_by(desc(pensum_model.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.post("/", response_model=pensum_schema_response)
def create_pensum(pensum_obj:pensum_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #advisor_obj["id"] = uuid.uuid4() 
            # print(type('esto es', advisor_obj))           
            pensum_obj = pensum_model(**pensum_obj.model_dump())  
            pensum_obj.uuid_pensum = uuid.uuid4()
            pensum_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')          
            #añade el recurso persona para subirse a la base de datos
            db.add(pensum_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(pensum_obj)
            return pensum_obj
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/{uuid_pensum}", response_model = pensum_schema_response)
def read_pensum(uuid_pensum: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(pensum_model).where(pensum_model.uuid_pensum == uuid_pensum).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException 
    
@router.delete("/{uuid_pensum}")
def delete_pensum(uuid_pensum: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:
            r=db.query(pensum_model).where(pensum_model.uuid_pensum == uuid_pensum).one_or_none()
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