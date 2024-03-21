from fastapi import APIRouter, Response, HTTPException, status, Depends
from fastapi_pagination import add_pagination, paginate, LimitOffsetPage
from sqlalchemy import desc
from app.schemas.student import Student as student_schema
from app.schemas.student import Student_update as student_schema_update
from app.schemas.student import Student_response as student_schema_response
from app.config.db import get_db,Session
from app.models.student import Student as student_models
from app.auth.auth_bearer import JWTBearer
from fastapi.encoders import jsonable_encoder
import uuid
from datetime import datetime

router =  APIRouter(prefix='/students', dependencies=[Depends(JWTBearer())], tags=['Students'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model= student_schema_response)
def create_student(student_obj : student_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            student_obj = student_models(**student_obj.model_dump())            
            #añade el recurso persona para subirse a la base de datos
            student_obj.uuid_student = uuid.uuid4()
            student_obj.created_at =  datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            db.add(student_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(student_obj)
            return student_obj
    #¡fin try!
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/all/", response_model = LimitOffsetPage[student_schema_response])
def get_students():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            #r=_paginate(db.query(student_models).order_by(desc(student_models.created_at)))        
            r=db.query(student_models).order_by(desc(student_models.created_at)).all()
            return paginate(r)
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/{uuid_student}", response_model = student_schema_response)
def read_student(uuid_student: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(student_models).where(student_models.uuid_student == uuid_student).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
    
@router.get("/", response_model = student_schema_response)
def get_advisor_identification_card(number_document: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
        #¡inicio try!
            session = get_db()
            db:Session
            for db in session:
                r=db.query(student_models).where(number_document==student_models.identification_card).first()
                #r=db.select(adv_models).where(adv_models.identification_card == number_document)
                if r is not None:
                    return r
                else:
                    return Response(status_code=status.HTTP_404_NOT_FOUND)
                
        #¡fin try!
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.patch("/{uuid_student}", response_model = student_schema_response)
def update_student(uuid:str, student_model_2: student_schema_update):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:                        
            r = db.query(student_models).filter_by(uuid_student = uuid).first()
            if not r:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id student not exist!')                
            else:                
                for key, value in student_model_2.model_dump(exclude_unset=True).items():
                    setattr(r, key, value)                           
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')                    
                db.commit()
                db.refresh(r)
                return r

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/{uuid_student}")
def delete_student(uuid_student: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:
            r=db.query(student_models).where(student_models.uuid_student == uuid_student).one_or_none()
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
    
add_pagination(router)