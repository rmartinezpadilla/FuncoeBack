from fastapi import APIRouter, Response, HTTPException, status, Depends
from schemas.concept import Concept as concept_schema
from config.db import get_db,Session
from models.concept import Concept as concept_models
from auth.auth_bearer import JWTBearer

router =  APIRouter(prefix='/concepts', dependencies=[Depends(JWTBearer())], tags=['Concepts'], responses={404 : {'message' : 'Not found'}})


@router.post("/")
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

@router.get("/",response_model = list[concept_schema])
def get_concepts():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(concept_models)
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/{uuid_concept}", response_model = concept_schema)
def read_concept(uuid_concept: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(concept_models).where(concept_models.uuid_concept == uuid_concept).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
        
@router.delete("/{uuid_concept}")
def delete_concept(uuid_concept: str):
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
            r=db.query(concept_models).where(concept_models.uuid_concept == uuid_concept).one_or_none()
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