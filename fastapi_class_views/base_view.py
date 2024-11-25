from fastapi import Request, Response
from fastapi.responses import JSONResponse

# Define the BaseView class
class BaseView:
    def __init__(self, request: Request, response_class=JSONResponse):
        self.request = request
        self.response_class = response_class

    # Method to handle GET requests
    async def get(self, *args, **kwargs):
        return self.response_class(content={"message": "GET method not implemented"})

    # Method to handle POST requests
    async def post(self, *args, **kwargs):
        return self.response_class(content={"message": "POST method not implemented"})

    # Method to handle PUT requests
    async def put(self, *args, **kwargs):
        return self.response_class(content={"message": "PUT method not implemented"})

    # Method to handle DELETE requests
    async def delete(self, *args, **kwargs):
        return self.response_class(content={"message": "DELETE method not implemented"})