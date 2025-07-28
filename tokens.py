from jose import JWTError, jwt
from datetime import datetime, timedelta

secret_key ="123"
algo = "HS256"
access_token_expire_seconds = 30
refresh_token_expire_seconds = 60 * 60 * 24 * 7
def create_access_token(data:dict,expire_time:timedelta|None=None):
    to_encode=data.copy()
    access_token_expires=(datetime.utcnow()+(expire_time or timedelta(seconds=access_token_expire_seconds)))
    to_encode.update({"exp":access_token_expires})
    encode_JWT=jwt.encode(to_encode,secret_key,algorithm=[algo])
    return encode_JWT


def create_refresh_token(data:dict,expire_time:timedelta|None=None):
    to_encode=data.copy()
    refresh_token_expires=(datetime.utcnow()+(expire_time or timedelta(seconds=refresh_token_expire_seconds)))
    to_encode.update({"exp":refresh_token_expires})
    encoded_jwt=jwt.encode(to_encode,secret_key,algorithm=[algo])
    return encoded_jwt


def verufy_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,secret_key,algorithms=[algo])
        username=payload.get("sub")
        if username is None:
            raise credentials_exception
        
        return username
    
    except JWTError:
        raise credentials_exception