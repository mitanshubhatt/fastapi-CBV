from fastapi.routing import APIRouter
from fastapi_class_views.base_view import BaseView
from typing import Type

def create_view_routes(view_cls: Type[BaseView], path: str, methods: list = ["get", "post", "put", "delete"]) -> APIRouter:
    router = APIRouter()
    for method in methods:
        if hasattr(view_cls, method):
            router.add_api_route(
                path=path,
                endpoint=getattr(view_cls, method),
                methods=[method.upper()],
                response_class=view_cls.response_class
            )
    return router