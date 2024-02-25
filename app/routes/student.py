from fastapi import APIRouter, Response, HTTPException, status, Depends
from app.schemas.student import Student as student_schema
from app.schemas.student import Student_update
from app.schemas.student import Student_response as student_schema_response
from app.config.db import get_db,Session
from app.models.student import Student as student_models
from app.auth.auth_bearer import JWTBearer
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
    
@router.get("/allStudents/", response_model = list[student_schema_response])
def get_students():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(student_models)
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

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

@router.patch("/update/", response_model = student_schema_response)
def update_student(student_uuid: str, student_model_2: Student_update):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            student_model_2 = student_models(**student_model_2.model_dump())
            r = db.query(student_models).where(student_models.uuid_student == student_uuid).first()        
            if r is not None:                                
                r.first_name = student_model_2.first_name
                r.last_name = student_model_2.last_name                
                r.phone = student_model_2.phone                                
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id teacher not exist!')

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
                return Response(status_code=status.HTTP_200_OK)
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