from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy import desc
from app.schemas.program import Program as program_schema
from app.schemas.program import Program_response as program_schema_response
from app.config.db import get_db,Session
from app.models.program import Program as program_models
from app.auth.auth_bearer import JWTBearer
from datetime import datetime
import uuid
import typing

router =  APIRouter(prefix='/programs', dependencies=[Depends(JWTBearer())], tags=['Programs'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model=program_schema_response)
async def create_program(program_obj:program_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #program_obj["id"] = uuid.uuid4() 
            # print(type('esto es', program_obj))           
            program_obj = program_models(**program_obj.model_dump())            
            #añade el recurso persona para subirse a la base de datos
            program_obj.uuid_program = uuid.uuid4()
            program_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            db.add(program_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(program_obj)
            return program_obj
    #¡fin try!
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/all/", response_model = typing.List[program_schema_response])
def get_programs():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:           
            r=db.query(program_models).order_by(desc(program_models.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/{uuid_program}", response_model = program_schema_response)
def read_program(uuid_program: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            r=db.query(program_models).where(program_models.uuid_program == uuid_program).first()
            if r != None:
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str('Id program not exist!'))
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.patch("/", response_model = program_schema_response)
def update_program(program_uuid: str, program_model_2: program_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            program_model_2 = program_models(**program_model_2.model_dump())
            r = db.query(program_models).where(program_models.uuid_program == program_uuid).first()        
            if r is not None:
                r.name = program_model_2.name
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Id program not exist!')

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/{uuid_program}")
def delete_program(uuid_program: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:
            r=db.query(program_models).where(program_models.uuid_program == uuid_program).one_or_none()
            if r is not None:
                db.delete(r)#instruccion para borrar un recurso
                db.commit()
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Program not exist!')
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))  