from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy import desc
import typing
from app.schemas.concept import Concept as concept_schema
from app.schemas.concept import Concept_response as concept_schema_response
from app.config.db import get_db,Session
from app.models.concept import Concept as concept_models
from app.auth.auth_bearer import JWTBearer
import uuid
from datetime import datetime

router =  APIRouter(prefix='/concepts', dependencies=[Depends(JWTBearer())], tags=['Concepts'], responses={404 : {'message' : 'Not found'}})

@router.post("/", response_model=concept_schema_response)
def create_concept(concept_obj:concept_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #concept_obj["id"] = uuid.uuid4() 
            # print(type('esto es', concept_obj))           
            concept_obj = concept_models(**concept_obj.model_dump())            
            #añade el recurso persona para subirse a la base de datos
            concept_obj.uuid_concept = uuid.uuid4()
            concept_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            db.add(concept_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(concept_obj)
            return concept_obj
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/all/",response_model = typing.List[concept_schema_response])
def get_concepts():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(concept_models).order_by(desc(concept_models.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/{uuid_concept}", response_model = concept_schema_response)
def read_concept(uuid_concept: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            r=db.query(concept_models).where(concept_models.uuid_concept == uuid_concept).first()
            if r is not None:                               
                return r
            else:
                raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Concept not exist!')
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.patch("/", response_model = concept_schema_response)
def update_concept(concept_uuid: str, concept_model_2: concept_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            concept_model_2 = concept_models(**concept_model_2.model_dump())
            r = db.query(concept_models).where(concept_models.uuid_concept == concept_uuid).first()        
            if r is not None:
                r.name = concept_model_2.name           
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Id concept not exist!')

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/{uuid_concept}")
def delete_concept(uuid_concept: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:            
            r=db.query(concept_models).where(concept_models.uuid_concept == uuid_concept).one_or_none()
            if r is not None:
                db.delete(r)#instruccion para borrar un recurso
                db.commit()
                return Response(status_code=status.HTTP_200_OK)
            else:
                raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Concept not exist!')
    #¡fin try!
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
       