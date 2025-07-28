from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import time

class RateLimitingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app,max_request:int=10,window_seconds:int=60):
        super().__init__(app)

        self.max_request = max_request
        self.window_seconds = window_seconds
        self.request_counts = {}

    async def dispatch(self, request: Request, call_next):
        client_ip=request.client.host
        current_time = time.time()
        request_time=self.clients.get(client_ip,[])
        request_time = [t for t in request_time if current_time -t< self.window_seconds]
        if len(request_time) >= self.max_request:
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
        request_time.append(current_time)
        self.clients[client_ip] = request_time
        response = await call_next(request)
        return response
        