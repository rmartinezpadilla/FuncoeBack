from cryptography.fernet import Fernet
from app.schemas.user import User_login as user_schema_login
from app.models.user import User as user_model
from app.routes.role import get_rols
from app.utils.func.rol import get_rol
from app.config.db import get_db,Session
import base64

# key = Fernet.generate_key()
# fernet = Fernet(key)

def encrypt_password(password : str):
    #enpassword = fernet.encrypt(password.encode('utf-8'))        
    enpassword = base64.b64encode(password.encode('utf-8'))
    return enpassword

def decrypt_password(password :  str):    
    #decryp_pass = fernet.decrypt(password).decode('utf-8')
    decryp_pass = base64.b64decode(password).decode('utf-8')
    return decryp_pass    

def validate_user(data : user_schema_login):    
    id_user = get_uuid_user(data.user)    
    session = get_db()    
    db:Session
    for db in session:       
        r1=db.query(user_model).where(user_model.uuid_user==id_user).one()
        pass_decrypt = decrypt_password(r1.password)
        if r1 is not None and data.password == pass_decrypt and r1.is_active == 1 and get_rol(r1.rol_uuid) == 'admin':
            return True
        else:
            return False
        
def get_uuid_user(user : str):
    session = get_db()
    db:Session
    for db in session:        
        r1=db.query(user_model).where(user_model.user==user).one()
        if r1 is not None:
            return r1.uuid_user
        else:
            return None