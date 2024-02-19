from fastapi import APIRouter, Response, HTTPException, status, Depends
from schemas.user import User as user_schema
from schemas.user import User_response as user_schema_response
from schemas.user import User_login as user_schema_login
import bcrypt
from auth.auth_bearer import JWTBearer

from config.db import get_db,Session
from models.user import User as user_model
import uuid
from datetime import datetime
from auth.auth_handler import signJWT

router =  APIRouter(prefix='/users', tags=['Users'], responses={404 : {'message' : 'Not found'}})

@router.post("/token")
def get_token(user: user_schema_login):
    if check_user(user):
        return signJWT(user.user)
    return {
        "error": "Wrong login details or user inactive!"
    }

@router.post("/", dependencies=[Depends(JWTBearer())], response_model= user_schema_response)
def create_user(user_obj:user_schema):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #advisor_obj["id"] = uuid.uuid4() 
            # print(type('esto es', advisor_obj))           
            user_obj = user_model(**user_obj.model_dump())  
            user_obj.uuid_user = uuid.uuid4()
            salt = bcrypt.gensalt()
            ashed = bcrypt.hashpw(user_obj.password.encode('utf-8'), salt)
            user_obj.password=ashed
            user_obj.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')          
            #añade el recurso persona para subirse a la base de datos
            db.add(user_obj)
            #se sube a la base de datos
            db.commit()
            #se refresca la información en la variable persona para poderla devolver
            #en el servicio
            db.refresh(user_obj)
            return user_obj
    #¡fin try!
    except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/all", dependencies=[Depends(JWTBearer())], response_model = list[user_schema_response])
def get_users():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(user_model)
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/actives", dependencies=[Depends(JWTBearer())], response_model = list[user_schema_response])
def get_users_actives():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(user_model).where(user_model.is_active==1).all()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException


@router.get("/inactives", dependencies=[Depends(JWTBearer())], response_model = list[user_schema_response])
def get_users_inactives():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(user_model).where(user_model.is_active==0).all()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException


@router.get("/{uuid_user}", dependencies=[Depends(JWTBearer())], response_model = user_schema_response)
def read_user(uuid_user: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(user_model).where(user_model.uuid_user == uuid_user).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.patch("/state_change/{uuid_user}", dependencies=[Depends(JWTBearer())], response_model = user_schema_response)
async def change_status_user(user_uuid: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #session.query(advisor_model).filter(adv_models.uuid_advisor == advisor_uuid).update(advisor_model)
            #db.execute(adv_models).update().values(advisor_model_2)).where(adv_models.uuid_advisor == adv_uuid)
            #advisor_model_2 = adv_models(**advisor_model_2.model_dump())
            r = db.query(user_model).where(user_model.uuid_user == user_uuid).first()        
            if r is not None:
                if r.is_active == 1:
                    r.is_active = 0
                else:
                    r.is_active = 1
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='el id del usuario no existe')
    
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.delete("/{uuid_user}", dependencies=[Depends(JWTBearer())])
def delete_user(uuid_user: str):
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
            r=db.query(user_model).where(user_model.uuid_user == uuid_user).one_or_none()
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

    
    # for user in users:
    #     if user.email == data.email and user.password == data.password:
    #         return True
    # return False

def check_user(data: user_schema_login):
    session = get_db()
    db:Session
    for db in session:
        r1=db.query(user_model).where(user_model.user==data.user).first()
        r2=db.query(user_model).where(user_model.password==data.password).first()        
        if r1 is not None and r2 is not None and r1.is_active == 1:
            return True
        else:
            return False