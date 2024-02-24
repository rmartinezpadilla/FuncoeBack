from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy import desc
from app.schemas.advisor import Advisor_response as adv_schema_response
from app.schemas.advisor import Advisor as adv_schema_create
from app.schemas.advisor import Advisor_update as adv_schema_update
from app.config.db import get_db,Session
from app.models.advisor import Advisor as adv_models
from app.routes.document_type import check_uuid_document_type
from app.routes.blood_type import check_uuid_blood_type
import uuid
from datetime import datetime
from app.auth.auth_bearer import JWTBearer

router =  APIRouter(prefix='/advisors', dependencies=[Depends(JWTBearer())], tags=['Advisors'], responses={404 : {'message' : 'Not found'}})

#haciendo un comentario
@router.post("/", response_model= adv_schema_response)
async def create_advisor(advisor_obj:adv_schema_create):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #advisor_obj["id"] = uuid.uuid4() 
            # print(type('esto es', advisor_obj))
            if not check_uuid_document_type(advisor_obj.document_type_uuid):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'uuid {advisor_obj.document_type_uuid} document_type not exist')
            if check_identification_card(advisor_obj.identification_card):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'uuid {advisor_obj.identification_card} identification card exist')
            elif not check_uuid_blood_type(advisor_obj.blood_type):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'uuid {advisor_obj.blood_type} blood_type not exist')
            else:
                advisor_obj = adv_models(**advisor_obj.model_dump())  
                advisor_obj.uuid_advisor = uuid.uuid4()
                advisor_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                #añade el recurso persona para subirse a la base de datos
                db.add(advisor_obj)
                #se sube a la base de datos
                db.commit()
                #se refresca la información en la variable persona para poderla devolver
                #en el servicio
                db.refresh(advisor_obj)
                return advisor_obj
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/all", response_model=list[adv_schema_response])
async def get_advisors():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(adv_models).order_by(adv_models.created_at)          
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/{id}", response_model = adv_schema_response)
async def read_advisor(uuid: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(adv_models).where(adv_models.uuid_advisor == uuid).first()
            if r is not None:               
                return r
            else:
                return Response(status_code=status.HTTP_404_NOT_FOUND)
            
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
    
@router.get("/", response_model = adv_schema_response)
async def get_advisor_identification_card(number_document: int):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
        #¡inicio try!
            session = get_db()
            db:Session
            for db in session:
                #se usa la instrucción where para buscar por el id y se ejecuta el first para
                #encontrar la primera coincidencia, esto es posible porque el id es un 
                #identificador unico
                r=db.query(adv_models).where(number_document==adv_models.identification_card).first()
                #r=db.select(adv_models).where(adv_models.identification_card == number_document)
                if r is not None:
                    return r
                else:
                    return Response(status_code=status.HTTP_404_NOT_FOUND)
                
        #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
            #se debe controlar siempre que nos conectamos a una base de datos con un try - except
            #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
            #y es muy posible que la conexión falle por lo cual debemos responder que paso
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
            #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
            #un error, en este caso el error esta contenido en HTTPException

@router.patch("/update", response_model = adv_schema_response)
async def update_advisor(adv_uuid: str, advisor_model_2: adv_schema_update):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #session.query(advisor_model).filter(adv_models.uuid_advisor == advisor_uuid).update(advisor_model)
            #db.execute(adv_models).update().values(advisor_model_2)).where(adv_models.uuid_advisor == adv_uuid)
            advisor_model_2 = adv_models(**advisor_model_2.model_dump())
            r = db.query(adv_models).where(adv_models.uuid_advisor == adv_uuid).first()        
            if r is not None:
                r.document_type_uuid = advisor_model_2.document_type_uuid
                r.identification_card = advisor_model_2.identification_card
                r.first_name = advisor_model_2.first_name
                r.last_name = advisor_model_2.last_name
                r.phone = advisor_model_2.phone
                r.email = advisor_model_2.email
                r.blood_type = advisor_model_2.blood_type
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id advisor not exist!')

    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
    
@router.delete("/{id}")
async def delete_advisor(id: str):
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
            r=db.query(adv_models).where(adv_models.uuid_advisor == id).one_or_none()
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
    

    """
    ADVISOR FUNCTIONS
    
    """

def check_identification_card(identification_card : str):
    try:
        session = get_db()
        db:Session
        for db in session:
            r = db.query(adv_models).where(adv_models.identification_card == identification_card).first()
            if r is None:                
                return False                
            else:
                return True
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
