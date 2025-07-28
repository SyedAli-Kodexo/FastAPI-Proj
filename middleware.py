from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request
from jose import JWTError, jwt
from tokens import secret_key, algo
from datetime import datetime, timedelta

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.rstrip("/") in ["/login","/register","docs","/openapi.json","/favicon.ico","/redoc"]:
            return await call_next(request)
        
        token=request.cookies.get("access_token")
        if not token:
            return JSONResponse({"detail": "Not authenticated"}, status_code=401)
        
        try:
            payload=jwt.decode(token,secret_key,algorithms=[algo])
            username=payload.get("sub")
            if not username:
                raise JWTError("Invalid token")
            
            request.state.username = username
        except JWTError:
            return JSONResponse({"detail": "Invalid token"}, status_code=401)
        
        response=await call_next(request)
        return response