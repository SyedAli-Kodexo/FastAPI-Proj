from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import time
"""
class RateLimitingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app,max_requests:int=10,window_seconds:int=60):
        super().__init__(app)

        self.max_request = max_requests
        self.window_seconds = window_seconds
        self.request_counts = {}

    async def dispatch(self, request: Request, call_next):
        client_ip=request.client.host
        current_time = time.time()
        request_times=self.request_counts.get(client_ip, [])
        request_times = [t for t in request_times if current_time -t< self.window_seconds]
        if len(request_times) >= self.max_request:
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
        request_times.append(current_time)
        self.request_counts[client_ip] = request_times
        response = await call_next(request)
        return response
        
        """
class RateLimitingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 10, time_window: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.time_window = time_window
        self.request_counts = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        request_times = self.request_counts.get(client_ip, [])
        request_times = [t for t in request_times if current_time - t < self.time_window]

        if len(request_times) >= self.max_requests:
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)

        request_times.append(current_time)
        self.request_counts[client_ip] = request_times
        return await call_next(request)
