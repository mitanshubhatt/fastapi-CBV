from fastapi import Request, Response, HTTPException
from fastapi.responses import JSONResponse
from typing import Type, Any

class BaseView:
    def __init__(self, request: Request, response_class=JSONResponse):
        self.request = request
        self.response_class = response_class

    async def get(self, *args, **kwargs):
        raise HTTPException(status_code=405, detail="GET method not allowed")

    async def post(self, *args, **kwargs):
        raise HTTPException(status_code=405, detail="POST method not allowed")

    async def put(self, *args, **kwargs):
        raise HTTPException(status_code=405, detail="PUT method not allowed")

    async def delete(self, *args, **kwargs):
        raise HTTPException(status_code=405, detail="DELETE method not allowed")
