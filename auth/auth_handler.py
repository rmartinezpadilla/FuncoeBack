# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict

import jwt
from decouple import config


# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")
JWT_SECRET = "use your secret code with secrets.token_hex(10)"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
<<<<<<< HEAD:auth/auth_handler.py
        "expires": time.time() + 1000
=======
        "expires": time.time() + 100000
>>>>>>> 9237c4bae302fe405a1538e9d8d4248f65035b1d:app/auth/auth_handler.py
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
