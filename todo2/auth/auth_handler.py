import time
import jwt
from typing import Dict
#from decouple import config

from core.env import Env


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    env=Env()
    payload = {
        "user_id": user_id,
        "expires": time.time() + int(env.get("JWT_EXPIRE_TIME"))
    }
    token = jwt.encode(payload, env.get("JWT_SECRET"),
                       algorithm=env.get("JWT_ALGORITHM"))

    return token_response(token)


def decodeJWT(token: str) -> dict:
    env=Env()
    try:
        decoded_token = jwt.decode(
            token, env.get("JWT_SECRET"), algorithms=[env.get("JWT_ALGORITHM")])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}