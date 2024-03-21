from fastapi import APIRouter, Response, HTTPException, status, Depends
from sqlalchemy import desc
from app.schemas.user import User as user_schema
from app.schemas.user import User_response as user_schema_response
from app.schemas.user import User_login as user_schema_login
from app.auth.auth_bearer import JWTBearer
from app.config.db import get_db,Session
from app.models.user import User as user_model
from app.func.user import *
from app.auth.auth_handler import signJWT
import uuid
import typing
from datetime import datetime

router =  APIRouter(prefix='/users', tags=['Users'], responses={404 : {'message' : 'Not found'}})

@router.post("/token/")
def get_token(user: user_schema_login):
    if validate_user(user):
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
                user_obj = user_model(**user_obj.model_dump()) 
                user_obj.uuid_user = uuid.uuid4()                 
                user_obj.password = encrypt_password(user_obj.password)                
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
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/all/", dependencies=[Depends(JWTBearer())], response_model = typing.List[user_schema_response])
def get_users():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(user_model).order_by(desc(user_model.created_at)).all()
            return r
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/actives/", dependencies=[Depends(JWTBearer())], response_model = list[user_schema_response])
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

@router.get("/inactives/", dependencies=[Depends(JWTBearer())], response_model = list[user_schema_response])
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

@router.get("/{uuid_user}/", dependencies=[Depends(JWTBearer())], response_model = user_schema_response)
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

@router.patch("/activate/", dependencies=[Depends(JWTBearer())], response_model = user_schema_response)
def activate_user(user_uuid: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            r = db.query(user_model).where(user_model.uuid_user == user_uuid).first()                        
            if r is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='el id del usuario no existe')
            elif r.is_active == 1:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f'User {user_uuid} is active')
            else:
                r.is_active = 1
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))        

@router.patch("/deactivate/", dependencies=[Depends(JWTBearer())], response_model = user_schema_response)
def deactivate_user(user_uuid: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:            
            r = db.query(user_model).where(user_model.uuid_user == user_uuid).first()                        
            if r is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='el id del usuario no existe')
            elif r.is_active == 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f'User {user_uuid} is desactive')
            else:
                r.is_active = 0
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.patch("/update/", response_model = user_schema_response)
def update_user(user_uuid: str, user_model_2: user_schema_login):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            user_model_2 = user_model(**user_model_2.model_dump())
            r = db.query(user_model).where(user_model.uuid_user == user_uuid).first()        
            if r is not None:                                
                r.user = user_model_2.user
                r.password = user_funcitons.encrypt_password(user_model_2.password)
                r.updated_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                db.commit()
                db.refresh(r)
                return r
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='id user not exist!')

    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))        

@router.delete("/delete/", dependencies=[Depends(JWTBearer())])
def delete_user(uuid_user: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
        session = get_db()
        db:Session
        for db in session:
            r=db.query(user_model).where(user_model.uuid_user == uuid_user).one_or_none()
            if r is not None:
                db.delete(r)#instruccion para borrar un recurso
                db.commit()
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status_code=status.HTTP_404_NOT_FOUND)
    #¡fin try!
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))


