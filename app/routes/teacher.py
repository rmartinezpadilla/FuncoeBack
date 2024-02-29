from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy import desc
from app.schemas.teacher import Teacher as teacher_schema
from app.schemas.teacher import Teacher_response as teacher_schema_response
from app.schemas.teacher import Teacher_update
from app.config.db import get_db, Session
from app.models.teacher import Teacher as teacher_models
from app.auth.auth_bearer import JWTBearer
from app.func.teacher import *
from datetime import datetime
import uuid
import typing

router =  APIRouter(prefix='/teachers', dependencies=[Depends(JWTBearer())], tags=['Teachers'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model=teacher_schema_response)
def create_teacher(teacher_obj:teacher_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            if check_teacher(teacher_obj.identification_card):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'uuid {teacher_obj.identification_card} identification card exist')
            else:
                teacher_obj = teacher_models(**teacher_obj.model_dump())            
                #añade el recurso persona para subirse a la base de datos
                teacher_obj.uuid_teacher = uuid.uuid4()
                teacher_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.add(teacher_obj)
                #se sube a la base de datos
                db.commit()
                #se refresca la información en la variable persona para poderla devolver
                #en el servicio
                db.refresh(teacher_obj)            
                return teacher_obj
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/all", response_model = typing.List[teacher_schema_response])
def get_teachers():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(teacher_models).order_by(desc(teacher_models.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/{uuid_teacher}", response_model = teacher_schema)
def read_teacher(uuid_teacher: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(teacher_models).where(teacher_models.uuid_teacher == uuid_teacher).first()
            if r is not None:
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Id {uuid_teacher} teacher not exist!')
                
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/teacher/", response_model = teacher_schema)
def read_teacher_identification_card(number_card: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
        #¡inicio try!
            session = get_db()
            db:Session
            for db in session:                
                r=db.query(teacher_models).where(teacher_models.identification_card == number_card).first()
                if r is not None:                
                    return r
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'number card {number_card} not exist!')

            
        #¡fin try!
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.patch("/{uuid_teacher}", response_model = teacher_schema_response)
def update_teacher(uuid:str, teacher_my_model: Teacher_update):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:                        
            r = db.query(teacher_models).filter_by(uuid_teacher = uuid).first()
            if not r:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id teacher not exist!')                
            else:                
                for key, value in teacher_my_model.model_dump(exclude_unset=True).items():
                    setattr(r, key, value)                           
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')                    
                db.commit()
                db.refresh(r)
                return r

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.delete("/{uuid_teacher}")
def delete_teacher(uuid_teacher: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:
            r=db.query(teacher_models).where(teacher_models.uuid_teacher == uuid_teacher).one_or_none()
            if r is not None:
                db.delete(r)#instruccion para borrar un recurso
                db.commit()
                return Response(status_code=status.HTTP_200_OK)
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id teacher not exist!')
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))