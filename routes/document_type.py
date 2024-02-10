from fastapi import APIRouter, Response, HTTPException, status
from schemas.document_type import Document_type as doc_type_schema
from config.db import get_db,Session
from models.document_type import Documents_types as doc_type_models
import uuid

router =  APIRouter(prefix='/document_type', tags=['Documents Types'], responses={404 : {'message' : 'Not found'}})


# @router.post("/")
# def create_document_type(doc_type_obj:doc_type_schema):
#     try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
#     #¡inicio try!
#         session = get_db()
#         db:Session
#         for db in session:
#             #doc_type_obj["id"] = uuid.uuid4() 
#             # print(type('esto es', doc_type_obj))           
#             doc_type_obj = doc_type_models(**doc_type_obj.model_dump())            
#             #añade el recurso persona para subirse a la base de datos
#             db.add(doc_type_obj)
#             #se sube a la base de datos
#             db.commit()
#             #se refresca la información en la variable persona para poderla devolver
#             #en el servicio
#             db.refresh(doc_type_obj)
#             return doc_type_obj
#     #¡fin try!
#     except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
#         #se debe controlar siempre que nos conectamos a una base de datos con un try - except
#         #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
#         #y es muy posible que la conexión falle por lo cual debemos responder que paso
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
#         #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
#         #un error, en este caso el error esta contenido en HTTPException

@router.get("/", response_model = list[doc_type_schema])
async def get_documents_types():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(doc_type_models)
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException

@router.get("/{id}", response_model = doc_type_schema)
async def read_document_type(id: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(doc_type_models).where(doc_type_models.uuid_document_type == id).first()
            return r
    #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
        #se debe controlar siempre que nos conectamos a una base de datos con un try - except
        #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
        #y es muy posible que la conexión falle por lo cual debemos responder que paso
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
        #un error, en este caso el error esta contenido en HTTPException
    
@router.get("/{name}", response_model = doc_type_schema)
async def read_document_type_for_name(name: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
        #¡inicio try!
            session = get_db()
            db:Session
            for db in session:
                #se usa la instrucción where para buscar por el id y se ejecuta el first para
                #encontrar la primera coincidencia, esto es posible porque el id es un 
                #identificador unico
                #r=db.query(doc_type_models).where(doc_type_models.document_type == name).first() 
                r=db.query(doc_type_models).filter_by(doc_type_models.document_type == name)
                return r
        #¡fin try!
    except Exception as e:#instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
            #se debe controlar siempre que nos conectamos a una base de datos con un try - except
            #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
            #y es muy posible que la conexión falle por lo cual debemos responder que paso
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
            #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
            #un error, en este caso el error esta contenido en HTTPException
    
# @router.delete("/{uuid_document_type}")
# def delete_document_type(uuid_document_type: str):
#     try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
#     #¡inicio try!
#         #si falla, se detendrá el flujo común y se ejecutará las instrucciones del except
#         session = get_db()
#         db:Session
#         for db in session:
#             #one or none es una instrucción que nos permite encontrar uno o ningún recurso
#             #en caso que sea un recurso lo añadiremos al delete ya que es el que vamos a borrar
#             #en caso que sea None se lanza un error, ya que no tenemos un dato con el id a borrar
#             #si intentamos borrar algo que no existe (en el caso que sea None) nos lanzará una 
#             #excepción y será atrapada en el except
#             r=db.query(doc_type_models).where(doc_type_models.uuid_document_type == uuid_document_type).one_or_none()
#             if r is not None:
#                 db.delete(r)#instruccion para borrar un recurso
#                 db.commit()
#                 return Response(status_code=status.HTTP_200_OK)
#             else:
#                 return Response(status_code=status.HTTP_404_NOT_FOUND)
#     #¡fin try!
#     except Exception as e: #instrucción que nos ayuda a atrapar la excepción que ocurre cuando alguna instrucción dentro de try falla
#         #se debe controlar siempre que nos conectamos a una base de datos con un try - except
#         #debido a que no podemos controlar la respuesta del servicio externo (en este caso la base de datos)
#         #y es muy posible que la conexión falle por lo cual debemos responder que paso
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
#         #la instrucción raise es similar a la instrucción return, pero en vez de retornar cualquier elemento, retornamos especificamente
#         #un error, en este caso el error esta contenido en HTTPException            }