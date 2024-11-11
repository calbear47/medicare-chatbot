import time
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    """
    Middleware to log API requests and responses.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        # Log request details
        duration = time.time() - start_time
        logger.info(
            f"Path: {request.path} | "
            f"Method: {request.method} | "
            f"Duration: {duration:.2f}s | "
            f"Status: {response.status_code}"
        )
        
        return response