from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy import desc
from app.schemas.gender import Gender as gender_schema
from app.schemas.gender import Gender_response as gender_schema_response
from app.config.db import get_db,Session
from app.models.gender import Gender as gender_models
from app.auth.auth_bearer import JWTBearer
import uuid
from datetime import datetime
import typing

router =  APIRouter(prefix='/genders', dependencies=[Depends(JWTBearer())], tags=['Genders'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model=gender_schema_response)
def create_gender(gender_obj:gender_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:          
            gender_obj = gender_models(**gender_obj.model_dump())            
            #añade el recurso persona para subirse a la base de datos
            gender_obj.uuid_gender = uuid.uuid4()
            gender_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            db.add(gender_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(gender_obj)
            return gender_obj
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/all/",response_model = typing.List[gender_schema_response])
def get_genders():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(gender_models).order_by(desc(gender_models.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/{uuid_gender}", response_model = gender_schema_response)
def read_gender(uuid_gendert: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            r=db.query(gender_models).where(gender_models.uuid_gender == uuid_gendert).first()
            if r is not None:                               
                return r
            else:
                raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Concept not exist!')
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.patch("/update", response_model = gender_schema_response)
def update_gender(gender_uuid: str, gender_models_2: gender_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            gender_models_2 = gender_models(**gender_models_2.model_dump())
            r = db.query(gender_models).where(gender_models.uuid_gender == gender_uuid).first()        
            if r is not None:
                r.gender = gender_models_2.gender           
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id Gender not exist!')

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/{uuid_gender}")
def delete_gender(uuid_gender: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:            
            r=db.query(gender_models).where(gender_models.uuid_gender == uuid_gender).one_or_none()
            if r is not None:
                db.delete(r)#instruccion para borrar un recurso
                db.commit()
                return Response(status_code=status.HTTP_200_OK)
            else:
                raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Gender not exist!')
    #¡fin try!
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
       