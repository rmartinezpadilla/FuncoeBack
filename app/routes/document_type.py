from fastapi import APIRouter, HTTPException, status, Response, Depends
from app.schemas.document_type import Document_type as doc_type_schema
from app.config.db import get_db, Session
from app.models.document_type import Documents_types as doc_type_models
from app.auth.auth_bearer import JWTBearer
from sqlalchemy import desc
import typing

router =  APIRouter(prefix='/document_type', dependencies=[Depends(JWTBearer())], tags=['Documents Types'], responses={404 : {'message' : 'Not found'}})

@router.get("/all", response_model = typing.List[doc_type_schema])
def get_documents_types():
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(doc_type_models).order_by(desc(doc_type_models.created_at)).all()
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
def read_document_type(id: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
    #¡inicio try!
        session = get_db()
        db:Session
        for db in session:
            #se usa la instrucción where para buscar por el id y se ejecuta el first para
            #encontrar la primera coincidencia, esto es posible porque el id es un 
            #identificador unico
            r=db.query(doc_type_models).where(doc_type_models.uuid_document_type == id).first()            
            if r is not None:
                return r
            else:
                raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id document type not exist!')
    #¡fin try!
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
    
@router.get("/document/", response_model = doc_type_schema)
def read_document_type_for_name(document: str):
    try:#instrucción try, atrapa de inicio a fin las lineas que intentaremos ejecutar y que tiene posibilidad de fallar
        #¡inicio try!
            session = get_db()
            db:Session
            for db in session:                
                r=db.query(doc_type_models).where(doc_type_models.document_type == document).first()
                if r is not None:
                    return r
                else:
                    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Name document type not exist!')
        #¡fin try!
    except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))        