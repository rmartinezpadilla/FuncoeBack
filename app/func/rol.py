from app.config.db import get_db,Session
from app.models.role import Role

def get_rol(id_rol : str):    
    session = get_db()    
    db:Session
    for db in session:        
        r1=db.query(Role).where(Role.uuid_rol==id_rol).first()        
        if r1 is not None:
            return r1.rol
        else:
            return None

def get_uuid_rol(rol : str):    
    session = get_db()    
    db:Session
    for db in session:        
        r1=db.query(Role).where(Role.rol==rol).one()        
        if r1 is not None:
            return r1.uuid_rol
        else:
            return None