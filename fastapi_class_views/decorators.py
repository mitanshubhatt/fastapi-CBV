from functools import wraps
from fastapi import Response, Request
import logging

# Define a decorator for caching responses
def cache_response(cache_store):
    """
    Decorator to cache the response of a view function.
    
    Args:
        cache_store (dict): A dictionary to store cached responses.
        
    Returns:
        function: The wrapped function with caching capability.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate a cache key based on function name and arguments
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            # Check if the response is already cached
            if cache_key in cache_store:
                return cache_store[cache_key]
            # Call the original function and cache its response
            response = await func(*args, **kwargs)
            cache_store[cache_key] = response
            return response
        return wrapper
    return decorator

# Define a decorator for logging requests
def log_request(logger=None):
    """
    Decorator to log the details of a request.
    
    Args:
        logger (logging.Logger, optional): A logger instance. Defaults to None.
        
    Returns:
        function: The wrapped function with logging capability.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            # Log the request details
            logger.info(f"Request: {request.method} {request.url}")
            # Call the original function
            response = await func(request, *args, **kwargs)
            # Log the response status
            if isinstance(response, Response):
                logger.info(f"Response status: {response.status_code}")
            return response
        return wrapper
    return decorator